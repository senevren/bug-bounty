# CSC Course
# Save a random salt and a hashed password to binary files for later use

import hashlib
import os

# Hash the user's password using a random salt

original_password = input('Enter password: ')
the_salt = os.urandom(32)
the_key = hashlib.pbkdf2_hmac('sha256', original_password.encode('utf-8'), the_salt, 100000)

# Create binary files, then save the salt and hashed password to the files

f = open('salts', 'wb')
h = open('hashes', 'wb')
f.write(the_salt)
h.write(the_key)

# Display the hashes as strings, then close the files

print("The salt is: " + (str(the_salt)))
print("The hashed password is: " + (str(the_key)))

f.close()
h.close()

# The End!
