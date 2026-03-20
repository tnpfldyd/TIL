S = input().strip()

count = [0] * 26

for c in S:
    count[ord(c) - ord('a')] += 1

print(*count)