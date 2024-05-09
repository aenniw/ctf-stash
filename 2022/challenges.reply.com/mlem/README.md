#### Challenge:

Up until this point, R-Boy has fulfilled his destiny, but now he’s regenerated Zer0 is worrying him greatly. Suddenly, a feline spirit appears and reveals to R-Boy the existence of multiple parallel universes. The spirit also tells him that Zer0 has taken refuge in one of these universes and is ready to unleash all his power.

[Binary100.zip](./Binary100.zip ":ignore")

---

#### Solution:

- opening the binary in `ghidra` reveals, that we need to determine values of `local_918` based on the `if` checks and after that's done just applying transformation functions reveals the flag. (In this case the `transform` function could not be decompiled thus it need to be reversed from assembly)

```c
undefined8 check(void)
{
  long lVar1;
  undefined8 uVar2;
  char *pcVar3;
  size_t sVar4;
  double local_918 [4];
  double local_8f8;
  double local_8f0;
  double local_8e8;
  double local_8e0;
  double local_8d8;
  double local_8d0;
  double local_8c8;
  double local_8c0;
  double local_8b8;
  double local_8b0;
  double local_8a8;
  double local_8a0;
  double local_898;
  double local_890;
  double local_888;
  double local_880;
  double local_878;
  double local_870;
  double local_868;
  double local_860;
  char acStack281 [257];
  size_t local_18;
  int local_10;
  int local_c;
  
  lVar1 = ptrace(PTRACE_TRACEME,0);
  if (lVar1 < 0) {
    puts("Please, do not use a debugger");
    uVar2 = 1;
  }
  else {
    puts(
        "\n  _____ __    _____ _____\n  |     |  |  |   __|     |\n  | | | |  |__|   __| | | |\n  |_ |_|_|_____|_____|_|_|_|\n  v1.0 - Poeta Errante\n\n"
        );
    puts(
        "  ,-.       _,---._ __  / \\\n /  )    .-\'       `./ /   \\\n(  (   ,\'            `/    / |\n \\  `-\"             \\\'\\   / |\n  `.              ,  \\ \\ /  |\n   /`.          ,\'- `----Y   |\n  (            ;        |   \'\n  |  ,-.    ,-\'         |  /\n  |  | (   |             | /\n  )  |  \\  `.___________|/\n  `--\'   `--\'\n\n"
        );
    puts("~ Help Wesley the cat to find the right word :3 ~\n\n");
    printf("~ Insert a word: ");
    pcVar3 = fgets(acStack281 + 1,0xff,stdin);
    if (pcVar3 == (char *)0x0) {
      puts("Insert a word");
      uVar2 = 0;
    }
    else {
      sVar4 = strlen(acStack281 + 1);
      acStack281[sVar4] = '\0';
      local_18 = strlen(acStack281 + 1);
      if (local_18 == 0x18) {
        for (local_c = 0; (ulong)(long)local_c < local_18; local_c = local_c + 1) {
          local_918[local_c] = (double)(int)acStack281[(long)local_c + 1];
        }
        if (local_8a0 == 91.0) {
          if (local_888 == 91.0) {
            if (local_918[0] + local_918[0] + 11.0 == local_918[0] + 130.0) {
              if (local_860 + local_860 + 6.0 == local_860 + 127.0) {
                if (local_918[1] * 7.0 == local_918[1] + 396.0) {
                  if (local_868 == 104.0) {
                    if ((local_918[2] + 2.0) * 3.0 - 2.0 == (local_918[2] - 17.0) * 4.0) {
                      if (local_870 == (local_870 + local_870) - 44.0) {
                        if (local_918[3] == 67.0) {
                          if ((local_878 * 3.0 - 2.0) * 3.0 - (local_878 * 5.0 + 2.0) * 4.0 ==
                              local_878 * -8.0 - 146.0) {
                            if ((local_8f8 * 5.0 - 2.0) * 5.0 - (local_8f8 + local_8f8 + 7.0) * 6.0
                                == local_8f8 * 33.0 - 1132.0) {
                              if (local_880 == (local_918[3] + local_878) - 16.0) {
                                if ((local_8f0 + local_8f0) / 3.0 == (local_8f0 + 44.0) / 3.0) {
                                  if (local_890 == 49.0) {
                                    if ((local_8e8 * 8.0 + 15.0) * 0.1666666666666667 ==
                                        (local_8e8 + local_8e8 + 81.0) * 0.5) {
                                      if (0.0 - local_898 / 5.0 == 36.0 - local_898) {
                                        if ((local_8e0 * 7.0) / 2.0 == local_8e0 * 3.0 + 23.5) {
                                          if (local_8a8 == local_8a8 / 2.0 + 48.0) {
                                            if (local_8d8 == 110.0) {
                                              if (local_8b0 == local_8a8 / 2.0 - 1.0) {
                                                if (local_8d0 == 104.0) {
                                                  if ((local_8b8 == local_8c0) &&
                                                     (local_8c0 == 108.0)) {
                                                    if (local_8c8 == 48.0) {
                                                      puts(
                                                  "Word found! But it\'s not the flag. Awww :3");
                                                  for (local_10 = 0;
                                                      (ulong)(long)local_10 < local_18;
                                                      local_10 = local_10 + 1) {
                                                    transform((int)(char)(int)local_918[local_10]);
                                                  }
                                                  uVar2 = 0;
                                                  }
                                                  else {
                                                    word_not_found();
                                                    uVar2 = 1;
                                                  }
                                                  }
                                                  else {
                                                    word_not_found();
                                                    uVar2 = 1;
                                                  }
                                                }
                                                else {
                                                  word_not_found();
                                                  uVar2 = 1;
                                                }
                                              }
                                              else {
                                                word_not_found();
                                                uVar2 = 1;
                                              }
                                            }
                                            else {
                                              word_not_found();
                                              uVar2 = 1;
                                            }
                                          }
                                          else {
                                            word_not_found();
                                            uVar2 = 1;
                                          }
                                        }
                                        else {
                                          word_not_found();
                                          uVar2 = 1;
                                        }
                                      }
                                      else {
                                        word_not_found();
                                        uVar2 = 1;
                                      }
                                    }
                                    else {
                                      word_not_found();
                                      uVar2 = 1;
                                    }
                                  }
                                  else {
                                    word_not_found();
                                    uVar2 = 1;
                                  }
                                }
                                else {
                                  word_not_found();
                                  uVar2 = 1;
                                }
                              }
                              else {
                                word_not_found();
                                uVar2 = 1;
                              }
                            }
                            else {
                              word_not_found();
                              uVar2 = 1;
                            }
                          }
                          else {
                            word_not_found();
                            uVar2 = 1;
                          }
                        }
                        else {
                          word_not_found();
                          uVar2 = 1;
                        }
                      }
                      else {
                        word_not_found();
                        uVar2 = 1;
                      }
                    }
                    else {
                      word_not_found();
                      uVar2 = 1;
                    }
                  }
                  else {
                    word_not_found();
                    uVar2 = 1;
                  }
                }
                else {
                  word_not_found();
                  uVar2 = 1;
                }
              }
              else {
                word_not_found();
                uVar2 = 1;
              }
            }
            else {
              word_not_found();
              uVar2 = 1;
            }
          }
          else {
            word_not_found();
            uVar2 = 1;
          }
        }
        else {
          word_not_found();
          uVar2 = 1;
        }
      }
      else {
        puts("Maybe you should search for a different length word! Meeoww");
        uVar2 = 1;
      }
    }
  }
  return uVar2;
}
```

```python
ch = [None] * 24
ch[15] = 91
ch[18] = 91
ch[0] = 119
ch[1] = 66
ch[19] = 95
ch[20] = 44
ch[21] = 44
ch[22] = 104
ch[23] = 121
ch[2] = 72
ch[3] = 67
ch[4] = 54
ch[5] = 44
ch[17] = 49
ch[6] = 114
ch[16] = 45
ch[7] = 47
ch[14] = 96
ch[8] = 110
ch[9] = 104
ch[10] = 48
ch[13] = 47
ch[11] = 108
ch[12] = 108

print(''.join([chr((o^4 if o  > 0x7e else o ) + 4) for o in ch]))
```

---

<details><summary>FLAG:</summary>

```
{FLG:0v3rl4pp3d_15_c00l}
```

</details>
