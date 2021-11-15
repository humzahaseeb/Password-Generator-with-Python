# password generator
import random

print("Welcome to Password Generator")

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'

number_of_passwords = int(input("\nHow many passwords do you want? : "))
number_of_characters = int(input("How many characters would you like your password to be? :  "))


for p in range(number_of_passwords):
    password = ''
    for c in range(number_of_characters):
        password += random.choice(characters)
    print(password)