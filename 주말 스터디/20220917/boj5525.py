N = int(input())
S = int(input())
Text = input()
cnt = 0
temp = 0
x = 1
while x < S-1:
    if Text[x-1] == 'I' and Text[x] == 'O' and Text[x+1] == 'I':
        temp += 1
        if temp == N:
            temp -= 1
            cnt += 1
        x += 1
    else:
        temp = 0
    x += 1
print(cnt)