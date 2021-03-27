#### Challenge:

I built this awesome game based off of cookie clicker! Bet you'll never beat my high score. Hehehe!

[http://web1.utctf.live:4270](http://web1.utctf.live:4270)

---

#### Solution:

We are greeted with simple game that counts number of mouse clicks in 30 seconds. Upon inspection of the javascript responsible for the game, it can be seen that the variable `numClicks` is the counter. Setting it in the browser console to number greater than the high score reveals the flag after the timer runs out.

---

<details><summary>FLAG:</summary>

```text
utflag{numnum_cookies_r_yumyum}
```

</details>
<br/>
