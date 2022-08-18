T = int(input())
 
for _ in range(T):
    cnt0 = [1,0]
    cnt1 = [0,1]
    N = int(input())
    for i in range(N-1):
        cnt0.append(cnt1[-1])
        cnt1.append(cnt1[-2]+cnt1[-1]) 
    print(cnt0[N], cnt1[N])