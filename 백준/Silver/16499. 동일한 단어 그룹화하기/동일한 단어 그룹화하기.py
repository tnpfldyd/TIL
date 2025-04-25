import sys
input = sys.stdin.readline

N = int(input())
words = [input().strip() for _ in range(N)]
groups = set()
for word in words:
    freq = [0] * 26
    for char in word:
        freq[ord(char) - ord('a')] += 1
    groups.add(tuple(freq))
print(len(groups))