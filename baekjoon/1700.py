import sys
input = sys.stdin.readline

N, K = map(int, input().split())
order = list(map(int, input().split()))
con = set()
ans = 0
for i in range(K):
    if order[i] in con:
        continue
    elif len(con) < N:
        con.add(order[i])
    else:
        res, num = -1, -1
        check = list(con.copy())
        for j in range(N):
            cnt = 0
            for k in range(i + 1, K):
                if check[j] == order[k]:
                    break
                cnt += 1
            if res < cnt:
                res = cnt
                num = check[j]
        con.remove(num); con.add(order[i])
        ans += 1

print(ans)