N = int(input())
P = list(map(int, input().split()))

P.sort()

total = 0
acc = 0
for time in P:
    acc += time
    total += acc

print(total)