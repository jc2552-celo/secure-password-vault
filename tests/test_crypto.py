from cryptography.fernet import Fernet
from vault import crypto

def test_encrypt_decrypt():
    key = Fernet.generate_key()
    f = Fernet(key)
    message = b"secret"
    encrypted = crypto.encrypt(message, f)
    decrypted = crypto.decrypt(encrypted, f)
    assert decrypted == message
