T = int(input())
numbers = [input() for _ in range(T)]
tong = []
for number in numbers:
    result = 0
    for j in number:
        result += int(j)
    while result > 9:
        temp = 0
        for j in str(result):
            temp += int(j)
        result = temp
    tong.append(result)
for i in range(T):
    print(f'#{i+1} {tong[i]}')