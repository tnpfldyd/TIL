import sys
input = sys.stdin.readline

def get_result(q):
    result = max_point = 0
    left = K
    while q:
        point, people = q.pop()
        max_point = max(max_point, point)
        if left < people:
            result += max_point * 2
            q.append((point, people - left))
            max_point = 0
            left = K
        else:
            left -= people
    return result + max_point * 2

N, K, S = map(int, input().split())
l, r = [], []
for _ in range(N):
    point, people = map(int, input().split())
    lr = point - S
    r.append((lr, people)) if lr >= 0 else l.append((abs(lr) , people))

print(get_result(sorted(l)) + get_result(sorted(r)))