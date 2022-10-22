text = input()
result = ["C", "P", "C", "U"]
for i in text:
    if result:
        if i == result[-1]:
            result.pop()
print("I hate UCPC" if result else "I love UCPC")
