def reverse_words(s):
    result = ''
    i = 0
    while i < len(s):
        if s[i] == '<':
            j = s.index('>', i)
            result += s[i:j+1]
            i = j + 1
        else:
            word = ''
            while i < len(s) and s[i] not in '< ':
                word += s[i]
                i += 1
            result += word[::-1]
            if i < len(s) and s[i] == ' ':
                result += ' '
                i += 1
    return result

print(reverse_words(input().strip()))