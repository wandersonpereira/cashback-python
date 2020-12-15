import unittest
from src.cashback.crypto.Crypto import Crypto

class TestGetLogin(unittest.TestCase):

    def test_genereated_hash_and_check_pwd(self):
        hashPwd = Crypto().encrypt("test12300")
        self.assertTrue(Crypto().isPasswordValid("test12300", hashPwd))

if __name__ == '__main__':
    unittest.main()