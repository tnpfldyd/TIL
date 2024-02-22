from collections import defaultdict
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [input().rstrip() for _ in range(R)]

def check_duplicates(mid):
    check = defaultdict(int)
    for j in range(C):
        temp = ''.join(arr[i][j] for i in range(mid, R))
        if check[temp]:
            return False
        check[temp] = True
    return True

result = 0
start, end = 0, R - 1

while start <= end:
    mid = (start + end) // 2

    if check_duplicates(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)