def solution(lines):
    dic = {}
    for line in lines:
        for i in range(line[0], line[1]):
            if i not in dic:
                dic[i] = 0
            else:
                dic[i] += 1
    answer = 0
    for k, v in dic.items():
        if v:
            answer += 1
    return answer

print(solution([[0, 1], [2, 5], [3, 9]]))