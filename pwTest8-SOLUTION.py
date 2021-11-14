# CSC Course
# Please make sure you have installed passlib. At a command prompt enter: pip install passlib

# Have fun with argon2 hashing

from passlib.hash import argon2

original_password = input('Enter password: ')

# Calculate the hash including a random salt

some_hash = argon2.using(rounds=4).hash(original_password)

print("This is your password hash: ")
print(some_hash)

# Validate the password by comparing hashes

new_password = input('Enter password: ')
new_hash = str(argon2.using(rounds=4).hash(new_password))
if argon2.verify(new_password, some_hash):
    print('Your password is correct! Come on in!')
else:
    print("Sorry, wrong password! Look at how different the hash is: ")
    print(new_hash)

# The End!
