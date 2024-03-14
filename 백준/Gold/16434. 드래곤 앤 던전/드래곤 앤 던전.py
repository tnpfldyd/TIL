import math, sys
input = sys.stdin.readline

N, H = map(int, input().split())
cur_hp = 0
max_hp = 0

for _ in range(N):
    t, a, h = map(int, input().split())
    
    if t == 1:
        d = (math.ceil(h / H) - 1) * a
        
        if cur_hp >= d:
            cur_hp -= d
        else:
            max_hp += d - cur_hp
            cur_hp = 0
    else:
        H += a
        cur_hp = min(cur_hp + h, max_hp)

print(max_hp + 1)