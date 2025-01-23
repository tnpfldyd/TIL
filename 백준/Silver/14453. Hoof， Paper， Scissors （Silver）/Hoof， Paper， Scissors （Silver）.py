import sys
input = sys.stdin.readline

N = int(input().rstrip())
array = [0] + [input().rstrip() for _ in range(N)]

H, P, S = [0], [0], [0]

for i in range(1, N + 1):
    H.append(H[i - 1] + (array[i] == 'H'))
    P.append(P[i - 1] + (array[i] == 'P'))
    S.append(S[i - 1] + (array[i] == 'S'))

result = 0
for i in range(1, N + 1):
    result = max(
        result,
        P[i - 1] + (H[N] - H[i - 1]),
        P[i - 1] + (S[N] - S[i - 1]),
        H[i - 1] + (S[N] - S[i - 1]),
        H[i - 1] + (P[N] - P[i - 1]),
        S[i - 1] + (P[N] - P[i - 1]),
        S[i - 1] + (H[N] - H[i - 1])
    )

print(result)