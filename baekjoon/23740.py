import sys
input = sys.stdin.readline

N = int(input())
bus_routes = sorted([tuple(map(int, input().split())) for _ in range(N)])
cs, ce, cc = bus_routes[0]
result = []
for i in range(1, N):
    ns, ne, nc = bus_routes[i]
    if ce < ns:
        result.append((cs, ce, cc))
        cs, ce, cc = ns, ne, nc
    else:
        ce, cc = max(ce, ne), min(cc, nc)

result.append((cs, ce, cc))

print(len(result))
for row in result:
    print(*row)