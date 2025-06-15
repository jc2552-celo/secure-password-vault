from cryptography.fernet import Fernet

def generate_key(password: str) -> bytes:
    return Fernet(Fernet.generate_key())  # Simplified; would normally derive key from password

def encrypt(data: bytes, fernet: Fernet) -> bytes:
    return fernet.encrypt(data)

def decrypt(data: bytes, fernet: Fernet) -> bytes:
    return fernet.decrypt(data)
