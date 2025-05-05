from collections import Counter

n = int(input())
a = list(map(int, input().split()))

count = Counter(a)
max_freq = max(count.values())
print(max_freq)