from heapq import heappop,heappush
k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
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
print(result)