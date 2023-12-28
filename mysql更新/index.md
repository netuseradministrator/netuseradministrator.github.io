# mysql更新






**MYSQL8.x****版本更新**

**系统版本：windows11**

**步骤1**

官网下载最新版8.0.35，下载链接[MySQL :: Download MySQL Community Server](https://dev.mysql.com/downloads/mysql/8.0.html)

![img](https://typora-1321866717.cos.ap-hongkong.myqcloud.com/typora/clip_image002.jpg)

**步骤2**

查询当前mysql的版本，连接到数据库后执行查询语句select version(); 

**![img](https://typora-1321866717.cos.ap-hongkong.myqcloud.com/typora/clip_image003.png)**

**步骤3（重要步骤，建议在DBA允许的情况下慎重操作）**

备份所有的数据库文件

mysqldump -u root -p --all-databases > D:\backup.sql

![img](https://typora-1321866717.cos.ap-hongkong.myqcloud.com/typora/clip_image005.jpg)

**步骤4（重要步骤，建议在DBA允许的情况下慎重操作）**

以管理员权限停止mysql服务，将下图中mysql-8.0.35-winx64文件里的所有文件拷贝到旧版本的对应目录下![img](https://typora-1321866717.cos.ap-hongkong.myqcloud.com/typora/clip_image007.jpg)

需要拷贝的所有文件如下图所示

![img](https://typora-1321866717.cos.ap-hongkong.myqcloud.com/typora/clip_image009.jpg)

拷贝到旧版本mysql的对应目录下，旧版本下的my.ini配置文件不要更改

![img](https://typora-1321866717.cos.ap-hongkong.myqcloud.com/typora/clip_image011.jpg)

**步骤5**

以管理员权限重启mysql服务，查看版本是否更新成功

![img](https://typora-1321866717.cos.ap-hongkong.myqcloud.com/typora/clip_image013.jpg)

![img](https://typora-1321866717.cos.ap-hongkong.myqcloud.com/typora/clip_image015.jpg)

 

 

**系统版本：SUSE Linux Enterprise 15**

**步骤1**

官网下载最新版8.0.35，下载链接[https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-8.0.35-1.sl15.x86_64.rpm-bundle.tar](https://cdn.mysql.com/Downloads/MySQL-8.0/mysql-8.0.35-1.sl15.x86_64.rpm-bundle.tar)，下载后解压

![img](https://typora-1321866717.cos.ap-hongkong.myqcloud.com/typora/clip_image017.jpg)

**步骤2**

查询当前mysql的版本，连接到数据库后执行查询语句select version(); 

![img](https://typora-1321866717.cos.ap-hongkong.myqcloud.com/typora/clip_image019.jpg)

**步骤3（重要步骤，建议在DBA允许的情况下慎重操作）**

备份所有的数据库文件命令sudo mysqldump -u root -p --all-databases > /root/databases.sql

![img](https://typora-1321866717.cos.ap-hongkong.myqcloud.com/typora/clip_image021.jpg)

**步骤4（重要步骤，建议在DBA允许的情况下慎重操作）**

停止mysql进程   systemctl stop mysql

卸载原先的mysql程序 查看已安装的mysql应用rpm -qa | grep mysql

![img](https://typora-1321866717.cos.ap-hongkong.myqcloud.com/typora/clip_image023.jpg)

卸载mysql命令 

rpm -ev mysql-community-libs-8.0.28-1.sl15.x86_64

mysql-community-common-8.0.28-1.sl15.x86_64

mysql-community-icu-data-files-8.0.28-1.sl15.x86_64

mysql-community-client-plugins-8.0.28-1.sl15.x86_64

mysql-community-server-8.0.28-1.sl15.x86_64

mysql-community-client-8.0.28-1.sl15.x86_64

删除所有程序，删除后使用rpm -qa | grep mysql查看有无残留

**步骤5（重要步骤，建议在DBA允许的情况下慎重操作）**

重新安装mysql 8.0.35，按照以下命令的顺序进行安装

rpm -ivh mysql-community-common-8.0.35-1.sl15.x86_64.rpm

rpm -ivh mysql-community-icu-data-files-8.0.35-1.sl15.x86_64.rpm

rpm -ivh mysql-community-client-plugins-8.0.35-1.sl15.x86_64.rpm

rpm -ivh mysql-community-libs-8.0.35-1.sl15.x86_64.rpm

rpm -ivh mysql-community-client-8.0.35-1.sl15.x86_64.rpm

rpm -ivh mysql-community-server-8.0.35-1.sl15.x86_64.rpm

**步骤6**

重启mysql 

Systemctl start mysql

连接到mysql，mysql账户密码和之前旧版本中的相同。

![img](https://typora-1321866717.cos.ap-hongkong.myqcloud.com/typora/clip_image029.jpg)

 

 

 

 
