a, b, c, d = map(int, input().split())
for i in range(1, d):
    a *= b
    a += c
print(a)