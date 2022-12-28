import itertools
babbling = ["aya", "yee", "u", "maa", "wyeoo"]
cases = ['aya','ye','woo','ma']
temp = set()
for i in range(1, 5):
    for j in itertools.permutations(cases, i):
        temp.add(''.join(j))
result = 0
for i in babbling:
    if i in temp:
        result += 1
