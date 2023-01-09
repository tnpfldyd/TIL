def solution(n, lost, reserve):
    reserve, lost = set(reserve) - set(lost), set(lost) - set(reserve)
    for reser in reserve:
        if reser - 1 in lost:
            lost.remove(reser - 1)
        elif reser + 1 in lost:
            lost.remove(reser + 1)
    answer = n - len(lost)
    return answer