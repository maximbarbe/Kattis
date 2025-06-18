n = int(input())
for i in range(n):
    string = input()
    for j in range(1, len(string) + 1):
        sub = string[:j]
        num_repeat = len(string)//len(sub)
        if sub*num_repeat == string[:len(string) - (len(string) % len(sub))] and sub.startswith(string[len(string) - (len(string) % len(sub)):]):
            print(j)
            break