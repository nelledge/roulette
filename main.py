import random
import time

def getting_what_you_want_to_bet():
        print ("What would you like to bet on?")
        print("1 --> INSIDE BETSS")
        print("2 --> OUTSIDE BETS")
        print("3 --> Im done")
        print("")
        bet = input("What do you want to bet on: ")
        print("")

        if bet == "1": #Inside Betts
            in_out_false = 1

        elif bet == "2": #Outsise Betts
            in_out_false = 2
            print("1 --> Red or Black")
            print("2 --> Odd or Even")
            print("3 --> Low or High")
            print("4 --> Dozens")
            print("5 --> Columns")
            print("")
            second_wave = input("What do you want to bet on: ")

        elif bet == "3":
            in_out_false = 3
            # betting = False
            # balnce = 0

        else:
            print("Wrong input, only 1, 2 or 3")

        return in_out_false, second_wave


balnce = 1000

while balnce > 0:

    betting = True
    while betting == True:
        random_number = random.randint(0, 36)

        in_out_false, second_wave = getting_what_you_want_to_bet()

        print(f"Your Nuber --> {in_out_false}")

        


    print(random_number)
        
