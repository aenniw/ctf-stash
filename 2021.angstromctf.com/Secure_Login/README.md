#### Challenge:

My login is, potentially, and I don't say this lightly, if you know me you know that's the truth, it's truly, and no this isn't snake oil, this is, no joke, the most [secure login service](./login ":ignore") in the world ([source](./login.c ":ignore")).

Try to hack me at `/problems/2021/secure_login` on the shell server.

---

#### Solution:

We are given source code (and also testing binary) of the login service. Upon quick inspection we see, that the self-proclaimed security of this service is based on the fact that it requires user to guess password that has (or to be more precise - "is supposed to have") 128 characters and is generated on every program run by function:

```c++
void generate_password() {
	FILE *file = fopen("/dev/urandom","r");
	fgets(password, 128, file);
	fclose(file);
}
```

Subsequently, the password is checked by this condition:

```c++
if (strcmp(input, password) == 0) {
```

The beautiful mistake of this system lies in the fact that `strcmp` may not be checking the full string (all 128 characters) because it compares two strings only until the end of the shorter one of them - to be more precise until NULL byte (`\0`) of the shorter one of them. So if we keep sending empty string (so just the `NULL byte`) as the password over and over again, with the chance `1:256` of the random generator generating `NULL byte` as the first character of the generated password, we have to hit the jackpot sooner or later. 


```bash
#!/bin/bash

for i in {1..1000}; do
    echo "" | ./login | grep "actf"
done;
```

---

<details><summary>FLAG:</summary>

```text
actf{if_youre_reading_this_ive_been_hacked}
```

</details>
<br/>
