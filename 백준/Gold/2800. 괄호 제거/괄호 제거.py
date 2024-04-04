import itertools

origin = list(input())
open_ = []
close = []
result = set()
for i in range(len(origin)):
    cur = origin[i]
    if cur == '(':
        open_.append(i)
    elif cur == ')':
        close.append((open_.pop(), i))

for i in range(len(close)):
    for comb in itertools.combinations(close, i + 1):
        temp = origin[:]
        for a, b in comb:
            temp[a] = temp[b] = ''
        result.add(''.join(temp))

print('\n'.join(sorted(result)))
