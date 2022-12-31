import sys, bisect
input = sys.stdin.readline

try:
    while input():
        N_list = list(map(int, input().strip().split()))
        result = []
        for n in N_list:
            if result:
                if result[-1] < n:
                    result.append(n)
                else:
                    idx = bisect.bisect_left(result, n)
                    result[idx] = n
            else:
                result.append(n)
        print(len(result))
except:
    exit()
