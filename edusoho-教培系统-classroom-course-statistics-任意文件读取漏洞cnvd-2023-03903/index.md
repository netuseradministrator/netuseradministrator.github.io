# edusoho 教培系统 classroom-course-statistics 任意文件读取漏洞（CNVD-2023-03903）

    ## fofa

```
title="Powered By EduSoho" || body="Powered by <a href=\"http://www.edusoho.com/\" target=\"_blank\">EduSoho" || (body="Powered By EduSoho" && body="var app")
```

EduSoho教培系统是由杭州阔知网络科技有限公司研发的开源网校系统,该教培系统<v22.4.7 存在未授权任意文件读取漏洞，通过该漏洞攻击者可以读取到config/parameters.yml文件的内容，拿到该文件中保存的secret值以及数据库账号密码等敏感信息。拿到secret值后，攻击者可以结合symfony框架_fragment路由实现RCE



## poc
