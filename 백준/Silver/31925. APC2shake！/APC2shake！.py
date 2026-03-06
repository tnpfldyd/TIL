import sys

input = sys.stdin.readline

n = int(input())
candidates = []

for _ in range(n):
    data = input().split()
    name = data[0]
    status = data[1]
    icpc = data[2]
    shake_rank = int(data[3])
    apc_rank = int(data[4])

    if status == 'jaehak' and icpc == 'notyet':
        if shake_rank == -1 or shake_rank > 3:
            candidates.append((apc_rank, name))

candidates.sort()

selected = []
limit = min(len(candidates), 10)
for i in range(limit):
    selected.append(candidates[i][1])

selected.sort()

print(len(selected))
for name in selected:
    print(name)