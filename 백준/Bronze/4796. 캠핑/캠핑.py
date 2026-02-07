import sys
input = sys.stdin.readline

case = 1

while True:
    L, P, V = map(int, input().split())

    if not L and not P and not V:
        break
        
    result = (V // P) * L + min(V % P, L)

    print("Case " + str(case) + ": " + str(result))

    case += 1