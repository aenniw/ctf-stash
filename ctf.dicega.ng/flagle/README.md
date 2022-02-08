#### Challenge:

How hard could it be? Just guess the [flag](https://flagle.mc.ax/).

---

#### Solution:

- we need to guess six fields each up to 5 characters, and validate it via `wasm` and `js` checks, thus reversing it will reveals the flag
- reversing [flag-checker.wasm](./flag-checker.wasm ":ignore") via [wabt](https://github.com/WebAssembly/wabt/releases/tag/1.0.24) we can see the logic for fields 1,2,3,5,6


```wasm
export function a():int {
  return 1684628325
}

data d_a(offset: 1024) = "dice{\00";

// dice{
export function validate_1(a:int):int {
  return streq(a, 1024)
}

// F!3lD
export function validate_2(a:int, b:int, c:int, d:int, e:int):int {
  var f:int = g_a - 16;
  f[15]:byte = a;
  f[14]:byte = b;
  f[13]:byte = c;
  f[12]:byte = d;
  d = f[14]:byte;
  f[14]:byte = f[13]:byte;
  f[13]:byte = d;
  d = f[13]:byte;
  f[13]:byte = f[12]:byte;
  f[12]:byte = d;
  d = f[13]:byte;
  f[13]:byte = f[15]:byte;
  f[15]:byte = d;
  d = f[13]:byte;
  f[13]:byte = f[12]:byte;
  f[12]:byte = d;
  d = f[15]:byte;
  f[15]:byte = f[14]:byte;
  f[14]:byte = d;
  d = 0;
  if (f[15]:byte != 51) goto B_a;
  if (f[14]:byte != 108) goto B_a;
  if (f[13]:byte != 33) goto B_a;
  d = e == 68 & f[12]:byte == 70;
  label B_a:
  return d;
}

// d0Nu7
export function validate_3(a:int, b:int, c:int, d:int, e:int):int {
  var f:int = 0;
  if (b * a != 4800) goto B_a;
  if (c + a != 178) goto B_a;
  if (c + b != 126) goto B_a;
  if (d * c != 9126) goto B_a;
  if (d - e != 62) goto B_a;
  f = c * 4800 - e * d == 367965;
  label B_a:
  return f;
}

// m@x!M
export function validate_5(a:int, b:int, c:int, d:int, e:int):int {
  var f:int = g_a - 16;
  f[15]:byte = a + 12;
  f[14]:byte = b + 4;
  f[13]:byte = c + 6;
  f[12]:byte = d + 2;
  d = 0;
  if ((a + 12) != 121) goto B_a;
  if ((b + 4) != 68) goto B_a;
  if ((c + 6) != 126) goto B_a;
  d = e == 77 & (d + 2) == 35;
  label B_a:
  return d;
}

// T$r3}
export function validate_6(a:int, b:int, c:int, d:int, e:int):int {
  var f:int = 0;
  if ((b + 2933) * (a + 1763) != 5483743) goto B_a;
  f = e == 125 & (d + 1546) * (c + 3913) == 6431119;
  label B_a:
  return f;
}

```

- the 4 field is validated in obfuscated `js`

```js
function c(b){var e={'HLPDd':function(g,h){return g===h;},'tIDVT':function(g,h){return g(h);},'QIMdf':function(g,h){return g-h;},'FIzyt':'int','oRXGA':function(g,h){return g<<h;},'AMINk':function(g,h){return g&h;}},f=current_guess;try{let g=e['HLPDd'](btoa(e['tIDVT'](intArrayToString,window[b](b[e['QIMdf'](f,0x26f4+0x1014+-0x3707*0x1)],e['FIzyt'])()['toString'](e['oRXGA'](e['AMINk'](f,-0x1a3*-0x15+0x82e*-0x1+-0x1a2d),0x124d+-0x1aca+0x87f))['match'](/.{2}/g)['map'](h=>parseInt(h,f*f)))),'ZGljZQ==')?-0x1*0x1d45+0x2110+-0x3ca:-0x9*0x295+-0x15*-0x3+0x36*0x6d;}catch{return 0x1b3c+-0xc9*0x2f+-0x19*-0x63;}}
```
- after some cleanup we can see that check depends also on `f` which reffers to guess try, so in short we need to find global function with length of 5, accepts 2 arguments `char` and `"int"` and needs to return number `1684628325`. Fotunatelly `wasm`  exports function `a()` that returns the value that we need.
```js
btoa(
    intArrayToString(
        window[b](b[f - 1], 'int')()        // needs to be 1684628325
            .toString((f & 4) << 2)         // (f & 4) << 2 needs to be 16
            .match(/.{2}/g)
            .map(h => parseInt(h, f * f))   // f * f needs to be 16, thus f = 4
    )
) === 'ZGljZQ==' // base64 value of dice
```
- after some filtering of candidates via `Object.keys(window).filter(k => k.length === 5)` we land upon `cwrap`

---

<details><summary>FLAG:</summary>

```
dice{F!3lDd0Nu7cwrapm@x!MT$r3} 
```

</details>
<br/>
