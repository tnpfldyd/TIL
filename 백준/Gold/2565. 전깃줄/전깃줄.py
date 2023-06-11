import sys, bisect
input = sys.stdin.readline

N = int(input())

wires = [tuple(map(int, input().strip().split())) for _ in range(N)]

wires.sort()

result = []

for wire in wires:
    a, b = wire
    if result:
        if b > result[-1]:
            result.append(b)
        else:
            idx = bisect.bisect_left(result, b)
            result[idx] = b
    else:
        result.append(b)

print(N - len(result))