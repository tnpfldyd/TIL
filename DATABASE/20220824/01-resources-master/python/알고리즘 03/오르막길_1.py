# https://www.acmicpc.net/problem/2846
"""
5
5 2 1 4 6

오르막길의 길이를 누적합으로 계산하고,
누적합들을 모두 리스트에 저장한 후 가장 큰 값을 출력합니다.
"""
import sys
sys.stdin = open("오르막길.txt")

# N : 리스트 길이
N = int(input())

# 높이 리스트 입력
list_ = list(map(int,input().split()))

# 누적합 저장 변수
sum_ = 0

# 누적합들을 저장할 리스트
sum_list = []

# 오르막길을 찾기 위해서 인덱싱
for i in range(1, len(list_)):
    # 오르막길은 현재 값 > 이전 값
    if list_[i] > list_[i-1]:
        # 오르막길의 전체 길이 = 부분 오르막길들의 길이의 누적합
        sum_ = sum_ + list_[i] - list_[i-1] # 누적합

        # 오르막길이면 누적합 저장
        sum_list.append(sum_)


    # 오르막길이 아니면
    else:
        # 평지, 내리막길을 만나면 누적합을 0으로 초기화합니다.
        sum_ = 0
 
 

# 저장된 오르막길이 없으면 0을 출력합니다.
if len(sum_list) == 0:
    print(0)

# 저장된 오르막길이 있으면 가장 긴 길이를 출력합니다.
else:
    print(max(sum_list))
"""
5
"""