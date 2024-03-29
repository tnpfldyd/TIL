import re

input_string = input()
pattern = r'(100+1+|01)+'
print("SUBMARINE" if re.fullmatch(pattern, input_string) else "NOISE")