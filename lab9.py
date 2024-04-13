#Kexin Zhou
def main():
    user_input = None
    encode = ""

    while user_input != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        user_input = int(input("\nPlease enter an option: "))

        if user_input == 1:
            password_to_encode = input("Please enter your password to encode: ")
            encode = encode_password(password_to_encode)
            print("Your password has been encoded and stored!\n")

        if user_input == 2:
            decoded = decode(encode)
            print('The encoded password is ', encode, ', and the original password is ', decoded, '.\n', sep='')


def encode_password(password):
    newpassword = ""
    for i in (password):
        encode = int(i) + 3
        if encode >= 10:
            encode -= 10
            newpassword = newpassword + str(encode)
        else:
            newpassword = newpassword + str(encode)
    return newpassword


# def decode(password):
#     decoded_password = ""
#     for digit in password:
#         decoded_digit = int(digit) - 3
#         if decoded_digit < 0:
#             decoded_digit += 10
#         decoded_password += str(decoded_digit)
#     return decoded_password


# Hope Carter
def decode(password):
    decoded_pw = ""
    for j in password:
        if j <= '2':
            if j == '2':
                decoded_pw += '9'
            elif j == '1':
                decoded_pw += '8'
            elif j == '0':
                decoded_pw += '7'
        else:
            decoded_digit = int(j) - 3
            decoded_pw += str(decoded_digit)
    return decoded_pw


if __name__ == "__main__":
    main()
