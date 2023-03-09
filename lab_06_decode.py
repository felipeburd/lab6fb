
def decoder(password):
    decode_password=""
    for nums in password:
        decode_password= decode_password +str((int(nums)-3) % 10)

    return decode_password


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
       pass
    elif options == 2:
        decoded = decoder()
        print(f"The encoded password is {} , and the original password is {decoded}.")
        print()

    elif options == 3:
        break
