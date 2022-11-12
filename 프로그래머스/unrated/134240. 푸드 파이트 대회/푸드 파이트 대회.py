def solution(food):
    text = ''
    for i in range(1, len(food)):
        temp = food[i] // 2
        text += str(i) * temp
    text = text + '0' + text[::-1]
    return text