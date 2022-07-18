number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1 # 카운트가 들여쓰기가 안돼있다보니 for문에 속해있지 않음. 

print(total // count)