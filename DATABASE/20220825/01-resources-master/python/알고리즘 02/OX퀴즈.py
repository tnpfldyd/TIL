import sys 
sys.stdin = open("input.txt")

# 총 테스트 개수를 입력 받습니다.
T = int(input())
O = "O"
X = "X"

# 테스트 횟수만큼 반복을 합니다.
for t in range(T):
    # 퀴즈의 정답 여부를 입력 받습니다.
    ox = input()

    count_o = 1 # 연속된 O의 개수
    sum_ = 0 # 점수의 합계

    # 퀴즈의 정답 여부를 순회합니다.
    for answer in ox:
        # 문제를 맞았다면(O)
        if answer == O:
            # 점수의 합계를 누적합니다.
            # 연속된 O의 개수를 증가시키기전에 누적합니다.
            sum_ = count_o + sum_
            
            count_o += 1 # O가 나왔으니 연속된 O의 개수를 1증가 시킵니다.

        if answer == X:
            count_o = 0 # 연속된 O의 개수를 초기화합니다.(0)
    
    print(sum_)
