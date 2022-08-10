result = [int(input()) for _ in range(3)]

if sum(result) == 180:
    if result[0] == result[1] == result[2]:
        print('Equilateral')
    elif result[0] == result[1] or result[0] == result[2] or result[1] == result[2]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print("Error")
