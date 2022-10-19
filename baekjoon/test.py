source = 'bbaabd'
source = list(source)
answer = ''
while source:
    temp = []
    resource = []
    for i in source:
        if i not in temp:
            temp.append(i)
        else:
            resource.append(i)
    temp.sort()
    answer += ''.join(temp)
    source = resource
print(answer)