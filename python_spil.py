import random
import time
alfabet = "abcdefghijklmnopqrstuvwxyz"
quit = False

def RandomNumber():
    print("Gaet et nummer mellem 1 og 100.")
    random_number = random.randint(1, 100)
    fundet = False
    gaet = 0
    while not fundet:
        bruger_gaet = input("Dit gaet: ")
        i = int(bruger_gaet)
        if i == random_number:
            print("")
            print("Rigtigt!")
            fundet = True
            gaet += 1
            print("antal gaet: " + str(gaet))
        elif i < random_number:
            print("Hoejere...")
            gaet += 1
        else:
            print("Lavere...")
            gaet += 1
    print("Tak for at spille")
    print("")


def RandomLetter():
    print("Gaet et bogstav mellem A og Z.")
    random_letter = random.choice(alfabet)
    fundet = False
    gaet = 0
    while not fundet:
        bruger_gaet = input("Dit gaet: ")
        i = (bruger_gaet)
        if i == random_letter:
            print("")
            print("Rigtigt!")
            print("")
            fundet = True
            gaet += 1
            print("antal gaet: " + str(gaet))
        elif alfabet.index(random_letter) < alfabet.index(i):
            print("Laengere tilbage...")
            gaet += 1
        else:
            print("Laengere frem...")
            gaet += 1
    print("Tak for at spille")
    print("")





while quit == False:
    spil = ["[TAL-JAGT = 1]", "[BOGSTAV-JAGT = 2]"]
    print("Alle spil:")
    print(" ".join(spil))
    valg = input("Vaelg et spil: ")
    print("")
    if valg == "1":
        RandomNumber()
    elif valg == "2":
        RandomLetter()


    quit = input("Vil du spille et nyt spil? j/n ")
    if quit == "n":
        quit = True
    elif quit == "j":
        quit = False
