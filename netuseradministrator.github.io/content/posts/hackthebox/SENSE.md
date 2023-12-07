
+++
title = 'SENSE'
date = '2023-12-07T16:08:29+08:00'
draft = true
+++
```
┌──(root💀Chinchin)-[~/桌面/htb]
└─# nmap -sS -A -sC -sV -p- --min-rate 5000 10.129.85.125
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-03 16:29 CST
Nmap scan report for 10.129.85.125
Host is up (0.58s latency).
Not shown: 65533 filtered tcp ports (no-response)
PORT    STATE SERVICE    VERSION
80/tcp  open  http       lighttpd 1.4.35
|_http-title: Did not follow redirect to https://10.129.85.125/
|_http-server-header: lighttpd/1.4.35
443/tcp open  ssl/https?
| ssl-cert: Subject: commonName=Common Name (eg, YOUR name)/organizationName=CompanyName/stateOrProvinceName=Somewhere/countryName=US
| Not valid before: 2017-10-14T19:21:35
|_Not valid after:  2023-04-06T19:21:35
|_ssl-date: TLS randomness does not represent time
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Device type: general purpose|specialized
Running (JUST GUESSING): OpenBSD 4.X (93%), Comau embedded (92%)
OS CPE: cpe:/o:openbsd:openbsd:4.0
Aggressive OS guesses: OpenBSD 4.0 (93%), Comau C4G robot control unit (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops

TRACEROUTE (using port 443/tcp)
HOP RTT       ADDRESS
1   797.66 ms 10.10.16.1
2   797.81 ms 10.129.85.125

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 63.72 seconds

```

