from collections import deque
S = input()
aq, bq = deque(), deque()

answer = 0

for i in range(len(S)):
    if S[i] == 'C':
        if bq and bq[0] < i:
            answer += 1
            bq.popleft()
    elif S[i] == 'B':
        bq.append(i)
    else:
        aq.append(i)

while aq and bq:
    if aq[0] < bq[0]:
        answer += 1
        bq.popleft()
        aq.popleft()
    else:
        bq.popleft()

print(answer)