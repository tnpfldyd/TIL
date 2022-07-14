word = 'HappyHacking'
a = 0
for b in word:
    if b in 'a':
        print(a, end=' ')
        a += 1
    elif not 'a' in word:
        print(0)
        break
    else:
        a += 1