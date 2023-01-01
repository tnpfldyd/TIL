import bisect, sys
input = sys.stdin.readline
N = int(input())
result = []
N_list = list(map(int, input().strip().split()))
for n in N_list:
    if result:
        if result[-1] < n:
            result.append(n)
        else:
            idx = bisect.bisect_left(result, n)
            result[idx] = n
    else:
        result.append(n)
print(N-len(result))