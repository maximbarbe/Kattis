n = int(input())
memes = []
for i in range(n):
    data = input().split(" ")
    memes.append((data[0], int(data[1]) * int(data[2])))
memes.sort(key=lambda el: (-el[1], el[0]), reverse=True)
print(memes[-1][0])