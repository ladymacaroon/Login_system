import hashlib

def menu():
    option = input("Do you want to login or register? ")
    if option == "login":
        login()
    else:
        print(f'Your username is: {register()}')

def register():
    username = create_username()
    password = input("Enter a password: ")
    encrypted_password = encrypt_password(password)
    with open("passwords.txt", "a") as file:
        file.write(f'{username} {encrypted_password}\n')
    
    return username

def create_username():
    fname = input("What is your first name? ")
    sname = input("What is your last name? ")
    age = input("What age are you? ")
    username = fname[:3] + sname[:3] + age
    
    return username

def login():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    encrypted_password = encrypt_password(password)

    with open("passwords.txt", "r") as file:
        for x in file:
            if x.strip() == f'{username} {encrypted_password}':
                print("Password is valid!")
                return None
        print("Password is invalid!")

def encrypt_password(password):
    password_hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return password_hash

menu()
