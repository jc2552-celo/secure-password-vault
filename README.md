# 🔐 Secure Password Vault CLI

A Python-based command-line password vault that encrypts and stores passwords securely using symmetric encryption.

## 🚀 Features

- AES encryption using the `cryptography` library
- Add, retrieve, and delete password entries
- Master password-based vault encryption
- CLI-based REPL loop
- Auto-encrypts vault on exit
- Unit tests and GitHub Actions CI

## 📦 Setup

```bash
git clone https://github.com/YOUR_USERNAME/secure-password-vault.git
cd secure-password-vault
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## ▶️ Usage

```bash
python cli.py
```

## 🧪 Run Tests

```bash
pytest --cov=vault tests/
```
