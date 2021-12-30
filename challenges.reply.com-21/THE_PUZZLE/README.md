#### Challenge:

Thanks to the ex-con, R-boy and IronCode discover that Zer0 has hidden an encrypted file in the Forbidden Forest, which contains the coordinates of his secret lair. The file is protected by a giant dragon. Help R-Boy and IronCode defeat the dragon and take the file. [coding200.zip](./coding200.zip ":ignore")

---

#### Solution:

This challenge is coding version of the classical real world "puzzles". Like the real world puzzles, you can only put together those pieces that connect to each other based on their shape on one of their (top/bottom/left/right) edges. Here the shape is represented by integers, e.g. if there are two pieces that have same integer on adjacent edges, e.g. "left" piece has this integer on the "right" edge and "right" piece has the same one on the "left" edge then these can be connected.
Like in real world puzzles, I started by putting together "the frame" by finding the `topleft` corner piece first, then building the `first column` and `first row` of the puzzle and finally the rest of the picture. When completed, printing the characters, which some of the pieces contained returns the password to the `ZIP` archive containing the flag.

```python
#!/usr/bin/env python

pieces = []

# puzzzle.txt is puzzle.txt without intro and w/h data
with open('puzzzle.txt') as f:
    lines = f.readlines()

U_piece_edges = []
D_piece_edges = []
L_piece_edges = []
R_piece_edges = []

up = 0
down = 1
left = 2
right = 3


i = 0
for line in lines:
    piece = line.strip().split(" ")
    # print(piece)
    U_piece_edges.append(piece[0])
    D_piece_edges.append(piece[1])
    L_piece_edges.append(piece[2])
    R_piece_edges.append(piece[3])
    if len(piece) == 4:
        pieces.append([piece[0], piece[1], piece[2], piece[3], " ", i])
        i = i+1

    elif len(piece) == 5:
        pieces.append([piece[0], piece[1], piece[2], piece[3], piece[4], i])
        i = i+1

    else:
        print("Error!")

# # Find top left piece:
# for piece in pieces:
#     if piece[left] not in R_piece_edges and piece[up] not in D_piece_edges:
#         print(piece)   

# # Top left piece:
# # ['38921', '11931', '64227', '142066', ' ', 13953]

picture =  [ [""] * 200 for _ in range(200)]
picture[0][0] = ['38921', '11931', '64227', '142066', ' ', 13953]

# build the leftmost edge of the picture from top to bottom
for h in range(1,200):
    for piece in pieces:
        if picture[h-1][0][down] == piece[up]:
            picture[h][0] = piece
            break;

# build the topmost edge of the picture from left to right
for w in range(1,200):
    for piece in pieces:
        if picture[0][w-1][right] == piece[left]:
            picture[0][w] = piece
            break;

# build the rest of the picture line by line
for h in range(1,200):
    for w in range(1,200):
        for piece in pieces:
            if picture[h][w-1][right] == piece[left] and picture[h-1][w][down] == piece[up]:
                picture[h][w] = piece
                break;
        print(picture[h][w][4].strip(), end="")
```

---

<details><summary>FLAG:</summary>

```
{FLG:++---N0t_4_H4mM3r---||}
```

</details>
