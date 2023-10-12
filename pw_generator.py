import random

password_characters = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'

password = ''

print("Your password is:")

for x in range(16):
    password += random.choice(password_characters)

print(password)