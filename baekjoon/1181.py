T = int(input())
result = {}
for i in range(T):
    text = input()
    result[text] = len(text)
result = sorted(result.items(), key = lambda x : (x[1],x[0]))
for i in result:
    print(i[0])