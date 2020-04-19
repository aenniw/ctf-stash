#### Challenge:

Like the title says, this challenge is dangerous and contains live malware.

Shoutout to the hacker that I stole this from challenge from. Sadly I can't give them credit because they sent the phish from a compromised email, but it's literally his/her code. I just defanged it (a little bit - it will still crash your webbrowser (usually, but don't test that outside of a VM)) and stuck a WPI flag in here.

To prevent accidental execution the file has been zipped with the password "I_understand_that_this_challenge_contains_LIVE_MALWARE"

[invoice.zip](./invoice.zip ":ignore")

---

#### Solution:

- update malicious `HTML` so that endless loop is gone...
- uncomment redirect part of code and the `URL` will contain flag, so just update code to print it instead of redirect...

```html
<html>
  <head>
    <title></title>
  </head>
  <body>
    <script>
      var a = [
        "ps:",
        "cte",
        "5df",
        "se_",
        "toS",
        "ing",
        "tri",
        "sub",
        "lac",
        "ryt",
        "d}.",
        "cod",
        "pro",
        "_no",
        "ran",
        "ing",
        "dom",
        "str",
        "ete",
        "rep",
      ];
      function abc(def) {
        popupWindow = window.open(
          def,
          "popUpWindow",
          "height=666,width=666,left=666,top=666"
        );
      }
      (function (c, d) {
        var e = function (f) {
          while (--f) {
            c["push"](c["shift"]());
          }
        };
        e(++d);
      })(a, 0xa8);
      var b = function (c, d) {
        c = c - 0x0;
        var e = a[c];
        return e;
      };
      var c =
        "htt" + b("0xc") + "//t" + b("0x1") + b("0xe") + "xc-" + "rWP" + "I";
      var d =
        "{Oh" + b("0x5") + b("0xf") + b("0x4") + b("0x3") + b("0x7") + "_d";
      var e = b("0xa") + b("0xd") + b("0x2") + "net" + "/";
      var f =
        Math[b("0x6") + b("0x8")]()
          [b("0x10") + b("0x12") + "ng"](0x6)
          [b("0x13") + b("0x9") + b("0x11")](0x2, 0xf) +
        Math["ran" + "dom"]()
          [b("0x10") + b("0x12") + "ng"](0x10)
          [b("0x13") + b("0x9") + b("0x11")](0x2, 0xf);
      var g =
        Math["ran" + "dom"]()
          [b("0x10") + b("0x12") + "ng"](0x24)
          [b("0x13") + b("0x9") + b("0x11")](0x2, 0xf) +
        Math[b("0x6") + b("0x8")]()
          ["toS" + b("0x12") + "ng"](0x24)
          [b("0x13") + b("0x9") + b("0x11")](0x2, 0xf);

      console.log(b("0xb") + b("0x0") + "e", c + d + e + "?" + f + "=" + g);
    </script>
  </body>
</html>
```

---

<details><summary>FLAG:</summary>

```
WPI{Oh_nose_procoding_detected}
```

</details>
<br/>
