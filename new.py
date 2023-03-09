def encode(password):
    encoded_password = ""
    for num in password:
        encoded_password = encoded_password + str((int(num) + 3) % 10)
    return encoded_password


print(encode("12345555"))

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print(" ")
    option = input(print("Please enter an option: "))
    if option == 1:
        password = input("Please enter your password to encode: ")
        encode(password)
        print("Your password has been encoded and stored!")
    elif option == 2:
        pass



