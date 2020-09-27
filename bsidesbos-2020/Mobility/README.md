#### Challenge:

Always wanted to calculate HMACs on your phone? Check out our new app! It supports 6 different algorithms.

---

#### Solution:

- decompile `apk` and check `MainActivity.java` for constants

```java
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView((int) R.layout.activity_main);
        final TextView textView = (TextView) findViewById(R.id.result_tv);
        final EditText editText = (EditText) findViewById(R.id.input_et);
        Button button = (Button) findViewById(R.id.submit);
        byte[] bArr = {102, 108, 97, 103, 123, 99, 108, 97, 115, 115, 105, 99, 95, 97, 112, 107, 95, 100, 101, 99, 111, 109, 112, 105, 108, 101, 95, 115, 104, 101, 110, 97, 110, 105, 103, 97, 110, 115, 125};
        StringBuilder sb = new StringBuilder("");
        for (int i = 0; i < 39; i++) {
            sb.append((char) bArr[i]);
        }
        this.secret = sb.toString();
        final Spinner spinner = (Spinner) findViewById(R.id.algorithm);
        ArrayAdapter arrayAdapter = new ArrayAdapter(this, 17367048, new String[]{"HmacMD5", "HmacSHA1", "HmacSHA224", "HmacSHA256", "HmacSHA384", "HmacSHA512"});
        arrayAdapter.setDropDownViewResource(17367049);
        spinner.setAdapter(arrayAdapter);
        button.setOnClickListener(new OnClickListener() {
            public void onClick(View view) {
                textView.setText(MainActivity.hmacDigest(editText.getText().toString(), MainActivity.this.secret, spinner.getSelectedItem().toString()));
            }
        });
    }
```

```python
flag = [102, 108, 97, 103, 123, 99, 108, 97, 115, 115, 105, 99, 95, 97, 112, 107, 95, 100, 101, 99, 111, 109, 112, 105, 108, 101, 95, 115, 104, 101, 110, 97, 110, 105, 103, 97, 110, 115, 125]
"".join(map(lambda c: chr(c), flag))
```

---

<details><summary>FLAG:</summary>

```
flag{classic_apk_decompile_shenanigans}
```

</details>
<br/>
