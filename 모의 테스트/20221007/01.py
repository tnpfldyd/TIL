oldWeapons = 4
golds = 8
sellingPrice = 3
repairCost = 4
temp = 0
result = 0

while temp < (repairCost * oldWeapons - golds)/(sellingPrice+repairCost) :
    temp += 1

print(oldWeapons-temp)