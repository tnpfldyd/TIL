from tkinter import N


word = 'banana'
for i in word:
    i = ord(i)
    print(chr(i-32), end='')


wor = 'apple'
for q in wor:
    print(chr(ord(q)-32), end='')