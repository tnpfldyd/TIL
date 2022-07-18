from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1 # fruit_count = {fruit:1} 은 fruit:1 을 conut 에 추가하는 것이 아닌 바꾸는 것이기 때문에 모든 것이 한번에 출력되려면 추가하는 형식으로 바꿔야함
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)