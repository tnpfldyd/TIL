N, K = map(int, input().split())
work_speeds = sorted([*map(int, input().split())])
min_time = float('inf')

for i in range(1, N):
    team1_speed = work_speeds[0] * i
    team2_speed = work_speeds[i] * (N - i)
    total_speed = team1_speed + team2_speed
    required_time = K // total_speed if K % total_speed == 0 else K // total_speed + 1
    min_time = min(min_time, required_time)

print(min_time)
