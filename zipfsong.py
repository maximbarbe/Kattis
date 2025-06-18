n, m = map(int, input().split())
songs = []
for i in range(n):
    fi, name = input().split(" ")
    fi = int(fi)
    songs.append((fi * (i + 1), name))
songs.sort(key=lambda el : (el[0]), reverse=True)

for i in range(m):
    print(songs[i][1])