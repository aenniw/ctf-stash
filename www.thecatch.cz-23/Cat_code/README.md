#### Challenge:

Ahoy, officer,

due to the lack of developers on board, the development of the access code generator for the satellite connection was entrusted to the cat of the chief officer. Your task is to analyze the cat's creation and find out the code.
	
May you have fair winds and following seas!

Download the [cat_code.zip](./cat_code.zip ":ignore").\
(MD5 checksum: `aac150b3f24e5b047ee99e25ad263f56`)

---

#### Solution:

- after initial run/inspection seems that the problem resides in the recursion of `def meow` which is taking ages 
    ```python
    def meow(kittens_of_the_world):
        """
        meowwwwww meow
        """
        print('meowwww ', end='')
        if kittens_of_the_world < UNITED:
            return kittens_of_the_world
        return meow(kittens_of_the_world - UNITE) + meow(kittens_of_the_world - UNITED)```
    ```
- altering the logic so that it uses just simple lookup cache speed up the processing enough to get to the actuall flag
    ```python
    cache = dict()

    def meow(kittens_of_the_world):
        """
        meowwwwww meow
        """
        # print('meowwww ', end='')
        if kittens_of_the_world < UNITED:
            return kittens_of_the_world
        if cache.get(kittens_of_the_world):
            return cache[kittens_of_the_world]
        res = meow(kittens_of_the_world - UNITE) + meow(kittens_of_the_world - UNITED)

        cache[kittens_of_the_world] = res
        return res
    ```

```bash
echo 'kittens' | python3 ./meowmeow.py 
```
---

<details><summary>FLAG:</summary>

```
FLAG{YcbS-IAbQ-KHRE-BTNR}
```

</details>
<br/>
