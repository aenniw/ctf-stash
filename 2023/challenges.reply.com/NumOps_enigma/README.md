#### Challenge:

Navigating the data ocean, R-Boy arrives in the Coding Realm: the journey begins. This submerged realm is a labyrinth of source code and complex algorithms, inhabited by shapeshifting creatures called Numbralisk. R-Boy knows that he will have to overcome these obstacles if he wants to obtain the first fragment.

[coding-100.zip](./coding-100.zip ":ignore")

---

#### Solution:

Unzipping `coding-100.zip` gives a `README.md` describing a **Sumdoku** (a killer-sudoku variant) and
`challenge.zip`, which contains `lvl_1.zip` + `lvl_1.txt`. Each `lvl_N.txt` is a Sumdoku puzzle; its
solved grid read row-by-row is the **password** for `lvl_N.zip`, which in turn holds
`lvl_(N+1).zip` + `lvl_(N+1).txt`. So it's a long chain of nested, puzzle-locked zips &mdash; I need to
solve each Sumdoku programmatically and keep descending until a level yields `flag.txt`.

The Sumdoku rules: fill an `NxN` grid with `1..N`, unique per row/column, and each lettered region's
cells must combine (via `+`, `*`, `-`, `/`) to the given result. That's a constraint-satisfaction
problem, so I model it with **z3**:

```python
from z3 import Int, And, Distinct, Sum, Product, If, Solver, sat

def solve_sumdoku(text):
    grid_s, rules_s = text.split("\n\n", 1)
    grid = [row.split() for row in grid_s.strip().split("\n")]
    N = len(grid[0])
    X = [[Int(f"x_{i}_{j}") for j in range(N)] for i in range(N)]
    C  = [And(1 <= X[i][j], X[i][j] <= N) for i in range(N) for j in range(N)]
    C += [Distinct(X[i]) for i in range(N)]                         # rows
    C += [Distinct([X[i][j] for i in range(N)]) for j in range(N)]  # cols
    for line in rules_s.strip().split("\n"):
        region, result, op = line.split(); res = int(result)
        cells = [X[i][j] for i, row in enumerate(grid)
                 for j, c in enumerate(row) if c == region]
        if   op == "+": C.append(Sum(cells) == res)
        elif op == "*": C.append(Product(cells) == res)
        elif op == "-": a, b = cells; C.append(If(a > b, a - b, b - a) == res)
        elif op == "/": a, b = cells; C.append(If(a > b, a == res*b, b == res*a))  # avoid real division
    s = Solver(); s.add(C); assert s.check() == sat
    m = s.model()
    return "".join(str(m.evaluate(X[i][j])) for i in range(N) for j in range(N))
```

Then I just loop: solve `lvl_N.txt`, use the grid string as the password to extract `lvl_N.zip`, and
repeat. The archives are AES-encrypted, so standard `unzip` fails (the challenge README warns about
this) &mdash; I use `7z`, or `pyzipper` from Python:

```python
import os, pyzipper
level = 1
while os.path.exists(f"lvl_{level}.txt"):
    pw = solve_sumdoku(open(f"lvl_{level}.txt").read())
    with pyzipper.AESZipFile(f"lvl_{level}.zip") as zf:
        zf.extractall(pwd=pw.encode())
    level += 1
# the final level contains flag.txt instead of another lvl_*.zip
```

The chain is **251 levels** deep; the last zip drops a `flag.txt` with the flag. I ran this end to end
and it recovers the committed flag.

---

<details><summary>FLAG:</summary>

```
{FLG:Y0u_4r3-0n-Th3-r19hT.p4tH_t0-tH3_c0D1n9.fR4gM3nT}
```

</details>
