R, C, Z_r, Z_c = map(int, input().split(" "))
strings = []
for i in range(R):
    string = input()
    enlarged_row = ""
    for char in string:
        enlarged_row += char * Z_c
    strings.append(enlarged_row)
for string in strings:
    for i in range(Z_r):
        print(string)