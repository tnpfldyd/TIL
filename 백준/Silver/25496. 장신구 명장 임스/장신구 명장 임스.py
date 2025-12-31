P, N = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
limit = 200
cur = P
cnt = 0

for a in A:
    if cur >= limit:
        break
    
    cur += a
    cnt += 1

print(cnt)