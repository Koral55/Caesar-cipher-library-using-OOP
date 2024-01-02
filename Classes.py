class Caesar:
    def __init__(self):
        pass

    @classmethod
    def code(cls, input_text, shift=1):
        coded_message = ""
        for x in input_text:
            coded_message += chr(ord(x) + shift)
        return coded_message

    @classmethod
    def decode(cls, input_code, shift=1):
        decoded_message = ""
        for x in input_code:
            decoded_message += chr(ord(x) - shift)
        return decoded_message
