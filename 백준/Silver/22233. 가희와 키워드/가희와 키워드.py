import sys
input = sys.stdin.readline

N, M = map(int, input().split())

memo = set()
for _ in range(N):
    memo.add(input().strip())

for _ in range(M):
    keywords = input().strip().split(',')
    for keyword in keywords:
        if keyword in memo:
            memo.remove(keyword)
    print(len(memo))