'''
script description Number race
dev:Fernando  Vi
date: 13/09/2024
'''
from random import randint 
import os


status_game=True


def main_menu():
    global status_opts
    status_opt=True
    print("::MAIN MENU::")    
    print("[1]. Start the game")
    print("[2]. About us")
    print("[3]. Exit")
    
    while status_opt:
        opt =int(input("Press any option: "))
        if opt < 1 or opt > 3:
            print("ERROR. Press any option between 1 and 3")
        else:
            status_opts=False
    return opt
        

while status_game:
    os.system('clear')
    op = main_menu() 
    if op == 1:
        os.system('clear')
        print ("::: WELCOME TO NUMBER RACE :::")
        players = int(input("Press number of player[1:4] "))   
        key = input("Press any key to go to the main menu...")
    elif op == 2:
        print ("Help under construction")
        key = input("Press any key to go to the main menu...")    
    else:
        print ("See 'u later")
        key = input("Press any key to exit")    
        break
        
          
       
       
# Generate two random numbers between 1 and 6
dice1 = randint(1,6)
dice2 = randint(1,6)


print (f"Dice1: {dice1} ")
print (f"Dice2: {dice2} ")