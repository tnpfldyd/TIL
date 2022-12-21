
text = ["aya", "ye", "woo", "ma"]
babbling = ["wooyemawooye", "mayaa", "ymaeaya"]
result = 0
for i in babbling:
    last = ''
    for j in text:
        if j+j not in i:
            i = i.replace(j, ' ')
    if not i.strip():
        result += 1
print(result)