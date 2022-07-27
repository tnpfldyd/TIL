A = list(map(int, input().split()))
B = list(map(int, input().split()))
A_cnt = 0
B_cnt = 0
A_score = []
B_score = []
for i in range(10):
    if A[i] > B[i]:
        A_cnt += 3
        A_score.append(3)
        B_score.append(1)
    elif A[i] == B[i]:
        A_cnt += 1
        B_cnt += 1
        A_score.append(1)
        B_score.append(1)
    else:
        B_cnt += 3
        B_score.append(3)
        A_score.append(1)
A_score.reverse()
B_score.reverse()
print(A_cnt, B_cnt)
if A_cnt == B_cnt == 10:
    print('D')
if A_cnt == B_cnt != 10:
    print('A' if A_score.index(3)<B_score.index(3) else 'B')
if A_cnt > B_cnt:
    print('A')
elif A_cnt < B_cnt:
    print('B')