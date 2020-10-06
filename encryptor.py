from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class Encryptor:
    def __init__(self, key_length, public_key):
        self.__length = key_length
        self.__public_key = RSA.importKey(public_key)

        self.__crypto = PKCS1_OAEP.new(self.__public_key)

    def __split_to_blocks(self, data):
        size = len(data)
        length = self.__length

        if size <= length:
            return [data]
        else:
            result = []

            for i in range(int(size / length)):
                result.append(data[length * i:length * (i + 1)])

            last = size % length

            if last != 0:
                result.append(data[:size - last])

            return result

    def __join_blocks(self):
        pass

    def encrypt(self, data_bytes):
        return self.__crypto.encrypt(data_bytes)
