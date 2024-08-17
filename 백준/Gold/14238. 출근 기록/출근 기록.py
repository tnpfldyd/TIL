def solution(a, b, c, pp, p):
    if a == worker[0] and b == worker[1] and c == worker[2]:
        return True
    
    if dp[a][b][c][pp][p]:
        return False
    
    dp[a][b][c][pp][p] = True
    
    if a + 1 <= worker[0]:
        res[a + b + c] = 'A'
        if solution(a + 1, b, c, p, 0):
            return True
    
    if b + 1 <= worker[1]:
        res[a + b + c] = 'B'
        if p != 1 and solution(a, b + 1, c, p, 1):
            return True
    
    if c + 1 <= worker[2]:
        res[a + b + c] = 'C'
        if pp != 2 and p != 2 and solution(a, b, c + 1, p, 2):
            return True
    
    return False

S = input()

worker = [0, 0, 0]
for char in S:
    if char == 'A':
        worker[0] += 1
    elif char == 'B':
        worker[1] += 1
    else:
        worker[2] += 1

dp = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(51)] for _ in range(51)] for _ in range(51)]

res = [''] * 51

if solution(0, 0, 0, -1, -1):
    print(''.join(res[:len(S)]))
else:
    print(-1)