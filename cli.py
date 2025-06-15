import json
import getpass
from cryptography.fernet import Fernet
from vault import crypto

VAULT_FILE = "vault.json"

def load_vault():
    try:
        with open(VAULT_FILE, "rb") as f:
            return f.read()
    except FileNotFoundError:
        return b''

def save_vault(encrypted_data):
    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted_data)

def main():
    print("🔐 Secure Password Vault CLI")
    password = getpass.getpass("Enter master password: ")
    key = Fernet.generate_key()
    fernet = Fernet(key)

    try:
        data = load_vault()
        decrypted = fernet.decrypt(data) if data else b'{}'
        vault = json.loads(decrypted.decode())
    except Exception:
        print("Failed to decrypt vault. Wrong password or corrupted file.")
        return

    while True:
        command = input("Command (add/get/delete/exit): ").strip().lower()
        if command == "exit":
            break
        elif command == "add":
            site = input("Site: ")
            pwd = input("Password: ")
            vault[site] = pwd
            print("✔️ Added.")
        elif command == "get":
            site = input("Site: ")
            print("🔑", vault.get(site, "Not found"))
        elif command == "delete":
            site = input("Site: ")
            vault.pop(site, None)
            print("🗑️ Deleted if it existed.")
        else:
            print("Unknown command.")

    encrypted = fernet.encrypt(json.dumps(vault).encode())
    save_vault(encrypted)
    print("🔒 Vault saved.")

if __name__ == "__main__":
    main()
