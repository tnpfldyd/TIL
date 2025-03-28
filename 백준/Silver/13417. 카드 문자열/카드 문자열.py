from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    cards = input().strip().split()
    
    result = deque([cards[0]])
    for i in range(1, N):
        left = cards[i] + ''.join(result)
        right = ''.join(result) + cards[i]
        if left <= right:
            result.appendleft(cards[i])
        else:
            result.append(cards[i])
    
    print(''.join(result))