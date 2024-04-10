def encode(num: str) -> str:
    encoded = ""
    for nums in num:
        encoded += nums str(list(num) + 3)
    return encoded



def main():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    while True:
        option = input("Please enter an option: ")

        if option == "1":
            password = input("Please enter your password to encode: ")


