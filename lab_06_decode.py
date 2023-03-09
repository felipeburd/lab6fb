
def decoder(password):
    decode_password=""
    for nums in password:
        decode_password= decode_password +str((int(nums)-3) % 10)

    return decode_password



