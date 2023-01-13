import bisect

def solution(array, height):
    array.sort()
    answer = len(array) - bisect.bisect_right(array, height)
    return answer
