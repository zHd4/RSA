import unittest
from keygen import KeyGen
from encryptor import Encryptor
from decryptor import Decryptor


class TestCrypt(unittest.TestCase):
    def test_crypt(self):
        key_size = 4096
        test_file = '/bin/bash'

        with open(test_file, 'rb') as bin_bash:
            test_data = bin_bash.read()

        keygen = KeyGen(key_size)

        public_key = keygen.get_public_key()
        private_key = keygen.get_private_key()

        encrypted = Encryptor(key_size, public_key).encrypt(test_data)

        decrypted = Decryptor(key_size, private_key).decrypt(encrypted)

        self.assertEqual(test_data, decrypted, msg='Initial and decrypted data are not equal')


if __name__ == '__main__':
    unittest.main()
