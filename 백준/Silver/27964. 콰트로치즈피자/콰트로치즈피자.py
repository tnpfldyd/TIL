n = int(input())
toppings = input().split()

cheese_set = set()

for topping in toppings:
    if topping.endswith("Cheese"):
        cheese_set.add(topping)

if len(cheese_set) >= 4:
    print("yummy")
else:
    print("sad")