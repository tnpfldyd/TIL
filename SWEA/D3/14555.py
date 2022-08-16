T = int(input())
for i in range(1, T+1):
    quiz = input()
    result = ''
    cnt = 0
    for j in quiz:
        result += j
        if '(|' in result:
            cnt += 1
            result = ''
        elif '|)' in result:
            cnt += 1
            result = ''
        elif '()' in result:
            cnt += 1
            result = ''
    print(f'#{i}', cnt)