G = int(input())
left = right = 1
answer = []
while True:
    temp = right ** 2 - left ** 2
    if temp == G: answer.append(right)

    if right - left == 1 and temp > G: break

    if temp > G: left += 1
    else: right += 1

[print(i) for i in answer] if answer else print(-1)