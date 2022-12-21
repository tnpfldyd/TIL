a = [1,2,3,4]
b = [-3,-1,0,2]
answer = 0
while a:
    answer += a.pop()*b.pop()
print(answer)