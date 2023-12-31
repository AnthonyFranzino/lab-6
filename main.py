def encode_password(user_password):
    # set encoded password blank
    encoded_password = ""
    for digit in str(user_password):
        # add 3 to the digit but if greater than 6 we have to make seperate rules
        encoded_digit = str((int(digit) + 3) % 10)  # use modulo division to keep it less than or equal to 9
        # add the new digit into the new encoded password
        encoded_password += encoded_digit
    return encoded_password

def decode_password(encoded):
    password = ""
    for num in str(encoded):
        new_num = str((int(num) - 3) % 10)
        password += new_num
    return password

# l
def menu():
    user_option = ""
    encoded = ""
    while user_option != "3":
        print("Menu")
        print("-------------")
        print("1. Encode\n2. Decode\n3. Quit")
        print("")
        print("")

        user_option = input("Please enter an option: ")
        if user_option == "1":
            user_password = input("Enter the password to encode: ")
            encoded = encode_password(user_password)  # Store the encoded password
            print("Your password has been encoded and stored!")
            print("")
            encode_password(user_password)
        if user_option == "2":
            decoded = decode_password(encoded)
            print("The encoded password is " + encoded + " and the original password is " + decoded + ".")
            print("")
        if user_option == "3":
            break

# sdf


menu()