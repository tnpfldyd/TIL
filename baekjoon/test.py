
text = 'python'
answer = ''
dano = ['py','yt','th','on']
start = []
print(text[2:])
for i in dano:
    if i == text[:len(i)]:

        start.append(i)
print(start)