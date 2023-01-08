import sys
input = sys.stdin.readline
INF = sys.maxsize
N = int(input())
N_list = sorted(list(map(int, input().strip().split())))
answer = INF
if N == 3:
    print(N_list)
else:
    for _ in range(N-2):
        temp = N_list.pop()
        left, right = 0, len(N_list)-1
        while left < right:
            sum_temp = temp + N_list[left] + N_list[right]
            if abs(sum_temp) < answer:
                answer = abs(sum_temp)
                result = [N_list[left], N_list[right], temp]
            if sum_temp < 0:
                left += 1
            else:
                right -= 1
        if not answer:
            break
print(*result)