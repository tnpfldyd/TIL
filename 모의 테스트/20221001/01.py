registered_list = ["cow","cow1","cow2","cow3","cow4","cow5","cow6","cow7","cow8","cow9","cow9"]
registered_list = set(registered_list)
new_id = "cow"
answer = ""
temp = ""
if new_id in registered_list:
    for i in new_id:
        if i in "0123456789":
            temp += i
        else:
            answer += i
    if len(temp) > 0:
        while answer+temp in registered_list:
            temp = int(temp)
            temp += 1
            temp = str(temp)
    else:
        temp = "1"
        if answer+temp in registered_list:
            while answer+temp in registered_list:
                temp = int(temp)
                temp += 1
                temp = str(temp)
    answer = answer+temp
else:
    answer += new_id
print(registered_list)