def set_smart_number(score, p1, p2, p3):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    previous_number = [p1, p2, p3]
    previous_number = set(previous_number)

    for item in previous_number:
        numbers.remove(item)

    score += max(numbers)
    return score


p1 = input().split(':')
p2 = input().split(':')
p3 = input().split(':')

player_3 = int(p3[2])  # smart Player

player_3 = set_smart_number(player_3, int(p1[1]), int(p2[1]), int(p3[1]))
print(player_3)
