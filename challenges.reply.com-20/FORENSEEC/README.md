#### Challenge:

R-Boy is suddenly thrown into a future post-apocalyptic era, arriving in the last ‘free human’ city. Everyone here is safe here, but the rest of the earth is ruled by Zer0. The all-seeing Zer0 has developed Antani, a new machine learning algorithm that uses the power of quantum computing to exploit humans as a ring in the master Tapioca blockchain.

The free humans have managed to steal a big file from a machine in an ancient building, which could reveal the key to Zer0’s power, defeat his terrible reign, and help R-boy return to the present.

---

#### Solution:

We are provided with what seems like an memory dump image. Running volatility to determine the profile:

```bash
python ./volatility/vol.py -f 699cef6a816882f0e02b40e1fe4d7e93.raw imageinfo
```

Returns:

```text
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win10x86_18362, Win10x86_17763
                     AS Layer1 : IA32PagedMemoryPae (Kernel AS)
                     AS Layer2 : VirtualBoxCoreDumpElf64 (Unnamed AS)
                     AS Layer3 : FileAddressSpace (/home/mfabry/Documents/challenge-replyers/misc200/699cef6a816882f0e02b40e1fe4d7e93.raw)
                      PAE type : PAE
                           DTB : 0x1a8000L
                          KDBG : 0x81895770L
          Number of Processors : 4
     Image Type (Service Pack) : 0
                KPCR for CPU 0 : 0x80a05000L
                KPCR for CPU 1 : 0x8a125000L
                KPCR for CPU 2 : 0x8a1a0000L
                KPCR for CPU 3 : 0x8a1f3000L
             KUSER_SHARED_DATA : 0xffdf0000L
           Image date and time : 2020-10-03 15:30:35 UTC+0000
     Image local date and time : 2020-10-03 17:30:35 +0200
```

Using `profile=Win10x86_17763` we try different volatility plugins, and in the list of processes returned by `pslist` we notice `firefox.exe` and `TimeVault.exe`.

Extracting the `TimeVault.exe`:

```bash
python ./volatility/vol.py -f 699cef6a816882f0e02b40e1fe4d7e93.raw --profile=Win10x86_17763 dumpfiles -n -r TimeVault\\.exe --dump-dir .
```

gives us executable binary that is requesting password:

```bash
./TimeVault.exe
Enter password:
asdffdsa
Padding is invalid and cannot be removed.
```

Going back to the image we wanted to check the firefox history, but the volatility firefox history plugin didn't work for some reason, so we had to get our hands dirty and dump the FF's `sqlite` database:

```bash
python ./volatility/vol.py -f 699cef6a816882f0e02b40e1fe4d7e93.raw --profile=Win10x86_17763 dumpfiles -n -r places\.sqlite --dump-dir .
```

Then we took a look at the history via `sqlite3`:

```bash
sqlite3 file.5660.0xb35a1290.places.sqlite.vacb
```

```sqlite
select * from moz_places;
```

returns:

```text
1|https://support.mozilla.org/it/products/firefox||gro.allizom.troppus.|0|0|0|131||zHkfBE00JIno|1|47360181922435|||1
2|https://support.mozilla.org/it/kb/customize-firefox-controls-buttons-and-toolbars?utm_source=firefox-browser&utm_medium=default-bookmarks&utm_campaign=customize||gro.allizom.troppus.|0|0|0|131||BJKUUJs5BFHW|1|47360128123038|||1
3|https://www.mozilla.org/it/contribute/||gro.allizom.www.|0|0|0|131||THKxJGV1DRo9|1|47360052817914|||2
4|https://www.mozilla.org/it/about/||gro.allizom.www.|0|0|0|131||qyhwz2ZEZI2W|1|47358028626657|||2
5|https://www.mozilla.org/it/firefox/central/||gro.allizom.www.|0|0|0|131||dmhsqbzDM8w3|1|47358789206170|||2
6|http://timevault.ddns.net:8080/|Home - TimeVault Website|ten.sndd.tluavemit.|1|0|1|2000|1601738876951000|E8Y1KjiXVJxU|0|125509484353782|||3

```

