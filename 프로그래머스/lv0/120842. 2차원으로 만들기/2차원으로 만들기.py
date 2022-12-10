def solution(num_list, n):
    result = []
    temp = []
    for idx, num in enumerate(num_list, 1):
        temp.append(num)
        if not idx % n:
            result.append(temp)
            temp = []
    return result