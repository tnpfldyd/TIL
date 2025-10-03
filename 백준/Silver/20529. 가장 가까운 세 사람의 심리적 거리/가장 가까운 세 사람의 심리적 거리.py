import sys
from itertools import combinations
input = sys.stdin.readline

def distance(mbti1, mbti2):
    return sum(c1 != c2 for c1, c2 in zip(mbti1, mbti2))

T = int(input())
for _ in range(T):
    N = int(input())
    mbti_list = input().split()
    
    if N > 32:
        print(0)
        continue
    
    min_dist = float('inf')
    for combo in combinations(mbti_list, 3):
        total_dist = distance(combo[0], combo[1]) + distance(combo[1], combo[2]) + distance(combo[0], combo[2])
        min_dist = min(min_dist, total_dist)
    
    print(min_dist)