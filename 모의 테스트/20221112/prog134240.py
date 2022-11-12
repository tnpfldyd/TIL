food = [1, 3, 4, 6]
text = ''
for i in range(1, len(food)):
    temp = food[i] // 2
    text += str(i) * temp
text = text + '0' + text[::-1]
print(text)