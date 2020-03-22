#### Challenge:

Maths, Maths, Maths,.... [task](./task ":ignore")

---

#### Solution:

- decompile with ghidra

```c
void FUN_00100820(void)
{
  local_128 = 0xd1;
  local_124 = 0x1e;
  local_120 = 0xdb;
  local_11c = 0xfb;
  local_118 = 0x74;
  local_114 = 0xcb;
  local_110 = 0x15;
  local_10c = 0xdd;
  local_108 = 0xfa;
  local_104 = 0x75;
  local_100 = 0xd9;
  local_fc = 0x4b;
  local_f8 = 0xda;
  local_f4 = 0xe8;
  local_f0 = 0x73;
  local_ec = 0xd1;
  local_e8 = 0x4f;
  local_e4 = 0xcc;
  local_e0 = 0xe7;
  local_dc = 0x36;
  local_d8 = 0xcc;
  local_d4 = 0x4e;
  local_d0 = 0xe7;
  local_cc = 0xfc;
  local_c8 = 0x36;
  local_c4 = 0xc1;
  local_c0 = 0x10;
  local_bc = 0x8d;
  local_b8 = 0xaf;
  local_b4 = 0x7b;
  local_b0 = 0xa8;
  iVar2 = FUN_0010080a();
  iVar3 = FUN_00100815();
  uVar5 = (ulong)local_118;
  dVar9 = (double)local_128;
  iVar4 = local_124 + -0x14;
  cVar1 = (char)local_124;
  puts("Hello REVERSER!");
  lVar7 = ptrace(PTRACE_TRACEME,0,0,0);
  lVar7 = (long)((int)lVar7 + 1) *
          ((long)iVar4 *
           (long)((dVar9 * (((double)iVar3 * 29.00000000 + 58.00000000) * (double)uVar5 +
                           110.00000000) + 141.00000000) * (double)iVar2 + 20.00000000) >>
          (cVar1 - 0x16U & 0x3f)) * 0xc0fe;
  printf("Give me the passcode:");
  if (lVar7 < 0) {
    lVar7 = lVar7 + 0xff;
  }
  fgets(local_58,0x31,_DAT_00302010);
  local_234 = 0;
  local_238 = 0;
  local_228 = lVar7 >> 8;
  while (sVar6 = strlen(local_58), (ulong)(long)local_238 < sVar6) {
    if (local_228 == 0) {
      local_228 = lVar7 >> 8;
    }
    auStack504[(long)local_238] = (int)local_58[(long)local_238] ^ (uint)local_228 & 0xff;
    local_228 = local_228 >> 8;
    local_238 = local_238 + 1;
  }
  local_238 = 0;
  while (local_238 < 0x1e) {
    local_234 = local_234 +
                (*(uint *)(&local_128 + (long)local_238) ^ auStack504[(long)local_238] | 1);
    local_238 = local_238 + 1;
  }
  lVar7 = ptrace(PTRACE_TRACEME,0,0);
  if (local_234 ==
      -((((((0x123456 << ((char)local_124 - 0x1aU & 0x1f)) >> ((char)local_128 + 0x48U & 0x1f)) +
          local_124) -
         ((0x654321 << ((char)local_124 - 0x1aU & 0x1f)) >> ((char)local_128 + 0x48U & 0x1f))) + 3)
       * (int)lVar7)) {
    puts("Good job!");
  }
  else {
    printf("NOOOOOOOO");
  }
}
```

- first `ptrace(PTRACE_TRACEME,0,0,0)` return `0` any other will fail and return `-1`
- our input is first xored against `local_228` and then xored against `local_128` and then checksum is computed
- checksum value should be `0x1e` for valid input, can be reconstructed via substitution of checksum if...
- xoring both masks should return valid flag, one mask `local_128` is static, and other `local_228` is conputed based on `long lVar7` value

```python
flag = ""
mask_1 = [162, 123, 184, 142, 6,
          162, 123, 184, 142, 6,
          162, 123, 184, 142, 6,
          162, 123, 184, 142, 6,
          162, 123, 184, 142, 6,
          162, 123, 184, 142, 6]
mask_2 = [0xd1, 0x1e, 0xdb, 0xfb, 0x74,
          0xcb, 0x15, 0xdd, 0xfa, 0x75,
          0xd9, 0x4b, 0xda, 0xe8, 0x73,
          0xd1, 0x4f, 0xcc, 0xe7, 0x36,
          0xcc, 0x4e, 0xe7, 0xfc, 0x36,
          0xc1, 0x10, 0x8d, 0xaf, 0x7b]

for i in range(30):
    flag += chr(mask_1[i] ^ mask_2[i])
```

---

<details><summary>FLAG:</summary>

```
securinets{0bfus4ti0n5_r0ck5!}
```

</details>
<br/>
