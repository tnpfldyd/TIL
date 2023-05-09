import sys
input = sys.stdin.readline

N = int(input())
L = list(input().strip() for _ in range(N))
K = int(input())
count = [[i, 0] for i in range(36)]
for l in L:
    for i in range(len(l)):
        num = l[len(l)-i-1]
        if num.isdigit():
            num = int(num)
        else:
            num = ord(num) - ord('A') + 10
        count[num][1] += (36 ** i)

count = sorted(count, key=lambda x : x[1] * 35 - x[1] * x[0], reverse=True)

cnt = 0
for i in range(36):
    if cnt == K:
        break
    if count[i][0] != 35:
        count[i][0] = 35
        cnt += 1

result = 0
for i in range(36):
    result += count[i][0] * count[i][1]

def to_36(num):
    if num < 10:
        return str(num)
    else:
        return chr(num - 10 + ord('A'))

def decimal_to_36(n):
    ans = ""
    while n:
        remain = n % 36
        ans = to_36(remain) + ans
        n //= 36
    return ans if ans else "0"

print(decimal_to_36(result))