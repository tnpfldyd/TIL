def solution(s):
    result = []
    temp = []
    an = ''
    for i in range(len(s)):
        if s[i] in '0123456789':
            an += s[i]
        else:
            if len(an) > 0:
                temp.append(int(an))
                an = ''
        if i + 1 < len(s):
            if s[i] == '}':
                if s[i+1] == ',' and s[i+2] == '{':
                    result.append(temp)
                    temp = []
    result.append(temp)
    temp = set()
    answer = []
    result.sort(key = lambda x : len(x))
    for i in result:
        for j in i:
            if j not in temp:
                answer.append(j)
            temp.add(j)
    return answer