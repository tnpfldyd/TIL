T = int(input())
for i in range(1, T + 1):
    text = input()
    card_dic = {"S": set(), "D": set(), "H": set(), "C": set()}
    for j in range(0, len(text), 3):
        card_dic[text[j]].add(text[j + 1] + text[j + 2])
    result = ""
    cnt = 0
    for k, v in card_dic.items():
        cnt += len(v)
        result += " " + str(13 - len(v))
    if cnt * 3 == len(text):
        print(f"#{i}{result}")
    else:
        print(f"#{i} ERROR")
