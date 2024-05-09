#### Challenge:

Can't find the flag? Just give up. <br><br> <b>Open the <code>Deployment</code> tab to start this challenge.</b>

---

#### Solution:

```console
bash-4.4$ busybox ps | busybox cat
busybox ps | busybox cat
PID   USER     TIME   COMMAND
    1 challeng   0:00 socat TCP-LISTEN:9999,reuseaddr,fork EXEC:/usr/bin/python3 -c 'exec(compile(chr(95)+chr(95)+chr(105)+chr(109)+chr(112)+chr(111)+chr(114)+chr(116)+chr(95)+chr(95)+chr(40)+chr(39)+chr(112)+chr(116)+chr(121)+chr(39)+chr(41)+chr(46)+chr(115)+chr(112)+chr(97)+chr(119)+chr(110)+chr(40)+chr(34)+chr(98)+chr(97)+chr(115)+chr(104)+chr(34)+chr(41)+";print(3338241147603780238248786938107867350016489922013403739812786768782254742117160331044416747901)", "<script>", "exec"))',stderr
exit
```

```python
hex(3338241147603780238248786938107867350016489922013403739812786768782254742117160331044416747901)[2:][:-1].decode('hex')
```

---

<details><summary>FLAG:</summary>

```
flag{sometimes_it_is_best_to_step_away}
```

</details>
<br/>
