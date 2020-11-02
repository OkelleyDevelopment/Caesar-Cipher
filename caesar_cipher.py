from string import ascii_letters

def encrypt(message, key):

    lexicon = ascii_letters

    result = ""

    for char in message:
        if char not in lexicon:
            result += char
        else:
            new_key = (lexicon.index(char) + key) % len(lexicon)
            result += lexicon[new_key]
    return result

def decrypt(message, key):
    return encrypt(message, (key * -1))



def main():
    while True:
        print("\n============ Menu ============")
        print(*["1.Encrpyt", "2.Decrypt", "3.Quit"], sep="\n")

        user_choice = input("Choose an option: ").strip() or "3"

        if user_choice not in ("1", "2", "3"):
            print("ERROR: Please enter a valid choice!")
        elif user_choice == "1":
            message = input("Please enter the string to be encrypted: ")
            key = int(input("Please enter off-set: ").strip())
            print(encrypt(message, key))
        elif user_choice == "2":
            message = input("Please enter the string to be decrypted: ")
            key = int(input("Please enter off-set: ").strip())
            print(decrypt(message, key))
        elif user_choice == "3":
            print("Farewell.")
            break

if __name__ == "__main__":
    main()






