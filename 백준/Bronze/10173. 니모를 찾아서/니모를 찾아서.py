import sys

for line in sys.stdin:
    line = line.rstrip('\n')
    
    if line == "EOI":
        break
    
    if "nemo" in line.lower():
        print("Found")
    else:
        print("Missing")