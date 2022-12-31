T = int(input())
for i in range(1, T+1):
    a, b, c = map(int, input().split())
    temp = min(a, b)
    print(f'#{i} {c//temp}')