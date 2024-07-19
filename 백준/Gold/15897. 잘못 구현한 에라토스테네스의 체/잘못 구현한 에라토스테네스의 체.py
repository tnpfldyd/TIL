n = int(input())

result = n
i = 2
j = 0

while i < n:
    j = (n - 1) // ((n - 1) // i)
    number = 1 + (n - 1) // i
    result += (j - i + 1) * number
    i = j + 1

if n != 1:
    result += 1

print(result)
