import random
import sys


def generator(l, m):
    char = "abcdefghijkmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ!#?=%&@£$€"
    password = []
    password2 = []
    for x in range(l):
        random_letter = random.choice(char)
        password.append(random_letter)
    for y in range(m):
        random_number = random.randint(0, 9)
        password.append(str(random_number))
    for z in range(len(password)):
        randomchar = random.choice(password)
        password2.append(randomchar)
    print("\n", "".join(password2))


def length():
    password_letters = input("Characters: ")
    passletboo = True
    try:
        password_letters = int(password_letters)
    except:
        passletboo = False
        return passletboo
    if not passletboo:
        password_letters = input("Characters: ")
    password_numbers = input("Numbers: ")
    passnumboo = True
    try:
        password_numbers = int(password_numbers)
    except:
        passnumboo = False
        return passnumboo
    if not passnumboo:
        password_numbers = input("Numbers: ")
    generator(password_letters, password_numbers)


quit = True


def UserQuit():
    user_quit = input("\nTry again? y/n: ")
    if user_quit == "y":
        quit = True
    elif user_quit == "n":
        sys.exit()
    return quit


while quit:
    print("Generate a password.\nSet your number of characters,\nand numbers.      (must be an integer)\n")
    length()
    UserQuit()
