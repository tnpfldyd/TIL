import sys
input = sys.stdin.readline

N = int(input())
tips = [int(input()) for _ in range(N)]

tips.sort(reverse=True)

total_tip = 0
for i in range(N):
    tip_amount = tips[i] - i
    if tip_amount > 0:
        total_tip += tip_amount

print(total_tip)