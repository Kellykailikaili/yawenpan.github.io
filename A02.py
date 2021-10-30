import random
def roll():
    pause = input("Press <Enter> to roll the dices!")
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    total = die1 + die2
    print("You rolled %d + %d = %d" % (die1, die2, total))
    return total

def usr_input():
    response= input("Do you want to roll the dices? (ROLL/QUIT)")
    while response not in ("ROLL","roll","QUIT","quit"):
        print("Wrong user input! 1 attempt left!")
        response = input("Do you want to roll the dices? (ROLL/QUIT)")
        break
    return response

def main():
    #initate the game from user input
    counter = 0
    response = usr_input()
       
    while response == 'ROLL' or response == 'roll':
        firstroll = roll()
        counter = counter + 1
        if firstroll == 7 or firstroll == 11:
            print("You won! :)")
            print("Total rounds played : %d" % counter)
            return 0
        elif firstroll == 2 or firstroll == 3 or firstroll ==12:
            print("You Lost! :(")
            print("Total rounds played : %d" % counter)
            return 0
        else:
            print("Total rounds played : %d" % counter)
            response = usr_input()

            while response == 'ROLL' or response == 'roll':
                newroll= roll()
                counter = counter + 1
                if newroll == 7 or newroll ==11:
                    print("You won! :)")
                    print("Total rounds played : %d" % counter)
                    return 0
                elif newroll == 2 or newroll == 3 or newroll ==12:
                    print("You lost! :(")
                    print("Total rounds played : %d" % counter)
                    return 0
                else:
                    print("Total rounds played : %d" % counter)
                    break
    print("See you!")







if __name__ == "__main__":
    main()
        