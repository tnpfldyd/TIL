a = int(input())
bit_count = 0
bit_mask = 1
bit_pair = 3

lower_bound = 0
upper_bound = 0

def get_nearest_lower():
    global lower_bound
    lower_bound = a ^ bit_pair
    lower_bound = lower_bound // bit_mask * bit_mask
    n = bit_mask >> 1
    count = bit_count
    while n and count > 0:
        lower_bound += n
        n >>= 1
        count -= 1

def get_nearest_higher():
    global upper_bound
    upper_bound = a ^ bit_pair
    upper_bound = upper_bound // bit_mask * bit_mask
    n = 1
    count = bit_count
    while n < bit_mask and count > 0:
        upper_bound += n
        n <<= 1
        count -= 1

while True:
    if lower_bound and upper_bound:
        break
    if bit_mask > a:
        break

    if (a & bit_pair) == (bit_mask << 1):
        get_nearest_lower()
    if (a & bit_pair) == bit_mask:
        get_nearest_higher()
    if a & bit_mask:
        bit_count += 1

    bit_mask <<= 1
    bit_pair <<= 1

print(lower_bound, upper_bound)