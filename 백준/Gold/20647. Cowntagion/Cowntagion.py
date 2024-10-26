import sys, math
from collections import defaultdict
input = sys.stdin.readline

answer = 0
graph = defaultdict(list)

def dfs(here, prv):
    global answer
    cnt = 0
    for there in graph[here]:
        if there != prv:
            cnt += 1
            dfs(there, here)
    answer += cnt
    answer += math.ceil(math.log2(cnt + 1))

def main():
    N = int(input())
    
    for _ in range(N - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)
    
    dfs(0, -1)
    print(answer)

if __name__ == "__main__":
    main()
