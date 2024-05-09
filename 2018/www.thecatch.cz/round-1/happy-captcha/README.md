#### Challenge:

Agent, we have discovered a service protected by a very peculiar CAPTCHA mechanism. If we can beat it using a computer, we might me able to enumerate the service and get a lot of information. That will take a lot of requests and we just don't have the manpower to do these CAPTCHAs by hand. To pass the CAPTCHA you need to identify "happy" smiley faces. Then lookup their R, G and B color channels. For each channel, xor together the values of all "happy" smileys and present the results to the CAPTCHA mechanism. You only get one try per image. Submit your results via POST or GET (whichever you like). Submit the values in decimal. Use parameters names of `r` (for the _red_ channel), `g` and `b`. There is also a time limit present! You have up to 5 seconds to submit your answer. [http://challenges.thecatch.cz:10001/](http://challenges.thecatch.cz:10001/) Good luck, Agent

---

#### Solution:

Unfortunately, I have lost the source codes for the solution of this challenge while cleaning up old VMs, so I will only document the idea behind my solution. We are presented with the captcha image that always contains 16 smiley faces and we are to find all the `happy faces` and to prove we found them we have to send `GET` request like `http://challenges.thecatch.cz:10001/?r=XXX&g=YYY&b=ZZZ`, where `XXX`, `YYY` and `ZZZ` are the result of `XOR` operation applied to the `RED`, `GREEN` and `BLUE` color components of all the `happy` smiley faces.

After inspecting few generated images I noticed following patterns:
- there are `always` `3 happy` faces and `13 sad` faces and only these two types exist
- each of the faces has different color, size, rotation and position in image
- the position never goes outside the uniform regular 4x4 grid
- the background is perfect black (`#000`) and colors of the smiley faces are sharp and consistent, so there are always only 17 colors in the captcha image (black background color and 16 smiley face colors)

With this knowledge, I have written python code that will split the image according to the grid getting 16 sub-images, each containing one smiley face and only 2 colors (background and smiley color). I have also written a function that will take 3 of these sub-images, (at that time the sub-image selection was hard-coded to 3 different sub-images), find the smiley face colors within them (simply taking first non-black pixel), `XOR` the respective channels, send the request and print the response. Only problem left to solve, was how to select the tree sub-images containing the smiley faces.

While I was struggling with setting up `OpenCV` for happy/sad detection, I left the program running in endless loop as it was, with the hard-coded selection, because the organizers hinted, that you have to solve only one captcha (so they were not multiple captchas chained, like its customary in these types of challenges). Since the number of all faces is `16` and number of `happy` faces is fixed to `3` and `XOR` is `symmetrical` operation, based on that, number of possible options is `'combinations of 3 out of 16' = 16C3 = 560`. So the chance to pick correct solution in one try is `1:560 = 0.0017857 ~= 0.18%`. I have actually done this math before trying to tackle the problem with `OpenCV`, that's why I let the partial solution run in endless loop. The tries were as fast as one round of HTTP request/response and there was no rate limiting / timeout / back-off (apart from the server going down, (probably because of me, so I then inserted a little sleep between tries) ). After few thousands tries the partial program actually hit the correct three sub-images and revealed the flag.

---

<details><summary>FLAG:</summary>

```
CT18-8Bl8-5Eyl-QGbO-GoY2
```

</details>
