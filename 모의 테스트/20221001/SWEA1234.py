for t in range(1, 11):
    N = input().split()
    answer = []
    if N[0] != '0':
        for i in range(int(N[0])):
            if len(answer) > 0:
                if answer[-1] == N[1][i]:
                    answer.pop()
                else:
                    answer.append(N[1][i])
            else:
                answer.append(N[1][i])
        print(f'#{t}', end=' ')
    print(''.join(answer))