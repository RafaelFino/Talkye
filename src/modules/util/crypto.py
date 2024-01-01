# References
# https://medium.com/@ashiqgiga07/asymmetric-cryptography-with-python-5eed86772731
#

import base64
import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet

class AssimetricCrypto:  
    def __init__(self):
        if not os.path.exists('./keys'):    
            os.mkdir('./keys')
        
        self._pr_path = f"./keys/private_key.pem"
        self._pu_path = f"./keys/public_key.pem"  
      
        if not os.path.isfile(self._pr_path):
            # create keys
            self._key = rsa.generate_private_key(
                backend=default_backend(),
                public_exponent=65537,
                key_size=2048
            )

            with open(self._pr_path, 'wb') as pr:
                pr.write(self._key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.PKCS8,
                    encryption_algorithm=serialization.NoEncryption()
                ))

            with open(self._pu_path, 'wb') as pu:
                pu.write(self._key.public_key().public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                ))
        else:
            with open(self._pr_path, 'rb') as key_file:
                self._key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )

        self._padding = padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )

    def Decript(self, message:str):
        base64_bytes = message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        return self._key.decrypt(message_bytes, self._padding).decode('ascii')

    def GetPrivateKey(self):
        return self._key

    def GetPublicKey(self):
        return self._key.public_key()

   
class Crypto:
    def __init__(self, key: str) -> None:
        self.key  = base64.b64encode(str(key.ljust(32, "#")[:32]).encode('ascii'))
        self.cipher = Fernet(self.key, backend=None)
    
    def encrypt(self, message: str) -> str:
        return self.cipher.encrypt(message.encode('ascii')).decode('ascii')

    def decrypt(self, message: str) -> str:
        m = message.encode('ascii')
        return self.cipher.decrypt(m,).decode('ascii')

