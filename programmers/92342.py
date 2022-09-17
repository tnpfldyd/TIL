import itertools
n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]
result = [0,0,0,0,0,0,0,0,0,0,0]
test = [3,2,2,2,1,1,1,1,1,1,1]
max_cnt = 0
for i in itertools.combinations_with_replacement(range(11), 5):
    print(i)