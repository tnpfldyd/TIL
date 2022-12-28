arr = [1,1,3,3,0,1,1]
answer = []
for i in arr:
    if answer:
        if answer[-1] != i:
            answer.append(i)
    else:
        answer.append(i)