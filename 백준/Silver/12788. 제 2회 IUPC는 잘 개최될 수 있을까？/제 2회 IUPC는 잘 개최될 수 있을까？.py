N = int(input())
M, K = map(int, input().split())
A = list(map(int, input().split()))

need = M * K

A.sort(reverse=True)

total = 0
count = 0

for pens in A:
    total += pens
    count += 1
    if total >= need:
        print(count)
        break
else:
    print("STRESS")