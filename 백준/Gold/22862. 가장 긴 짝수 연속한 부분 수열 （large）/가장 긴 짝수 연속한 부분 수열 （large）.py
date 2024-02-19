N, K = map(int, input().split())
S = list(map(int, input().split()))

l = r = cnt = answer = 0

while True:
    if cnt > K:
        if S[l] % 2:
            cnt -= 1
        l += 1
    elif r == N:
        break
    else:
        if S[r] % 2:
            cnt += 1
        r += 1

    if cnt <= K:
        answer = max(answer, r - l - cnt)
    
print(answer)