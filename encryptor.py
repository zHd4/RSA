from Crypto.Cipher import PKCS1_OAEP


class Encryptor:
    def __init__(self, key_length, public_key):
        self.__length = key_length
        self.__public_key = public_key

        self.__crypto = PKCS1_OAEP.new(public_key)

    def encrypt(self, data_bytes):
        return self.__crypto.encrypt(data_bytes)
