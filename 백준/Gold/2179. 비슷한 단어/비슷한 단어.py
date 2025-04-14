import sys

def common_prefix_length(a, b):
    count = 0
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            break
        count += 1
    return count

input = sys.stdin.readline
n = int(input())
words = [input().strip() for _ in range(n)]

indexed = list(enumerate(words))
sorted_words = sorted(indexed, key=lambda x: x[1])

max_len = 0
prefix_lengths = [0] * n

for i in range(n - 1):
    (i1, w1), (i2, w2) = sorted_words[i], sorted_words[i + 1]
    lcp = common_prefix_length(w1, w2)
    max_len = max(max_len, lcp)
    prefix_lengths[i1] = max(prefix_lengths[i1], lcp)
    prefix_lengths[i2] = max(prefix_lengths[i2], lcp)

first = ""
prefix = ""

for i in range(n):
    if prefix_lengths[i] == max_len:
        if not first:
            first = words[i]
            prefix = first[:max_len]
            print(first)
        elif words[i][:max_len] == prefix:
            print(words[i])
            break