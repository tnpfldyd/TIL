import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
k = int(input())

G = N // k 
result = []

for i in range(0, N, G):
    sub_array = A[i : i + G]
    sub_array.sort() 
    result.extend(sub_array)

print(*(result))