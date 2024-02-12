import sys
input = sys.stdin.readline

N, T = map(int, input().split())
carrot = sorted([tuple(map(int, input().split())) for _ in range(N)], key = lambda x : (x[1], x[0]))
answer = sum(w + p * (i + T - N) for i, (w, p) in enumerate(carrot))

print(answer)
