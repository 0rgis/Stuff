```sh
map -sV -A -p-65535 10.10.90.182 -v

Nmap scan report for 10.10.90.182
Host is up (0.038s latency).
Not shown: 65532 closed ports
PORT      STATE SERVICE VERSION
**80/tcp    open  http    nginx 1.16.1**
| http-methods: 
|_  Supported Methods: GET HEAD
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: nginx/1.16.1
|_http-title: Welcome to nginx!
**6498/tcp  open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)**
| ssh-hostkey: 
|   2048 30:4a:2b:22:ac:d9:56:09:f2:da:12:20:57:f4:6c:d4 (RSA)
|   256 bf:86:c9:c7:b7:ef:8c:8b:b9:94:ae:01:88:c0:85:4d (ECDSA)
|_  256 a1:72:ef:6c:81:29:13:ef:5a:6c:24:03:4c:fe:3d:0b (ED25519)
**65524/tcp open  http    Apache httpd 2.4.43 ((Ubuntu))**
| http-methods: 
|_  Supported Methods: OPTIONS HEAD GET POST
| http-robots.txt: 1 disallowed entry 
|_/
|_http-server-header: Apache/2.4.43 (Ubuntu)
|_http-title: Apache2 Debian Default Page: It works
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 12:21
Completed NSE at 12:21, 0.00s elapsed
Initiating NSE at 12:21
Completed NSE at 12:21, 0.00s elapsed
Initiating NSE at 12:21
Completed NSE at 12:21, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 28.55 seconds
```

next lot of text