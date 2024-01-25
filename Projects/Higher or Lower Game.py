from game_data import data
import random

endgame = False

def random_value_a():
    figure = random.choice(data)
    return figure

def random_value_b():
    figure = random.choice(data)
    return figure


figure_one = random_value_a()
figure_second = random_value_b()

while endgame == False:



    guess = input(f"Guess who has more followers? {figure_one['name']} OR {figure_second['name']}: ").lower()

    if guess == 'a' and figure_one['follower_count'] > figure_second['follower_count']:
        print(f"{figure_one['name']} has {figure_one['follower_count']}mln followers, when {figure_second['name']} has {figure_second['follower_count']}mln followers")
        figure_second = random_value_b()

    elif guess == 'b' and figure_one['follower_count'] < figure_second['follower_count']:
        print(f"{figure_second['name']} has {figure_second['follower_count']}mln followers, when {figure_one['name']} has {figure_one['follower_count']}mln followers")
        figure_one = random_value_a()
    else:
        print("You are wrong...")
        print("Game Over!")
        endgame = True

