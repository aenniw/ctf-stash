#### Challenge:

Clam saw all those cool celebrities posting everything they do on twitter, so he decided to give it a go himself. Turns out, that's a horrible idea. After recovering from his emotional trauma, he wrote a [secure vault](https://secure-vault.web.actf.co) to store his deepest secrets. Legend has it that there's even a flag in there. Can you get it?

[Source](./index.js ":ignore")

---

#### Solution:
We need to exploit javascript true / false comparison and the fact that undefined is a "falsy" value - meaning that comparison between undefined and variable
will be evaluated as false. The server allows us to log in and get a signed JWT token in a cookie. We can copy this JWT token value to use later. 
Afterwards we log out and delete the user from storage and recreate the login cookie using the previously obtained JWT token value. 
The server checks the validity of the JWT and  attempts to find a user in its storage. 
If it cannot find one it creates an empty user object. Following that the server attempts to make check if user variable restricted is true
but since it is undefined the result is false and server will return the flag. 


```py



```

---

<details><summary>FLAG:</summary>

```
actf{is_this_what_uaf_is}
```

</details>
<br/>
