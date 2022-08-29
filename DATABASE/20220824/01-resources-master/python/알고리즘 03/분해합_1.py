# https://www.acmicpc.net/problem/2231
"""
215
"""
import sys
sys.stdin = open("분해합.txt")

# 숫자 N 입력 
N = int(input())


number_list = []

# 1부터 N 사이의 모든 수의 분해합을 탐색
for number in range(1,N):

    # 분해합 저장 변수
    split_sum = 0
    
    # 각 자리수의 합 계산
    for digit in str(number):
        split_sum = split_sum + int(digit)
    
    # 각 자리수의 합 + 수의 합 => 분해합
    split_sum = split_sum + number
    
    # 현재 수와 현재 수로 만든 분해합 출력.
    # print(number,split_sum)

    # 현재 수(number)로 만든 분해합과 입력 N이 같은면 number는 N의 생성자입니다.
    if N == split_sum:
        # 가장 작은 생성자를 찾기위해 number를 저장합니다.
        number_list.append(number)

# 저장된 생성자가 없으면 0을 출력합니다.
if len(number_list) == 0:
    print(0)
else:
    print(min(number_list))
"""
198
"""
