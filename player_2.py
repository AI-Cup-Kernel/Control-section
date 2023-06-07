import random


def set_smart_number(p1, p2, p3):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]  # all of the possible scores
    
    previous_number = [p1, p2, p3] # #numbers which chosen by players in the previous round
    previous_number = set(previous_number) # numbers which chosen by players in the previous round

    for item in previous_number:
        # remove previous numbers from list due to our algorithem
        numbers.remove(item)

    score = max(numbers)
    return score


def set_random_number():

    random.seed(random.random())
    score = (random.randint(1, 8))
    return score

# -----------------------------------------


p1 = input().split(':')
p2 = input().split(':')
p3 = input().split(':')
player_2 = 0  # moody Player

random.seed(random.random())
chance = random.randint(0, 3)

if chance == random.randint(0, 3):
# if chance which is a random number be equal with an other random number, player_2 will choose a number between 6-8
    player_2 = random.randint(6, 8)
else:
    chance = random.randint(0, 1) #Player 2 has a 50% chance of being either a normal player or a smart player

    if chance:
        player_2 = set_smart_number(
            int(p1[1]), int(p2[1]), int(p3[1]))
    else:
        player_2 = set_random_number()


print(player_2)
