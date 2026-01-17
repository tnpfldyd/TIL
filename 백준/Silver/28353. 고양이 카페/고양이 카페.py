N, K = map(int, input().split())
w = list(map(int, input().split()))

w.sort()

l, r = 0, N - 1
answer = 0

while l < r:
    if w[l] + w[r] <= K:
        answer += 1
        l += 1
        r -= 1
    else:
        r -= 1

print(answer)