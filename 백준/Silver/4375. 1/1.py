import sys
input = sys.stdin.readline

while True:
   try:
       n = int(input())
       
       remainder = 1 % n
       digits = 1
       
       while remainder != 0:
           remainder = (remainder * 10 + 1) % n
           digits += 1
       
       print(digits)
   except:
       break