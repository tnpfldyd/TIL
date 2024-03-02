string = input()

s = string[0]
for i in range(1, len(string)):
    if s[-1] < string[i]:
        s = string[i] + s
    else:
        s = s + string[i]
s = s[::-1]

print(s)