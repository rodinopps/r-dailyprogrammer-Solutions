text = input("Enter text: ")
choice = input("Encrypt or decrypt? ")
if choice.lower() == "encrypt":
    eshift = {
'a': 'd', 'b': 'e', 'c': 'f', 'd': 'g', 'e': 'h', 'f': 'i', 'g': 'j', 
 'h': 'k', 'i': 'l', 'j': 'm', 'k': 'n', 'l': 'o', 'm': 'p', 'n': 'q', 
 'o': 'r', 'p': 's', 'q': 't', 'r': 'u', 's': 'v', 't': 'w', 'u': 'x', 
 'v': 'y', 'w': 'z', 'x': 'a', 'y': 'b', 'z': 'c', " ": " "}
    enc = ""
    for i in text:
        enc += eshift[i]
    print(enc)

elif choice.lower() == "decrypt":
    dshift = {
    'd': 'a', 'e': 'b', 'f': 'c', 'g': 'd', 'h': 'e', 'i': 'f', 'j': 'g', 
    'k': 'h', 'l': 'i', 'm': 'j', 'n': 'k', 'o': 'l', 'p': 'm', 'q': 'n', 
    'r': 'o', 's': 'p', 't': 'q', 'u': 'r', 'v': 's', 'w': 't ', 'x': 'u', 
    'y': 'v', 'z': 'w', 'a': 'x', 'b': 'y', 'c': 'z', " ": " "}
    dec = ""
    for i in text:
        dec += dshift[i]
    print(dec)

    
