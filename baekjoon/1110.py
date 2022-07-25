T = int(input())
cnt = 0
N = T
while True:
    a = N // 10
    b = N % 10
    c = (a + b) % 10
    N = (b * 10) + c
    cnt += 1
    if N == T:
        break
print(cnt)
