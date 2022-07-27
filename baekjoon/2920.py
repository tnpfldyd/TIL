T = list(map(int, input().split()))

if T == sorted(T):
    print('ascending')
elif T == sorted(T, reverse=True):
    print('descending')
else:
    print('mixed')