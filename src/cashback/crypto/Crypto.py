from passlib.context import CryptContext

class Crypto(object):
    context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=50000
    )

    def encrypt(self, password):
        return self.context.hash(password.encode('utf8'))

    def isPasswordValid(self, password, passwordEncrypt):
        return self.context.verify(password, passwordEncrypt)