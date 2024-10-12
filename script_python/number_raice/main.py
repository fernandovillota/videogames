'''
script description Number race
dev:Fernando  Vi
date: 13/09/2024
'''
from random import randint 
dice1 = randint(1,6)
dice2 = randint(1,6)

def main_menu():
    print("::MAIN MENU::")
    
    print("[1]. Start the game")
    print("[2]. About us")
    print("[3]. Exit")
    opt =int(input("Press any option: "))
    


print (f"Dice1: {dice1} ")
print (f"Dice2: {dice2} ")