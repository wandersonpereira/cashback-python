import jwt
import datetime

class Jwt:
    hasKey: str = '97E7AE26DD766'
    algorithm: str = 'HS256'
    secondsExp = 60 * 60 * 24

    def encrypt(self, payload):
        payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=self.secondsExp)
        return jwt.encode(payload, self.hasKey, self.algorithm)
    
    def decrypt(self, token):
        return jwt.decode(token, self.hasKey, self.algorithm)