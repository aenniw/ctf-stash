#### Challenge:

Clam was browsing armstrongctf.com when suddenly a popup appeared saying "GET YOUR FREE FLAGS HERE!!!" along with [a download](./free_flags ":ignore"). Can you fill out the survey for free flags?

Find it on the shell server at `/problems/2021/free_flags` or over netcat at `nc shell.actf.co 21703`.

---

#### Solution:

We are given a binary, that when opened in `Ghidra` reveals following code: 

```c++
puts(
      "Congratulations! You are the 1000th CTFer!!! Fill out this short survey to get FREE FLAGS!!!"
      );
  puts("What number am I thinking of???");
  __isoc99_scanf(0x1020e1,&local_11c);
  if (local_11c == 0x7a69) {
    puts("What two numbers am I thinking of???");
    __isoc99_scanf("%d %d",&local_120,&local_124);
    if ((local_120 + local_124 == 0x476) && (local_120 * local_124 == 0x49f59)) {
      puts("What animal am I thinking of???");
      __isoc99_scanf(" %256s",local_118);
      sVar2 = strcspn(local_118,"\n");
      local_118[sVar2] = '\0';
      iVar1 = strcmp(local_118,"banana");
      if (iVar1 == 0) {
        puts("Wow!!! Now I can sell your information to the Russian government!!!");
        puts("Oh yeah, here\'s the FREE FLAG:");
        print_flag();
        local_128 = 0;
      }
      else {
        puts("Wrong >:((((");
        local_128 = 1;
      }
    }
    else {
      puts("Wrong >:((((");
      local_128 = 1;
    }
  }
  else {
    puts("Wrong >:((((");
    local_128 = 1;
  }
```

We can see that the server binary will print the flag if we correctly answer the three questions. The answers to first and last questions are trivial (`31337`, resp. `banana`), but the second one requires to solve following set of equations:

```math
x + y = 1142
x * y = 302937
```

Grade / middle / high schoolers should not have a problem with this, but I'm neither of them anymore, so I shamefully confess that I used [wolfram](https://www.wolframalpha.com/input/?i=x+%2B+y+%3D+1142%3B+x+*+y+%3D+302937).

---

<details><summary>FLAG:</summary>

```text
actf{what_do_you_mean_bananas_arent_animals}
```

</details>
<br/>
