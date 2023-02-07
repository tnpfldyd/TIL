
text = list(map(lambda x : sum(map(int, x.split('+'))), input().split('-')))
result = text[0] - sum(text[1:])
print(result)