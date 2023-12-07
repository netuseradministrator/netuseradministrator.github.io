
+++
title = 'wheels'
date = '2023-12-07T16:08:29+08:00'
draft = true
+++
```shell
bob@wheels:~$ ./linpeas.sh


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
OS: Linux version 5.4.0-113-generic (buildd@lcy02-amd64-067) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1)) #127-Ubuntu SMP Wed May 18 14:30:56 UTC 2022
User & Groups: uid=1000(bob) gid=1000(bob) groups=1000(bob)
Hostname: wheels
Writable folder: /dev/shm
[+] /usr/bin/ping is available for network discovery (linpeas can discover hosts, learn more with -h)
[+] /usr/bin/nc is available for network discover & port scanning (linpeas can discover hosts and scan ports, learn more with -h)                                                                                                                 
                                                                                                                         

Caching directories using 1 threads . . . . . . . . . . . . . . . . . . . . . . . . DONE
                                                                                                                         
════════════════════════════════════╣ System Information ╠════════════════════════════════════
[+] Operative system                                                                                                     
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#kernel-exploits                                          
Linux version 5.4.0-113-generic (buildd@lcy02-amd64-067) (gcc version 9.4.0 (Ubuntu 9.4.0-1ubuntu1~20.04.1)) #127-Ubuntu SMP Wed May 18 14:30:56 UTC 2022
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.4 LTS
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
Thu 18 May 2023 09:38:15 AM UTC                                                                                          

[+] System stats
Filesystem      Size  Used Avail Use% Mounted on                                                                         
udev            445M     0  445M   0% /dev
tmpfs            98M  1.2M   97M   2% /run
/dev/sda2       9.8G  5.9G  3.4G  64% /
tmpfs           489M     0  489M   0% /dev/shm
tmpfs           5.0M     0  5.0M   0% /run/lock
tmpfs           489M     0  489M   0% /sys/fs/cgroup
/dev/loop0       56M   56M     0 100% /snap/core18/2409
/dev/loop4       45M   45M     0 100% /snap/snapd/15904
/dev/loop1       56M   56M     0 100% /snap/core18/2128
/dev/loop2       62M   62M     0 100% /snap/core20/1434
/dev/loop5       45M   45M     0 100% /snap/snapd/15534
/dev/loop6       71M   71M     0 100% /snap/lxd/21029
/dev/loop3       68M   68M     0 100% /snap/lxd/22753
tmpfs            98M     0   98M   0% /run/user/1000
              total        used        free      shared  buff/cache   available
Mem:        1000244      279992       85420        3608      634832      527740
Swap:       1994748        3596     1991152

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
CPU family:                      25
Model:                           1
Model name:                      AMD EPYC 7413 24-Core Processor
Stepping:                        1
CPU MHz:                         2649.999
BogoMIPS:                        5299.99
Hypervisor vendor:               VMware
Virtualization type:             full
L1d cache:                       32 KiB
L1i cache:                       32 KiB
L2 cache:                        512 KiB
L3 cache:                        128 MiB
NUMA node0 CPU(s):               0
Vulnerability Itlb multihit:     Not affected
Vulnerability L1tf:              Not affected
Vulnerability Mds:               Not affected
Vulnerability Meltdown:          Not affected
Vulnerability Spec store bypass: Vulnerable
Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user
                                  pointer sanitization
Vulnerability Spectre v2:        Mitigation; Retpolines, IBPB conditional, STIBP
                                  disabled, RSB filling
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Not affected
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtr
                                 r pge mca cmov pat pse36 clflush mmx fxsr sse s
                                 se2 syscall nx mmxext fxsr_opt pdpe1gb rdtscp l
                                 m constant_tsc rep_good nopl tsc_reliable nonst
                                 op_tsc cpuid extd_apicid pni pclmulqdq ssse3 fm
                                 a cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt a
                                 es xsave avx f16c rdrand hypervisor lahf_lm ext
                                 apic cr8_legacy abm sse4a misalignsse 3dnowpref
                                 etch osvw invpcid_single ibpb vmmcall fsgsbase 
                                 bmi1 avx2 smep bmi2 invpcid rdseed adx smap clf
                                 lushopt clwb sha_ni xsaveopt xsavec xgetbv1 xsa
                                 ves clzero wbnoinvd arat umip pku ospke vaes vp
                                 clmulqdq rdpid overflow_recov succor

[+] Environment
[i] Any private information inside environment variables?                                                                
LESSOPEN=| /usr/bin/lesspipe %s                                                                                          
HISTFILESIZE=0
USER=bob
SSH_CLIENT=192.168.45.156 58180 22
XDG_SESSION_TYPE=tty
SHLVL=1
MOTD_SHOWN=pam
HOME=/home/bob
SSH_TTY=/dev/pts/0
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
LOGNAME=bob
_=./linpeas.sh
XDG_SESSION_CLASS=user
TERM=xterm-256color
XDG_SESSION_ID=42
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
XDG_RUNTIME_DIR=/run/user/1000
LANG=en_US.UTF-8
HISTSIZE=0
SHELL=/bin/sh
LESSCLOSE=/usr/bin/lesspipe %s %s
SSH_CONNECTION=192.168.45.156 58180 192.168.195.202 22
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

[+] Unmounted file-system?
[i] Check if you can mount umounted devices                                                                              
/dev/disk/by-uuid/a11e5f3b-c0bc-49ee-9ff1-6958065c095d / ext4 defaults 0 0                                               
/swap.img       none    swap    sw      0       0


════════════════════════════════════╣ Available Software ╠════════════════════════════════════
[+] Useful software                                                                                                      
/usr/bin/nc                                                                                                              
/usr/bin/netcat
/usr/bin/wget
/usr/bin/curl
/usr/bin/ping
/usr/bin/base64
/usr/bin/socat
/usr/bin/python3
/usr/bin/perl
/usr/bin/php
/usr/bin/sudo
/snap/bin/lxc

[+] Installed Compiler
                                                                                                                         

══════════════════════════════╣ Processes, Cron, Services, Timers & Sockets ╠════════════════════════════════
[+] Cleaned processes                                                                                                    
[i] Check weird & unexpected proceses run by root: https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes 
root         665  0.0  0.0   2488   572 ?        S    May17   0:00  _ bpfilter_umh                                       
root           1  0.0  1.2 170288 12696 ?        Ss   May17   0:02 /sbin/init maybe-ubiquity
root         453  0.0  1.8  69676 18176 ?        S<s  May17   0:05 /lib/systemd/systemd-journald
root         487  0.0  0.8  24512  8392 ?        Ss   May17   0:04 /lib/systemd/systemd-udevd
root       26030  0.0  0.5  23972  5568 ?        S    09:38   0:00  _ /lib/systemd/systemd-udevd
root       26031  0.0  0.5  23972  5568 ?        S    09:38   0:00  _ /lib/systemd/systemd-udevd
root       26032  0.0  0.6  24512  6096 ?        S    09:38   0:00  _ /lib/systemd/systemd-udevd
root       26033  0.0  0.6  24512  6096 ?        S    09:38   0:00  _ /lib/systemd/systemd-udevd
root       26034  0.0  0.6  24512  6096 ?        S    09:38   0:00  _ /lib/systemd/systemd-udevd
root         619  0.0  1.7 345768 17996 ?        SLsl May17   0:10 /sbin/multipathd -d -s
systemd+     657  0.0  0.5  90188  5992 ?        Ssl  May17   0:02 /lib/systemd/systemd-timesyncd
  └─(Caps) 0x0000000002000000=cap_sys_time
root         682  0.0  1.0  47688 10276 ?        Ss   May17   0:00 /usr/bin/VGAuthService
root         684  0.0  0.8 311636  8248 ?        Ssl  May17   0:24 /usr/bin/vmtoolsd
systemd+     785  0.0  0.7  26672  7772 ?        Ss   May17   0:00 /lib/systemd/systemd-networkd
  └─(Caps) 0x0000000000003c00=cap_net_bind_service,cap_net_broadcast,cap_net_admin,cap_net_raw
systemd+     798  0.0  1.1  23860 11748 ?        Ss   May17   0:01 /lib/systemd/systemd-resolved
root         868  0.0  0.7 235560  7312 ?        Ssl  May17   0:01 /usr/lib/accountsservice/accounts-daemon
root         872  0.0  0.2   6812  2984 ?        Ss   May17   0:00 /usr/sbin/cron -f
message+     873  0.0  0.4   7664  4692 ?        Ss   May17   0:00 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
  └─(Caps) 0x0000000020000000=cap_audit_write
root         881  0.0  1.8  29656 18036 ?        Ss   May17   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         885  0.0  0.6 232712  6640 ?        Ssl  May17   0:00 /usr/lib/policykit-1/polkitd --no-debug
syslog       886  0.0  0.4 224344  4984 ?        Ssl  May17   0:01 /usr/sbin/rsyslogd -n -iNONE
root         888  0.0  3.6 735048 36164 ?        Ssl  May17   0:02 /usr/lib/snapd/snapd
root         890  0.0  0.7  16612  7576 ?        Ss   May17   0:00 /lib/systemd/systemd-logind
root         892  0.0  1.1 392500 11740 ?        Ssl  May17   0:00 /usr/lib/udisks2/udisksd
daemon[0m       895  0.0  0.2   3792  2228 ?        Ss   May17   0:00 /usr/sbin/atd -f
root         960  0.0  0.1   5828  1744 tty1     Ss+  May17   0:00 /sbin/agetty -o -p -- u --noclear tty1 linux
mysql       1012  0.0  7.5 1271568 75648 ?       Ssl  May17   0:10 /usr/sbin/mysqld
bob        25262  0.0  0.5  13948  5900 ?        S    09:31   0:00      _ sshd: bob@pts/0
bob        25270  0.0  0.1   2608  1696 pts/0    Ss   09:31   0:00          _ -sh
bob        25346  0.0  0.9  15796  9704 pts/0    S+   09:34   0:00              _ python3 -c import pty;pty.spawn("/bin/bash");
bob        25347  0.0  0.5   8176  5116 pts/1    Ss   09:34   0:00                  _ /bin/bash
bob        25479  0.3  0.2   3084  2144 pts/1    S+   09:38   0:00                      _ /bin/sh ./linpeas.sh
bob        26159  0.0  0.0   3084   612 pts/1    S+   09:38   0:00                          _ /bin/sh ./linpeas.sh
bob        26163  0.0  0.3   9220  3672 pts/1    R+   09:38   0:00                          |   _ ps fauxwww
bob        26162  0.0  0.0   3084   612 pts/1    S+   09:38   0:00                          _ /bin/sh ./linpeas.sh
root        1020  0.0  1.9 107904 19652 ?        Ssl  May17   0:00 /usr/bin/python3 /usr/share/unattended-upgrades/unattended-upgrade-shutdown --wait-for-signal
root        1025  0.0  1.0 314456 10384 ?        Ssl  May17   0:00 /usr/sbin/ModemManager
root        1032  0.0  1.8 196360 18656 ?        Ss   May17   0:01 /usr/sbin/apache2 -k start
www-data   21729  0.0  1.5 197120 15596 ?        S    07:36   0:00  _ /usr/sbin/apache2 -k start
www-data   21730  0.0  1.3 197120 13196 ?        S    07:36   0:00  _ /usr/sbin/apache2 -k start
www-data   21732  0.0  1.6 197104 16236 ?        S    07:36   0:00  _ /usr/sbin/apache2 -k start
www-data   21733  0.0  1.5 197112 15772 ?        S    07:36   0:00  _ /usr/sbin/apache2 -k start
www-data   23470  0.0  1.5 197112 15272 ?        S    08:29   0:00  _ /usr/sbin/apache2 -k start
www-data   23473  0.0  1.5 197104 15012 ?        S    08:29   0:00  _ /usr/sbin/apache2 -k start
www-data   23474  0.0  1.5 197112 15192 ?        S    08:29   0:00  _ /usr/sbin/apache2 -k start
www-data   23475  0.0  1.3 197120 13036 ?        S    08:29   0:00  _ /usr/sbin/apache2 -k start
www-data   23476  0.0  1.5 197112 15020 ?        S    08:29   0:00  _ /usr/sbin/apache2 -k start
www-data   23477  0.0  1.2 197104 12976 ?        S    08:29   0:00  _ /usr/sbin/apache2 -k start
bob        25152  0.0  0.9  18456  9628 ?        Ss   09:31   0:00 /lib/systemd/systemd --user
bob        25155  0.0  0.4 171504  4476 ?        S    09:31   0:00  _ (sd-pam)
bob        26105  0.0  0.3   7104  3948 ?        Ss   09:38   0:00  _ /usr/bin/dbus-daemon[0m --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only

[+] Binary processes permissions
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#processes                                                
1.2M -rwxr-xr-x 1 root root 1.2M Apr 18  2022 /bin/bash                                                                  
   0 lrwxrwxrwx 1 root root    4 Jul 31  2020 /bin/sh -> dash
1.6M -rwxr-xr-x 1 root root 1.6M Apr 21  2022 /lib/systemd/systemd
160K -rwxr-xr-x 1 root root 159K Apr 21  2022 /lib/systemd/systemd-journald
264K -rwxr-xr-x 1 root root 263K Apr 21  2022 /lib/systemd/systemd-logind
2.2M -rwxr-xr-x 1 root root 2.2M Apr 21  2022 /lib/systemd/systemd-networkd
408K -rwxr-xr-x 1 root root 407K Apr 21  2022 /lib/systemd/systemd-resolved
 56K -rwxr-xr-x 1 root root  55K Apr 21  2022 /lib/systemd/systemd-timesyncd
728K -rwxr-xr-x 1 root root 727K Apr 21  2022 /lib/systemd/systemd-udevd
 68K -rwxr-xr-x 1 root root  68K Feb  7  2022 /sbin/agetty
   0 lrwxrwxrwx 1 root root   20 Apr 21  2022 /sbin/init -> /lib/systemd/systemd
128K -rwxr-xr-x 1 root root 127K Apr  6  2020 /sbin/multipathd
244K -rwxr-xr-x 1 root root 244K Apr 29  2022 /usr/bin/dbus-daemon[0m
   0 lrwxrwxrwx 1 root root    9 Mar 13  2020 /usr/bin/python3 -> python3.8
140K -rwxr-xr-x 1 root root 139K Oct 12  2021 /usr/bin/VGAuthService
 76K -rwxr-xr-x 1 root root  75K Oct 12  2021 /usr/bin/vmtoolsd
200K -rwxr-xr-x 1 root root 199K Nov  9  2021 /usr/lib/accountsservice/accounts-daemon
120K -rwxr-xr-x 1 root root 119K Feb 21  2022 /usr/lib/policykit-1/polkitd
 30M -rwxr-xr-x 1 root root  30M Apr 27  2022 /usr/lib/snapd/snapd
472K -rwxr-xr-x 1 root root 472K Sep  6  2021 /usr/lib/udisks2/udisksd
696K -rwxr-xr-x 1 root root 693K Mar 16  2022 /usr/sbin/apache2
 32K -rwxr-xr-x 1 root root  31K Nov 12  2018 /usr/sbin/atd
 56K -rwxr-xr-x 1 root root  55K Feb 13  2020 /usr/sbin/cron
1.7M -rwxr-xr-x 1 root root 1.7M Oct 21  2021 /usr/sbin/ModemManager
 21M -rwxr-xr-x 1 root root  21M Feb 18  2022 /usr/sbin/mysqld
712K -rwxr-xr-x 1 root root 711K May  3  2022 /usr/sbin/rsyslogd

[+] Files opened by processes belonging to other users
[i] This is usually empty because of the lack of privileges to read other user processes information                     
COMMAND     PID  TID TASKCMD               USER   FD      TYPE             DEVICE SIZE/OFF       NODE NAME               

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
drwxr-xr-x   2 root root 4096 May 11  2022 .
drwxr-xr-x 102 root root 4096 May 18  2022 ..
-rw-r--r--   1 root root  201 Feb 14  2020 e2scrub_all
-rw-r--r--   1 root root  712 Mar 27  2020 php
-rw-r--r--   1 root root  102 Feb 13  2020 .placeholder
-rw-r--r--   1 root root  190 Jul 31  2020 popularity-contest

/etc/cron.daily:
total 52
drwxr-xr-x   2 root root 4096 May 18  2022 .
drwxr-xr-x 102 root root 4096 May 18  2022 ..
-rwxr-xr-x   1 root root  539 Sep 30  2020 apache2
-rwxr-xr-x   1 root root  376 Dec  4  2019 apport
-rwxr-xr-x   1 root root 1478 Apr  9  2020 apt-compat
-rwxr-xr-x   1 root root  355 Dec 29  2017 bsdmainutils
-rwxr-xr-x   1 root root 1187 Sep  5  2019 dpkg
-rwxr-xr-x   1 root root  377 Jan 21  2019 logrotate
-rwxr-xr-x   1 root root 1123 Feb 25  2020 man-db
-rw-r--r--   1 root root  102 Feb 13  2020 .placeholder
-rwxr-xr-x   1 root root 4574 Jul 18  2019 popularity-contest
-rwxr-xr-x   1 root root  214 Apr  2  2020 update-notifier-common

/etc/cron.hourly:
total 12
drwxr-xr-x   2 root root 4096 Jul 31  2020 .
drwxr-xr-x 102 root root 4096 May 18  2022 ..
-rw-r--r--   1 root root  102 Feb 13  2020 .placeholder

/etc/cron.monthly:
total 12
drwxr-xr-x   2 root root 4096 Jul 31  2020 .
drwxr-xr-x 102 root root 4096 May 18  2022 ..
-rw-r--r--   1 root root  102 Feb 13  2020 .placeholder

/etc/cron.weekly:
total 20
drwxr-xr-x   2 root root 4096 May 11  2022 .
drwxr-xr-x 102 root root 4096 May 18  2022 ..
-rwxr-xr-x   1 root root  813 Feb 25  2020 man-db
-rw-r--r--   1 root root  102 Feb 13  2020 .placeholder
-rwxr-xr-x   1 root root  403 Aug  5  2021 update-notifier-common

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
 [ - ]  grub-common
 [ - ]  hwclock.sh
 [ - ]  irqbalance
 [ - ]  iscsid
 [ - ]  keyboard-setup.sh
 [ + ]  kmod
 [ - ]  lvm2
 [ - ]  lvm2-lvmpolld
 [ + ]  multipath-tools
 [ + ]  mysql
 [ + ]  netfilter-persistent
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
/lib/systemd/system/grub-common.service is executing some relative path
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
/lib/systemd/system/sysinit.target.wants/systemd-udevd.service is executing some relative path
/lib/systemd/system/sysinit.target.wants/systemd-udev-trigger.service is executing some relative path
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
/lib/systemd/system/systemd-udevd.service is executing some relative path
/lib/systemd/system/systemd-udev-settle.service is executing some relative path
/lib/systemd/system/systemd-udev-trigger.service is executing some relative path
/lib/systemd/system/udev.service is executing some relative path
/lib/systemd/user/systemd-tmpfiles-clean.service is executing some relative path
/lib/systemd/user/systemd-tmpfiles-setup.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/initrd-cleanup.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/initrd-parse-etc.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/initrd-switch-root.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/initrd-udevadm-cleanup-db.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/sysinit.target.wants/systemd-boot-system-token.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/sysinit.target.wants/systemd-hwdb-update.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/sysinit.target.wants/systemd-journal-flush.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/sysinit.target.wants/systemd-machine-id-commit.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/sysinit.target.wants/systemd-sysusers.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/sysinit.target.wants/systemd-udevd.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/sysinit.target.wants/systemd-udev-trigger.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/systemd-ask-password-console.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/systemd-ask-password-wall.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/systemd-boot-system-token.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/systemd-halt.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/systemd-hwdb-update.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/systemd-journal-flush.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/systemd-kexec.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/systemd-machine-id-commit.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/systemd-sysusers.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/systemd-tmpfiles-clean.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/systemd-udevd.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/systemd-udev-settle.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/systemd-udev-trigger.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/system/udev.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/user/systemd-tmpfiles-clean.service is executing some relative path
/snap/core20/1434/usr/lib/systemd/user/systemd-tmpfiles-setup.service is executing some relative path
You can't write on systemd PATH

[+] System timers
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers                                                   
NEXT                        LEFT        LAST                        PASSED               UNIT                         ACTIVATES                     
Thu 2023-05-18 09:39:00 UTC 37s left    Thu 2023-05-18 09:09:09 UTC 29min ago            phpsessionclean.timer        phpsessionclean.service       
Thu 2023-05-18 10:15:11 UTC 36min left  Fri 2023-02-17 18:26:57 UTC 2 months 28 days ago ua-timer.timer               ua-timer.service              
Thu 2023-05-18 16:11:47 UTC 6h left     Thu 2023-05-18 07:36:21 UTC 2h 2min ago          motd-news.timer              motd-news.service             
Thu 2023-05-18 19:50:41 UTC 10h left    Fri 2023-02-17 10:52:35 UTC 2 months 29 days ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
Thu 2023-05-18 22:50:33 UTC 13h left    Thu 2023-05-18 07:36:21 UTC 2h 2min ago          fwupd-refresh.timer          fwupd-refresh.service         
Fri 2023-05-19 00:00:00 UTC 14h left    Thu 2023-05-18 07:36:21 UTC 2h 2min ago          logrotate.timer              logrotate.service             
Fri 2023-05-19 00:00:00 UTC 14h left    Thu 2023-05-18 07:36:21 UTC 2h 2min ago          man-db.timer                 man-db.service                
Fri 2023-05-19 02:22:56 UTC 16h left    Thu 2023-05-18 07:36:21 UTC 2h 2min ago          apt-daily.timer              apt-daily.service             
Fri 2023-05-19 06:55:10 UTC 21h left    Thu 2023-05-18 07:36:21 UTC 2h 2min ago          apt-daily-upgrade.timer      apt-daily-upgrade.service     
Sun 2023-05-21 03:10:01 UTC 2 days left Thu 2023-05-18 07:36:21 UTC 2h 2min ago          e2scrub_all.timer            e2scrub_all.service           
Mon 2023-05-22 00:00:00 UTC 3 days left Thu 2023-05-18 07:36:21 UTC 2h 2min ago          fstrim.timer                 fstrim.service                
n/a                         n/a         n/a                         n/a                  snapd.snap-repair.timer      snapd.snap-repair.service     
n/a                         n/a         n/a                         n/a                  ua-license-check.timer       ua-license-check.service      

[+] Analyzing .timer files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#timers                                                   
                                                                                                                         
[+] Analyzing .socket files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets                                                  
                                                                                                                         
[+] HTTP sockets
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sockets                                                  
Socket /run/user/1000/snapd-session-agent.socket owned by bob uses HTTP. Response to /index:                             
{"type":"error","result":{"message":"method \"GET\" not allowed"}}
Socket /run/snapd.socket owned by root uses HTTP. Response to /index:
{"type":"sync","status-code":200,"status":"OK","result":["TBD"]}
Socket /run/snapd-snap.socket owned by root uses HTTP. Response to /index:
{"type":"error","status-code":403,"status":"Forbidden","result":{"message":"access denied","kind":"login-required"}}

[+] D-Bus config files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus                                                    
Possible weak user policy found on /etc/dbus-1/system.d/org.freedesktop.thermald.conf (        <policy group="power">)   

[+] D-Bus Service Objects list
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#d-bus                                                    
NAME                            PID PROCESS         USER             CONNECTION    UNIT                        SESSION DESCRIPTION
:1.0                            785 systemd-network systemd-network  :1.0          systemd-networkd.service    -       -
:1.1                            798 systemd-resolve systemd-resolve  :1.1          systemd-resolved.service    -       -
:1.10                          1025 ModemManager    root             :1.10         ModemManager.service        -       -
:1.11                           888 snapd           root             :1.11         snapd.service               -       -
:1.153                        46533 busctl          bob              :1.153        session-42.scope            42      -
:1.2                            657 systemd-timesyn systemd-timesync :1.2          systemd-timesyncd.service   -       -
:1.3                              1 systemd         root             :1.3          init.scope                  -       -
:1.35                         25152 systemd         bob              :1.35         user@1000.service           -       -
:1.4                            890 systemd-logind  root             :1.4          systemd-logind.service      -       -
:1.5                            868 accounts-daemon root             :1.5          accounts-daemon.service     -       -
:1.6                            885 polkitd         root             :1.6          polkit.service              -       -
:1.7                            881 networkd-dispat root             :1.7          networkd-dispatcher.service -       -
:1.8                            892 udisksd         root             :1.8          udisks2.service             -       -
:1.9                           1020 unattended-upgr root             :1.9          unattended-upgrades.service -       -
com.ubuntu.LanguageSelector       - -               -                (activatable) -                           -       -
com.ubuntu.SoftwareProperties     - -               -                (activatable) -                           -       -
io.netplan.Netplan                - -               -                (activatable) -                           -       -
org.freedesktop.Accounts        868 accounts-daemon root             :1.5          accounts-daemon.service     -       -
org.freedesktop.DBus              1 systemd         root             -             init.scope                  -       -
org.freedesktop.ModemManager1  1025 ModemManager    root             :1.10         ModemManager.service        -       -
org.freedesktop.PackageKit        - -               -                (activatable) -                           -       -
org.freedesktop.PolicyKit1      885 polkitd         root             :1.6          polkit.service              -       -
org.freedesktop.UDisks2         892 udisksd         root             :1.8          udisks2.service             -       -
org.freedesktop.UPower            - -               -                (activatable) -                           -       -
org.freedesktop.bolt              - -               -                (activatable) -                           -       -
org.freedesktop.fwupd             - -               -                (activatable) -                           -       -
org.freedesktop.hostname1         - -               -                (activatable) -                           -       -
org.freedesktop.locale1           - -               -                (activatable) -                           -       -
org.freedesktop.login1          890 systemd-logind  root             :1.4          systemd-logind.service      -       -
org.freedesktop.network1        785 systemd-network systemd-network  :1.0          systemd-networkd.service    -       -
org.freedesktop.resolve1        798 systemd-resolve systemd-resolve  :1.1          systemd-resolved.service    -       -
org.freedesktop.systemd1          1 systemd         root             :1.3          init.scope                  -       -
org.freedesktop.thermald          - -               -                (activatable) -                           -       -
org.freedesktop.timedate1         - -               -                (activatable) -                           -       -
org.freedesktop.timesync1       657 systemd-timesyn systemd-timesync :1.2          systemd-timesyncd.service   -       -


═══════════════════════════════════╣ Network Information ╠════════════════════════════════════
[+] Hostname, hosts and DNS                                                                                              
wheels                                                                                                                   
127.0.0.1 localhost
127.0.0.1 wheels

nameserver 127.0.0.53
options edns0 trust-ad

[+] Content of /etc/inetd.conf & /etc/xinetd.conf
/etc/inetd.conf Not Found                                                                                                
                                                                                                                         
[+] Interfaces
# symbolic names for networks, see networks(5) for more information                                                      
link-local 169.254.0.0
ens160: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.195.202  netmask 255.255.255.0  broadcast 192.168.195.255
        ether 00:50:56:ba:7b:fd  txqueuelen 1000  (Ethernet)
        RX packets 25147  bytes 3473024 (3.4 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 22410  bytes 8611617 (8.6 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 115904  bytes 8234756 (8.2 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 115904  bytes 8234756 (8.2 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0


[+] Networks and neighbours
Kernel IP routing table                                                                                                  
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         _gateway        0.0.0.0         UG    0      0        0 ens160
192.168.195.0   0.0.0.0         255.255.255.0   U     0      0        0 ens160
Address                  HWtype  HWaddress           Flags Mask            Iface
_gateway                 ether   00:50:56:ba:f3:39   C                     ens160

[+] Iptables rules
iptables rules Not Found                                                                                                 
                                                                                                                         
[+] Active Ports
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#open-ports                                               
tcp        0      0 127.0.0.1:3306          0.0.0.0:*               LISTEN      -                                        
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   

[+] Can I sniff with tcpdump?
No                                                                                                                       
                                                                                                                         

════════════════════════════════════╣ Users Information ╠════════════════════════════════════
[+] My user                                                                                                              
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#users                                                    
uid=1000(bob) gid=1000(bob) groups=1000(bob)                                                                             

[+] Do I have PGP keys?
/usr/bin/gpg                                                                                                             
netpgpkeys Not Found
netpgp Not Found                                                                                                         
                                                                                                                         
[+] Clipboard or highlighted text?
xsel and xclip Not Found                                                                                                 
                                                                                                                         
[+] Checking 'sudo -l', /etc/sudoers, and /etc/sudoers.d
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid                                            
Sorry, try again.                                                                                                        

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
bob:x:1000:1000::/home/bob:/bin/sh                                                                                       
root:x:0:0:root:/root:/bin/bash

[+] All users & groups
uid=0(root) gid=0(root) groups=0(root)                                                                                   
uid=1000(bob) gid=1000(bob) groups=1000(bob)
uid=100(systemd-network) gid=102(systemd-network) groups=102(systemd-network)
uid=101(systemd-resolve) gid=103(systemd-resolve) groups=103(systemd-resolve)
uid=102(systemd-timesync) gid=104(systemd-timesync) groups=104(systemd-timesync)
uid=103(messagebus) gid=106(messagebus) groups=106(messagebus)
uid=104(syslog) gid=110(syslog) groups=110(syslog),4(adm),5(tty)
uid=105(_apt) gid=65534(nogroup) groups=65534(nogroup)
uid=106(tss) gid=111(tss) groups=111(tss)
uid=107(uuidd) gid=112(uuidd) groups=112(uuidd)
uid=108(tcpdump) gid=113(tcpdump) groups=113(tcpdump)
uid=109(landscape) gid=115(landscape) groups=115(landscape)
uid=10(uucp) gid=10(uucp) groups=10(uucp)
uid=110(pollinate) gid=1(daemon[0m) groups=1(daemon[0m)
uid=111(sshd) gid=65534(nogroup) groups=65534(nogroup)
uid=112(usbmux) gid=46(plugdev) groups=46(plugdev)
uid=113(mysql) gid=117(mysql) groups=117(mysql)
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
uid=998(lxd) gid=100(users) groups=100(users)
uid=999(systemd-coredump) gid=999(systemd-coredump) groups=999(systemd-coredump)
uid=9(news) gid=9(news) groups=9(news)

[+] Login now
 09:38:32 up 14:03,  1 user,  load average: 0.36, 0.10, 0.03                                                             
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
bob      pts/0    192.168.45.156   09:31   24.00s  0.03s  0.03s python3 -c import pty;pty.spawn("/bin/bash");

[+] Last logons
root     pts/1        Tue May 17 19:23:01 2022 - Tue May 17 19:23:02 2022  (00:00)     192.168.118.14                    
bob      pts/0        Tue May 17 19:22:53 2022 - Tue May 17 19:23:02 2022  (00:00)     192.168.118.14
reboot   system boot  Tue May 17 19:21:47 2022   still running                         0.0.0.0
root     tty1         Wed May 11 11:04:58 2022 - down                      (00:00)     0.0.0.0
bob      pts/0        Wed May 11 11:03:27 2022 - Wed May 11 11:05:09 2022  (00:01)     192.168.118.18
reboot   system boot  Wed May 11 11:01:18 2022 - Wed May 11 11:05:10 2022  (00:03)     0.0.0.0
root     pts/0        Wed May 11 10:58:06 2022 - down                      (00:01)     192.168.118.18
reboot   system boot  Wed May 11 10:56:26 2022 - Wed May 11 11:00:03 2022  (00:03)     0.0.0.0

wtmp begins Wed May 11 10:14:08 2022

[+] Last time logon each user
Username         Port     From             Latest                                                                        
root             pts/1    192.168.118.14   Tue May 17 19:23:01 +0000 2022
bob              pts/0    192.168.45.156   Thu May 18 09:31:29 +0000 2023

[+] Password policy
PASS_MAX_DAYS   99999                                                                                                    
PASS_MIN_DAYS   0
PASS_WARN_AGE   7
ENCRYPT_METHOD SHA512

[+] Do not forget to test 'su' as any other user with shell: without password and with their names as password (I can't do it...)                                                                                                                 
[+] Do not forget to execute 'sudo -l' without password or with valid password (if you know it)!!                        
                                                                                                                         

═══════════════════════════════════╣ Software Information ╠═══════════════════════════════════
[+] MySQL version                                                                                                        
mysql  Ver 15.1 Distrib 10.3.34-MariaDB, for debian-linux-gnu (x86_64) using readline 5.2                                

[+] MySQL connection using default root/root ........... No
[+] MySQL connection using root/toor ................... No                                                              
[+] MySQL connection using root/NOPASS ................. No                                                              
[+] Searching mysql credentials and exec                                                                                 
From '/etc/mysql/mariadb.conf.d/50-server.cnf' Mysql user: user                    = mysql                               
Found readable /etc/mysql/my.cnf
[client-server]
!includedir /etc/mysql/conf.d/
!includedir /etc/mysql/mariadb.conf.d/

[+] PostgreSQL version and pgadmin credentials
 Not Found                                                                                                               
                                                                                                                         
[+] PostgreSQL connection to template0 using postgres/NOPASS ........ No
[+] PostgreSQL connection to template1 using postgres/NOPASS ........ No                                                 
[+] PostgreSQL connection to template0 using pgsql/NOPASS ........... No                                                 
[+] PostgreSQL connection to template1 using pgsql/NOPASS ........... No                                                 
                                                                                                                         
[+] Apache server info
Version: Server version: Apache/2.4.41 (Ubuntu)                                                                          
Server built:   2022-03-16T16:52:53
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
PermitRootLogin yes                                                                                                      
PermitRootLogin yes
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
No Sockets found in /run/screen/S-bob.                                                                                   

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
total 52
-rw-r--r-- 1 root root 2247 Oct  1  2021 ubuntu-advantage-cc-eal.gpg
-rw-r--r-- 1 root root 2274 Jan 25  2021 ubuntu-advantage-cis.gpg
-rw-r--r-- 1 root root 2236 Oct 15  2020 ubuntu-advantage-esm-apps.gpg
-rw-r--r-- 1 root root 2264 Oct 15  2020 ubuntu-advantage-esm-infra-trusty.gpg
-rw-r--r-- 1 root root 2275 Oct 15  2020 ubuntu-advantage-fips.gpg
-rw-r--r-- 1 root root 2235 Oct  1  2021 ubuntu-advantage-ros.gpg
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
-rwsr-sr-x 1 daemon daemon           55K Nov 12  2018 /usr/bin/at  --->  RTru64_UNIX_4.0g(CVE-2002-1614)                 
-rwsr-xr-x 1 root   root            427K Mar  4  2019 /snap/core18/2128/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root   root             59K Mar 22  2019 /snap/core18/2128/usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                             
-rwsr-xr-x 1 root   root             40K Mar 22  2019 /snap/core18/2128/usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root   root             75K Mar 22  2019 /snap/core18/2128/usr/bin/gpasswd
-rwsr-xr-x 1 root   root             44K Mar 22  2019 /snap/core18/2128/usr/bin/chsh
-rwsr-xr-x 1 root   root             75K Mar 22  2019 /snap/core18/2128/usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root   root             44K Mar 22  2019 /snap/core18/2128/bin/su
-rwsr-xr-x 1 root   root             63K Jun 28  2019 /snap/core18/2409/bin/ping
-rwsr-xr-x 1 root   root             63K Jun 28  2019 /snap/core18/2128/bin/ping
-rwsr-xr-x 1 root   root             15K Jul  8  2019 /usr/lib/eject/dmcrypt-get-device
-rwsr-xr-x 1 root   root            427K Mar  3  2020 /snap/core18/2409/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root   root             39K Mar  7  2020 /usr/bin/fusermount
-rwsr-xr-- 1 root   systemd-resolve  51K Jun 11  2020 /snap/core20/1434/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-- 1 root   systemd-resolve  42K Jun 11  2020 /snap/core18/2409/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-- 1 root   systemd-resolve  42K Jun 11  2020 /snap/core18/2128/usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root   root             27K Sep 16  2020 /snap/core18/2409/bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root   root             43K Sep 16  2020 /snap/core18/2409/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8                                                                                            
-rwsr-xr-x 1 root   root             27K Sep 16  2020 /snap/core18/2128/bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root   root             43K Sep 16  2020 /snap/core18/2128/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8                                                                                            
-rwsr-xr-x 1 root   root            163K Jan 19  2021 /usr/bin/sudo
-rwsr-xr-x 1 root   root            163K Jan 19  2021 /snap/core20/1434/usr/bin/sudo
-rwsr-xr-x 1 root   root            146K Jan 19  2021 /snap/core18/2409/usr/bin/sudo
-rwsr-xr-x 1 root   root            146K Jan 19  2021 /snap/core18/2128/usr/bin/sudo
-rwsr-xr-x 1 root   root             67K Jul 14  2021 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                                              
-rwsr-xr-x 1 root   root             44K Jul 14  2021 /usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root   root             87K Jul 14  2021 /usr/bin/gpasswd
-rwsr-xr-x 1 root   root             52K Jul 14  2021 /usr/bin/chsh
-rwsr-xr-x 1 root   root             84K Jul 14  2021 /usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root   root             67K Jul 14  2021 /snap/core20/1434/usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                             
-rwsr-xr-x 1 root   root             44K Jul 14  2021 /snap/core20/1434/usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root   root             87K Jul 14  2021 /snap/core20/1434/usr/bin/gpasswd
-rwsr-xr-x 1 root   root             52K Jul 14  2021 /snap/core20/1434/usr/bin/chsh
-rwsr-xr-x 1 root   root             84K Jul 14  2021 /snap/core20/1434/usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root   root            463K Dec  2  2021 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root   root            463K Dec  2  2021 /snap/core20/1434/usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root   root             59K Jan 25  2022 /snap/core18/2409/usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                                                             
-rwsr-xr-x 1 root   root             40K Jan 25  2022 /snap/core18/2409/usr/bin/newgrp  --->  HP-UX_10.20
-rwsr-xr-x 1 root   root             75K Jan 25  2022 /snap/core18/2409/usr/bin/gpasswd
-rwsr-xr-x 1 root   root             44K Jan 25  2022 /snap/core18/2409/usr/bin/chsh
-rwsr-xr-x 1 root   root             75K Jan 25  2022 /snap/core18/2409/usr/bin/chfn  --->  SuSE_9.3/10
-rwsr-xr-x 1 root   root             44K Jan 25  2022 /snap/core18/2409/bin/su
-rwsr-xr-x 1 root   root             39K Feb  7  2022 /usr/bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root   root             67K Feb  7  2022 /usr/bin/su
-rwsr-xr-x 1 root   root             55K Feb  7  2022 /usr/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8                                                                                                         
-rwsr-xr-x 1 root   root             39K Feb  7  2022 /snap/core20/1434/usr/bin/umount  --->  BSD/Linux(08-1996)
-rwsr-xr-x 1 root   root             67K Feb  7  2022 /snap/core20/1434/usr/bin/su
-rwsr-xr-x 1 root   root             55K Feb  7  2022 /snap/core20/1434/usr/bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8                                                                                        
-rwsr-xr-x 1 root   root             23K Feb 21  2022 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-x 1 root   root             31K Feb 21  2022 /usr/bin/pkexec  --->  Linux4.10_to_5.1.17(CVE-2019-13272)/rhel_6(CVE-2011-1485)                                                                                                            
-rwsr-xr-x 1 root   root            121K Apr  8  2022 /snap/snapd/15534/usr/lib/snapd/snap-confine
-rwsr-xr-x 1 root   root            140K Apr 27  2022 /usr/lib/snapd/snap-confine
-rwsr-xr-- 1 root   messagebus       51K Apr 29  2022 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-rwsr-xr-x 1 root   root            121K May 11  2022 /snap/snapd/15904/usr/lib/snapd/snap-confine
-rwsr-sr-x 1 root   root             17K May 11  2022 /opt/get-list

[+] SGID
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#sudo-and-suid                                            
-rwsr-sr-x 1 daemon daemon   55K Nov 12  2018 /usr/bin/at                                                                
-rwxr-sr-x 1 root   crontab 355K Mar  4  2019 /snap/core18/2128/usr/bin/ssh-agent
-rwxr-sr-x 1 root   shadow   23K Mar 22  2019 /snap/core18/2128/usr/bin/expiry
-rwxr-sr-x 1 root   shadow   71K Mar 22  2019 /snap/core18/2128/usr/bin/chage
-rwxr-sr-x 1 root   utmp     15K Sep 30  2019 /usr/lib/x86_64-linux-gnu/utempter/utempter
-rwxr-sr-x 1 root   crontab  43K Feb 13  2020 /usr/bin/crontab
-rwxr-sr-x 1 root   crontab 355K Mar  3  2020 /snap/core18/2409/usr/bin/ssh-agent
-rwxr-sr-x 1 root   tty      15K Mar 30  2020 /usr/bin/bsd-write
-rwxr-sr-x 1 root   tty      31K Sep 16  2020 /snap/core18/2409/usr/bin/wall
-rwxr-sr-x 1 root   tty      31K Sep 16  2020 /snap/core18/2128/usr/bin/wall
-rwxr-sr-x 1 root   shadow   34K Apr  8  2021 /snap/core18/2409/sbin/unix_chkpwd
-rwxr-sr-x 1 root   shadow   34K Apr  8  2021 /snap/core18/2409/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root   shadow   34K Apr  8  2021 /snap/core18/2128/sbin/unix_chkpwd
-rwxr-sr-x 1 root   shadow   34K Apr  8  2021 /snap/core18/2128/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root   shadow   31K Jul 14  2021 /usr/bin/expiry
-rwxr-sr-x 1 root   shadow   83K Jul 14  2021 /usr/bin/chage
-rwxr-sr-x 1 root   shadow   31K Jul 14  2021 /snap/core20/1434/usr/bin/expiry
-rwxr-sr-x 1 root   shadow   83K Jul 14  2021 /snap/core20/1434/usr/bin/chage
-rwxr-sr-x 1 root   shadow   43K Sep 17  2021 /usr/sbin/unix_chkpwd
-rwxr-sr-x 1 root   shadow   43K Sep 17  2021 /usr/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root   shadow   43K Sep 17  2021 /snap/core20/1434/usr/sbin/unix_chkpwd
-rwxr-sr-x 1 root   shadow   43K Sep 17  2021 /snap/core20/1434/usr/sbin/pam_extrausers_chkpwd
-rwxr-sr-x 1 root   ssh     343K Dec  2  2021 /usr/bin/ssh-agent
-rwxr-sr-x 1 root   crontab 343K Dec  2  2021 /snap/core20/1434/usr/bin/ssh-agent
-rwxr-sr-x 1 root   shadow   23K Jan 25  2022 /snap/core18/2409/usr/bin/expiry
-rwxr-sr-x 1 root   shadow   71K Jan 25  2022 /snap/core18/2409/usr/bin/chage
-rwxr-sr-x 1 root   tty      35K Feb  7  2022 /usr/bin/wall
-rwxr-sr-x 1 root   tty      35K Feb  7  2022 /snap/core20/1434/usr/bin/wall
-rwsr-sr-x 1 root   root     17K May 11  2022 /opt/get-list

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
/snap/core20/1434/usr/bin/ping = cap_net_raw+ep
/usr/lib/x86_64-linux-gnu/gstreamer1.0/gstreamer-1.0/gst-ptp-helper = cap_net_bind_service,cap_net_admin+ep
/usr/bin/traceroute6.iputils = cap_net_raw+ep
/usr/bin/ping = cap_net_raw+ep
/usr/bin/mtr-packet = cap_net_raw+ep

[+] Users with capabilities
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#capabilities                                             
                                                                                                                         
[+] Files with ACLs
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#acls                                                     
files with acls in searched folders Not Found                                                                            
                                                                                                                         
[+] .sh files in path
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#script-binaries-in-path                                  
/usr/bin/gettext.sh                                                                                                      
/usr/bin/rescan-scsi-bus.sh

[+] Unexpected in root
/lib32                                                                                                                   
/swap.img
/libx32
/lost+found

[+] Files (scripts) in /etc/profile.d/
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#profiles-files                                           
total 44                                                                                                                 
drwxr-xr-x   2 root root 4096 May 11  2022 .
drwxr-xr-x 102 root root 4096 May 18  2022 ..
-rw-r--r--   1 root root   96 Dec  5  2019 01-locale-fix.sh
-rw-r--r--   1 root root  835 Sep  9  2021 apps-bin-path.sh
-rw-r--r--   1 root root  729 Feb  2  2020 bash_completion.sh
-rw-r--r--   1 root root 1003 Aug 13  2019 cedilla-portuguese.sh
-rw-r--r--   1 root root 1107 Nov  3  2019 gawk.csh
-rw-r--r--   1 root root  757 Nov  3  2019 gawk.sh
-rw-r--r--   1 root root 1557 Feb 17  2020 Z97-byobu.sh
-rwxr-xr-x   1 root root  873 Jun  2  2020 Z99-cloudinit-warnings.sh
-rwxr-xr-x   1 root root 3417 Jun  2  2020 Z99-cloud-locale-test.sh

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
/home/bob/.bash_history
/root/

[+] Searching folders owned by me containing others files on it
                                                                                                                         
[+] Readable files belonging to root and readable by me but not world readable
                                                                                                                         
[+] Modified interesting files in the last 5mins (limit 100)
/var/log/auth.log                                                                                                        
/var/log/journal/b266781b406945aeb7b9b987494ac6b1/user-1000.journal
/var/log/journal/b266781b406945aeb7b9b987494ac6b1/system.journal
/var/log/vmware-vmsvc-root.log
/var/log/syslog
/var/log/kern.log
/home/bob/snap/lxd/common/config/config.yml
/home/bob/.gnupg/trustdb.gpg
/home/bob/.gnupg/pubring.kbx
/home/bob/.gnupg/crls.d/DIR.txt

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

[+] Files inside /home/bob (limit 20)
total 364                                                                                                                
drwxr-xr-x 5 bob  bob    4096 May 18 09:38 .
drwxr-xr-x 3 root root   4096 May 11  2022 ..
lrwxrwxrwx 1 root root      9 May 11  2022 .bash_history -> /dev/null
-rw-r--r-- 1 bob  bob     220 Feb 25  2020 .bash_logout
-rw-r--r-- 1 bob  bob    3771 Feb 25  2020 .bashrc
drwx------ 2 bob  bob    4096 May 11  2022 .cache
drwx------ 4 bob  bob    4096 May 18 09:38 .gnupg
-rwxrwxr-x 1 bob  bob  332111 May  5 08:06 linpeas.sh
-rw-r--r-- 1 bob  bob      33 May 18 07:36 local.txt
-rw-r--r-- 1 bob  bob     807 Feb 25  2020 .profile
drwx------ 3 bob  bob    4096 May 18 09:38 snap

[+] Files inside others home (limit 20)
                                                                                                                         
[+] Searching installed mail applications
                                                                                                                         
[+] Mails (limit 50)
                                                                                                                         
[+] Backup folders
drwxr-xr-x 2 root root 4096 Feb 17 12:42 /var/backups                                                                    
total 1856
-rw-r--r-- 1 root root  51200 May 18  2022 alternatives.tar.0
-rw-r--r-- 1 root root  38730 Feb 17 11:22 apt.extended_states.0
-rw-r--r-- 1 root root   4269 May 25  2022 apt.extended_states.1.gz
-rw-r--r-- 1 root root   4251 May 17  2022 apt.extended_states.2.gz
-rw-r--r-- 1 root root   4300 May 11  2022 apt.extended_states.3.gz
-rw-r--r-- 1 root root   3998 May 11  2022 apt.extended_states.4.gz
-rw-r--r-- 1 root root   3913 Oct 21  2021 apt.extended_states.5.gz
-rw-r--r-- 1 root root   3886 Aug 25  2021 apt.extended_states.6.gz
-rw-r--r-- 1 root root    268 Jan  7  2021 dpkg.diversions.0
-rw-r--r-- 1 root root    139 Jan  7  2021 dpkg.diversions.1.gz
-rw-r--r-- 1 root root    139 Jan  7  2021 dpkg.diversions.2.gz
-rw-r--r-- 1 root root    139 Jan  7  2021 dpkg.diversions.3.gz
-rw-r--r-- 1 root root    139 Jan  7  2021 dpkg.diversions.4.gz
-rw-r--r-- 1 root root    139 Jan  7  2021 dpkg.diversions.5.gz
-rw-r--r-- 1 root root    139 Jan  7  2021 dpkg.diversions.6.gz
-rw-r--r-- 1 root root    172 May 11  2022 dpkg.statoverride.0
-rw-r--r-- 1 root root    161 May 11  2022 dpkg.statoverride.1.gz
-rw-r--r-- 1 root root    161 May 11  2022 dpkg.statoverride.2.gz
-rw-r--r-- 1 root root    161 May 11  2022 dpkg.statoverride.3.gz
-rw-r--r-- 1 root root    161 May 11  2022 dpkg.statoverride.4.gz
-rw-r--r-- 1 root root    161 May 11  2022 dpkg.statoverride.5.gz
-rw-r--r-- 1 root root    161 May 11  2022 dpkg.statoverride.6.gz
-rw-r--r-- 1 root root 675890 May 18  2022 dpkg.status.0
-rw-r--r-- 1 root root 171660 May 18  2022 dpkg.status.1.gz
-rw-r--r-- 1 root root 171660 May 18  2022 dpkg.status.2.gz
-rw-r--r-- 1 root root 171660 May 18  2022 dpkg.status.3.gz
-rw-r--r-- 1 root root 171660 May 18  2022 dpkg.status.4.gz
-rw-r--r-- 1 root root 171660 May 18  2022 dpkg.status.5.gz
-rw-r--r-- 1 root root 171660 May 18  2022 dpkg.status.6.gz


[+] Backup files
-rw-r--r-- 1 root root 2743 Jul 31  2020 /etc/apt/sources.list.curtin.old                                                
-rw-r--r-- 1 root root 170 Feb 17 10:37 /run/blkid/blkid.tab.old
-rwxr-xr-x 1 root root 226 Feb 17  2020 /usr/share/byobu/desktop/byobu.desktop.old
-rw-r--r-- 1 root root 7867 Jul 16  1996 /usr/share/doc/telnet/README.old.gz
-rw-r--r-- 1 root root 392817 Feb  9  2020 /usr/share/doc/manpages/Changes.old.gz
-rw-r--r-- 1 root root 348 Feb 18  2022 /usr/share/man/man1/wsrep_sst_mariabackup.1.gz
-rw-r--r-- 1 root root 2756 Feb 13  2020 /usr/share/man/man8/vgcfgbackup.8.gz
-rw-r--r-- 1 root root 11886 May 11  2022 /usr/share/info/dir.old
-rw-r--r-- 1 root root 237986 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/.config.old
-rw-r--r-- 1 root root 0 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/include/config/net/team/mode/activebackup.h
-rw-r--r-- 1 root root 0 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/include/config/wm831x/backup.h
-rw-r--r-- 1 root root 237986 Apr 14  2022 /usr/src/linux-headers-5.4.0-110-generic/.config.old
-rw-r--r-- 1 root root 0 Apr 14  2022 /usr/src/linux-headers-5.4.0-110-generic/include/config/net/team/mode/activebackup.h
-rw-r--r-- 1 root root 0 Apr 14  2022 /usr/src/linux-headers-5.4.0-110-generic/include/config/wm831x/backup.h
-rwxr-xr-x 1 root root 1086 Nov 25  2019 /usr/src/linux-headers-5.4.0-113/tools/testing/selftests/net/tcp_fastopen_backup_key.sh
-rwxr-xr-x 1 root root 1086 Nov 25  2019 /usr/src/linux-headers-5.4.0-110/tools/testing/selftests/net/tcp_fastopen_backup_key.sh
-rw-r--r-- 1 root root 1413 May 11  2022 /usr/lib/python3/dist-packages/sos/report/plugins/__pycache__/ovirt_engine_backup.cpython-38.pyc                                                                                                         
-rw-r--r-- 1 root root 1802 Feb 15  2022 /usr/lib/python3/dist-packages/sos/report/plugins/ovirt_engine_backup.py
-rw-r--r-- 1 root root 9833 Apr 14  2022 /usr/lib/modules/5.4.0-110-generic/kernel/drivers/power/supply/wm831x_backup.ko
-rw-r--r-- 1 root root 9073 Apr 14  2022 /usr/lib/modules/5.4.0-110-generic/kernel/drivers/net/team/team_mode_activebackup.ko                                                                                                                     
-rw-r--r-- 1 root root 9833 May 18  2022 /usr/lib/modules/5.4.0-113-generic/kernel/drivers/power/supply/wm831x_backup.ko
-rw-r--r-- 1 root root 9073 May 18  2022 /usr/lib/modules/5.4.0-113-generic/kernel/drivers/net/team/team_mode_activebackup.ko                                                                                                                     
-rw-r--r-- 1 root root 44048 Oct 12  2021 /usr/lib/x86_64-linux-gnu/open-vm-tools/plugins/vmsvc/libvmbackup.so
-rwxr-xr-x 1 root root 43891 Feb 18  2022 /usr/bin/wsrep_sst_mariabackup

[+] Searching tables inside readable .db/.sql/.sqlite files (limit 100)
                                                                                                                         
[+] Web files?(output limit)
/var/www/:                                                                                                               
total 16K
drwxr-xr-x  4 root root  4.0K May 11  2022 .
drwxr-xr-x 14 root root  4.0K May 11  2022 ..
drwxr-xr-x  8 root root  4.0K May 11  2022 html
drwxr-xr-x  2  501 staff 4.0K Mar 15  2022 Search

/var/www/html:
total 96K
drwxr-xr-x 8 root root  4.0K May 11  2022 .

[+] Readable hidden interesting files
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#read-sensitive-data                                      
                                                                                                                         
[+] All hidden files (not in /sys/ or the ones listed in the previous check) (limit 70)
-rw------- 1 root root 0 Apr 28  2022 /snap/core18/2409/etc/.pwd.lock                                                    
-rw-r--r-- 1 root root 220 Apr  4  2018 /snap/core18/2409/etc/skel/.bash_logout
-rw-r--r-- 1 root root 3771 Apr  4  2018 /snap/core18/2409/etc/skel/.bashrc
-rw-r--r-- 1 root root 807 Apr  4  2018 /snap/core18/2409/etc/skel/.profile
-rw-r--r-- 1 root root 39 Apr 28  2022 /snap/core18/2409/var/home/.gitignore
-rw------- 1 root root 0 Jul 22  2021 /snap/core18/2128/etc/.pwd.lock
-rw-r--r-- 1 root root 220 Apr  4  2018 /snap/core18/2128/etc/skel/.bash_logout
-rw-r--r-- 1 root root 3771 Apr  4  2018 /snap/core18/2128/etc/skel/.bashrc
-rw-r--r-- 1 root root 807 Apr  4  2018 /snap/core18/2128/etc/skel/.profile
-rw-r--r-- 1 root root 39 Jul 22  2021 /snap/core18/2128/var/home/.gitignore
-rw------- 1 root root 0 Mar 29  2022 /snap/core20/1434/etc/.pwd.lock
-rw-r--r-- 1 root root 220 Feb 25  2020 /snap/core20/1434/etc/skel/.bash_logout
-rw-r--r-- 1 root root 3771 Feb 25  2020 /snap/core20/1434/etc/skel/.bashrc
-rw-r--r-- 1 root root 807 Feb 25  2020 /snap/core20/1434/etc/skel/.profile
-rw-r--r-- 1 root root 102 Feb 13  2020 /etc/cron.monthly/.placeholder
-rw-r--r-- 1 root root 102 Feb 13  2020 /etc/cron.weekly/.placeholder
-rw-r--r-- 1 root root 102 Feb 13  2020 /etc/cron.d/.placeholder
-rw-r--r-- 1 root root 102 Feb 13  2020 /etc/cron.hourly/.placeholder
-rw------- 1 root root 0 Jul 31  2020 /etc/.pwd.lock
-rw-r--r-- 1 root root 102 Feb 13  2020 /etc/cron.daily/.placeholder
-rw-r--r-- 1 root root 220 Feb 25  2020 /etc/skel/.bash_logout
-rw-r--r-- 1 root root 3771 Feb 25  2020 /etc/skel/.bashrc
-rw-r--r-- 1 root root 807 Feb 25  2020 /etc/skel/.profile
-rw-r--r-- 1 501 staff 6148 Mar 14  2022 /var/www/html/scss/.DS_Store
-rw-r--r-- 1 landscape landscape 0 Jul 31  2020 /var/lib/landscape/.cleanup.user
-rw------- 1 root root 0 Feb 17 10:42 /run/snapd/lock/.lock
-rw-r--r-- 1 root root 20 Feb 17 10:42 /run/cloud-init/.instance-id
-rw-r--r-- 1 root root 2 May 18 07:36 /run/cloud-init/.ds-identify.result
-rw-r--r-- 1 bob bob 220 Feb 25  2020 /home/bob/.bash_logout
-rw-r--r-- 1 bob bob 3771 Feb 25  2020 /home/bob/.bashrc
-rw-r--r-- 1 bob bob 807 Feb 25  2020 /home/bob/.profile
-rw-r--r-- 1 root root 4409 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/basic/.fixdep.cmd
-rw-r--r-- 1 root root 4732 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/.asn1_compiler.cmd
-rw-r--r-- 1 root root 6628 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/.insert-sys-cert.cmd
-rw-r--r-- 1 root root 1655 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/.bin2c.cmd
-rw-r--r-- 1 root root 3686 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/.conmakehash.cmd
-rw-r--r-- 1 root root 8168 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/.sign-file.cmd
-rw-r--r-- 1 root root 216 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/genksyms/.parse.tab.c.cmd
-rw-r--r-- 1 root root 155 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/genksyms/.genksyms.cmd
-rw-r--r-- 1 root root 126 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/genksyms/.lex.lex.c.cmd
-rw-r--r-- 1 root root 3756 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/genksyms/.parse.tab.o.cmd
-rw-r--r-- 1 root root 4225 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/genksyms/.genksyms.o.cmd
-rw-r--r-- 1 root root 4770 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/genksyms/.lex.lex.o.cmd
-rw-r--r-- 1 root root 5242 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/.sortextable.cmd
-rw-r--r-- 1 root root 6805 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/selinux/mdp/.mdp.cmd
-rw-r--r-- 1 root root 5973 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/selinux/genheaders/.genheaders.cmd
-rw-r--r-- 1 root root 6749 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/.extract-cert.cmd
-rw-r--r-- 1 root root 5084 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/mod/.file2alias.o.cmd
-rw-r--r-- 1 root root 3430 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/mod/.empty.o.cmd
-rw-r--r-- 1 root root 3889 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/mod/.mk_elfconfig.cmd
-rw-r--r-- 1 root root 104 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/mod/.elfconfig.h.cmd
-rw-r--r-- 1 root root 6884 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/mod/.devicetable-offsets.s.cmd
-rw-r--r-- 1 root root 131 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/mod/.modpost.cmd
-rw-r--r-- 1 root root 6952 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/mod/.modpost.o.cmd
-rw-r--r-- 1 root root 6428 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/mod/.sumversion.o.cmd
-rw-r--r-- 1 root root 129 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/kconfig/.lexer.lex.c.cmd
-rw-r--r-- 1 root root 4065 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/kconfig/.preprocess.o.cmd
-rw-r--r-- 1 root root 4227 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/kconfig/.parser.tab.o.cmd
-rw-r--r-- 1 root root 5349 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/kconfig/.conf.o.cmd
-rw-r--r-- 1 root root 4987 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/kconfig/.lexer.lex.o.cmd
-rw-r--r-- 1 root root 176 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/kconfig/.parser.tab.h.cmd
-rw-r--r-- 1 root root 245 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/kconfig/.conf.cmd
-rw-r--r-- 1 root root 5738 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/kconfig/.confdata.o.cmd
-rw-r--r-- 1 root root 4147 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/kconfig/.symbol.o.cmd
-rw-r--r-- 1 root root 4233 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/kconfig/.expr.o.cmd
-rw-r--r-- 1 root root 4941 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/.recordmcount.cmd
-rw-r--r-- 1 root root 3950 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/scripts/.kallsyms.cmd
-rw-r--r-- 1 root root 237838 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/.config
-rw-r--r-- 1 root root 237986 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/.config.old
-rw-r--r-- 1 root root 14556 May 18  2022 /usr/src/linux-headers-5.4.0-113-generic/kernel/.bounds.s.cmd
grep: write error: Broken pipe

[+] Readable files inside /tmp, /var/tmp, /private/tmp, /private/var/at/tmp, /private/var/tmp, and backup folders (limit 70)                                                                                                                      
-rw-r--r-- 1 root root 172 May 11  2022 /var/backups/dpkg.statoverride.0                                                 
-rw-r--r-- 1 root root 268 Jan  7  2021 /var/backups/dpkg.diversions.0
-rw-r--r-- 1 root root 3886 Aug 25  2021 /var/backups/apt.extended_states.6.gz
-rw-r--r-- 1 root root 161 May 11  2022 /var/backups/dpkg.statoverride.4.gz
-rw-r--r-- 1 root root 675890 May 18  2022 /var/backups/dpkg.status.0
-rw-r--r-- 1 root root 171660 May 18  2022 /var/backups/dpkg.status.6.gz
-rw-r--r-- 1 root root 3913 Oct 21  2021 /var/backups/apt.extended_states.5.gz
-rw-r--r-- 1 root root 38730 Feb 17 11:22 /var/backups/apt.extended_states.0
-rw-r--r-- 1 root root 139 Jan  7  2021 /var/backups/dpkg.diversions.3.gz
-rw-r--r-- 1 root root 51200 May 18  2022 /var/backups/alternatives.tar.0
-rw-r--r-- 1 root root 4251 May 17  2022 /var/backups/apt.extended_states.2.gz
-rw-r--r-- 1 root root 3998 May 11  2022 /var/backups/apt.extended_states.4.gz
-rw-r--r-- 1 root root 161 May 11  2022 /var/backups/dpkg.statoverride.2.gz
-rw-r--r-- 1 root root 161 May 11  2022 /var/backups/dpkg.statoverride.3.gz
-rw-r--r-- 1 root root 139 Jan  7  2021 /var/backups/dpkg.diversions.1.gz
-rw-r--r-- 1 root root 161 May 11  2022 /var/backups/dpkg.statoverride.6.gz
-rw-r--r-- 1 root root 171660 May 18  2022 /var/backups/dpkg.status.2.gz
-rw-r--r-- 1 root root 139 Jan  7  2021 /var/backups/dpkg.diversions.5.gz
-rw-r--r-- 1 root root 4300 May 11  2022 /var/backups/apt.extended_states.3.gz
-rw-r--r-- 1 root root 161 May 11  2022 /var/backups/dpkg.statoverride.5.gz
-rw-r--r-- 1 root root 161 May 11  2022 /var/backups/dpkg.statoverride.1.gz
-rw-r--r-- 1 root root 4269 May 25  2022 /var/backups/apt.extended_states.1.gz
-rw-r--r-- 1 root root 171660 May 18  2022 /var/backups/dpkg.status.3.gz
-rw-r--r-- 1 root root 139 Jan  7  2021 /var/backups/dpkg.diversions.6.gz
-rw-r--r-- 1 root root 139 Jan  7  2021 /var/backups/dpkg.diversions.4.gz
-rw-r--r-- 1 root root 171660 May 18  2022 /var/backups/dpkg.status.5.gz
-rw-r--r-- 1 root root 171660 May 18  2022 /var/backups/dpkg.status.4.gz
-rw-r--r-- 1 root root 139 Jan  7  2021 /var/backups/dpkg.diversions.2.gz
-rw-r--r-- 1 root root 171660 May 18  2022 /var/backups/dpkg.status.1.gz

[+] Interesting writable files owned by me or writable by everyone (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files                                           
/dev/mqueue                                                                                                              
/dev/shm
/home/bob
/run/lock
/run/screen
/run/screen/S-bob
/run/user/1000
/run/user/1000/dbus-1
/run/user/1000/dbus-1/services
/run/user/1000/gnupg
/run/user/1000/inaccessible
/run/user/1000/systemd
/run/user/1000/systemd/transient
/run/user/1000/systemd/units
/snap/core18/2128/tmp
/snap/core18/2128/var/tmp
/snap/core18/2409/tmp
/snap/core18/2409/var/tmp
/snap/core20/1434/run/lock
/snap/core20/1434/tmp
/snap/core20/1434/var/tmp
/tmp
/tmp/.font-unix
/tmp/.ICE-unix
/tmp/.Test-unix
/tmp/tmux-1000
/tmp/.X11-unix
#)You_can_write_even_more_files_inside_last_directory

/var/crash
/var/lib/php/sessions
/var/tmp

[+] Interesting GROUP writable files (not in Home) (max 500)
[i] https://book.hacktricks.xyz/linux-unix/privilege-escalation#writable-files                                           
  Group bob:                                                                                                             
                                                                                                                         

[+] Searching passwords in config PHP files
                                                                                                                         
[+] Checking for TTY (sudo/su) passwords in audit logs
                                                                                                                         
[+] Finding IPs inside logs (limit 70)
      4 /var/log/journal/b266781b406945aeb7b9b987494ac6b1/user-1000@a18a5118db084efb8d30e00eeb0f14a6-0000000000005c67-0005deba63fc16d8.journal:192.168.118.14
      2 /var/log/wtmp:192.168.118.18
      2 /var/log/wtmp:192.168.118.14
      1 /var/log/wtmp:192.168.45.156
      1 /var/log/lastlog:192.168.45.156
      1 /var/log/lastlog:192.168.118.14

[+] Finding passwords inside logs (limit 70)
Binary file /var/log/cloud-init.log matches                                                                              
Binary file /var/log/journal/b266781b406945aeb7b9b987494ac6b1/user-1000.journal matches
/var/log/cloud-init.log:2022-05-11 10:56:41,961 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
/var/log/cloud-init.log:2022-05-11 11:01:30,771 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
/var/log/cloud-init.log:2022-05-17 19:22:04,292 - helpers.py[DEBUG]: config-set-passwords already ran (freq=once-per-instance)
/var/log/dmesg.0:[    3.852147] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
/var/log/dmesg.0:[    4.452729] systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
/var/log/dmesg.0:[    4.453394] systemd[1]: Condition check resulted in Forward Password Requests to Plymouth Directory Watch being skipped.
/var/log/dmesg:[   93.093503] systemd[1]: Started Forward Password Requests to Wall Directory Watch.

[+] Finding emails inside logs (limit 70)
      1 /var/log/dmesg:giometti@linux.it                                                                                 
      1 /var/log/dmesg:dm-devel@redhat.com
      1 /var/log/dmesg.0:giometti@linux.it
      1 /var/log/dmesg.0:dm-devel@redhat.com

[+] Finding *password* or *credential* files in home (limit 70)
                                                                                                                         
[+] Finding passwords inside key folders (limit 70) - only PHP files
/var/www/html/config.php:    define('DATABASE', 'wheels');                                                               
/var/www/html/config.php:    define('PASSWORD', 'CanRipperCrackthis?09');
/var/www/html/config.php:    define('USER', 'wheels');
/var/www/html/login.php:        $password = $_POST['password'];
/var/www/html/login.php:                      <input type="password" name="password" required />
/var/www/html/register.php:        $password = $_POST['password'];
/var/www/html/register.php:        $password_hash = password_hash($password, PASSWORD_BCRYPT);
/var/www/html/register.php:            $query->bindParam("password_hash", $password_hash, PDO::PARAM_STR);
/var/www/html/register.php:                    <input type="password" name="password" required />

[+] Finding passwords inside key folders (limit 70) - no PHP files
/etc/apache2/sites-available/default-ssl.conf:          #        file needs this password: `xxj31ZMTZzkVA'.              
/etc/cloud/cloud.cfg:     lock_passwd: True
/etc/cloud/cloud.cfg:     sudo: ["ALL=(ALL) NOPASSWD:ALL"]
/etc/debconf.conf:#BindPasswd: secret
/etc/nsswitch.conf:passwd:         files systemd
/etc/overlayroot.conf:#      $ MAPNAME="secure"; DEV="/dev/vdg"; PASSWORD="foobar"
/etc/overlayroot.conf:#     crypt:dev=/dev/vdb,pass=somepassword,mkfs=0
/etc/pam.d/common-password:password     [success=1 default=ignore]      pam_unix.so obscure sha512
/etc/security/namespace.init:                gid=$(echo "$passwd" | cut -f4 -d":")
/etc/security/namespace.init:        homedir=$(echo "$passwd" | cut -f6 -d":")
/etc/security/namespace.init:        passwd=$(getent passwd "$user")
/etc/sos/sos.conf:#password = true
/etc/ssl/openssl.cnf:challengePassword          = A challenge password
/etc/ssl/openssl.cnf:challengePassword_max              = 20
/etc/ssl/openssl.cnf:challengePassword_min              = 4
/etc/ssl/openssl.cnf:# input_password = secret
/etc/ssl/openssl.cnf:# output_password = secret
/var/backups/dpkg.status.0:Depends: passwd, debconf (>= 0.5) | debconf-2.0

