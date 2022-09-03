T = int(input())
dic = {}
for i in range(T):
    a = input().split('.')
    if a[1] in dic:
        dic[a[1]] += 1
    else:
        dic[a[1]] = 1
for i in sorted(dic.items(), key = lambda x : x[0]):
    print(*i)