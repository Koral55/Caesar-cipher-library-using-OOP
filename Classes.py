class Character:
    def __init__(self, character):
        self.character = character
        self.unicode = ord(self.character)

class Enigma:
    def __init__(self, text, shift):
        self.text = text
        self.shift = shift
    def assign(self):
        list_of_characters = list(self.text)
        global objects
        objects = []
        for x in list_of_characters:
            a = Character(x)
            objects.append(a)
    def code(self):
        global cipher
        cipher_list = []
        self.assign()
        for x in objects:
            x.unicode += self.shift
            cipher_list.append(chr(x.unicode))
            cipher = "".join(cipher_list)
        print(cipher)

    def decode(self):
        global uncoded_cipher
        uncoded_cipher_list = []
        self.assign()
        for x in objects:
            x.unicode -= self.shift
            uncoded_cipher_list.append(chr(x.unicode))
            uncoded_cipher = "".join(uncoded_cipher_list)
        print(uncoded_cipher)









