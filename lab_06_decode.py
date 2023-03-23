
def decoder(password):
    decode_password=""
    for nums in password:
        decode_password= decode_password +str((int(nums)-3) % 10)

    return decode_password


def encode(password):
    encoded_password = ""
    for num in password:
        encoded_password = encoded_password + str((int(num) + 3) % 10)
    return encoded_password

def menu():
    print("Menu\n"
          "-------------\n" 
          "1. Encode\n" 
          "2. Decode\n" 
          "3. Quit\n")



while True:
    menu()
    options= int(input("Please enter an option: "))
    if options == 1:
        password = input("Please enter your password to encode: ")
        encoded = encode(password)
        print("Your password has been encoded and stored!")
        print()
    elif options == 2:
        decoded = decoder(encoded)
        print(f"The encoded password is {encoded}, and the original password is {decoded}.")
        print()

    elif options == 3:
        break
