#### Challenge:

Ahoy, deck cadet,

your task is to prepare good coffee for captain. As a cadet, you are prohibited from going to the captain's cabin, so you will have to solve the task remotely. Good news is that the coffee maker in captain's cabin is online and can be managed via API. 

May you have fair winds and following seas!

Coffee maker API is available at <a href="http://coffee-maker.cns-jv.tcc" target="_blank">http:&#47;&#47;coffee-maker.cns-jv.tcc</a>.

---

#### Solution:
We were presented with a simple API server <a href="http://coffee-maker.cns-jv.tcc" target="_blank">http:&#47;&#47;coffee-maker.cns-jv.tcc</a>. After accessing it showed the following message
```json
{"status":"Coffemaker ready","msg":"Visit /docs for documentation"}
```
Based on the message above, we went to <a href="http://coffee-maker.cns-jv.tcc/docs" target="_blank">http:&#47;&#47;coffee-maker.cns-jv.tcc/docs</a> which made the Coffeemaker API available.

Firstly, we expanded the `/coffeeMenu`, then clicked on the `Try it out` and `Execute` buttons. This returned the following response:
```json
{
  "Menu": [
    {
      "drink_name": "Espresso",
      "drink_id": 456597044
    },
    {
      "drink_name": "Lungo",
      "drink_id": 354005463
    },
    {
      "drink_name": "Capuccino",
      "drink_id": 234357596
    },
    {
      "drink_name": "Naval Espresso with rum",
      "drink_id": 501176144
    }
  ]
}
```


As we need to prepare a **good** coffee for the captain, the only acceptable option from the coffee menu is the **Naval Espresso with rum**.
Next, we examine the POST method `/makeCoffee/`, which takes `drink_id` as a value. We use the value for the **Naval Espresso with rum**.
```json
{
  "drink_id": 501176144
}
```

Executing the `/makeCoffee/` method with this value returns the following response which contains the FLAG
```json
{
  "message": "Your Naval Espresso with rum is ready for pickup",
  "validation_code": "Use this validation code FLAG{ccLH-dsaz-4kFA-P7GC}"
}
```


---
<details><summary>FLAG:</summary>

```
FLAG{ccLH-dsaz-4kFA-P7GC}
```

</details>
<br/>
