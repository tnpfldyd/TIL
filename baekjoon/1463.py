a = int(input())
cnt = 0
while a != 1:
    if a % 3 == 0:
        a //= 3
        cnt += 1
    elif a % 2 == 0:
        a //= 2
        cnt += 1
    else:
        a -= 1
        cnt += 1
print(cnt)