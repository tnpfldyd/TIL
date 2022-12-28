import bisect
A = int(input())
A_list = list(map(int, input().strip().split()))
result = []
for i in A_list:
    if result:
        if result[-1] < i:
            result.append(i)
        else:
            idx = bisect.bisect_left(result, i)
            result[idx] = i
    else:
        result.append(i)
print(len(result))