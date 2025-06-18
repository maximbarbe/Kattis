from collections import defaultdict

n = int(input())
persons = defaultdict(lambda: False)
for i in range(n):
    data = input().split(" ")
    if data[0] == "entry":
        
        if persons[data[1]] == True:
            print(f"{data[1]} entered (ANOMALY)")
        else:
            print(f"{data[1]} entered")
            persons[data[1]] = True
    else:
        if persons[data[1]] == False:
            print(f"{data[1]} exited (ANOMALY)")
        else:
            print(f"{data[1]} exited")
            persons[data[1]] = False