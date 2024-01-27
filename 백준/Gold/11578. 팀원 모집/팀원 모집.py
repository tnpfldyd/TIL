from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

items = [0] * M
answer = (1 << N) - 1

for i in range(M):
    _, *numbers = list(map(int, input().split()))
    for number in numbers:
        items[i] |= (1 << number - 1)

def solve():
    for i in range(1, M + 1):
        combies = combinations(items, i)
        for comb in combies:
            temp = 0
            for number in comb:
                temp |= number
                if answer == temp:
                    return i
    return -1 
                
print(solve())