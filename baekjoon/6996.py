T = int(input())
for _ in range(T):
    A, B = input().split()
    A_dic = {}
    B_dic = {}
    for i in A:
        if i not in A_dic:
            A_dic[i] = 1
        else:
            A_dic[i] += 1
    for i in B:
        if i not in B_dic:
            B_dic[i] = 1
        else:
            B_dic[i] += 1
    if A_dic == B_dic:
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')