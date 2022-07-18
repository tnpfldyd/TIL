a = int(input())
b = list(map(int, input().split()))

c = b[0]

for i in b:
    if i < c:
        c = i
print(c)