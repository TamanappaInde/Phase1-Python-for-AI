
def addressVal(address):
    dot = address.find(".")
    at = address.find("@")

    if (dot == -1):
        print("Invalid")
    elif (at == -1):
        print("Invalid")
    else:
        print("valid")

print("This program will validate your email address is valid")
while(True):
    print("A valid email address needs an '@' symbol and a '.'")
    x = input("Input your email address: ")

    addressVal(x)

    
    