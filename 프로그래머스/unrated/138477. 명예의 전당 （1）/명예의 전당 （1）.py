from heapq import heappop,heappush
def solution(k, score):
    result = []
    stack = []
    for i in score:
        if len(stack) < k:
            heappush(stack, i)
        elif len(stack) == k:
            if i > stack[0]:
                heappop(stack)
                heappush(stack, i)
        result.append(stack[0])
    return result