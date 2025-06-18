string = input()
smallest = 101
for i in range(1, len(string) + 1):
    if len(string) % i == 0:
        for j in range(i, len(string), i):
            sub = string[j:j + i]
            if string[j - i:j] != sub[1:]+sub[0]:
                break
        else:
            print(i)
            exit()
        