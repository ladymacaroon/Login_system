import hashlib

credentials = {}

with open("credentials.txt") as cred_file:
    for line in cred_file:
       (key, val) = line.split()
       credentials[key] = val

username = input("username: ")
password = input("password: ")

password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()

print(password_hash)

if credentials.get(username) == None:
    print("username not known")
else:
    if credentials[username] == password_hash:
        print("password valid")
    else:
        print("password invalid")
