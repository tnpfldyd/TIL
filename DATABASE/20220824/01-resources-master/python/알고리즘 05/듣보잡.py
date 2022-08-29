import sys
sys.stdin = open("_듣보잡.txt")

"""
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton
---
2
baesangwook
ohhenrie
"""
N,M = list(map(int,input().split()))
print(N,M)
list_ = []
# dict_ = dict()
# set_ = set()
# N의 크기만큼 듣도못한 사람을 입력
for i in range(N):
    p = input()
    # dict_[p] = "듣도못한"
    list_.append(p)

    
# list_=[]
# # M의 크기만금 보도못한 사람을 입력
# for i in range(M):
#     p = input()
#     # 입력받은 사람이 딕셔너리의 키 중에 있느냐?
#     if p in dict_:
#         list_.append(p)

# list_.sort()
# print(len(list_))
# for p in list_:
#     print(p)
# print(list_)
# # 이름을 키로 사용해서 저장할 딕셔너리 변수
# dict_["ohhenrie"] = "듣도못한사람"
# dict_["charlie"] = "듣도못한사람"
# dict_["baesangwook"] = "듣도못한사람"

# if "obama" in dict_:
#     print("obama 듣도보도못한사람")

# if "baesangwook" in dict_:
#     print("baesangwook 듣도보도못한사람")

# if "ohhenrie" in dict_:
#     print("ohhenrie 듣도보도못한사람")

# if "clinton" in dict_:
#     print("clinton 듣도보도못한사람")
