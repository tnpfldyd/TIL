n=int(input())

def cal(a,b):
    nums=[]
    nums.append(a)
    while a >= 0 and b >= 0:
        nums.append(b)
        c=b
        b=a-b
        a=c
    
    return nums

prev=[]
now=[]
rs=[]
for i in range(n//2,n):
    prev=now
    now=cal(n, i)
    if len(prev) < len(now):
        rs=now
print(len(rs))
print(*rs)