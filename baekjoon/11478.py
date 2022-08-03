Text = input()
result = set()
for i in range(len(Text)):
    for j in range(i, len(Text)):
        ex = Text[i:j+1]
        result.add(ex)
print(len(result))