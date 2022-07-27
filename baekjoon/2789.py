text_=input()
new_t = []
for i in text_:
    if i not in 'CAMBRIDGE':
        new_t.append(i)
for j in new_t:
    print(j, end='')