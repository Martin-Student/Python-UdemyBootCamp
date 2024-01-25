import random

numbers = []
endgame = False

for i in range(1, 101):
    numbers.append(i)

mystery = random.choice(numbers)
print(mystery)



pkt = 0
level = input("How hard the game should be? Type: EASY/HARD ").lower()
if level == "hard":
    pkt = 5
else:
    pkt = 10

while endgame == False:


    guess = int(input("Guess a number from 1 to 100: "))

    if guess == mystery:
        print("Win!")
        endgame = True
    else:
        print("Wrong!")
        pkt -= 1
        if guess > mystery:
            print(f"You still have {pkt} bets! But your type is too high!")
        elif guess < mystery:
            print(f"You still have {pkt} bets! But your type is too low!")
        if pkt == 0:
            print("Game Over!")
            endgame = True