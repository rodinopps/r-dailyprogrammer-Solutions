name = input("Enter your name: ")
age = input("Enter your age: ")
reddit = input("Enter your reddit username: ")

with open('info.txt', 'w') as file:
    file.write(f"Your name is {name}, you are {age} years old, and your username is {reddit}\n")

print("Info has been saved to a text file:")
