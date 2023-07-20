import sys
input = sys.stdin.readline
N = int(input())
ranks = [[0, 0] for _ in range(10)]

for _ in range(N):
    string = input().strip()
    value = 1
    ranks[ord(string[0]) - ord('A')][1] = 1
    for i in range(len(string) - 1, -1, -1):
        ranks[ord(string[i]) - ord('A')][0] += value
        value *= 10
ranks.sort(reverse=True)
if ranks[9][1]:
    for i in range(8, -1, -1):
        if not ranks[i][1]:
            ranks.pop(i)
            break
answer = 0
for i in range(9):
    answer += ranks[i][0] * (9 - i)
print(answer)