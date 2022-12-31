db = [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]
id_pw = ["meosseugi", "1234"]
db_dic = {}
for a, b in db:
    db_dic[a] = b
if id_pw[0] not in db_dic:
    print('fail')
else:
    if db_dic[id_pw[0]] != id_pw[1]:
        print('wrong pw')
    else:
        print('login')