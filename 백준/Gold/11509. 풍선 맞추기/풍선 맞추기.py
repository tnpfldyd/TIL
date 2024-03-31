N = int(input())
arr = list(map(int, input().split()))
result = 0
arrow = [0] * 1000001

for x in arr:
    if arrow[x]:
        arrow[x] -= 1
        arrow[x - 1] += 1
    else:
        arrow[x - 1] += 1
        result += 1

print(result)