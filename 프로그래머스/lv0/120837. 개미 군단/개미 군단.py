def solution(hp):
    answer = 0
    one, two, three = 0, 0, 0
    one += hp // 5
    hp %= 5
    two += hp // 3
    hp %= 3
    three += hp // 1
    answer = one + two + three
    return answer