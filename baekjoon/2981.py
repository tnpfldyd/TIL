import sys
input = sys.stdin.readline
T = int(input())
result = [(int(input())) for _ in range(T)]

number_ = set()
num = set()
for j in range(2, min(result)+1):
    if len(number_) == 1:
        num.add(j-1)
    number_.clear()
    for i in result:
        i %= j
        number_.add(i)
print(*num)