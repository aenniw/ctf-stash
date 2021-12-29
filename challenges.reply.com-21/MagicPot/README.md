#### Challenge:

Duplex and Codex-Girl chase Zer0 to the Oracle Temple. However, the temple is surrounded by carnivorous plants. The two Legends have to prepare a very powerful potion to transform the plants into vines. Help the two superheroes make the perfect potion! [binary100-4346df085c353067ee69667e2e49d9b8.exe](./binary100-4346df085c353067ee69667e2e49d9b8.exe ":ignore")

---

#### Solution:

```c
void main(void)

{
  undefined8 *option;
  undefined4 uVar1;
  int iVar2;
  char *str;
  char *str_end;
  uint iii;
  code *pcVar3;
  int ii;
  code *pcVar4;
  bool ingredients;
  int i;
  undefined4 flag_1;
  undefined4 flag_2;
  undefined4 flag_3;
  undefined4 flag_4;
  undefined4 key_1;
  undefined4 key_2;
  undefined4 key_3;
  undefined4 key_4;
  undefined flag_end;
  uint local_8;
  char c;
  int ingrecient_i;
  
  local_8 = DAT_00405004 ^ (uint)&stack0xfffffffc;
  printf("************************************************\n");
  printf("** Welcome to the MAGIC POT                 ****\n");
  Sleep(500);
  printf("** Code is desapearing..                    ****\n");
  Sleep(500);
  printf("** ... strings are confused ...             ****\n");
  Sleep(500);
  printf("**  ... and functions are mixed!!           ****\n");
  printf("************************************************\n\n");
  Sleep(1000);
  printf("************************************************\n");
  printf("** Insert your items for the magical potion ****\n");
  printf("**   and shake them with your magic spoon   ****\n");
  printf("*****   AND GET THE SECRET!!            ****\n");
  printf("************************************************\n\n");
  option = (undefined8 *)FUN_0040176e(8);
  pcVar3 = getchar_exref;
  pcVar4 = fseek_exref;
  *option = 0;
LAB_00401540:
  do {
    printf("Select The action:\n");
    printf("A - Add woods\n");
    printf("B - Shake the pot\n");
    printf("C - Cool the mix\n");
    printf("D - Blow on the fire\n");
    printf("E - Throw the ingredients\n");
    printf(&DAT_004034e0);
    c = (*pcVar3)();
    uVar1 = __acrt_iob_func(0,0,2);
    (*pcVar4)(uVar1);
    switch(*(int *)option) {
    case 0:
      if (c != 'A') goto switchD_004015ae_caseD_5;
      *(undefined4 *)option = 1;
      goto LAB_00401540;
    case 1:
      if (c != 'E') goto switchD_004015ae_caseD_5;
      *(undefined4 *)option = 2;
      iii = add_ingredient();
      break;
    case 2:
      if (c != 'B') goto switchD_004015ae_caseD_5;
      ii = 0;
      *(undefined4 *)option = 3;
      ingrecient_i = 0;
      do {
        iVar2 = (**(code **)(**(int **)(*(int *)((int)option + 4) + ingrecient_i * 4) + 0xc))();
        ii = ii + iVar2;
        uVar1 = (**(code **)**(code ***)(*(int *)((int)option + 4) + ingrecient_i * 4))();
        printf("%s is shaked\n",uVar1);
        pcVar4 = fseek_exref;
        pcVar3 = getchar_exref;
        if (ingrecient_i == 0) {
          ingredients = ii == 1;
LAB_0040162d:
          if (!ingredients) {
            iii = 1;
            goto LAB_00401649;
          }
        }
        else {
          if (ingrecient_i == 1) {
            ingredients = ii == 3;
            goto LAB_0040162d;
          }
        }
        ingrecient_i = ingrecient_i + 1;
      } while (ingrecient_i < 3);
      iii = (uint)(ii != 6);
      break;
    case 3:
      if (c != 'D') goto switchD_004015ae_caseD_5;
      *(undefined4 *)option = 4;
      goto LAB_00401540;
    case 4:
      if (c == 'C') {
        *(int *)option = *(int *)option + 1;
      }
    default:
      goto switchD_004015ae_caseD_5;
    }
LAB_00401649:
    if (iii != 0) {
switchD_004015ae_caseD_5:
      if (*(int *)option != 5) {
        printf("Your potion is wrong! Check the recipe!");
        FUN_00401760();
        return;
      }
      ii = 1;
      ingrecient_i = *(int *)((int)option + 4);
      flag_1 = 0x2025044e;
      flag_2 = 0x7031f5c;
      flag_3 = 0x36510a7f;
      flag_4 = 0x361a6502;
      flag_end = 0;
      key_1 = 0x1b1d27;
      key_2 = 0x115374b;
      key_3 = 0x73303d43;
      key_4 = 0x1b1f071f;
      i = 0;
      do {
        str = (char *)(**(code **)**(code ***)(ingrecient_i + i * 4))();
        if (i == 2) {
          str = (char *)(**(code **)(**(int **)(ingrecient_i + 8) + 8))();
        }
        iii = 0;
        str_end = str;
        do {
          c = *str_end;
          str_end = str_end + 1;
        } while (c != '\0');
        if (str_end != str + 1) {
          do {
            *(byte *)((int)&flag_1 + ii) = *(byte *)((int)&flag_1 + ii) ^ str[iii];
            ii = ii + 1;
            if (0x1f < ii) break;
            iii = iii + 1;
            str_end = str;
            do {
              c = *str_end;
              str_end = str_end + 1;
            } while (c != '\0');
          } while (iii < (uint)((int)str_end - (int)(str + 1)));
        }
        i = i + 1;
        if (2 < i) {
          flag_1 = flag_1 ^ 0x35;
          printf("\nThe magic is made and the plants are vines: %s\n",&flag_1);
          FUN_00401760();
          return;
        }
      } while( true );
    }
  } while( true );
}
```
- from the decompiled binary we can see the order of operations that needs to take place:
    - 1. A - Add woods
    - 2. E - Throw the ingredients
    - 3. B - Shake the pot
    - 4. D - Blow on the fire
    - 5. C - Cool the mix

- last thing that remains are the names and order of the ingredients `items.txt`
```
Bigfoot nail
Unicorn hair
Sugar
Eyelashes
```

---

<details><summary>FLAG:</summary>

```
{FLG:pls_d0_n0t_Drink_th1s_Soup}
```

</details>
