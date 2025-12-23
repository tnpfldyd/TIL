import sys
input = sys.stdin.readline

N, K, Q, M = map(int, input().split())

is_sleeping = [False] * (N + 3)
for x in map(int, input().split()):
    is_sleeping[x] = True

is_attended = [0] * (N + 3)
for student in map(int, input().split()):
    if is_sleeping[student]:
        continue
    
    for target in range(student, N + 3, student):
        if not is_sleeping[target]:
            is_attended[target] = 1

prefix_sum = [0] * (N + 3)
for i in range(3, N + 3):
    not_attended_count = 1 if is_attended[i] == 0 else 0
    prefix_sum[i] = prefix_sum[i - 1] + not_attended_count

for _ in range(M):
    S, E = map(int, input().split())
    print(prefix_sum[E] - prefix_sum[S - 1])