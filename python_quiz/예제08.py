word = "HappyHacking"

count = 0

for char in word:
    #if char == "a" or "e" or "i" or "o" or "u":
    #위와 같은 코드는 if char 는 aeiou가 들어가있나요? 가 아닌 aeiou와 같은 다른 알파벳과 같나요?  라고 묻는것과 같음.
    #해결을 위해선 == 와 or을 제거하고 in을 넣어야함.
    if char in 'aeiou':
        count += 1

print(count)