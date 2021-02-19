import random

def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    while True:
        pa = input("Do you want to play again? ==> ")
        if pa == 'y' or pa == 'Y' or pa == 'yes' or pa == 'YES':
            return True
            break
        elif pa == 'n' or pa == 'N' or pa == 'no' or pa == 'NO':
            return False
            break
        else:
            print("You must enter Y/YES/N/NO to continue. Please try again")
            pass
        
        
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    while True:
        b = int(input("How many chips do you want to wager? ==> "))
        if b <= 0:
            print("Too low a value, you can only choose 1 -", bank, "chips")
        elif b > bank:
            print("Too high a value, you can only choose 1 -", bank, "chips")
        elif b > 0 and b <= bank:
            break            
    return b

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    r1 = random.randint(1, 10)
    r2 = random.randint(1, 10)
    r3 = random.randint(1, 10)
    return r1, r2, r3

def get_matches(ra, rb, rc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if ra == rb and ra == rc:
        return 3
    elif ra == rb or ra == rc or rb == rc:
        return 2
    else:
        return 0

def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    while True:
        bn = int(input("How many chips do you want to start with? ==>"))
        if bn <= 0:
            print("Too low a value, you can only choose 1 - 100 chips")
        elif bn > 100:
            print("Too high a value, you can only choose 1 - 100 chips")
        elif bn > 0 and bn <= 100:
            return bn
            break

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 5 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        pay1 = (10 * wager) - wager
    elif matches == 2:
        pay1 = (3 * wager) - wager
    elif matches == 0:
        pay1 = - wager
    return pay1    


if __name__ == "__main__":

    playing = True
    wager = 0
    while playing:

        bank = get_bank()


        while bank >= wager:
            wager = get_wager(bank)
            reel1, reel2, reel3 = get_slot_results()
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
           
        print("You lost all", 0, "in", 0, "spins")
        print("The most chips you had was", 0)
        playing = play_again()
