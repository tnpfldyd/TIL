X = int(input())

line = 1
while X > line:
    X -= line
    line += 1

if line % 2 == 0:
    numerator = X
    denominator = line - X + 1
else:
    numerator = line - X + 1
    denominator = X

print(f"{numerator}/{denominator}")