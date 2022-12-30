def solution(s1, s2):
    answer = len(set(s1)&set(s2))
    return answer

print(solution(['a','b','c'],["com", "b", "d", "p", "c"]))