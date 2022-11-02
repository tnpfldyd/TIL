numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
key = {1: [0,0], 2: [0,1], 3: [0, 2], 4: [1,0], 5: [1,1], 6: [1,2], 7: [2,0], 8: [2,1], 9: [2,2], 10: [3,0], 11: [3,1], 12: [3,2]}
L, R = [1,4,7], [3,6,9]
curL = 10
curR = 12
answer = ''
for i in numbers:
    if i in L:
        curL = i
        answer += 'L'
    elif i in R:
        curR = i
        answer += 'R'
    else:
        Lcost = abs(key[curL][0] - key[i][0]) + abs(key[curL][1] - key[i][1])
        Rcost = abs(key[curR][0] - key[i][0]) + abs(key[curR][1] - key[i][1])
        if Lcost > Rcost:
            curR = i
            answer += 'R'
        elif Lcost < Rcost:
            curL = i
            answer += 'L'
        else:
            if hand == 'right':
                curR = i
                answer += 'R'
            else:
                curL = i
                answer += 'L'
print(answer)