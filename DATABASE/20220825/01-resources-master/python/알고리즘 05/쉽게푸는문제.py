import sys
# sys.stdin = open("_쉽게푸는문제.txt")

"""
3 7 / 15
"""

수열 = []
A = 3
B = 10000
N = 1


# 수열에 얼마만큼 숫자를 추가해야하나?
# 수열의 길이가 B보다 작을 때까지 수열에 숫자를 추가하자. 
i = 0
while i < B:
    # N 의 크기만큼 수열 리스트에 N을 추가한다.
    for _ in range(N):
        수열.append(N)
    # 1->2
    # 2->3
    N += 1
print(수열,len(수열))

# N = 1
# 수열 = []
# for i in range(B+1):
#     for _ in range(N):
#         수열.append(N)

#         if len(수열) > B:
#             break
    
#     if len(수열) > B:
#             break

    
#     N+=1
# print(수열,len(수열))