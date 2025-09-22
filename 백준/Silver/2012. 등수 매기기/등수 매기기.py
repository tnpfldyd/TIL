import sys
input = sys.stdin.readline

n = int(input())
expected = [int(input()) for _ in range(n)]

expected.sort()

result = sum(abs(expected[i] - (i + 1)) for i in range(n))

print(result)