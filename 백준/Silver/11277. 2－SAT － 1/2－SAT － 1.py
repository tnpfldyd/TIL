import sys
input = sys.stdin.readline

N, M = map(int, input().split())
clauses = [tuple(map(int, input().split())) for _ in range(M)]

def eval_lit(lit, mask):
    v = (mask >> (abs(lit) - 1)) & 1
    return v if lit > 0 else not v

for mask in range(1 << N):
    for a, b in clauses:
        if not (eval_lit(a, mask) or eval_lit(b, mask)):
            break
    else:
        print(1)
        break
else:
    print(0)