def solution(arr):
    min_num = 987654321
    for i in arr:
        min_num = min(min_num, i)
    result = []
    for i in arr:
        if i != min_num:
            result.append(i)
    if not result:
        result.append(-1)
    return result

print(solution([2,2,2,2]))