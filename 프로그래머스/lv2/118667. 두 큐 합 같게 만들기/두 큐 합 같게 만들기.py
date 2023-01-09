from collections import deque
def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    q1, q2 = sum(queue1), sum(queue2)
    if (q1 + q2) % 2:
        return -1
    cnt, max_cnt = 0, len(queue1) * 4
    if q1 == q2:
        return 0
    while True:
        if q1 < q2:
            temp = queue2.popleft()
            q2 -= temp; q1 += temp
            queue1.append(temp)
        elif q1 > q2:
            temp = queue1.popleft()
            q1 -= temp; q2 += temp
            queue2.append(temp)
        else:
            break
        cnt += 1
        if cnt > max_cnt:
            return -1
    return cnt