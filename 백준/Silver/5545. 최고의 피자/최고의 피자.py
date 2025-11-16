import sys
input = sys.stdin.readline

N = int(input())
A, B = map(int, input().split())
C = int(input())
t = [int(input()) for _ in range(N)]
t.sort(reverse=True)

total_cal = C
total_price = A
best = total_cal / total_price

for cal in t:
    if (total_cal + cal) / (total_price + B) >= best:
        total_cal += cal
        total_price += B
        best = total_cal / total_price
    else:
        break

print(int(best))