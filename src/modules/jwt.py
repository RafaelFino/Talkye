import jwt

class JWT:
    def __init__(self, privateKey, publicKey) -> None:
        self.privateKey = privateKey
        self.publicKey = publicKey

    def create(self, payload = {}):
        return jwt.encode(payload, key=self.privateKey, algorithm='RS256')    
    
    def getClaims(self, token):
        return jwt.decode(token, key=self.publicKey, algorithms=[ 'RS256', ], options={"verify_signature": True, "verify_exp": True})    