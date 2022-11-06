import hashlib

def hash_password(password):
    encrypte_password = hashlib.md5(password.encode()).hexdigest()
    return encrypte_password

print(hash_password('123456'))