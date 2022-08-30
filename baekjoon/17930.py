import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(map(int, input().rstrip().split()))
num_list.sort()
for i in range(1, len(num_list)):
    num_list[i] = num_list[i] + num_list[i-1]
for i in range(M):
    a, b = map(int, input().split())
    if a == 1:
        print(num_list[b-a])
    else:
        print(num_list[b-1] - num_list[a-2])
