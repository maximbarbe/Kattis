n =int(input())
mine = input()
friend = input()
same = 0
for i in range(len(mine)):
    if mine[i] == friend[i]:
        same += 1
res = min(n, same) + min(len(friend) - n, len(friend) - same)
print(res)