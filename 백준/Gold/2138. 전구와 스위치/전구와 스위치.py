def switch_on(i):
    if i:
        s[i - 1] = '0' if s[i - 1] == '1' else '1'
    s[i] = '0' if s[i] == '1' else '1'
    if i != len(s) - 1:
        s[i + 1] = '0' if s[i + 1] == '1' else '1'

def greedy():
    cnt = 0

    for i in range(1, len(s)):
        if s[i - 1] != original[i - 1]:
            switch_on(i)
            cnt += 1

    return cnt if s == original else -1

n = int(input())
s = list(input().strip())
original = list(input().strip())

backup = s.copy()

res1 = greedy()

s = backup.copy()
switch_on(0)

temp = greedy()
res2 = -1 if temp == -1 else temp + 1

if res1 == -1:
    print(res2)
elif res2 == -1:
    print(res1)
else:
    print(min(res1, res2))

