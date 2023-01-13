import sys, itertools, bisect
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().strip().split()))
n1, n2 = numbers[N//2:], numbers[:N//2]
n1_sum, n2_sum = [], []
for i in range(1, len(n1)+1):
    for j in itertools.combinations(n1, i):
        n1_sum.append(sum(j))
for i in range(1, len(n2)+1):
    for j in itertools.combinations(n2, i):
        n2_sum.append(sum(j))
n1_sum.sort(); n2_sum.sort()

answer = 0

answer += bisect.bisect_right(n1_sum, S) - bisect.bisect_left(n1_sum, S)
answer += bisect.bisect_right(n2_sum, S) - bisect.bisect_left(n2_sum, S)

for i in n1_sum:
    temp = S - i
    answer += bisect.bisect_right(n2_sum, temp) - bisect.bisect_left(n2_sum, temp)

print(answer)
