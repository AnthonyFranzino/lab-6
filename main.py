def decode_password(encoded):
    password = ""
    for num in str(encoded):
        new_num = str((int(num) - 3) % 10)
        password += new_num
    return password


def menu():

    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    user_selection = int(input("Please enter an option: "))

    if user_selection == 2:
        decoded = decode_password(encoded)
        print("The encoded password is " + encoded + ", and the original password is " + decoded + ".")
