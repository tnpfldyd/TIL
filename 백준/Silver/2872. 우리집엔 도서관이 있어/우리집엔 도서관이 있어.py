import sys
input = sys.stdin.readline

n = int(input())
books = [int(input()) for _ in range(n)]

for i in range(n - 1, -1, -1):
    if books[i] == n:
        n -= 1
        
print(n)