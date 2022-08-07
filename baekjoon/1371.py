dic = {}
while True:
    try:
        T = input()
        for i in T:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
    except EOFError:
        break
try:
	del dic[' ']
except KeyError:
	pass
div = [k for k, v in dic.items() if max(dic.values()) == v]
div.sort()
print(''.join(div))