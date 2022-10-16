def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        temp = prices[i]
        cnt = 0
        for j in range(i+1, len(prices)):
            if i != j:
                cnt += 1
                if temp > prices[j]:
                    break
        answer.append(cnt)
    answer.append(0)
    return answer