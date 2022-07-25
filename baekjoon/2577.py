a = int(input())
b = int(input())
c = int(input())
d = a*b*c
result = [0] * 10
for i in str(d):
    result[int(i)] += 1
print(*result, sep='\n')