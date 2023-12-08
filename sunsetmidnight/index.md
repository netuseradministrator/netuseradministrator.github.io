# SunsetMidnight

```
┌──(root㉿kali)-[~]
└─# nmap -sV -sS -A --min-rate 5000 -p- 192.168.192.88        
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-26 14:18 CST
Nmap scan report for 192.168.192.88
Host is up (0.21s latency).
Not shown: 65532 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 9cfe0b8b8d15e7727e3c23e58655512d (RSA)
|   256 feebef5d40e706679b6367f8d97ed3e2 (ECDSA)
|_  256 3583682c338bb46c2421200d52edcd16 (ED25519)
80/tcp   open  http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
| http-robots.txt: 1 disallowed entry 
|_/wp-admin/
|_http-title: Did not follow redirect to http://sunset-midnight/
3306/tcp open  mysql   MySQL 5.5.5-10.3.22-MariaDB-0+deb10u1
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.22-MariaDB-0+deb10u1
|   Thread ID: 15
|   Capabilities flags: 63486
|   Some Capabilities: Speaks41ProtocolNew, Support41Auth, SupportsTransactions, SupportsLoadDataLocal, Speaks41ProtocolOld, IgnoreSigpipes, FoundRows, ODBCClient, InteractiveClient, IgnoreSpaceBeforeParenthesis, DontAllowDatabaseTableColumn, LongColumnFlag, SupportsCompression, ConnectWithDatabase, SupportsAuthPlugins, SupportsMultipleStatments, SupportsMultipleResults
|   Status: Autocommit
|   Salt: \~*P8bg`*P3OqkEU\NS5
|_  Auth Plugin Name: mysql_native_password
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.93%E=4%D=5/26%OT=22%CT=1%CU=34273%PV=Y%DS=4%DC=T%G=Y%TM=64704F8
OS:4%P=x86_64-pc-linux-gnu)SEQ(SP=106%GCD=1%ISR=108%TI=Z%II=I%TS=A)SEQ(SP=1
OS:06%GCD=1%ISR=108%TI=Z%TS=1)OPS(O1=M0ST11NW7%O2=M0ST11NW7%O3=M0NNT11NW7%O
OS:4=M0ST11NW7%O5=M0ST11NW7%O6=M0ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W
OS:5=FE88%W6=FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=M0NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T
OS:=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=Y%DF=Y%T=40%W=0%S=Z%
OS:A=S+%F=AR%O=%RD=0%Q=)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%
OS:RID=G%RIPCK=G%RUCK=D4AC%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 554/tcp)
HOP RTT       ADDRESS
1   205.79 ms 192.168.45.1
2   205.89 ms 192.168.45.254
3   205.99 ms 192.168.251.1
4   206.18 ms 192.168.192.88

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 57.99 seconds

```

```
wpscan --url http://sunset-midnight/ --usernames admin --passwords /usr/share/wordlists/rockyou.txt
```

## 爆破没有得到结果，访问robots.txt

```
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

```

## 访问/wp-admin，查看源代码发现了一些ajax的接口

```
<script>
var spAjax = {"url":"http:\/\/sunset-midnight\/wp-admin\/admin-ajax.php"};
</script>
<script src='http://sunset-midnight/wp-content/plugins/simply-poll-master/script/simplypoll.js?ver=1.4'></script>
<script>
var _zxcvbnSettings = {"src":"http:\/\/sunset-midnight\/wp-includes\/js\/zxcvbn.min.js"};
</script>
<script src='http://sunset-midnight/wp-includes/js/zxcvbn-async.min.js?ver=1.0'></script>
<script>
var pwsL10n = {"unknown":"Password strength unknown","short":"Very weak","bad":"Weak","good":"Medium","strong":"Strong","mismatch":"Mismatch"};
</script>
<script src='http://sunset-midnight/wp-admin/js/password-strength-meter.min.js?ver=5.4.2'></script>
<script src='http://sunset-midnight/wp-includes/js/underscore.min.js?ver=1.8.3'></script>
<script>
var _wpUtilSettings = {"ajax":{"url":"\/wp-admin\/admin-ajax.php"}};
</script>
<script src='http://sunset-midnight/wp-includes/js/wp-util.min.js?ver=5.4.2'></script>
<script>
var userProfileL10n = {"warn":"Your new password has not been saved.","warnWeak":"Confirm use of weak password","show":"Show","hide":"Hide","cancel":"Cancel","ariaShow":"Show password","ariaHide":"Hide password"};
</script>
<script src='http://sunset-midnight/wp-admin/js/user-profile.min.js?ver=5.4.2'></script>
	<div class="clear"></div>
	</body>
	</html>
	
```

尝试构造了请求，但是没有什么收获。看了下walkthrough,发现走的路线不正确，原本想构造接口，看看有没有提供有用信息的接口，但是action参数不管传啥都返回0

```

```

![image-20230526154858655](/image/image-20230526154858655.png)

