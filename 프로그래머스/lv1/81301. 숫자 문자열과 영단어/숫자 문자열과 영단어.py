def solution(s):

    numbers = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5',
            'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    for j in numbers:
        if j in s:
            s = s.replace(j, numbers.get(j))
    answer = int(s.strip('"'))
    return answer