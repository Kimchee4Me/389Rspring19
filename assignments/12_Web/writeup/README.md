# Crypto II Writeup

Name: Esther Malone
Section: 0101

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Esther Malone

## Assignment Writeup

### Part 1 (40 Pts)
For part one I noticed that each link had a similar URL that ended with item?id=num, with num varying with each page. I tried editing this with id=1 OR '1'='1', similary to the powerpoint slides. However this did not work and I tried other variations of this. Eventually I learned that I needed to use the || operator. So http://1337bank.money:5000/item?id=2' || '1' = '1 gave the flag: CMSC389R-{y0u_ar3_th3_SQ1_ninj@}. 

### Part 2 (60 Pts)

For the first level, I injected this script: <script>alert("alert")</script> which launched an alert stating "alert".

For the second level, I had to check the hints which recommended to use a JavaScript attribute, such as an img. I then used <img src="https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500" onload=alert("cat")>
This gave an alert "cat".

For the third level, I checked the hints and it recommended checking the JavaScript code. I could see + ".jpg'/>". So I edited the URL with https://xss-game.appspot.com/level3/frame#1.jpg' onload=alert("test")><img src='> and this gave the alert. 

For the fourth level it was a bit harder for me to figure out. I tried onalert again however this did not work. However I eventually realized what the hints meant and tried 3');alert('test and this worked. 

Initially for the fifth level I tried injecting scripts into the enter email: space. However this did not work, so I tried editing the URL next with https://xss-game.appspot.com/level5/frame/signup?next=javascript.alert("test") and this worked.

For the last level I had to use all of the hints that recommended using google.com/jsapi?callback=foo, I used this to change the URL to https://xss-game.appspot.com/level6/frame#//google.com/jsapi?callback=alert, which gave an undentified alert. 
