import sys
sys.stdin = open("_쉽게푸는문제.txt")

"""
3 7 / 15
"""
A, B = list(map(int,input().split()))

list_ = []
N = 1
while len(list_) < B:
    for i in range(N):
        list_.append(N)
    N += 1
print(list_,len(list_))

list_ = []
N = 1
for i in range(B+1):
    for i in range(N):
        list_.append(N)
    N += 1

print(list_,len(list_))
print(sum(list_[A - 1 : B]))