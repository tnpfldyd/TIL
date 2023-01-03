from heapq import heappop, heappush
def solution(n, k, enemy):
    temp = []
    answer = 0
    for i in enemy:
        if len(temp) < k:
            heappush(temp, i)
            answer += 1
        else:
            if i > temp[0]:
                x = heappop(temp)
                n -= x
                heappush(temp, i)
            else:
                n -= i
            if n >= 0:
                answer += 1
    return answer