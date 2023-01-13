import bisect

def solution(array, height):
    array.sort()
    answer = len(array) - bisect.bisect_right(array, height)
    return answer

print(solution([180, 120, 140], 190))