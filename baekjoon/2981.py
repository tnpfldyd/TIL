import sys
input = sys.stdin.readline
def GCD(a, b):
    while b != 0:
        temp = a
        a = b
        b = a % b
    return a
T = int(input())
result = [(int(input())) for _ in range(T)]
start = GCD(min(result), max(result))
number_ = set()
num = set()
for j in range(2, start):
    if len(number_) == 1:
        num.add(j-1)
    number_.clear()
    for i in result:
        i %= j
        number_.add(i)
print(*num)