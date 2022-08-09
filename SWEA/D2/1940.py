import sys

sys.stdin = open("1940input.txt", "r")

T = int(input())
for i in range(1, T+1):
    cnt = int(input())
    result = 0
    temp = 0
    for j in range(cnt):
        a = input()
        if a[0] == '1':
            temp += int(a[2])
            result += temp
        elif a[0] == '0':
            result += temp
        else:
            if temp - int(a[2]) < 0:
                temp = 0
            else :
                temp -= int(a[2])
            result += temp
    print(f'#{i}',result)