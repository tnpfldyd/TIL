import sys
input = sys.stdin.readline
T = int(input())

def binary_search():
    l, r = 0, N - 1
    answer = 1e9
    cnt = 0
    while l < r:
        temp = numbers[l] + numbers[r]
        if abs(temp - K) < abs(answer - K):
            answer = temp
            cnt = 1
        elif abs(temp - K) == abs(answer - K):
            cnt += 1
        if temp > K:
            r -= 1
        else:
            l += 1
    return cnt

for _ in range(T):
    N, K = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))
    result = binary_search()
    print(result)