import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        N = int(input())
        v = [int(input()) for _ in range(N)]
        v.sort()
        l, r = 0, N - 1
        result = 0
        answer = False
        while l < r:
            result = v[l] + v[r]
            if result == x:
                print(f'yes {v[l]} {v[r]}')
                answer = True
                break
            else:
                if result < x:
                    l += 1
                else:
                    r -= 1
        if not answer:
            print('danger')
    except:
        break