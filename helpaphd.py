n = int(input())
for i in range(n):  
    string = input()
    if string == "P=NP":
        print("skipped")
    else:
        print(eval(string))