[+] Finding possible password variables inside key folders (limit 140)
/var/www/html/lib/tempusdominus/js/tempusdominus-bootstrap-4.js:        DATA_API_KEY = '.data-api',                      

[+] Finding possible password in config files
 /etc/adduser.conf                                                                                                       
passwd
 /etc/nsswitch.conf
passwd:         files systemd
 /etc/apache2/apache2.conf
passwd files from being
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
 /etc/sysctl.d/10-ptrace.conf
credentials that exist in memory (re-using existing SSH connections,
 /etc/security/faillock.conf
passwd and ignore centralized (AD, IdM, LDAP, etc.) users.

[+] Finding 'username' string inside key folders (limit 70)
/var/www/html/login.php:        $query = $connection->prepare("SELECT * FROM users WHERE username=:username");           
/var/www/html/login.php:        $query->bindParam("username", $username, PDO::PARAM_STR);
/var/www/html/login.php:        $username = $_POST['username'];
/var/www/html/login.php:                      <input type="text" name="username" pattern="[a-zA-Z0-9]+" required />
/var/www/html/register.php:            $query->bindParam("username", $username, PDO::PARAM_STR);
/var/www/html/register.php:        $username = $_POST['username'];
/var/www/html/register.php:                    <input type="text" name="username" pattern="[a-zA-Z0-9]+" required />

[+] Searching specific hashes inside files - less false positives (limit 70)

```

