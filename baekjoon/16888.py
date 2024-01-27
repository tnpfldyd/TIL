import sys, math
input = sys.stdin.readline
answer = [False] * 1000001

for i in range(1, int(math.sqrt(1000000)) + 1):
        answer[i * i] = True

for i in range(2, 1000001):
        if not answer[i]:
            j = 1
            while j * j + i <= 1000000:
                answer[i + j * j] = True
                j += 1

T = int(input())
result = []

for _ in range(T):
    N = int(input())
    result.append("koosaga" if answer[N] else "cubelover")

print('\n'.join(result))