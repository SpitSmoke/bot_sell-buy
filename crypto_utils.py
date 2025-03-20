from cryptography.fernet import Fernet
import os

SECRET_KEY_FILE = "secret.key"

def generate_secret_key():
    """ Gera e salva uma chave secreta para criptografia """
    if not os.path.exists(SECRET_KEY_FILE):
        key = Fernet.generate_key()
        with open(SECRET_KEY_FILE, "wb") as key_file:
            key_file.write(key)

def load_secret_key():
    """ Carrega a chave secreta """
    with open(SECRET_KEY_FILE, "rb") as key_file:
        return key_file.read()

def encrypt_data(data):
    """ Encripta os dados com AES """
    cipher = Fernet(load_secret_key())
    return cipher.encrypt(data.encode()).decode()

def decrypt_data(encrypted_data):
    """ Desencripta os dados """
    cipher = Fernet(load_secret_key())
    return cipher.decrypt(encrypted_data.encode()).decode()

# Gera a chave secreta ao iniciar o sistema
generate_secret_key()
