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
    print("".join(password2))



def length():
    password_letters = int(input("Letters: "))
    while password_letters > 128:
        password_letters = int(input("Letters: "))
    password_numbers = int(input("Numbers: "))
    while password_numbers > 128:
        password_numbers = int(input("Numbers: "))
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
    print("Generate a password.\nSet your number of characters,\nand numbers.\n")
    length()
    UserQuit()
