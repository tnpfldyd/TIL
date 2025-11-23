import sys
input = sys.stdin.readline

n = int(input())
citations = list(map(int, input().split()))

citations.sort(reverse=True)

q_index = 0
for i in range(n):
    if citations[i] >= i + 1:
        q_index = i + 1
    else:
        break

print(q_index)