from bisect import bisect_left

N = int(input())
numbers = sorted(list(map(int, input().split())))

answer = 0
for i in range(N - 2):
    l, r = i + 1, N - 1
    while l < r:
        cur, left, right = numbers[i], numbers[l], numbers[r]
        result = cur + left + right
        if result > 0:
            r -= 1
        else:
            if not result:
                if left == right:
                    answer += r - l
                else:
                    idx = bisect_left(numbers, right)
                    answer += r - idx + 1
            l += 1

print(answer)