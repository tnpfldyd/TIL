import sys
input = sys.stdin.readline
N = int(input())
N_list = list(map(int, input().strip().split()))
N_list.sort()
C = int(input())
C_list = list(map(int, input().strip().split()))

for c in C_list:
    left = 0
    right = N-1
    answer = False
    while left <= right:
        mid = (left + right) // 2
        if N_list[mid] == c:
            answer = True
            break
        if c < N_list[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if answer:
        print(1)
    else:
        print(0)