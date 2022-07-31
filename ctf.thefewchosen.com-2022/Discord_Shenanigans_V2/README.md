#### Challenge:

We know that our Discord flags are the most specials ones. They raise our status! We plan to keep this tradition going, no matter what!

This one is hidden in plain s̷̤̎i̷̡͝g̴̤̿ḧ̴͚́ṫ̵̹.

Note: |̸̥͔͚͕̟̔̓̚|̴̨̫̿̎|̷͈̓̌̈|̷̼̱̦̲͐́́|̷̧͍̥͚̈̅͜͝|̷̱̱̭̏̓̈́̍̚|̴̨͚̫͇̽̌̽̕͝|̸͚̏|̴̨̬͉͔̩̈́̉͆̂͋|̸̟͇̈̾͝|̸̱͇̔̓ might be able to help you... if you ask nicely. He's a bit shy, though.

Hint: Read the message he gives you when you ask nicely very carefully!
Hint2: The flag is in #announcements

---

#### Solution:

Challenge description tells us to ask bot - `nicely` and that he is `shy` - asking him `/flag please` (nicely) in `DM message` (shy) gives us:

```
Look, I'm not supposed to help you. But, what you need to do is to e̶̛͕x̴̧̜ǐ̴̗̑f̵̢̧ļ̷̢̧ţ̶̻̠r̷̢̨á̷̡̡ț̸̡̣e̵̛͓ ̶̢͍t̷̢̖h̵̡̤ë̷̛͖ ̶̫̼f̸̨̣l̸̢͖a̸̢̛ģ̸̲̤
```

First hint tells us to read his message `carefully` - it does not say exfiltrate but `EXIF`ltrate.
Second hint tells us that the flag is in `announcements` channel. Also there is **status** boldened and the **sight** obfuscated in the challenge description. 

So running exiftool on the image with the picture of progress bar and label `status` found in the announcements channel gives us the flag:

![current-50.png](./current-50.png ":ignore")

```
exiftool current-50.png
```

---

<details><summary>FLAG:</summary>

```

```

</details>
<br/>
