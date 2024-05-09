#### Challenge:

Top secrets lie behind this definitely secure JS lock. [js-lock.html](./js-lock.html ":ignore")

---

#### Solution:

- reversing the `javascript` blocks reveals that the key is encoded in nested array structure, backtracking the structure in browser decrypts flag

```js
lookups = {}

function lookup(data, indexes = []) {
    if (typeof data === 'number' && lookups[data] === undefined) {
        lookups[data] = indexes;
    } else if (Array.isArray(data)) {
        data.forEach((candidate, index) => {
            lookup(candidate, [...indexes, index])
        })
    }
}
function solver() {
    for (let i = 1; i <= 1337; i++) {
        const indexes = lookups[i];
        const key = indexes.map((v) => {
            for (let i = 0; i < v; i++) {
                S.key += '1'
            }
            S.key += '0'
        });
        console.log('solved', i)
    }

}

lookup(LOCK);
solver();
win();
```

---

<details><summary>FLAG:</summary>

```
DUCTF{s3arch1ng_thr0ugh_an_arr4y_1s_n0t_th4t_h4rd_ab894d8dfea17}
```

</details>
<br/>
