num = set(range(1, 10001))
s_num = set()
for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    s_num.add(i)
new_num = sorted(num - s_num)
for i in new_num:
    print(i)