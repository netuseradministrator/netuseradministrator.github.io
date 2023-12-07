
+++
title = 'webdeveloper靶机'
date = '2023-12-07T16:08:29+08:00'
draft = true
+++

将靶机设置为桥接模式，和其他机器处于一个局域网里。arp-scan -l查看局域网里其他主机，发现VMWARE的描述，确定靶机的IP地址![image-20230307121430030](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230307121430030.png)

探测靶机开放的端口，对端口上的服务进行识别（goby会更方便）![image-20230307121521145](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230307121521145.png)

80端口的网站是wordpress框架搭建的，用dirb爆破下目录

![image-20230307122641647](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230307122641647.png)

/ipdata路径下有个.cap文件，wireshark打开，检索到登录的数据包![image-20230307132218726](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230307132218726.png)

用账户密码登录到后台，翻看有啥插件可以利用

![image-20230307133619014](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230307133619014.png)

利用file manager查看根目录下的配置文件![image-20230307133730804](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230307133730804.png)

拿到了数据库的配置文件，数据库的连接用户名和密码![image-20230307134054029](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230307134054029.png)

猜想，他的数据库用户名和密码有可能重复使用，作为SSH服务的账户密码，尝试登录

![image-20230307134136074](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230307134136074.png)

登陆成功，但是没有权限访问/root目录

sudo -l查看所有可以用root权限运行的命令![image-20230307134537279](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230307134537279.png)

结合网上教程，新建一个文件，![image-20230307134705518](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230307134705518.png)

赋予/root目录所有用户可读写权限![image-20230307134747630](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230307134747630.png)

```shell
sudo tcpdump -i eth0 -w /dev/null -W 1 -G 1 -z 1 -Z root

```

-Z参数指定使用root用户执行，-z参数指定要执行的命令从文件1中读取

成功访问/root/flag.txt

![image-20230307134949730](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230307134949730.png)