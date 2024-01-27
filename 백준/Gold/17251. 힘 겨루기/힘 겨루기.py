N = int(input())
numbers = list(map(int, input().split()))

max_value = left = right = 0

for i in range(N):
    cur = numbers[i]
    if cur > max_value:
        max_value = cur
        left = right = i
    elif cur == max_value:
        right = i
N -= 1
if left > N - right:
    print('B')
elif left < N - right:
    print('R')
else:
    print('X')