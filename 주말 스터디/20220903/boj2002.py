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
    if text == result[rere]: # 추월 안했다면
        rere += 1
    else: # 추월 했다면
        cnt += 1
        temp = result.index(text) 
        result.pop(temp)
print(cnt)