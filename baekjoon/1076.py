Text_om = {'black' : ['0', 1], 'brown' : ['1', 10], 'red' : ['2', 100], 'orange' : ['3', 1000], 'yellow' : ['4', 10000], 'green' : ['5', 100000], 'blue' : ['6', 1000000],
            'violet' : ['7', 10000000], 'grey' : ['8', 100000000], 'white' : ['9', 1000000000]}
result = []
for i in range(3):
    Text = input()
    if i == 2:
        result.append(Text_om[Text][1])
    elif Text in Text_om:
        result.append(Text_om[Text][0])
print(int(result[0]+result[1]) * result[2])