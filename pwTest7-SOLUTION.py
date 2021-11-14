

# Retrieve the saved salt and password hash for password verification

import hashlib

# Prompt the user for their password

entered_password = input('Enter password: ')

# Open the saved files and retrieve the hashes

h = open('hashes', 'rb')
s = open('salts', 'rb')
saved_hashes = h.read()
saved_salts = s.read()

# Use the saved salt to hash the new password, then compare it to the original hash

provided_password = hashlib.pbkdf2_hmac('sha256', entered_password.encode('utf-8'), saved_salts, 100000)

if saved_hashes == provided_password:
    print('Password is correct')
else:
    print('Password is incorrect')

# Display hashes for comparison and close the files

print("The user's saved salt is: " + (str(saved_salts)))
print("The hash for the user's original password is:  " + (str(saved_hashes)))
print("The hash for the password the user entered is: " + (str(provided_password)))


h.close()
s.close()

# The End!
