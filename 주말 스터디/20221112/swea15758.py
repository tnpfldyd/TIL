T = int(input())
for i in range(1, T+1):
    a, b = input().split()
    tempa = a; tempb = b
    while len(tempa) != len(tempb):
        if len(tempa) > len(tempb):
            tempb += b
        else:
            tempa += a
    if tempa == tempb:
        print(f'#{i} yes')
    else:
        print(f'#{i} no')
