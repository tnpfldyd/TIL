import bisect

N = int(input())
N_list = list(map(int, input().strip().split()))
result = []
for i in N_list:
    if result:
        if i > result[-1]:
            result.append(i)
        else:
            idx = bisect.bisect_left(result, i)
            result[idx] = i
    else:
        result.append(i)
print(result)