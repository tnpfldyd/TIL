import itertools
text = ['a','b','c','d','e']
qw = []
for i in range(2, 6):
    for j in itertools.combinations(text, i):
            qw.append(j)
print(qw)