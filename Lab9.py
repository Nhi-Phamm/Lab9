def encode(num: str):
    encoded = ""
    for nums in num:
        encoded += str(int(nums) + 3)
    return encoded

def decode(encoded_nums: str) -> str:
    decoded = ""
    for num in encoded_nums:
        decoded += str(int(num) - 3)

    return decoded

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
            password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif option == "2":
            decoded_pass = decode(password)
            print(f"The encoded password is {password}, and the original password is {decoded_pass}.\n")
        elif option == "3":
            break

if __name__ == "__main__":
    main()




