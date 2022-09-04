def prime_list(n):
    sieve = [True] * n
    m = int(n ** 0.5) # 제곱근(이하 버림)
    for i in range(2, m + 1):
        if sieve[i] == True:# i가 소수인 경우
            for j in range(i+i, n, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False
    return [i for i in range(a, n) if sieve[i] == True]
a, b = map(int, input().split())
if a < 2:
    a = 2
result = prime_list(b+1)
for i in result:
    print(i)