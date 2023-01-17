
string = input()
bomb = list(input())
answer = []
for i in string:
    answer.append(i)
    if answer[-len(bomb):] == bomb:
        for j in range(len(bomb)):
            answer.pop()
print(''.join(answer) if answer else 'FRULA')
