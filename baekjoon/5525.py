N = int(input())
S = int(input())
Text = input()
test = ['I']
for i in range(N):
    test = test + ['O', 'I']
result = []
cnt = 0
for i in Text:
    result.append(i)
    if i == 'I':
        if result[-len(test):] == test:
            cnt += 1
print(cnt)