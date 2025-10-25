import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))

numbers.sort()

median = numbers[(N - 1) // 2]

print(median)