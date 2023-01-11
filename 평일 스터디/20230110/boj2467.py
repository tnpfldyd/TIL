import sys
input = sys.stdin.readline
N = int(input())
N_list = list(map(int, input().strip().split()))

left, right = 0, N-1
result = abs(N_list[left] + N_list[right])
a, b = N_list[left], N_list[right]
while left < right:
    temp = N_list[left] + N_list[right]
    if abs(temp) < result:
        result = abs(temp)
        a, b = N_list[left], N_list[right]
    if temp < 0:
        left += 1
    else:
        right -= 1
print(a, b)