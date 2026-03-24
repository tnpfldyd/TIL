import sys
input = sys.stdin.readline

L = int(input())
s = input().strip()

MOD = 1234567891
r = 31

result = 0
power = 1

for ch in s:
    value = ord(ch) - ord('a') + 1
    result = (result + value * power) % MOD
    power = (power * r) % MOD

print(result)