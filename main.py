


import random
import os
import time
from sys import platform


def clear_screen() -> None:
    if platform == 'win32':
        os.system("cls")
    os.system("clear")


def header(title:str,delay:float) -> None:
    print("=" * 40)
    print(title)
    print("=" * 40)
    time.sleep(delay)
    clear_screen()

def pop(title:str) -> None:
    print("=" * 40)
    print(title)
    print("=" * 40)

def get_pop(title:str) -> str:
    print("=" * 40)
    temp = input(title)
    print("=" * 40)
    time.sleep(1.5)
    clear_screen()
    return temp

answer = 'y'
while answer != 'n':
    colors = "RGBY"
    simon = ""
    
    header(
            title = "Game Rule: Guess a colors sequence",
            delay = 3.0
        )


    for count in range(1,4):
        header(title = f"Get Ready! in {count}",delay = 1.5)
    
    header(title = "Let's Go!",delay = 1.5)

    for score in range(0,5):
        simon += random.choice(colors)
        for color in colors:
            header(title = f'Color: {color}',delay = 1.5)
        guess = get_pop("Enter a Guess: ")
        guess = guess.upper()
        time.sleep(1)
        clear_screen()
        if guess != simon:
            break
        header(title = "Next Round")
        time.sleep(1)
        clear_screen("clear")
        
    header(
           title = f'Game Over! Your Final Score Is {score}',
           delay = 1.5
         )
    answer = get_pop("Play Again? Yes[y] or No[n]: ")

pop("Thank you for playing the game :) \nAuthor: John Jayson B De Leon\nGithub: savjaylade84\nEmail: savjaylade84@gmail.com")
