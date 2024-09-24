force = input("Enter force: ")
mass = input("Enter mass:")
acc = input("Enter acceleration: ")
choice = input("Press F, M or A")

if choice.lower() == "f":
    print(int(mass) * int(acc))
    
elif choice.lower() == "m":
    print(int(force) / int(acc))

elif choice.lower() == "a":
    print(int(force) / int(mass))
