p = {'R':0, 'T':0, 'C':0 ,'F':0, 'J':0, 'M':0, 'A':0, 'N':0}

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
for i in range(len(survey)):
    if choices[i] > 4:
        p[survey[i][1]] += choices[i]-4
    else:
        p[survey[i][0]] += abs(choices[i]-4)
q = []
for k, v in p.items():
    q.append((k, v))
result = []
for i in range(len(q)):
    if i % 2 == 1:
        if (q[i][1]) > q[i-1][1]:
            result.append(q[i][0])
        else:
            result.append(q[i-1][0])         
print(''.join(result))

# def solution(survey, choices):
#     p = {'R':0, 'T':0, 'C':0 ,'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
#     for i in range(len(survey)):
#         if choices[i] > 4:
#             p[survey[i][1]] += choices[i]-4
#         else:
#             p[survey[i][0]] += abs(choices[i]-4)
#     q = []
#     for k, v in p.items():
#         q.append((k, v))
#     result = []
#     for i in range(len(q)):
#         if i % 2 == 1:
#             if (q[i][1]) > q[i-1][1]:
#                 result.append(q[i][0])
#             else:
#                 result.append(q[i-1][0]) 

#     return ''.join
# print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))

