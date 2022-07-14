word = 'banana'
tcid = {}
for q in word:
    if tcid.get(q) == None:
        tcid[q] = 1
    else:
        tcid[q] += 1
for q in tcid:
    print(q, tcid.get(q))