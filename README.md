Secure Authentication API

A secure authentication API built with Python and Flask that implements common security controls used in modern web applications.

This project demonstrates secure password storage, authentication, brute-force protection, and security logging, simulating how authentication systems are designed in production environments.

Features
User registration system
Secure password hashing using bcrypt
Token-based authentication using JSON Web Token
Brute-force attack protection with Flask-Limiter
SQLite user database
Login attempt monitoring and logging
Account lockout after multiple failed login attempts
Security Controls Implemented
Control	Purpose
Password Hashing	Protects stored passwords using bcrypt
JWT Authentication	Secure session token generation
Rate Limiting	Prevents brute-force login attacks
Account Lockout	Locks user account after multiple failed attempts
Logging	Enables monitoring of authentication activity
Project Structure
secure-auth-app
│
├── app.py
├── users.db
├── requirements.txt
└── security.log
Installation

Clone the repository:

git clone https://github.com/yourusername/secure-auth-app.git
cd secure-auth-app

Install dependencies:

pip install -r requirements.txt

Run the application:

python app.py

The API will start on:

http://127.0.0.1:5000
API Endpoints
Register User
POST /register

Example request:

{
  "username": "testuser",
  "password": "securepassword"
}

Response:

User registered successfully
Login
POST /login

Example request:

{
  "username": "testuser",
  "password": "securepassword"
}

Response:

{
  "token": "JWT_TOKEN"
}
Example Attack Protection

If a user attempts to log in multiple times with incorrect credentials:

Requests are rate limited
Failed attempts are tracked
After 5 failed attempts, the account is locked

This simulates real-world authentication protection against brute force attacks.

Security Logging

Authentication activity is logged for monitoring and detection purposes.

Example log entry:

Failed login attempt for user: admin

These logs could be forwarded to a SIEM system for threat detection.

Technologies Used
Python
Flask
bcrypt
JSON Web Token
Flask-Limiter
SQLite
Future Improvements
Containerize the application using Docker
Add role-based access control
Implement refresh tokens
Integrate with a SIEM for real-time alerting
Deploy to a cloud environment
Learning Objectives

This project was built to practice:

Secure authentication design
Defensive programming practices
Brute-force attack mitigation
Security monitoring concepts
Backend API development