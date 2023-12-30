from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

@app.route("/get-token/<secret>", methods=["POST"])
def get_token(secret):
    data = request.get_json()

    token = jwt.encode(
        payload = data,
        key = secret
    )
    return token

if __name__ == "__main__":
    app.run(debug=True)