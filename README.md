# HOW TO USE
1. To **code** a message use code() function like so: Enigma(text="text to code").code() 
2. To **decode** a message use decode() function like so: Enigma(text="text to decode").decode() 
3. Default unicode shift of a character is 1, if you want to **change shift value**, let's say to 3, simply add shift=3 like so: Enigma(text="text to code", shift=3).code()
4. Remember, that when decoding a message, **shift value must be the same** as when the message was coded.
