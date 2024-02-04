import sys
input = sys.stdin.readline

while True:
    try:
        N = int(input())
        p = 1
        result = 0
        while True:
            p *= 9
            if p >= N:
                result = 1
                break
            p *= 2
            if p >= N:
                result = 0
                break
        print('Baekjoon wins.' if result else 'Donghyuk wins.')
    except:
        break