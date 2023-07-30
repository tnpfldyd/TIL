N = int(input())
arr = list(map(int, input().split()))
prev = arr[0]
cnt = 1
cnts = []

for i in range(1, N):
    if arr[i] == prev:
        cnts.append(cnt)
        cnt = 1
    else:
        cnt += 1
        prev = arr[i]
cnts.append(cnt)

ans = 0
if len(cnts) == 1:
    ans = sum(cnts)
elif len(cnts) == 2:
    ans = sum(cnts)
else:
    for i in range(len(cnts)-2):
        ans = max(ans, cnts[i] + cnts[i+1] + cnts[i+2])

print(ans)
