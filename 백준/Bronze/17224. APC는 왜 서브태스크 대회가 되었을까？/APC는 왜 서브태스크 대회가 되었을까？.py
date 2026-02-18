import sys
input = sys.stdin.readline

n, l, k = map(int, input().split())

hard = easy = 0
for _ in range(n):
    sub1, sub2 = map(int, input().split())
    if sub2 <= l:
        hard += 1
    elif sub1 <= l:
        easy += 1

h = min(hard, k)
e = min(easy, k - h)
print(h * 140 + e * 100)
