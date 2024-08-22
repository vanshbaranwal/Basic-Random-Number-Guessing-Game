#1. Number Guessing Game

import random

def play_game():
    
    print("\nWelcome user!!\n")
    print('''    This is a number guessing game where you will be guessing a number
    between start_range to end_range and a number will be guessed by the computer if the number guessed by you and the 
    computer is same then you won otherwise you loose and you will get total 3 attempts to make a
    correct guess.\n    ''')
    
    attempts=0
    total_attempts=3

    start_range=int(input("enter starting range : "))
    end_range=int(input("enter ending range : "))

    if(start_range>=end_range):
        print("invalid range! starting range should be less than the ending range.")
        return
    else:
        random_num=random.randint(start_range,end_range)

    while attempts < total_attempts:
    
        attempts+=1

        user_num=int(input(f"enter a number between ('{start_range}-{end_range}') : "))

        if(random_num==user_num):
            print("you guessed it correct!")
            if(attempts==1):
                print(f"you got the correct guess in {attempts} attempt.")
            else:
                print(f"you got the correct guess in {attempts} attempts.")
            break

        elif(user_num<start_range or user_num>end_range):
            print(f"invalid number guess within ('{start_range}-{end_range}').")
        elif(random_num<user_num):
            print("the guess is high.")
        elif(random_num>user_num):
            print("the guess is low.")

    if(attempts==total_attempts):
        print(f"Oops!! you ran out of your 3 attempts.")
        print(f"you were not able to make a correct guess in {attempts} attempts.")
    else:
        print("")  

        
while True:
    play_game()
    user_choice=input("Do you want to play the game again('yes or no') : ")
    if(user_choice.lower()=='no'):
        break
    elif(user_choice.lower()=="yes"):
        print("You have choosen to play the game again!")
        print("All The Best")
    else:
        print("Invalid choice.\nchoose between 'yes or no' specifically.")
        
print("\nThank you for playing!")
