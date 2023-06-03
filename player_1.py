import random

def set_random_number(score):

    random.seed(random.random())
    score += (random.randint(0, 8))
    return score

p1 = input().split(':')
p2 = input().split(':')
p3 = input().split(':')
player_1 = int(p1[2])  # Normal player

player_1 = set_random_number(player_1)
print(player_1)
