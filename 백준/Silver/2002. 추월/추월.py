import sys
input = sys.stdin.readline
result = []
T = int(input())
for i in range(T):
    result.append(input())
cnt = 0
rere = 0
for i in range(T):
    text = input()
    if text == result[rere]:
        rere += 1
    else:
        cnt += 1
        temp = result.index(text)
        result.pop(temp)
print(cnt)