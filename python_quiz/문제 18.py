word = 'banana'
tcid = {}
for q in word:
    if q not in tcid:
        tcid[q] = 1
    else:
        tcid[q] += 1
for a, b in tcid.items():
    print(a, b)