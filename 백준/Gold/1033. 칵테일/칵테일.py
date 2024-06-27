import sys, math
input = sys.stdin.readline

def update(idx, val, line, cnt):
    branch = materials[idx][1]
    materials[idx][0] *= val
    materials[idx][1] = line
    if cnt == 1 and branch != line and branch != -1:
        for j, m in enumerate(materials):
            if m[1] == branch and j != idx:
                update(j, val, line, 2)

N = int(input())
materials = [[1, -1] for _ in range(N)]

for i in range(N - 1):
    a, b, p, q = map(int, input().split())
    gcd = math.gcd(p, q)
    a_val = materials[b][0] * p // gcd
    b_val = materials[a][0] * q // gcd
    gcd = math.gcd(a_val, b_val)
    update(a, a_val // gcd, i, 1)
    update(b, b_val // gcd, i, 1)

print(*[m[0] for m in materials])
