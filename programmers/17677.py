import math
str1 = 'aa1+aa2'
str2 = 'AAAA12'
str1 = str1.upper(); str2 = str2.upper()
result1 = []
result2 = []
cnt = 0; cntt = 0
for i in range(len(str1)-1):
    if str1[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM' and str1[i+1] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        result1.append(str1[i]+str1[i+1])
for i in range(len(str2)-1):
    if str2[i] in 'QWERTYUIOPASDFGHJKLZXCVBNM' and str2[i+1] in 'QWERTYUIOPASDFGHJKLZXCVBNM':
        result2.append(str2[i]+str2[i+1])
gyo_result = []
for i in result2:
    if i in result1:
        if gyo_result.count(i) < result1.count(i):
            gyo_result.append(i)
if len(result1) == 0 and len(result2) == 0:
    print(65536)
else:
    print(math.trunc((len(gyo_result)/(len(result1)+len(result2)-len(gyo_result)))*65536))

