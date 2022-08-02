import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    numbers = list(map(int, input().split()))
    if numbers[0] < numbers[1] - numbers[2]:
        print('advertise')
    elif numbers[0] == numbers[1] - numbers[2]:
        print('does not matter')
    else:
        print('do not advertise')