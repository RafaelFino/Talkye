from http import HTTPStatus
from flask import Flask, request
from datetime import datetime, timedelta, timezone
from flasgger import Swagger, swag_from
from cryptography.hazmat.primitives import serialization
import jwt
import json
from modules.crypto import AssimetricCrypto, SymetricCrypto

class Talkye:
    def __init__(self) -> None:        
        self.app = Flask(__name__)
        self.swagger = Swagger(self.app)
        self.cripto = AssimetricCrypto()

if __name__ == "__main__":
    talkye = Talkye()
    talkye.app.run(host="
