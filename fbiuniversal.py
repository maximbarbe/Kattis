values = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "A": 10,
    "C": 11,
    "D": 12,
    "E": 13,
    "F": 14,
    "H": 15,
    "J": 16,
    "K": 17,
    "L": 18,
    "M": 19,
    "N": 20,
    "P": 21,
    "R": 22,
    "T": 23,
    "V": 24,
    "W": 25,
    "X": 26,

}
confusing = {
    "B": "8",
    "G": "C",
    "I": "1",
    "O": '0',
    "S": "5",
    "U": "V",
    "Y": "V",
    "Z": "2"
}
n = int(input())
for i in range(n):
    data = input().split(" ")
    k = data[0]
    nums = [*data[1]]
    for i in range(len(nums)):
        if confusing.get(nums[i], nums[i]) !=  nums[i]:
            nums[i] = confusing[nums[i]]
    check_digit = values[nums[-1]]
    check_sum = (2 * values[nums[0]] + 4 * values[nums[1]] + 5 * values[nums[2]] + 7 * values[nums[3]] + 8 * values[nums[4]] + 10 * values[nums[5]] + 11 * values[nums[6]] + 13 * values[nums[7]]) % 27
    if check_sum != check_digit:
        print(f"{k} invalid")
    else:
        res=  0
        for i in range(0, 8):
            res += values[nums[i]] * pow(27, 7 - i)
        print(f"{k} {res}")