from flask import Flask, request, jsonify
import jwt
import datetime
#import flask limiter
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import logging

logging.basicConfig(
    filename="security.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)
app = Flask(__name__)

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]
)

SECRET_KEY = "supersecretkey"
@app.route("/")
def home():
    return "Secure Authentication App Running"

#create-database 
import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db() 

#add bcrypt
import bcrypt
from flask import request, jsonify

#registration route 
@app.route("/register", methods=["POST"])
def register():

    data = request.get_json()
    username = data["username"]
    password = data["password"]

    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
        conn.commit()
    except:
        return jsonify({"message": "User already exists"})

    conn.close()

    return jsonify({"message": "User registered successfully"})

#login route
@app.route("/login", methods=["POST"])
@limiter.limit("5 per minute")
def login():

    data = request.get_json()
    username = data["username"]
    password = data["password"]

    ip = request.remote_addr
    logging.info(f"Login attempt from {ip} with username {username}")

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    conn.close()

    if user and bcrypt.checkpw(password.encode("utf-8"), user[0]):

        token = jwt.encode({"user": username}, "secret", algorithm="HS256")

        return jsonify({"token": token})

    return jsonify({"message": "Invalid credentials"}), 401
    


#require authentication
@app.route("/profile", methods=["GET"])
def profile():

    token = request.headers.get("Authorization")

    if not token:
        return jsonify({"message": "Token missing"}), 403

    try:
        decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({"user": decoded["user"]})

    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token expired"}), 401
if __name__ == "__main__":
    app.run(debug=True)
