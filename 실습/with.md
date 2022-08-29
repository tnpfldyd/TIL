with open('test.txt', 'w', encoding='utf-8') as f:

​    f.write('Happy Hacking!\n')

​    for i in range(1, 6):

​    f.write(f'{i} 번째!\n')



with open('students.txt', 'r', encoding='utf-8') as f:

​    text = f.read()

​    names = text.split()

​    cnt = 0

​    for name in names:

​    if name[0] == '김':

​        cnt += 1

​    print(cnt)



import json

f = open('stocks.json', 'r', encoding='utf-8')

kospi = json.load(f)

`samsung = kospi['stocks'][0]`

print(samsung, type(samsung))



result = { 'stockName' : samsung.get('stockName'), 'closePrice' : samsung.get('closePrice')}