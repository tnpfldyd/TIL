d = {'apple' : '사과', 'banana' : '바나나'}

print(d.get('apple'))
for a in d.values():
    print(a)

v = d.pop('apple')
print(v)

print(d)