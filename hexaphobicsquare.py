n = int(input())
cur = n + 1
while True:
    if "6" not in str(cur**2):
        print(cur)
        exit()
    cur += 1