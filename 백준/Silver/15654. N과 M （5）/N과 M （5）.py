import itertools, sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = sorted(map(int, input().split()))

for perm in itertools.permutations(numbers, M):
    print(*perm)