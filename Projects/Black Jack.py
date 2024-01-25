import random
from replit import clear

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) ==2:
        return 21
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw!"
    elif user_score == 21:
        return "You win!"
    elif computer_score == 21:
        return "Opponent win!"
    elif computer_score == 0:
        return "Lose! Opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over 21. You lose"
    elif computer_score > 21:
        return "Opponent went over 21. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_cards = []
    computer_cards = []
    endgame = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not endgame:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer cards: {computer_cards}, current score: {computer_score}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            endgame = True
        else:
            user_choice = input("Type 'y' to get another card or type 'n' to pass: ")
            if user_choice == "y":
                user_cards.append(deal_card())
            else:
                endgame = True

        if computer_score != 0 or computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

    print(f" Your final hand: {user_cards}, with final score: {user_score}")
    print(f" Computer final hand: {computer_cards}, with final score: {computer_score}")

    print(compare(user_score, computer_score))

while input("Do you want to play BlackJack? Type 'y' for YES or 'n' for NO") == "y":
    clear()
    play_game()
