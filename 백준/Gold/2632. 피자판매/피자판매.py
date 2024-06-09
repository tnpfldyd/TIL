from collections import defaultdict
import sys
input = sys.stdin.readline

def get_case(p, l):
    dic = defaultdict(int)
    for i in range(l):
        arr = p[i:] + p[:i]
        sums = 0
        for number in arr:
            sums += number
            dic[sums] += 1
    dic[sum(p)] = 1
    return dic

def main():
    K = int(input())
    M, N = map(int,input().split())
    A = [int(input()) for _ in range(M)]
    B = [int(input()) for _ in range(N)]

    a_dic = get_case(A, M)
    b_dic = get_case(B, N)

    result = a_dic[K] + b_dic[K]
    for number in a_dic:
        result += a_dic[number] * b_dic[K - number]
    print(result)


if __name__ == "__main__":
    main()