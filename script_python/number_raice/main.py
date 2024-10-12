'''
script description Number race
dev:Fernando  Vi
date: 13/09/2024
'''
from random import randint 
status_game=True


def main_menu():
    print("::MAIN MENU::")    
    print("[1]. Start the game")
    print("[2]. About us")
    print("[3]. Exit")
    opt =int(input("Press any option: "))
    
   

    

while status_game:
    main_menu() 
    op = main_menu() 
    if op == 1:
        print ("Game under construction")
        key = ("Press any key to go to the main menu...")
          
       
       
# Generate two random numbers between 1 and 6
        
dice1 = randint(1,6)
dice2 = randint(1,6)


print (f"Dice1: {dice1} ")
print (f"Dice2: {dice2} ")