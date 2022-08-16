import sys
sys.stdin = open('1208input.txt', 'r')
T = 10
for i in range(1, T+1):
    num = int(input())
    num_list = list(map(int, input().split()))
    for j in range(num):
        num_list.sort()
        A = num_list.pop(0); B = num_list.pop()
        A += 1; B -= 1
        num_list.append(A); num_list.append(B)
    print(f'#{i}', max(num_list) - min(num_list))