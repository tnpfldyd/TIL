N = int(input())
W = list(map(int, input().split()))

ans = 0

def dfs(energy, balls):
    global ans
    if len(balls) == 2:
        ans = max(ans, energy)
        return

    for i in range(1, len(balls) - 1):
        gain = balls[i - 1] * balls[i + 1]
        removed = balls[i]
        balls.pop(i)
        dfs(energy + gain, balls)
        balls.insert(i, removed)

dfs(0, W)
print(ans)