N, X = map(int, input().split())

array = list(map(int, input().split()))

array.sort()
count = 0
count += array.count(X)
for i in range(count):
    array.pop()

s = 0
e = N - 1 - count
rest_count = N - count
while s < e:
    if array[s] + array[e] >= X / 2:
        count += 1
        rest_count -= 2
        e -= 1
        s += 1
    else:
        s += 1

print(count + rest_count // 3)