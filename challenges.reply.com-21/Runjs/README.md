#### Challenge:

Using the vines, the two Legends climb to the threshold of the temple. But an earthquake stops them. Zer0 has discovered the Third Dogma, the Mentor is weakening, and the temple is collapsing. Codex-Girl and Duplex know only one way to save the temple from destruction. Create an impenetrable force field. [app.tar.xz](./app.tar.xz ":ignore")

---

#### Solution:

- analyzing the provided binary reveals that its `Electron` thus, its content can be extracted via `npx asar extract app.asar ./expanded/`
- here we can see that the game sends user keystrokes as codes `69oUki78` via `TCP` ending with `Game_Over`, this is then check and decrypted via `server`
- all we need to do then is to determine keystroke order so that `check` function passes to obtain the flag

```c
#include <stdio.h>
#include <string.h>

int check(char *msg)

{
  int acc_buff;
  size_t in_len;
  int winned = 1;
  int check_1;
  int i;
  char *in_buffer;
  char input_5;
  char *input_6;
  char *input_7;
  
  in_len = strlen(msg);
  if (in_len == 24) {
    check_1 = 0;
    in_buffer = msg;
    for (i = 0; i < 5; i = i + 1) {
      check_1 = check_1 + *in_buffer + -48;
      in_buffer = in_buffer + 1;
    }
    if (check_1 == 30) {
      input_6 = in_buffer + 1;
      input_5 = *in_buffer;
      input_7 = in_buffer + 2;
      in_buffer = in_buffer + 3;
      if ((int)input_5 + (int)*input_6 + *input_7 + -114 == 57) {
        check_1 = 0;
        for (i = 0; i < 4; i = i + 1) {
          acc_buff = *in_buffer + -0x30 >> 0x1f;
          if (((*in_buffer + -0x30) - acc_buff & 1U) + acc_buff == 1) {
            check_1 = check_1 + (*in_buffer + -0x30) / 2;
          }
          in_buffer = in_buffer + 1;
        }
        if (check_1 == 0xc) {
          for (i = 0; i < 3; i = i + 1) {
            if (((int)*in_buffer - 0x30U & 1) == 0) {
              check_1 = check_1 + (*in_buffer + -0x30) / 2;
            }
            in_buffer = in_buffer + 1;
          }
          if (check_1 == 0x18) {
            winned = 1;
          }
          else {
            winned = 0;
          }
        }
        else {
          winned = 0;
        }
      }
      else {
        winned = 0;
      }
    }
    else {
      winned = 0;
    }
  }
  else {
    winned = 0;
  }
  return winned;
}

void decrypt(char *msg) {
    int key[25]= {
        9,  0x23,  0x3a,  8,  0x65,  0x3c,  2,  0x14,
        0x18,  0xc,  0x4a,  0x5d,  0x68,  100,  7,  0x68,
        0x4a,  0x4d,  0x6b,  0x59,  0x58,  0x51,  0x17,  0x4b,
        0
    };
    char flag[25] = {'\0'};
    
    int len = strlen((char *)msg);
    char *msg_end = msg + len + -1;
    for (int i = 0; i < len; i = i + 1) {
        flag[i] = *msg_end ^ key[i];
        msg_end = msg_end + -1;
    }
    printf("%s", flag);
}


void main() {
    char *opts = "69oUki78";
    char msg[25] = {
        '6','6','6','6','6',
        '9','9','9',
        '7', '7', '7', '7',
        '8','8','8','G', 'a', 'm',
        'e', '_', 'O', 'v', 'e', 'r',
        '\0'
    };


    if (check(msg)) {
        decrypt(msg);
    }
}
```

---

<details><summary>FLAG:</summary>

```
{FLG:You_4re_S0_stRong!}
```

</details>
