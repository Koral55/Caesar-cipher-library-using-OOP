# HOW TO USE
1. To **receive a coded message** you can assign it to a variable like so: coded_message = Caesar.code(text="example text") 
2. To **receive a decoded message** you can assign it to a variable like so: decoded_message = Caesar.decode(text="coded text")  
3. Default unicode shift of a character is 1, if you want to **change shift value**, let's say to 3, simply add shift=3 to code() or decode() function like so: Caesar.code(text="example text", shift=3)
4. Remember that when decoding a message, **shift value must be the same** as when the message was coded.
