letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
data = input()
while data != "0":
    data = data.split(" ")
    n = int(data[0])
    string = data[1][::-1]
    res = ""
    for char in string:
        res += letters[(letters.index(char) + n) % 28]
    
    print(res)
    
    data = input()