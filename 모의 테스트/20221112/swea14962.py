T = int(input())
for i in range(1, T+1):
    a = int(input())
    if a % 2 == 1:
        print(f'#{i} Bob')
    else:
        print(f'#{i} Alice')  