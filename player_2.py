import random

def set_smart_number(score, p1, p2, p3):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    previous_number = [p1, p2, p3]
    previous_number = set(previous_number)

    for item in previous_number:
        numbers.remove(item)

    score += max(numbers)
    return score


def set_random_number(socre):

    random.seed(random.random())
    score += (random.randint(0, 8))
    return score

# -----------------------------------------


p1 = input().split(':')
p2 = input().split(':')
p3 = input().split(':')
player_2 = int(p2[2])  # moody Player

random.seed(random.random())
chance = random.randint(0, 3)
if chance == random.randint(0, 3):
    player_2 = random.randint(6, 8)
else:
    chance = random.randint(0, 1)

    if chance:
        player_2 = set_smart_number(
            player_2, int(p1[1]), int(p2[1]), int(p3[1]))
    else:
        player_2 = set_random_number(player_2)


print(player_2)
