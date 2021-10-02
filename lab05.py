########################################################################
##
## CS 101 Lab
## Program #3
## Name: Tyler Faust
## Email: tefqhg@umsystem.edu
##
## PROBLEM : Describe the problem
##      fill all functions to make the game playable
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

import random


def play_again() -> bool:
    while playing:
        play = input("Do you want to play again? ==> ").lower()
        if play == "yes" or play == "y":
            return True
        elif play == "no" or play == "n":
            return False
        else: 
            print("You must enter Y/YES/N/NO to continue. Please try again.")
     
def get_wager(bank : int) -> int:
    while playing: 
        wag = int(input("How many chips would you like to wager? ==> ")) 
        if wag <= 0 or wag > bank:
            print("Please enter a number above 0 and below your bank.")
        else:
            return wag

def get_slot_results() -> tuple:
    return random.randint(1,10), random.randint(1,10), random.randint(1,10)

def get_matches(reela, reelb, reelc) -> int:
    if reela == reelb and reelb == reelc:
        return 3
    elif (reela == reelb) or (reela == reelc) or (reelb == reelc):
        return 2
    else:
        return 0

def get_bank() -> int:
    while playing:
        ban = int(input("How many chips do you wish to start with? ==> "))
        if ban <= 0 or ban > 100:
            print("Please input a number between 1 and 100.")
        else: 
            return ban

def get_payout(wager, matches):
    if matches == 3:
        return wager * 10
    elif matches == 2:
        return wager * 3
    else:
        return wager * -1     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        initialBank = bank
        spins = 0
        max = bank

        while bank > 0:
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()
            spins += 1

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            if bank > max:
                max = bank

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
        print("You lost all", initialBank, "in", spins, "spins")
        print("The most chips you had was", max)
        playing = play_again()