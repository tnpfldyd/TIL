S, K, H = map(int, input().split())
dic = {}
dic[S] = 'Soongsil'
dic[K] = 'Korea'
dic[H] = 'Hanyang'
if sum(dic.keys()) >= 100:
    print('OK')
else:
    print(dic.get(min(S, K, H)))