result = []
for i in range(102):
    Text = input()
    if Text == '문제':
        result.append(Text)
    elif Text == '고무오리':
        if result:
            result.pop()
        else:
            result.append('문제')
            result.append('문제')
    elif Text == '고무오리 디버깅 끝':
        break
print('고무오리야 사랑해' if len(result) == 0 else '힝구')