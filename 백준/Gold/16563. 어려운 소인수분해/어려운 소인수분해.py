prime = [i for i in range(5000001)]
for i in range(2, 2250):
    if prime[i] == i:
        for j in range(i * 2, 5000001, i):
            if prime[j] == j: 
                prime[j] = i

def factorize(N):
    arr = []
    while N > 1:
        arr.append(str(prime[N]))
        N = N // prime[N]
    print(" ".join(arr))
    
    
x, l = input(), map(int, input().split())
for i in l:
    factorize(i)