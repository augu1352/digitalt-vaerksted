import random
import time
import sys


def Saenkeslagskibe():
    board = []
    for x in range(5):
        board.append(["O"] * 5)

    def print_board(board):
        for row in board:
            print(" ".join(row))

    print("Lad os spille Saenkeslagskibe!")
    print_board(board)

    def random_row(board):
        return random.randint(0, len(board) - 1)

    def random_col(board):
        return random.randint(0, len(board[0]) - 1)

    ship_col = random_col(board)
    ship_row = random_row(board)

    for turn in range(5):
        guess_col = int(input("Gaet Horisontal: "))
        guess_row = int(input("Gaet Vertikal: "))

        if guess_row == ship_row and guess_col == ship_col:
            print("\nTillykke! du har sunket mit slagskib!")
            print("ture: ", turn + 1)
            break
        else:
            if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
                print("\nOops, det var ikke engang i havet.")
            elif(board[guess_row][guess_col] == "X"):
                print("\nDen har du allerede gaettet før.")
            else:
                print("\nDu ramte ikke mit slagskib!")
                board[guess_row][guess_col] = "X"
        if turn == 4:
            time.sleep(1.5)
            print("\nGAME OVER!\n")
        print("ture: ", turn + 1, "\n")
        print_board(board)


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
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    print("Gaet et bogstav mellem A og Z.")
    random_letter = random.choice(alfabet)
    fundet = False
    gaet = 0
    while not fundet:
        i = input("Dit gaet: ")
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
    spil = ["[TAL-JAGT = 1]", "[BOGSTAV-JAGT = 2]", "[Saenkeslagskibe = 3]"]
    print("=" * 120)
    print("Alle spil:")
    print(" ".join(spil))
    valg = input("Vaelg et spil: ")
    print("")
    if valg == "1":
        RandomNumber()
    elif valg == "2":
        RandomLetter()
    elif valg == "3":
        Saenkeslagskibe()
    else:
        menu()


def UserQuit():
    user_quit = input("\nVil du spille et nyt spil? j/n ")
    if user_quit == "n":
        sys.exit()
    elif user_quit == "j":
        main()
    else:
        UserQuit()
    return quit


def main():
    menu()
    UserQuit()


if __name__ == "__main__":
    main()
