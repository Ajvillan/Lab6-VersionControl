# Anthony Villanueva

def encode(password):
    encoded_password = ""
    for digit in password:
        new_digit = (int(digit) + 3)
        if new_digit >= 10: # Digits over 7 have 2 digits
            new_digit = (str(new_digit))[1]

        encoded_password += str(new_digit)

    return encoded_password

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!\n")

        elif option == "2":
            # decoded_pass = decode(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass}.\n")

        elif option == "3":
            break

        else:
            print("Invalid option. Try again!\n")


if __name__ == '__main__':
    main()