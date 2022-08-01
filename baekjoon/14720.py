T = int(input())
cnt = 0
T_list = list(map(int, input().split()))
for i in range(T):
    if T_list[i] == cnt % 3:
        cnt += 1
print(cnt)