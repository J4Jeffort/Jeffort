from art import logo, vs
from game_data import data
import random
from os import system, name
from time import sleep


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def game_start():
    print(logo)
    print("Welcome to higher/lower! \n")
    sleep(2)
    print("game starts in\n")
    sleep(1)
    print("3\n")
    sleep(1)
    print("2\n")
    sleep(1)
    print("1\n")
    sleep(1)
    print("Good luck!")
    sleep(2)
    clear()


game_start()

print(logo)


def format_data(selection):
    """format data into printable format."""
    account_name = selection["name"]
    account_description = selection["description"]
    account_country = selection["country"]
    return f"{account_name}, a {account_description}, from {account_country} "


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


score = 0
continue_game = True
selection_b = random.choice(data)

while continue_game:
    selection_a = selection_b
    selection_b = random.choice(data)

    while selection_a == selection_b:
        selection_b = random.choice(data)

    print(f"Compare A: {format_data(selection_a)}.")
    print(vs)
    print(f"Against B: {format_data(selection_b)}.")

    guess = input("Who has more followers? 'A' or 'B': \n").lower()

    a_follower_count = selection_a["follower_count"]
    b_follower_count = selection_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    clear()
    print(logo)
    if is_correct:
        score += 1
        print(f"Correct! Your current score is {score}. ")

    else:
        continue_game = False
        print(f"You were wrong. Game over. Final score was {score} ")
