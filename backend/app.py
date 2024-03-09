from flask import Flask, jsonify, render_template, request, redirect, url_for, session
import json 
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

users = {
    "user1": "password",
    "user2": "password2"
}


@app.route('/')
def hello():
    return "hello world"

@app.route('/users')
def all_users():
    return jsonify(users)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify(error="Both username and password are required"), 400

    if username in users and users[username] == password:
        return jsonify(message="Login successful"), 200
    else:
        return jsonify(error="Invalid username or password"), 401
    
@app.route('/user',methods=['POST'])
def submit():
    data = request.json
    if data.get('username') not in users:
        username = data.get('username')
        password = data.get('password')
        if username and password:
            users[username] = password
            return jsonify(message=f"User was successfully added"), 200
        else: 
            return jsonify(error=" Must include both username and password"), 404
    else:
        return jsonify(error=" Usename already exist"), 404
    

if __name__ == '__main__':
    app.run()


