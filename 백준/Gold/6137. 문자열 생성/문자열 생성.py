import sys
input = sys.stdin.readline
N = int(input())
S = [ord(input().strip()) for _ in range(N)]

l, r = 0, N - 1
result = ''
cnt = 0
while l <= r:
    if S[l] < S[r]:
        result += chr(S[l])
        l += 1
    elif S[l] == S[r]:
        tl, tr = l, r
        while tl <= tr:
            if S[tl] < S[tr]:
                result += chr(S[l])
                l += 1
                break
            elif S[tl] == S[tr]:
                tl += 1
                tr -= 1
            else:
                result += chr(S[r])
                r -= 1
                break
        else:
            result += chr(S[l])
            l += 1
    else:
        result += chr(S[r])
        r -= 1
    cnt += 1
    if not cnt % 80:
        result += '\n'

print(result)