import itertools
def solution(number):
    result = 0
    for i in itertools.combinations(number, 3):
        if sum(i) == 0:
            result += 1
    return result

print(solution([-2, 3, 0, 2, -5]))