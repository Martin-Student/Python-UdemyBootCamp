import random

word_list = ["cat", "dog", "penguin"]

chosen_word = random.choice(word_list)

display = []
for i in range(len(chosen_word)):
    display += "_"

pkt = 6
end_game = False
while not end_game:
    guess = input("Podaj literę: ").lower()
    if chosen_word == guess:
        display = guess


    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if "_" not in display:
        print("Wygrałeś!")
        end_game = True

    if guess not in chosen_word:
        pkt -= 1
        print(pkt)
        if pkt == 0:
            print("Przegrałeś!")
            end_game = True

    print(display)