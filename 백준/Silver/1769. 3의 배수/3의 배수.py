x = input().strip()
count = 0

while len(x) > 1:
    x = str(sum(int(digit) for digit in x))
    count += 1

print(count)
if int(x) % 3 == 0:
    print("YES")
else:
    print("NO")