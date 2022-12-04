from heapq import heappop, heappush
import sys
lines = sys.stdin.readlines()
time_dic = {}
matrix = [[] for _ in range(26)]
in_degree = [0] * 26
times = [0] * 26
for line in lines:
    A = line.split()
    b = ord(A[0])-65
    if len(A) == 2:
        time_dic[b] = int(A[1])
    else:
        time_dic[b] = int(A[1])
        in_degree[b] += len(A[2])
        for i in A[2]:
            matrix[ord(i)-65].append(b)
start = []
for i in time_dic:
    if not in_degree[i]:
        heappush(start, i)
        times[i] = time_dic[i]
while start:
    x = heappop(start)
    for i in matrix[x]:
        in_degree[i] -= 1
        times[i] = max(times[x] + time_dic[i], times[i])
        if not in_degree[i]:
            heappush(start, i)
print(max(times))