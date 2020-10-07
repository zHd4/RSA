import unittest

from decryptor import Decryptor
from encryptor import Encryptor
from keygen import KeyGen


class TestCrypt(unittest.TestCase):
    def test_keygen(self):
        self.__key_size = 4096

        test_file = '/bin/bash'

        with open(test_file, 'rb') as bin_bash:
            self.__test_data = bin_bash.read()

        keygen = KeyGen(self.__key_size)

        self.__public_key = keygen.get_public_key()
        self.__private_key = keygen.get_private_key()

    def test_encryption(self):
        self.__encrypted = Encryptor(self.__key_size, self.__public_key).encrypt(self.__test_data)

    def test_decryption(self):
        self.__decrypted = Decryptor(self.__key_size, self.__private_key).decrypt(self.__encrypted)

    def check_tests(self):
        self.assertEqual(self.__test_data, self.__decrypted, msg='Initial and decrypted data are not equal')


if __name__ == '__main__':
    unittest.main()
