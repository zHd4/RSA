from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class Encryptor:
    def __init__(self, key_length, public_key):
        self.__length = key_length
        self.__public_key = RSA.importKey(public_key)

        self.__crypto = PKCS1_OAEP.new(self.__public_key)

    def encrypt(self, data_bytes):
        return self.__crypto.encrypt(data_bytes)

    def __split_to_blocks(self, data):
        size, length = len(data), self.__length
        return [data[i:i + length] for i in range(0, size, length)]

    # noinspection PyMethodMayBeStatic
    def __join_blocks(self, blocks):
        return b''.join(blocks) if len(blocks) > 0 else blocks
