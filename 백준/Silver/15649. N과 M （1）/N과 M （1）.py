import itertools
N, M = map(int,input().split())
result = []
for i in range(1, N+1):
    result.append(i)
final = []
for i in itertools.permutations(result, M):
    final.append(i)
for i in final:
    print(*i)