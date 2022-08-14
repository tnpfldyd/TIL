import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num_list = list(map(int, input().rstrip().split()))
temp_sum = sum(num_list[:M])
result = [temp_sum]
for i in range(0, N-M):
    temp_sum = temp_sum - num_list[i] + num_list[i+M]
    result.append(temp_sum)
print(max(result))
