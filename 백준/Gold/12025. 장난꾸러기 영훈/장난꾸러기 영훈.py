input_str = input()
n = int(input())

cnt = 1
input_str_list = list(input_str)
check = ('1', '6', '2', '7')
for i in range(len(input_str_list)):
    cur = input_str_list[i]
    if cur in check:
        input_str_list[i] = '1' if cur == '6' else '2' if cur == '7' else cur
        cnt *= 2

if n > cnt:
    print(-1)
else:
    n -= 1
    for i in range(len(input_str_list) - 1, -1, -1):
        cur = input_str_list[i]
        if cur == '1' or cur == '2':
            if n % 2:
                input_str_list[i] = '6' if cur =='1' else '7'
            n //= 2

    print(''.join(input_str_list))