
+++
title = 'OSCP靶场'
date = '2023-12-07T16:08:29+08:00'
draft = true
+++
![在这里插入图片描述](https://img-blog.csdnimg.cn/ee2924a7ca634bb98035aa2fd90424ca.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg3OTM0NA==,size_16,color_FFFFFF,t_70)

![image-20230526161100776](C:\Users\root\AppData\Roaming\Typora\typora-user-images\image-20230526161100776.png)

| <?php |                                            |
| ----- | ------------------------------------------ |
|       |                                            |
|       | print $_POST['ip'];                        |
|       | if (isset($_POST['submit'])){              |
|       | $target = $_REQUEST[ 'ip' ];               |
|       | echo '<pre>';                              |
|       | echo shell_exec( 'ping -c 3 ' . $target ); |
|       | echo '</pre>';                             |
|       | }                                          |
|       | ?>                                         |
|       | </pre>                                     |