from collections import deque
import sys
input = sys.stdin.readline

N = 500001
graph = [[] for _ in range(N)]
characters = ['']

def init():
    n = int(input().strip())
    characters.extend(input().strip())
    for _ in range(n - 1):
        u, v = map(int, input().strip().split())
        graph[u].append(v)
        graph[v].append(u)

def solve(initial_string):
    queue = deque([1])
    visited = [False] * N
    visited[1] = True
    result = initial_string

    while queue:
        next_queue = deque()
        max_char = ''
        
        for _ in range(len(queue)):
            current = queue.popleft()
            for neighbor in graph[current]:
                if not visited[neighbor] and characters[neighbor] >= max_char:
                    max_char = characters[neighbor]
                    visited[neighbor] = True
                    next_queue.append(neighbor)

        if max_char:
            result += max_char
            while next_queue:
                if characters[next_queue[0]] == max_char:
                    queue.append(next_queue.popleft())
                else:
                    next_queue.popleft()

    print(result)

if __name__ == "__main__":
    init()
    solve(characters[1])