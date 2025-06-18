def get_carry(first, sec):
    carry = 0
    res = 0
    if len(first) < len(sec):
        first = [0] * (len(sec) - len(first)) + first
    elif len(first) > len(sec):
        sec = [0] * (len(first) - len(sec)) + sec
    for i in range(len(sec) - 1, -1, -1):
        if sec[i] + first[i] + carry >= 10:
            carry = 1
            res += 1
        else:
            carry = 0
    return res

while True:
    a, b = input().split()
    if a == b and a == "0":
        exit()
    res = get_carry([int(digit) for digit in a], [int(digit) for digit in b])
    print(f"{res if res != 0 else 'No'} carry operation{'s' if res > 1 else ''}.")