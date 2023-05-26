# importing the random module to generate random characters
import random
# importing the string module to get the string of characters
import string

# defining the function to generate the password
def generate_password():
    # user decides the length of the password
    length = int(input("Enter the desired length of the password: "))
    # user decides if to make lowercase letters available; abcdefghijklmnopqrstuvwxyz
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == "y"
    # user decides if to make uppercase letters available; ABCDEFGHIJKLMNOPQRSTUVWXYZ
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    # user decides if to include numbers; 0123456789
    include_digits = input("Include digits? (y/n): ").lower() == "y"
    # user decides if to make special characters available; !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    include_special_chars = input("Include special characters? (y/n): ").lower() == "y"

    # creating an empty string that will be used to store all the characters that the user chose to include in the password
    character_pool = ""
    # if the user chose to include lowercase letters, add them to the character pool
    if include_lowercase:
        character_pool += string.ascii_lowercase
    # if the user chose to include uppercase letters, add them to the character pool
    if include_uppercase:
        character_pool += string.ascii_uppercase
    # if the user chose to include digits, add them to the character pool
    if include_digits:
        character_pool += string.digits
    # if the user chose to include special characters, add them to the character pool
    if include_special_chars:
        character_pool += string.punctuation

    # randomly chooses characters from the 'character_pool' string, 'length' number of times (for loop). for _ in range(length) indicates the loop index is not needed. Concatenate (join) the chosen characters in an empty string "" to form the password string. Store it in the 'password' variable.
    password = "".join(random.choice(character_pool) for _ in range(length))
    # print the generated password
    print("Generated Password:", password)

# calling the function
generate_password()