mult = input()
n = int(input())
for i in range(n):
    string = input()
    encoded = ""
    for i in range(len(string)):
        val = ord(string[i]) - ord("A")
        val *= int(mult[i])
        val %= 26
        encoded += chr(ord("A") + val)
    print(encoded)