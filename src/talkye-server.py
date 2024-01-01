from http import HTTPStatus
from flask import Flask, request
from datetime import datetime, timedelta, timezone
from flasgger import Swagger, swag_from
from cryptography.hazmat.primitives import serialization
import jwt
import json
from modules.crypto import AssimetricCrypto, SymetricCrypto

def main():
    app = Flask(__name__)
    swagger = Swagger(app)
    cripto = AssimetricCrypto()

if __name__ == "__main__":
    main()
