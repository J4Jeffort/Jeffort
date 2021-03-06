import random



def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, cpu_score):
    # Bug fix. If you and the computer are both over, you lose.
    if user_score > 21 and cpu_score > 21:
        return "You went over. You lose 😤"

    if user_score == cpu_score:
        return "Draw 🙃"
    elif cpu_score == 0:
        return "You lost, opponent has Blackjack 😱"
    elif user_score == 0:
        return "You win with a Blackjack! 😎"
    elif user_score > 21:
        return "You bustedy. You lose 😭"
    elif cpu_score > 21:
        return "Opponent busted. You win 😁"
    elif user_score > cpu_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    

    user_cards = []
    cpu_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        cpu_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        cpu_score = calculate_score(cpu_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {cpu_cards[0]}")

        if user_score == 0 or cpu_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while cpu_score != 0 and cpu_score < 17:
        cpu_cards.append(deal_card())
        cpu_score = calculate_score(cpu_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {cpu_cards}, final score: {cpu_score}")
    print(compare(user_score, cpu_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
