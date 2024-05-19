import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
s = int(input())

for i in range(N - 1):
    if not s:
        break
    
    cnt = 0
    num = arr[i]
    idx = i
    
    for j in range(i + 1, N):
        if cnt >= s:
            break
        if num < arr[j]:
            num = arr[j]
            idx = j
        cnt += 1
    
    if idx != i:
        arr[i : idx + 1] = [arr[idx]] + arr[i : idx]
        s -= idx - i

print(" ".join(map(str, arr)))