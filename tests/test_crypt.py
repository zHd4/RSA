import unittest
from keygen import KeyGen


class TestCrypt(unittest.TestCase):
    def test_keygen(self):
        self.__key_size = 4096

        keygen = KeyGen(self.__key_size)

        self.__public_key = keygen.get_public_key()
        self.__private_key = keygen.get_private_key()


if __name__ == '__main__':
    unittest.main()
