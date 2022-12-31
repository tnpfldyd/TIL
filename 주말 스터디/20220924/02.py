cap = 4
n = 5
deliveries = [0,1,0,3,1,2]
pickups = [0,0,3,0,4,0]
result = 0
temp = 0
temp2 = 0
temp3 = 0
for i in range(n, 0, -1):
    temp += deliveries[i]
    temp2 += pickups[i]
    temp3 = max(temp3, i)
    if temp > cap or temp2 > cap:
        result += temp3*2
        temp3 = i
        temp = deliveries[i]
        temp2 = pickups[i]
if deliveries[1]+temp > cap or pickups[1]+temp2 > cap:
    result += temp3*2
print(result)