from collections import deque
N, T, G = map(int, input().split())
q = deque([N])
visited = set([N])

for t in range(T + 1):
    flag = False
    for i in range(len(q)):
        x = q.popleft()
        if x == G:
            print(t)
            flag = True
            break

        a = x + 1
        if a < 100000 and a not in visited:
            q.append(a)
            visited.add(a)

        b = x * 2
        if b and b < 100000:
            first_digit = int(str(b)[0])
            b = int(str(first_digit - 1) + str(b)[1:])
            if b not in visited:
                q.append(b)
                visited.add(b)

    if flag:
        break
else:
    print("ANG")