import random
import time
alfabet = "abcdefghijklmnopqrstuvwxyz"


def RandomNumber():
    print("Gaet et nummer mellem 1 og 100.")
    random_number = random.randint(1, 100)
    fundet = False
    gaet = 0
    while not fundet:
        bruger_gaet = input("Dit gaet: ")
        i = int(bruger_gaet)
        if i == random_number:
            print("\nRigtigt!")
            fundet = True
            gaet += 1
            print("antal gaet: ", gaet, "\n")
            time.sleep(1)
        elif i < random_number:
            print("Hoejere...")
            gaet += 1
        else:
            print("Lavere...")
            gaet += 1
    print("Tak for at spille!\n")
    time.sleep(1)


def RandomLetter():
    print("Gaet et bogstav mellem A og Z.")
    random_letter = random.choice(alfabet)
    fundet = False
    gaet = 0
    while not fundet:
        bruger_gaet = input("Dit gaet: ")
        i = (bruger_gaet)
        if i == random_letter:
            print("\nRigtigt!")
            fundet = True
            gaet += 1
            time.sleep(1)
            print("antal gaet: ", gaet, "\n")
            time.sleep(1)
        elif alfabet.index(random_letter) < alfabet.index(i):
            print("Laengere tilbage...")
            gaet += 1
        else:
            print("Laengere frem...")
            gaet += 1
    print("Tak for at spille!\n")
    time.sleep(1)


def menu():
    spil = ["[TAL-JAGT = 1]", "[BOGSTAV-JAGT = 2]"]
    print("=" * 80)
    print("Alle spil:")
    print(" ".join(spil))
    valg = str(input("Vaelg et spil: "))
    print("")
    if valg == "1":
        RandomNumber()
    elif valg == "2":
        RandomLetter()
    else:
        menu()


quit = True


def TryAgain(n):
    n = input("Vil du spille et nyt spil? j/n ")
    if n == "n":
        n = False
    elif n == "j":
        n = True
    else:
        TryAgain()


while quit is True:
    menu()
    TryAgain(quit)
