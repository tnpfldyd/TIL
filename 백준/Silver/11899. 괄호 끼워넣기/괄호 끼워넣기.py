S = input().strip()
sum_val = 0
min_sum = 0

for char in S:
    if char == '(':
        sum_val += 1
    else:
        sum_val -= 1
    min_sum = min(min_sum, sum_val)

front = 0 if min_sum >= 0 else -min_sum
final_sum = sum_val + front
back = 0 if final_sum <= 0 else final_sum
total = front + back
print(total)