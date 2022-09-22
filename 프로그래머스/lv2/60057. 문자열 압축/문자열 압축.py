def solution(s):
    final = 1000
    if len(s) == 1:
        return 1
    for i in range(1, (len(s)//2)+1):
        result = ''
        cnt = 1
        temp = s[:i]
        for j in range(i, len(s)+i, i):
            if s[j:j+i] == temp:
                cnt += 1
            else:
                if cnt == 1:
                    result += temp
                else:
                    result += str(cnt) + temp
                temp = s[j:j+i]
                cnt = 1
        if final > len(result):
            final = len(result)
    return final