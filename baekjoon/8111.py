from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    number = int(input())
    visited = [''] * 20001
    start = deque()
    start.append(1)
    visited[1] = '1'
    answer = False
    while start and not answer:
        x = start.popleft()
        if len(visited[x]) == 100:
            print('BRAK')
            break
        for i in (0, 1):
            next_number = (x * 10 + i) % number
            if next_number:
                if visited[next_number] == '':
                    visited[next_number] = visited[x] + str(i)
                    start.append(next_number)
            else:
                print(visited[x]+str(i))
                answer = True
                break
    