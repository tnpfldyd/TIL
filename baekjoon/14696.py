T = int(input())
for i in range(T):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.remove(A[0])
    B.remove(B[0])
    A_num = [A.count(4), A.count(3), A.count(2), A.count(1)]
    B_num = [B.count(4), B.count(3), B.count(2), B.count(1)]
    if A_num[0] > B_num[0]:
        print('A')
    elif A_num[0] < B_num[0]:
        print('B')
    elif A_num[1] > B_num[1] :
        print('A')
    elif B_num[1] > A_num[1] :
        print('B')
    elif A_num[2] > B_num[2] :
        print('A')
    elif B_num[2] > A_num[2] :
        print('B')
    elif A_num[3] > B_num[3] :
        print('A')
    elif B_num[3] > A_num[3] :
        print('B')
    else :
        print('D')    