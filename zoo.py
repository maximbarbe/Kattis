from collections import defaultdict
list_num = 1
while True:
    n = int(input())
    if n == 0:
        break
    dict = defaultdict(lambda:0)
    for i in range(n):
        type = input().split(" ")[-1].lower()
        dict[type] += 1
    keys = list(dict.keys())
    keys.sort()
    print(f"List {list_num}:")
    for key in keys:
        print(f"{key} | {dict[key]}")
    list_num += 1