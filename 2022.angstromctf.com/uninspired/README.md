#### Challenge:

clam has no more inspiration :(
[maybe help him get some?](./uninspired ":ignore")

---

#### Solution:

- quick decompilation via `ghidra` shows that if we want get the `flag` we need to figure out the logic behind the input validation as it's also used as the `key` for `flag` "decryption"


```c
undefined8 main(void)
{
  size_t input_len;
  long i;
  undefined8 uVar1;
  char *input_pointer;
  char input_array [10];
  char local_3e [6];
  undefined increment_arr_pointer [16];
  undefined local_28 [16];
  undefined8 local_18;
  char i_char;
  
  input_pointer = input_array;
  puts("there\'s no more inspiration :(");
  fgets(input_array,0x10,stdin);
  input_len = strcspn(input_array,"\n");
  input_array[(int)input_len] = '\0';
  if ((int)input_len == 10) {
    local_18 = 0;
    increment_arr_pointer = (undefined  [16])0x0;
    local_28 = (undefined  [16])0x0;
    do {
      i_char = *input_pointer;
      if (9 < (byte)(i_char - 0x30U)) {
        puts("I don\'t like your inspiration :(");
        return 1;
      }
      input_pointer = input_pointer + 1;
      *(int *)(increment_arr_pointer + (long)(char)(i_char - 0x30U) * 4) =
           *(int *)(increment_arr_pointer + (long)(char)(i_char - 0x30U) * 4) + 1;
    } while (input_pointer != local_3e);
    i = 0;
    do {
      if (*(int *)(increment_arr_pointer + i * 4) != input_array[i] + -0x30) {
        puts("that\'s not good inspiration :(");
        return 1;
      }
      i = i + 1;
    } while (i != 10);
    puts("yay I\'m inspired now, have a flag :)");
    print_flag(input_array);
    uVar1 = 0;
  }
  else {
    puts("that\'s not very inspiring :(");
    uVar1 = 1;
  }
  return uVar1;
}
```

- from the source we can see:
  - input must contain 10 characters 
    - `if (input_len == 10)`
  - that we can only input starting form `0` char
    - `if (9 < (byte)(i_char - 0x30U))`
  - we go through each character and use it as index `(i_char - 0x30) * 4` to increment validation array values by `1`
    - `*(int *)(increment_arr_pointer + (long)(char)(i_char - 0x30U) * 4) = *(int *)(increment_arr_pointer + (long)(char)(i_char - 0x30U) * 4) + 1`
  - then we validates that each 4th value of validation array equals one of our input chars
    - `input_array[i] - 0x30` `if (*(int *)(increment_arr_pointer + i * 4) != input_array[i] + -0x30)` 
- based on that we just need to figure out `code` that satisfies the condition, as it was just `10` characters long it could be easily done by hand

```bash
python3 -c 'print("".join([chr(x + 48) for x in [6, 2, 1, 0, 0, 0, 1, 0, 0, 0]]))' | ./uninspired 
```

---

<details><summary>FLAG:</summary>

```
actf{ten_digit_numbers_are_very_inspiring}
```

</details>
<br/>
