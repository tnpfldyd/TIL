N = int(input())
v = list(map(int, input().split()))

if N == 1:
    print(v[0])
else:
    v.sort()

    sum_val = sum(v)
    max_val = max(sum_val / N, v[-2])

    print("{:.7f}".format(max_val))