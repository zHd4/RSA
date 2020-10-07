from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


class Decryptor:
    def __init__(self, key_length, private_key):
        self.__length = key_length
        self.__crypto = PKCS1_OAEP.new(RSA.importKey(private_key))

    def decrypt(self, data_bytes):
        decrypted_chunks = []

        for chunk in self.__split_to_blocks(data_bytes):
            decrypted_chunks.append(self.__crypto.decrypt(chunk))

        return self.__join_blocks(decrypted_chunks)

    def __split_to_blocks(self, data):
        size, length = len(data), self.__length
        return [data[i:i + length] for i in range(0, size, length)]

    # noinspection PyMethodMayBeStatic
    def __join_blocks(self, blocks):
        return b''.join(blocks) if len(blocks) > 0 else blocks
