import itertools
marbles = [3,9,7,5]
result = 0
answer = []
for i in range(len(marbles), 0, -1):
    for j in itertools.permutations(marbles, i):
        if len(j) % 2 == 0:
            if sum(j[0:len(j)//2]) == sum(j[len(j)//2:len(j)]):
                if sum(j) > result:
                    result = sum(j)
                    answer = [j]
                if sum(j) == result:
                    answer.append(j)
        else:
            if sum(j[0:len(j)//2]) == sum(j[len(j)//2+1:len(j)]):
                if sum(j) > result:
                    result = sum(j)
                    answer = [j]
                if sum(j) == result:
                    answer.append(j)
answer.sort()
print(answer)