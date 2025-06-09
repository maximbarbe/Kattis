n = int(input())
tb = 0
lr = 0
for i in range(n):
    string = input()
    for j in range(len(string)):
        if j < 2 and string[j] == '0':
            tb += 1
        else:
            if string[j] == '0':
                lr += 1
num_tb = tb//2
num_lr = lr//2
swords = min(num_lr, num_tb)
tb -= 2 *swords
lr -= 2 * swords
print(f"{swords} {tb} {lr}")