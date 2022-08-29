# https://www.acmicpc.net/problem/2846
"""
5
5 2 1 4 6

특정 오르막길의 끝 값과 시작 값을 빼서
오르막길의 길이를 구합니다.
조건이 많으니 유의해주세요.
"""
import sys
sys.stdin = open("오르막길.txt")

# N : 리스트 길이
N = int(input())

# 높이 리스트 입력
list_ = list(map(int,input().split()))

# 가장 긴 오르막길 길이를 저장할 변수
max_ = 0

# 오르막길 시작 값 변수
start = 0 
# 오르막길 끝 값 변수
end = 0

for i in range(1, len(list_)):
    if list_[i] > list_[i-1]:
        # 오르막길이 시작 전일 때만 시작 값(start)을 변경합니다.
        # 이 조건이 없으면 오르막길이 발생할 때마다 시작 값이 변경됩니다.
        if start == 0:
            start = list_[i-1]

        if i == len(list_) - 1:
            end = list_[i]
            max_ = max(max_, end - start)

       
       


    else:
        # start가 0이라면 오르막길을 시작을 하지 않았다는 의미입니다.
        # 그러니 start가 0이 아닐 때 오르막길의 끝 값을 구해서
        # 오르막길의 길이를 계산합니다.
        if start != 0:
            end = list_[i-1]
            # 끝 값과 첫 값을 사용해서 오르막길 길이를 구합니다.
            length = end - start
            # 가장 긴 길이를 갱신합니다.
            max_ = max(max_, length)
            # 오르막길의 시작 값을 0으로 초기화합니다.
            start = 0

print(max_)
"""
5
"""