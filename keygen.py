from Crypto.PublicKey import RSA


class KeyGen:
    def __init__(self, key_length):
        self.__key_pair = RSA.generate(key_length)

    def get_public_key(self):
        return self.__key_pair.publickey()

    def get_private_key(self):
        return self.__key_pair
