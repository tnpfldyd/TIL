text = input()
result = []
ppap = ['P','P','A','P']
for i in range(len(text)):
    result.append(text[i])
    if result[-len(ppap):] == ppap:
        for j in ppap:
            result.pop()
        result.insert(i-3, 'P')
print('PPAP' if result == ['P'] else 'NP')