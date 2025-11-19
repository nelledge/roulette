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
            betting_number = input("Do you want to bet on 1, 2, 4 or 6 nubers?: ")
            if betting_number == 1:
                 print("Numers 0 - 36")
                 second_wave = input("--> ")
            if betting_number == 2:
                 print("")
            if betting_number == 3:
                 print("")
            if betting_number == 4:
                 print("")
            if betting_number == 6:
                 print("")

        elif bet == "2": #Outsise Betts
            in_out_false = 2

            print("1 --> Red")
            print("2 --> Black")
            print("3 --> Odd")
            print("4 --> Even")
            print("5 --> Low")
            print("6 --> High")
            print("7 --> 1. Dozens(1-12)")
            print("8 --> 2. Dozens(13 - 24)")
            print("9 --> 3. Dozens(25 - 36)")
            print("10 --> 1. Column")
            print("11 --> 2. Column")
            print("12 --> 3. Column")
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

        if in_out_false == "3":
             betting = False

        print(f"Your Nuber --> {in_out_false}")

        


    print(random_number)
        
