#### Challenge:

Oh no! My computer crashed. Can you help me find out why?

What is the module name?

What is the latest entry on the call stack?

What is the process name?

What is the bug check name?

What is the value of the IRQL? (full name)

What is the SID for the integrity level of the process?

[memory.tar.lzma](./memory.tar.lzma ":ignore")

---

#### Solution:

We are given `Windows Crash Dump` file. By analyzing it in `WinDBG` ( command `!analyze -v`) we can answer the questions we are asked:

What is the module name?

- in the analysis click `myfault`:

    ```
    myfault.sys
    ```

What is the latest entry on the call stack?

- View stack - first entry (0x0):

    ```
    nt!KeBugCheckEx
    ```

What is the process name?

- can be seen in the analysis:

    ```
    notmyfault64.exe
    ```


What is the bug check name?

- can be seen in the analysis (first line):

    ```
    DRIVER_IRQL_NOT_LESS_OR_EQUAL
    ```

What is the value of the IRQL? (full name)

- can be seen in the process details `!process` that its `0x2` which corresponds to:

    ```
    DISPATCH_LEVEL
    ```

What is the SID for the integrity level of the process?

- Googled integrity level SIDs (there are 4) and found this one in the `!process` -> `token response`. 

    ```
    S-1-16-12288
    ```

---

<details><summary>FLAG:</summary>

```
^^^SEE ABOVE^^^
```

</details>
<br/>
