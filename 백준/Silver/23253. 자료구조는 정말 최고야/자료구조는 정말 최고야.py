import sys
input = sys.stdin.readline

N, M = map(int, input().split())

for _ in range(M):
    k = int(input())
    books = list(map(int, input().split()))
    for i in range(k - 1):
        if books[i] < books[i + 1]:
            print("No")
            sys.exit()

print("Yes")