import random


def set_random_number():  # choose a random number between 1-8

    random.seed(random.random())
    score = (random.randint(1, 8))
    return score


p1 = input().split(':')
p2 = input().split(':')
p3 = input().split(':')
player_1 = 0  # Normal player

player_1 = set_random_number()
print(player_1)
