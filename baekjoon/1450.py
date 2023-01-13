import itertools
N, C = map(int, input().split())
N_list = list(map(int, input().strip().split()))
N1, N2 = N_list[:N//2], N_list[N//2:]
sum_left, sum_right = [], []

for i in range(1, len(N1)+1):
    for j in itertools.combinations(N1, i):
        sum_left.append(sum(j))
for i in range(1, len(N2)+1):
    for j in itertools.combinations(N2, i):
        sum_right.append(sum(j))
sum_left.append(0); sum_right.append(0)
sum_left.sort()
answer = 0
for i in sum_right:
    if i > C:
        continue
    left, right = 0, len(sum_left)

    while left < right:
        mid = (left + right) // 2
        if sum_left[mid] + i > C:
            right = mid
        else:
            left = mid + 1
    answer += right
print(answer)