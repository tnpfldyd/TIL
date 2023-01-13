d = [1,3,2,5,4]
budget = 9
cnt = 0
d.sort(reverse=True)
while budget > 0 and d:
    x = d.pop()
    budget -= x
    cnt += 1
if budget < 0:
    cnt -= 1
print(cnt)