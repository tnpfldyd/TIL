import itertools
T = int(input())
for i in range(1, T+1):
    num_list = list(map(int, input().split()))
    result = set()
    for j in itertools.combinations(num_list, 3):
        result.add(sum(j))
    answer = []
    for j in result:
        answer.append(j)
    answer.sort(reverse=True)
    print(f'#{i} {answer[4]}')