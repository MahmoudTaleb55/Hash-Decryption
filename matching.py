from passlib.hash import phpass

hash = 'Your hash'
passwords = [
    # List your wordlist here
]

for password in passwords:
    if phpass.verify(password, hash):
        print(f"The password is: {password}")
        break
