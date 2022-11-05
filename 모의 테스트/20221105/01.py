line = 'aabbbc'
result = ''
for i in line:
    if len(result):
        if result[-1] == '*':
            if result[-2] == i:
                continue
            else:
                result += i
        elif result[-1] == i:
            result += '*'
        else:
            result += i
    else:
        result += i
print(result)