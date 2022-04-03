#### Challenge:

Can you sink all the server's ships? Me thinks no :P

`http://misc1.utctf.live:9998`

---

#### Solution:

- inspecting `websocket` traffic reveals that we send our map to `AI` player so that he can cheat. This is sent as an `protobuf` [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')Protobuf_Decode('',false,false)&input=MDgxNDEwMTQxYTBhMGEwNDA4MDAxMDAwMTAwMDE4MDUxYTBhMGEwNDA4MDAxMDAxMTAwMDE4MDQxYTBhMGEwNDA4MDAxMDAyMTAwMDE4MDMxYTBhMGEwNDA4MDAxMDAzMTAwMDE4MDMxYTBhMGEwNDA4MDAxMDA0MTAwMDE4MDIxYTBhMGEwNDA4MDAxMDA1MTAwMDE4MDUxYTBhMGEwNDA4MDAxMDA2MTAwMDE4MDQxYTBhMGEwNDA4MDAxMDA3MTAwMDE4MDMxYTBhMGEwNDA4MDAxMDA4MTAwMDE4MDMxYTBhMGEwNDA4MDAxMDA5MTAwMDE4MDI), sending a fake map allows us to play "fairly" and win.

```js
class WebSocket__ extends WebSocket {
    payload = "081410141a0a0a0408001000100018051a0a0a0408001001100018041a0a0a0408001002100018031a0a0a0408001003100018031a0a0a0408001004100018021a0a0a0408001005100018051a0a0a0408001006100018041a0a0a0408001007100018031a0a0a0408001008100018031a0a0a040800100910001802"
    sendCount = 0;
    send(args) {
        this.sendCount ++;
        console.log('send', this.sendCount, args.reduce((str, byte) => str + byte.toString(16).padStart(2, '0'), ''));
        if (this.sendCount === 2) {
            console.log('send', this.sendCount, this.payload);
            return super.send(
                new Uint8Array(this.payload.match(/.{1,2}/g).map(byte => parseInt(byte, 16)))
            );
        }
        return super.send(args);
    }
}

WebSocket = WebSocket__
```

---

<details><summary>FLAG:</summary>

```
utflag{if_u_want_it_done_right_dont_rely_on_client}
```

</details>
<br/>
