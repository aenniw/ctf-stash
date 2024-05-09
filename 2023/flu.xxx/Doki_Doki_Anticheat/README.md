#### Challenge:

Heyo stranger,
I really need ur help! My PC hasn't been working for the past few days and the only thing I'm left with are my savefiles (I always have them on my USB-Stick, just in case). I need to know what's next in my favorite video game, could you please load these [savefiles](./savefiles.zip ":ignore") and tell me the following dialogue, please, I can't wait any longer!

Here's a link to the game, you can even run it easily on Linux: https://teamsalvato.itch.io/ddlc

I don't know how to contact you, so just text me the dialogue as a flag, ok?
So if the dialogue says:"Sayori, what is up with you.." Then just send flag{Sayori,_what_is_up_with_you..}
I'd be really REALLY thankful if you'd do that!

---

#### Solution:

- after restoring the `savefile` in `~/.renpy` and loading it we are greeted with `anti-cheat` protection, poking around reveals that save file can be directly edited via [saveeditonline](https://www.saveeditonline.com/) and just adjusting the `anticheat` parameter to higher value resolves the issue

---

<details><summary>FLAG:</summary>

```
flag{...There_is_no_way_I'm_going_to_your_club.}
```

</details>
