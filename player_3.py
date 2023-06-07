def set_smart_number(p1, p2, p3):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8] #all of the possible scores
    previous_number = [p1, p2, p3] #numbers which chosen by players in the previous round
    previous_number = set(previous_number) #convert list to set for removing duplicated number

    for item in previous_number:
        numbers.remove(item)    #remove previous numbers from list due to our algorithem

    score = max(numbers)
    return score


p1 = input().split(':')
p2 = input().split(':')
p3 = input().split(':')

player_3 = 0 # smart Player

player_3 = set_smart_number(int(p1[1]), int(p2[1]), int(p3[1]))
print(player_3)
