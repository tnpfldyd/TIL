result = [0,0,0]
num1 = [1,2,3,4,5]
num2 = [2,1,2,3,2,4,2,5]
num3 = [3,3,1,1,2,2,4,4,5,5]
answers = [1,2,3,4,5]
for i in range(len(answers)):
    if answers[i] == num1[i % len(num1)]:
        result[0] += 1
    if answers[i] == num2[i % len(num2)]:
        result[1] += 1
    if answers[i] == num3[i % len(num3)]:
        result[2] += 1
final = []
for i in range(len(result)):
    if result[i] == max(result):
        final.append(i+1)
print(final)