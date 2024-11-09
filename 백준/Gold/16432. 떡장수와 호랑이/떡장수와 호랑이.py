import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

rice_cakes_per_day = [[] for _ in range(N)]
for k in range(N):
    rice_cake = input().split()[1:]
    rice_cakes_per_day[k] = rice_cake

def dfs(day, history):
    if day == N:
        print('\n'.join(history.split()))
        exit(0)

    for cake in rice_cakes_per_day[day]:
        if day == 0:
            visited[day + 1][int(cake)] = True
            dfs(day + 1, history + cake + ' ')
        elif cake != history[-2] and not visited[day + 1][int(cake)]:
            visited[day + 1][int(cake)] = True
            dfs(day + 1, history + cake + ' ')

visited = [[False] * 10 for _ in range(N + 1)]
dfs(0, '')
print(-1)