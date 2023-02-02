def solution(common):
    a, b, c = common[0], common[1], common[2]
    diff1, diff2 = b - a, c - b
    if diff1 == diff2:
        answer = common[-1] + diff1
    else:
        ratio = diff2 // diff1
        answer = common[-1] * ratio
    return answer

print(solution([2, 4, 8]))