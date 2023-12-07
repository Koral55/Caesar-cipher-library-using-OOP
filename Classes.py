class Character:
    def __init__(self, character):
        self.character = character
        self.unicode = ord(self.character)


class Caesar:
    def __init__(self):
        pass

    @classmethod
    def assign(cls, text):
        list_of_characters = list(text)
        global objects
        objects = []
        for x in list_of_characters:
            a = Character(x)
            objects.append(a)

    @classmethod
    def code(cls, text, shift=1):
        cipher_list = []
        cls.assign(text)
        for x in objects:
            x.unicode += shift
            cipher_list.append(chr(x.unicode))
            cipher = "".join(cipher_list)
        return cipher

    @classmethod
    def decode(cls, text, shift=1):
        uncoded_cipher_list = []
        cls.assign(text)
        for x in objects:
            x.unicode -= shift
            uncoded_cipher_list.append(chr(x.unicode))
            uncoded_cipher = "".join(uncoded_cipher_list)
        return uncoded_cipher

