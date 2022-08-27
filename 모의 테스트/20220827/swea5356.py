T = int(input())
for k in range(1, T+1):
    Text = [input() for _ in range(5)]
    print(f'#{k} ', end='')
    for i in range(len(max(Text, key=len))):
        for j in range(5):
            if len(Text[j]) < i+1: # i번째 글자를 출력할건데, 만약 i보다 Text[j] 번째의 글자수가 작으면 무시 인덱스는 0부터기 때문에 i+1
                continue
            print(Text[j][i], end='')
    print()