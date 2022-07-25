T = int(input())
if T % 4 == 0:
    if T % 400 == 0:
        print('1')
    elif T % 100 != 0:
        print('1')
    else:
        print('0')
else:
    print('0')        