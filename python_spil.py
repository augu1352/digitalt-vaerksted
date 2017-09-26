import random
alfabet = "abcdefghijklmnopqrstuvwxyz"

def RandomNumber():
    print("gaet et nummer mellem 1 og 100.")
    random_number = random.randint(1, 100)
    fundet = False
    gaet = 0
    while not fundet:
        bruger_gaet = input("Dit gaet: ")
        i = int(bruger_gaet)
        if i == random_number:
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





def RandomLetter():
    print("Gaet et bogstav mellem A og Z.")
    random_letter = random.choice(alfabet)
    fundet = False
    gaet = 0
    while not fundet:
        bruger_gaet = input("Dit gaet: ")
        i = (bruger_gaet)
        if i == random_letter:
            print("Rigtigt!")
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


quit = False

while quit == False:
    spil = "[TAL = 1] [BOGSTAV = 2]"
    print("Alle spil:")
    print(spil)
    valg = input("Vaelg et spil: ")
    if valg == "1" or valg == "4":
        RandomNumber()
    elif valg == "2" or valg == "3":
        RandomLetter()
    quit = input("Vil du proeve igen? ")
    if quit == "nej":
        quit = True
    else:
        quit = False
