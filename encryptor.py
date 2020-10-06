from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class Encryptor:
    def __init__(self, key_length, public_key):
        self.__length = key_length
        self.__public_key = RSA.importKey(public_key)

        self.__crypto = PKCS1_OAEP.new(self.__public_key)

    def __split_to_blocks(self):
        pass

    def __join_to_blocks(self):
        pass

    def encrypt(self, data_bytes):
        return self.__crypto.encrypt(data_bytes)
