from flask import Flask, jsonify
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

PORT = int(os.getenv("PORT", 8080))
HOST = os.getenv("HOST", '0.0.0.0')
SECRET_KEY = os.getenv("SECRET_KEY")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")

@app.route('/')
def get_secrets():
    return jsonify({
        "hello": "Hello",
        "first_page": "/data",
        "second_page": "/secrets"
    })

@app.route('/data')
def get_data():
    with open('data.json', 'r') as file:
        data = file.read()
    return jsonify(data)

@app.route('/secrets')
def get_secrets():
    return jsonify({
        "secretKey": SECRET_KEY,
        "user": USER,
        "password": PASSWORD
    })

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
