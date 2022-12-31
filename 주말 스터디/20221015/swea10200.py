T = int(input())
for i in range(1, T+1):
    a, b, c = map(int, input().split())
    ans1 = min(b, c)
    ans2 = b+c-a
    if ans2 < 0:
        ans2 = 0
    print(f'#{i} {ans1} {ans2}')