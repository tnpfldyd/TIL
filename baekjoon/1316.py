T = int(input())
cnt = 0
for i in range(T):
    text = input()
    result = []
    for j in range(len(text)):
        if j == 0:
            result.append(text[j])
        elif text[j] == text[j-1]:
            result.append(text[j])
        elif text[j] != text[j-1] and text[j] not in result:
            result.append(text[j])
    if len(text) == len(result):
        cnt += 1
print(cnt)