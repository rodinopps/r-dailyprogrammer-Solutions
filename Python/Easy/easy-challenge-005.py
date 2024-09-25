username = "roro"
password = "majora"

while True:
    try1 = input("Enter correct username: ")
    try2 = input("Enter correct password: ")
    if try1 == username and try2 == password:
        print("you've met with a terrible fate, haven't you?")
        break
    else:
        print("You FOOL! Try again!")
