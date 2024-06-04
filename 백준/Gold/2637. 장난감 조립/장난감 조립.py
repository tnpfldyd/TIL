from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def main():
    N, M = int(input()), int(input())
    graph = defaultdict(list)
    in_degree = [0] * (N + 1)
    count = [0] * (N + 1)

    for _ in range(M):
        x, y, k = map(int, input().split())
        graph[x].append((y, k))
        in_degree[y] += 1

    q = deque([N])
    count[N] = 1
    answer = []

    while q:
        cur = q.popleft()
        if not graph[cur]:
            answer.append(cur)
        for nxt, c in graph[cur]:
            count[nxt] += count[cur] * c
            in_degree[nxt] -= 1
            if not in_degree[nxt]:
                q.append(nxt)

    answer.sort()
    for node in answer:
        print(node, count[node])

if __name__ == "__main__":
    main()
