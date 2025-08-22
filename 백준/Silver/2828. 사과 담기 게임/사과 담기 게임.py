import sys
input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())

left = 1
right = M
distance = 0

for _ in range(J):
    apple = int(input())
    
    if apple < left:
        move = left - apple
        distance += move
        left = apple
        right = apple + M - 1
    elif apple > right:
        move = apple - right
        distance += move
        right = apple
        left = apple - M + 1

print(distance)