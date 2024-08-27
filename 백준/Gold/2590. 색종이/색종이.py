a = [0]
for i in range(6):
    a.append(int(input()))
c = a[-1]
while a[5] > 0:
    c += 1
    a[5] -= 1
    a[1] = max(a[1]-11, 0)
while a[4] > 0:
    w = 20 - min(a[2], 5)*4
    a[4] -= 1
    c += 1
    a[2] = max(a[2]-5, 0)
    a[1] = max(a[1]-w, 0)
while a[3] > 0:
    w = 36 - 9*min(4, a[3])
    if a[3] >= 4:
        a[3] -= 4
    elif a[3] == 3:
        a[3] -= 3
        w -= min(1, a[2])*4
        a[2] = max(a[2]-1, 0)
    elif a[3] == 2:
        a[3] -= 2
        w -= min(3, a[2])*4
        a[2] = max(a[2]-3, 0)
    else:
        a[3] -= 1
        w -= min(5, a[2])*4
        a[2] = max(a[2]-5, 0)
    a[1] = max(a[1]-w, 0)
    c += 1
while a[2] > 0:
    w = 36 - 4*min(a[2], 9)
    a[2] = max(a[2]-9, 0)
    a[1] = max(a[1]-w, 0)
    c += 1
while a[1] > 0:
    a[1] = max(a[1]-36, 0)
    c += 1

print(c)