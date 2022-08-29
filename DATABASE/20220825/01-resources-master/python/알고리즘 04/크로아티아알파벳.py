import sys
sys.stdin = open("_크로아티아알파벳.txt")
string = input() # ljes=njak

# 변환표를 보고 알파벳을 크로아티아 알파벳으로 replace
string = string.replace("c=", "č")
string = string.replace("c-", "ć")
string = string.replace("d-", "đ")
string = string.replace("s=", "š")
string = string.replace("z=", "ž")
string = string.replace("lj", "lj")
string = string.replace("nj", "nj")
string = string.replace("dz=", "dž")

two_word_list = ["lj","nj","dž"]
two_word_count = 0

for two_word in two_word_list:
    two_word_count += string.count(two_word)

print(len(string) - two_word_count)