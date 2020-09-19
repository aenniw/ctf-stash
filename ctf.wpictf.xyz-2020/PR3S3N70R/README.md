#### Challenge:

i wuz @r2con2019 

(Hint: you may need to sort-by new)

- made by awg 


---

#### Solution:

Googling for `r2con2019` leads to [https://rada.re/con/2019/](https://rada.re/con/2019/). But it seems like valid conference site. 

The second lead is the handle of the author of the challenge - `awg`. His profile in CTFd platform leads to his github - [https://github.com/roboman2444](https://github.com/roboman2444), which reveals his name - `Alex Gaines`. 

Searching his name in the r2con2019's [agenda](https://rada.re/con/2019/agenda.html#) reveals the name of his presentetion - `Object Diversification with the help of r2`. Video of it is available on [youtube](https://www.youtube.com/watch?v=fBGc7mhmYFg&ab_channel=PancakeNopcode). There we need to use the hint - sort video comments by `Newest first` because youtube by default shows only most popular comments. This reveals comment by author himself with incomplete flag:

```
Oh look! Replace NAMEHERE with what I call my inserted code bits. WPI{@wg_1s4ch@nNAMEHERE}
```

For the rest of the flag we need to rewatch the video and do some trial and error, but in the end we got it.

---

<details><summary>FLAG:</summary>

```
WPI{@wg_1s4ch@ncruftable}
```

</details>
<br/>
