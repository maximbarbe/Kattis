string = input().split(" ")
if len(set(string)) == len(string):
    print("yes")
else:
    print("no")