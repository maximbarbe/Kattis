row1 = input()
row2 = input()
row3 = input()
if row1 == "OOO" or row2 == "OOO" or row3 == "OOO" or row1[0] + row2[0] + row3[0] == "OOO" or row1[1] + row2[1] + row3[1] == "OOO" or row1[2] + row2[2] + row3[2] == "OOO" or row1[0] + row2[1] + row3[2] == "OOO" or row1[2] + row2[1] + row3[0] == "OOO":
    print("Jebb")
else:
    print("Neibb")