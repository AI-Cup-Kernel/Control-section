scores = [0, 0, 0]   #all scores in a row
while(scores[0] < 101 and scores[1] < 101 and scores[2] < 101):
    x = int(input())  #score player1
    y = int(input())   #score player2
    z = int(input())   #score player3
    if(x > 8 or x < 1):   #invalid input
        x = 0
    if(y > 8 or y < 1):
        y = 0
    if(z > 8 or z < 1):
        z = 0
    if(x != y and y != z and x != z):   #if all three were different
        scores[0] += 2 * x
        scores[1] += 2 * y
        scores[2] += 2 * z
    else:
        if(x == y and y != z):   #if just x and y were the same
            scores[0] += int(x / 2)
            scores[1] += int(y / 2)
            scores[2] += 2 * z
        else:
            if(x == z and z != y):  #if just x and z were the same
                scores[0] += int(x / 2)
                scores[2] += int(z / 2)
                scores[1] += 2 * y
            else:
                if(y == z and z != x):  #if just y and z were the same
                    scores[1] += int(y / 2) 
                    scores[2] += int(z / 2)
                    scores[0] += 2 * x 
                else:    #if all of them were the same
                    scores[0] += int(x / 3)
                    scores[1] += int(y / 3)
                    scores[2] += int(z / 3)
    print(f"p1-{x}:{scores[0]}\np2-{y}:{scores[1]}\np3-{z}:{scores[2]}")
