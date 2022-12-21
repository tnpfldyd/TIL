s = "aaabbaccccabba"
result = 0
text = ''
cntdic = {}
for i in s:
    if not cntdic:
        text = i
        cntdic[i] = 1
    elif i == text:
        cntdic[i] += 1
    else:
        if cntdic.get('other'):
            cntdic['other'] += 1
        else:
            cntdic['other'] = 1
    if len(cntdic) == 2:
        if cntdic[text] == cntdic['other']:
            cntdic = {}
            result += 1
if cntdic:
    result += 1
print(result)
