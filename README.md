# Secure Authentication API

Flask JWT authentication API with an automated DevSecOps CI/CD pipeline — security gates block every commit that introduces vulnerabilities.

![Pipeline](https://github.com/kofid99/Secure-authentication-app/actions/workflows/pipeline.yml/badge.svg)

---

## What it does

- Secure user registration and login with bcrypt password hashing and JWT tokens
- Brute-force protection via rate limiting and account lockout after 5 failed attempts
- Security logging on all authentication events
- Fully containerized with Docker, non-root user, multi-stage build

---

## CI/CD Pipeline

| Stage | Tool | Fails On |
|-------|------|----------|
| Code Quality | flake8 | Unused imports, duplicate code |
| SAST | Bandit | Medium+ severity findings |
| Container Build | Docker | Build failure |
| CVE Scan | Trivy | CRITICAL or HIGH vulnerabilities |

## Security Findings Caught and Fixed

| CVE / Finding | Severity | Fix |
|---------------|----------|-----|
| B201 — Flask debug=True (arbitrary code execution) | High | Disabled, controlled via env var |
| CVE-2026-48526 — PyJWT auth bypass | High | Upgraded to 2.13.0 |
| CVE-2026-32597 — PyJWT crit header violation | High | Upgraded to 2.13.0 |

---

## How to Run

```bash
git clone https://github.com/kofid99/Secure-authentication-app.git
cd Secure-authentication-app
docker build -t secure-auth-api:v1 .
docker run -p 5001:5000 secure-auth-api:v1
```

**POST /register** and **POST /login** available at `http://localhost:5001`

---

## Tech Stack

GitHub Actions · Docker · Python 3.11 · Flask · Bandit · Trivy · flake8 · PyJWT · bcrypt · Flask-Limiter