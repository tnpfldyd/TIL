import sys
import math

input = sys.stdin.readline

n = int(input().strip())
fact = str(math.factorial(n))

count = 0
for digit in reversed(fact):
    if digit == '0':
        count += 1
    else:
        break
print(count)