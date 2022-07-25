T = int(input())

result = 0
for i in range(1, T+1):
    T_list = list(map(int, str(i)))
    if i < 100:
        result += 1
    elif T_list[0]-T_list[1] == T_list[1]-T_list[2]:
        result += 1
print(result)