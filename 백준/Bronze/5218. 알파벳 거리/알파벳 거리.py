import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    origin, distance = input().strip().split()
    N = len(origin)
    answer = []
    for i in range(N):
        temp = ord(distance[i]) - ord(origin[i])
        if temp < 0:
            temp += 26
        answer.append(temp)
    print('Distances: ', end='')
    print(*answer)