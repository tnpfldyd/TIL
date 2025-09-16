import sys
input = sys.stdin.readline

S = input().strip()
q = int(input())

prefix = [[0] * 26 for _ in range(len(S) + 1)]

for i in range(len(S)):
    for j in range(26):
        prefix[i + 1][j] = prefix[i][j]
    prefix[i + 1][ord(S[i]) - ord('a')] += 1

for _ in range(q):
    alpha, l, r = input().split()
    l, r = int(l), int(r)
    alpha_idx = ord(alpha) - ord('a')
    count = prefix[r + 1][alpha_idx] - prefix[l][alpha_idx]
    print(count)