Text = input()
# happy = Text.count(':-)')
# sad = Text.count(':-(')
# if happy == 0 and sad == 0:
#     print('none')
# else:
#     if happy > sad:
#         print('happy')
#     elif sad > happy:
#         print('sad')
#     else:
#         print('unsure')
result = []
a, b = 0, 0
for i in Text:
    if i == ')':
        if result[-1] == '-' and result[-2] == ':':
            a += 1
    elif i == '(':
        if result[-1] == '-' and result[-2] == ':':
            b += 1
    result.append(i)
if a == 0 and b == 0:
    print('none')
elif a > b:
    print('happy')
elif a < b:
    print('sad')
elif a == b:
    print('unsure')