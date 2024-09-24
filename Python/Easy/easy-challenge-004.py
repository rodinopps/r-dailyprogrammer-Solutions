import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
special = "!@€£#$%^&*()-_=+[{]};:'\"|,<.>/?`~"

characters = lowercase + uppercase + digits + special

while True:
    enter = int(input("How many passwords do you want to generate? "))
    length = int(input("Enter length of passwords: "))
    for i in range(enter):
        print("".join(random.choice(characters) for i in range(length)))
        print()
