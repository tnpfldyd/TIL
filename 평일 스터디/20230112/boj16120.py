text = input()
result = []
ppap = ['P','P','A','P']
for i in range(len(text)):
    result.append(text[i])
    if result[-len(ppap):] == ppap:
        for j in range(3):
            result.pop()
print('PPAP' if result == ['P'] else 'NP')