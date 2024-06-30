from collections import defaultdict

def main():
    
    n = int(input())
    values = list(map(int, input().split())) 

    m = [defaultdict(int) for _ in range(n)]
    p = defaultdict(int)
    pp = []

    for i in range(n):
        x = values[i]
        for j in range(2, int(x**0.5) + 1):
            if x % j == 0:
                cnt = 0
                while x % j == 0:
                    x //= j
                    cnt += 1
                m[i][j] = cnt
                if not p[j]:
                    pp.append(j)
                p[j] += cnt
        if x > 1:
            m[i][x] = 1
            if not p[x]:
                pp.append(x)
            p[x] += 1

    gcd = 1
    ans = 0

    for prime in pp:
        k = p[prime] // n
        mul = prime ** k
        gcd *= mul
        for i in range(n):
            if m[i][prime] < k:
                ans += k - m[i][prime]

    print(gcd, ans)

if __name__ == "__main__":
    main()
