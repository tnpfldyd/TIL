import sys
input = sys.stdin.readline

N = int(input())
friends = [list(map(str, input().split())) for _ in range(N)]

count = [0] * 1000000
for friend in friends:
    start, end = int(friend[0].replace('-', '')), int(friend[1].replace('-', ''))
    count[start] += 1
    count[end + 1] -= 1

for i in range(1, len(count)):
    count[i] += count[i - 1]

result = count.index(max(count))

print(f'{result // 100}-{str(result % 100).zfill(2)}')