The DNS name for the site [http://timevault.ddns.net:8080/](http://timevault.ddns.net:8080/) is not resolvable but the hint for this challange is:

```text
ehi man, we are in the future, many website are no longer available!
```

So we put it into the `Wayback machine` and found a hit:

[https://web.archive.org/web/20201003151234/http://timevault.ddns.net:8080/](https://web.archive.org/web/20201003151234/http://timevault.ddns.net:8080/)

The captured site is only static image of a wormhole or something but it contains this comment in the source code:

```html
<!--if my calculations are correct, when this challenge hits 88 miles per hour, you're gonna see some serious PWD c54a1db0b68d3c039df1e25569fc67b7-->
```

Using the provided password with the `TimeVault.exe` binary:

```bash
./TimeVault.exe
Enter password:
c54a1db0b68d3c039df1e25569fc67b7
Decrypted data: gamebox1.reply.it/b8216e21b7d4030dc263f82416389175/Wait_a_minute_Zer0_Are_you_telling_me_you_built_a_time_challenge_out_of_a_DeLorean
```

Provides us with the current site:

[http://gamebox1.reply.it/b8216e21b7d4030dc263f82416389175/Wait_a_minute_Zer0_Are_you_telling_me_you_built_a_time_challenge_out_of_a_DeLorean](http://gamebox1.reply.it/b8216e21b7d4030dc263f82416389175/Wait_a_minute_Zer0_Are_you_telling_me_you_built_a_time_challenge_out_of_a_DeLorean)

Unfortunately this site requires basic authentication credentials. After being stuck on this for long time we tried several different random things. One of them was running `lsadump` volatility plugin on the image, which gave us hexdump bellow that shows that our adversary `Zer0` is using password `bedtimebuddy` as answer to all the secret questions.

```bash
python ./volatility/vol.py -f 699cef6a816882f0e02b40e1fe4d7e93.raw --profile=Win10x86_17763 lsadump
```

```hexdump
0x00000000  06 02 00 00 00 00 00 00 00 00 00 00 00 00 00 00   ................
0x00000010  7b 00 22 00 76 00 65 00 72 00 73 00 69 00 6f 00   {.".v.e.r.s.i.o.
0x00000020  6e 00 22 00 3a 00 31 00 2c 00 22 00 71 00 75 00   n.".:.1.,.".q.u.
0x00000030  65 00 73 00 74 00 69 00 6f 00 6e 00 73 00 22 00   e.s.t.i.o.n.s.".
0x00000040  3a 00 5b 00 7b 00 22 00 71 00 75 00 65 00 73 00   :.[.{.".q.u.e.s.
0x00000050  74 00 69 00 6f 00 6e 00 22 00 3a 00 22 00 57 00   t.i.o.n.".:.".W.
0x00000060  68 00 61 00 74 00 20 00 77 00 61 00 73 00 20 00   h.a.t...w.a.s...
0x00000070  79 00 6f 00 75 00 72 00 20 00 66 00 69 00 72 00   y.o.u.r...f.i.r.
0x00000080  73 00 74 00 20 00 70 00 65 00 74 00 19 20 73 00   s.t...p.e.t...s.
0x00000090  20 00 6e 00 61 00 6d 00 65 00 3f 00 22 00 2c 00   ..n.a.m.e.?.".,.
0x000000a0  22 00 61 00 6e 00 73 00 77 00 65 00 72 00 22 00   ".a.n.s.w.e.r.".
0x000000b0  3a 00 22 00 62 00 65 00 64 00 74 00 69 00 6d 00   :.".b.e.d.t.i.m.
0x000000c0  65 00 62 00 75 00 64 00 64 00 79 00 22 00 7d 00   e.b.u.d.d.y.".}.
0x000000d0  2c 00 7b 00 22 00 71 00 75 00 65 00 73 00 74 00   ,.{.".q.u.e.s.t.
0x000000e0  69 00 6f 00 6e 00 22 00 3a 00 22 00 57 00 68 00   i.o.n.".:.".W.h.
0x000000f0  61 00 74 00 19 20 73 00 20 00 74 00 68 00 65 00   a.t...s...t.h.e.
0x00000100  20 00 6e 00 61 00 6d 00 65 00 20 00 6f 00 66 00   ..n.a.m.e...o.f.
0x00000110  20 00 74 00 68 00 65 00 20 00 63 00 69 00 74 00   ..t.h.e...c.i.t.
0x00000120  79 00 20 00 77 00 68 00 65 00 72 00 65 00 20 00   y...w.h.e.r.e...
0x00000130  79 00 6f 00 75 00 20 00 77 00 65 00 72 00 65 00   y.o.u...w.e.r.e.
0x00000140  20 00 62 00 6f 00 72 00 6e 00 3f 00 22 00 2c 00   ..b.o.r.n.?.".,.
0x00000150  22 00 61 00 6e 00 73 00 77 00 65 00 72 00 22 00   ".a.n.s.w.e.r.".
0x00000160  3a 00 22 00 62 00 65 00 64 00 74 00 69 00 6d 00   :.".b.e.d.t.i.m.
0x00000170  65 00 62 00 75 00 64 00 64 00 79 00 22 00 7d 00   e.b.u.d.d.y.".}.
0x00000180  2c 00 7b 00 22 00 71 00 75 00 65 00 73 00 74 00   ,.{.".q.u.e.s.t.
0x00000190  69 00 6f 00 6e 00 22 00 3a 00 22 00 57 00 68 00   i.o.n.".:.".W.h.
0x000001a0  61 00 74 00 20 00 77 00 61 00 73 00 20 00 79 00   a.t...w.a.s...y.
0x000001b0  6f 00 75 00 72 00 20 00 63 00 68 00 69 00 6c 00   o.u.r...c.h.i.l.
0x000001c0  64 00 68 00 6f 00 6f 00 64 00 20 00 6e 00 69 00   d.h.o.o.d...n.i.
0x000001d0  63 00 6b 00 6e 00 61 00 6d 00 65 00 3f 00 22 00   c.k.n.a.m.e.?.".
0x000001e0  2c 00 22 00 61 00 6e 00 73 00 77 00 65 00 72 00   ,.".a.n.s.w.e.r.
0x000001f0  22 00 3a 00 22 00 62 00 65 00 64 00 74 00 69 00   ".:.".b.e.d.t.i.
0x00000200  6d 00 65 00 62 00 75 00 64 00 64 00 79 00 22 00   m.e.b.u.d.d.y.".
0x00000210  7d 00 5d 00 7d 00 00 00 00 00 00 00 00 00 00 00   }.].}...........
```

Using credentials `Zer0:bedtimebuddy` on the current version of the site reveals the flag.

If you ask me, this challenge took too much time, skill, luck and guesswork for measly 200 points.

---

<details><summary>FLAG:</summary>

```
{FLG:3v3n_R4M_l4st_f0r3v3r}
```

</details>
