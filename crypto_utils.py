
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import os

def generate_aes_key():
    key = get_random_bytes(16)  # AES-128
    with open("aes_key.key", "wb") as f:
        f.write(key)
    return key

def load_key():
    try:
        with open("aes_key.key", "rb") as f:
            return f.read()
    except FileNotFoundError:
        return None

def save_key(key):
    with open("aes_key.key", "wb") as f:
        f.write(key)

def encrypt_message(plaintext, key):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plaintext.encode())
    encrypted = cipher.nonce + tag + ciphertext
    return base64.b64encode(encrypted).decode()

def decrypt_message(ciphertext, key):
    try:
        encrypted = base64.b64decode(ciphertext.encode())
        nonce = encrypted[:16]
        tag = encrypted[16:32]
        cipher_text = encrypted[32:]
        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        return cipher.decrypt_and_verify(cipher_text, tag).decode()
    except Exception:
        return "[Decryption Failed]"
