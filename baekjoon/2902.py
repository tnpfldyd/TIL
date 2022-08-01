Text = input().split('-')
result = []
for i in range(len(Text)):
    result.append(Text[i][0])
result = ''.join(result)
print(result)