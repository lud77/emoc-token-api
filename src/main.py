from flask import Flask, request, jsonify
import jwt
from cryptography.hazmat.primitives import serialization

app = Flask(__name__)

private_key = open('.ssh/id_rsa', 'r').read()
key = serialization.load_ssh_private_key(private_key.encode(), password=b'')

@app.route("/get-token/<secret>", methods=["POST"])
def get_token(secret):
    data = request.get_json()

    token = jwt.encode(
        payload = data,
        key = secret
    )
    return token

@app.route("/get-secure-token/", methods=["POST"])
def get_secure_token():
    data = request.get_json()

    token = jwt.encode(
        payload = data,
        key = key,
        algorithm='RS256'
    )
    return token


if __name__ == "__main__":
    app.run(debug=True)