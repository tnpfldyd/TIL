# https://www.acmicpc.net/problem/2231
"""
215
"""
import sys
sys.stdin = open("분해합.txt")

# 숫자 N 입력 
N = int(input())

# 가장 작은 생서자를 저장할 변수
answer = 0


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
        # 생성자를 찾았으니 반복문을 종료합니다.
        answer = number
        break

# 발견한 생성자를 출력합니다.
# 만약 생성자를 발견하지 못했다면 처음에 할당한 0이 출력됩니다.
print(answer)
"""
198
"""
