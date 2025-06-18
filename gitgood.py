n = int(input())
seen = dict()
folders = []
for i in range(n):
    data = input().split()
    match data[0]:
        case "cd":
            if data[1] == ".." and len(folders) != 0:
                folders.pop()
            else:
                folders.append(data[1])
        case _:
            if len(folders) == 0:
                seen[data[1]] = True
            else:
                seen["/".join(folders) +"/" + data[1]] = True
for key in sorted(seen.keys()):
    print("git add", key)
print("git commit")
print("git push")