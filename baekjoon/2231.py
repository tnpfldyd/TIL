T = int(input())
min_T = T - (len(str(T)) * 9)
if min_T < 10:
    min_T = 0
for i in range(min_T, T):
    tmp = sum(map(int, str(i)))
    result = tmp + i
    if result == T:
        print(i)
        break
else:
    print(0)