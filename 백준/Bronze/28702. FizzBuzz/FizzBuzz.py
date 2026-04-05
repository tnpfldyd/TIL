arr = [input().strip() for _ in range(3)]

for i in range(3):
    if arr[i].isdigit():
        n = int(arr[i]) + (3 - i)
        break

if n % 15 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)