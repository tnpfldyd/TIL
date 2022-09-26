
def solution(numbers):
    number = []
    for i in numbers:
        number.append(str(i))
    number.sort(key = lambda x : x * 3, reverse=True)
    number = ''.join(number)
    return str(int(number))