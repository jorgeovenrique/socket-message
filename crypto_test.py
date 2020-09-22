# import hashlib
# m = hashlib.shake_256(b"mon message")
# m.update(b"qsdfkdfjkqlsndfklSEIROUTYHNX?SQNCIOZ")
# # print(m.digest(42))
# # print(m.hexdigest(42))
# dk = hashlib.pbkdf2_hmac('sha256', b'password', b'salt', 100000)
# print(dk)
# print(m)
# print(hashlib.algorithms_guaranteed)
# print(hashlib.algorithms_available)

# Utilise la bibliotèque python "cryptography" et importe la recette de haut niveau "fernet"
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"my deep dark secret")
print("fernet's token:")
print(token)
decrypted_token = f.decrypt(token)
print("fernet's decrypted token:")
print(decrypted_token)