a, b = map(int, input().strip().split(' '))
matrix = [['*'] * a for _ in range(b)]
for i in matrix:
    print(''.join(i))