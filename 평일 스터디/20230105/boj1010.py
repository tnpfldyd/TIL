import sys, math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    print(math.factorial(b) // (math.factorial(a) * math.factorial(b-a)))