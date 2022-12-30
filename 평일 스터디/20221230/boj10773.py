import sys
input = sys.stdin.readline

T = int(input())
result = []
for i in range(T):
    in_put = int(input())
    if in_put:
        result.append(in_put)
    else:
        result.pop()
print(sum(result))