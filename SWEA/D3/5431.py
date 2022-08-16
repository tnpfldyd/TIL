# T = int(input())
# for i in range(1, T+1):
#     chong, person = map(int, input().split())
#     name = list(map(int, input().split()))
#     result = []
#     for j in range(1, chong + 1):
#         result.append(j)
#     for k in name:
#         result.remove(k)
    
#     print(f'#{i}', *result)
T = int(input())
for i in range(1, T+1):
    N, K = map(int, input().split())
    students = [0] * (N+1)
    # print(students)
    number_list = list(map(int, input().split()))
    for j in number_list:
        students[j] = 1
    print(f'#{i}', end = ' ')
    for k in range(1, N+1):
        if students[k] != 1:
            print(k, end = ' ')
    print()