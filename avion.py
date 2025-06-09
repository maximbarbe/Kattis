indices = []
for i in range(5):
    if "FBI" in input():
        indices.append(str(i + 1))
if indices != []:
    print(" ".join(indices))
else:
    print("HE GOT AWAY!")