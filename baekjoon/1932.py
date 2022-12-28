import sys
input = sys.stdin.readline
N = int(input())
result = []
for i in range(N):
    num_list = list(map(int, input().strip().split()))
    temp = []
    for a, b, c in zip([0]+result, result+[0], num_list):
        temp.append(max(a+c, b+c))
    result = temp
print(max(result))