from game_data import data
import random


#a_key = 'name'
#b_key = 'follower_count'
#list_of_names = [a_dict[a_key] for a_dict in data]
#list_of_followers = [a_dict[b_key] for a_dict in data]

endgame = False

def losownik_a():
    ac = random.choice(data)
    return ac

def losownik_b():
    ba = random.choice(data)
    return ba





while endgame == False:

    ac = losownik_a()
    ba = losownik_b()

    wpis = input(f"Kto ma więcej? {ac['name']} czy {ba['name']} ")

    if wpis == 'a' and ac['follower_count'] > ba['follower_count']:
        print(f"{ac['name']} ma więcej, ponieważ ma {ac['follower_count']}mln followersów, a {ba['name']} ma {ba['follower_count']}mln followersów")

    elif wpis == 'b' and ac['follower_count'] < ba['follower_count']:
        print(f"{ba['name']} ma więcej, ponieważ ma {ba['follower_count']}mln followersów, a {ac['name']} ma {ac['follower_count']}mln followersów")
    else:
        print("Błąd!")
        endgame = True

