w = []
b = []
order = ["K", "Q", "R", "B", "N", "P"]
r = 0
for i in range(17):
    row = input()
    if i % 2 == 1:
        r += 1
        row = row.lstrip("|")
        row = row.rstrip("|")
        row = row.split("|")
        for j, c in enumerate(row):
            if c[1].isalpha():
                if c[1].isupper():
                    w.append((c[1], 8-r, j))
                else:
                    b.append((c[1].upper(), 8-r, j))
w.sort(key=lambda el:(order.index(el[0]), el[1], el[2]))
b.sort(key=lambda el:(order.index(el[0]), -el[1], el[2]))
w = map(lambda el: f"{el[0]}{chr(ord('a') + el[2])}{el[1] + 1}" if el[0] != 'P' else f"{chr(ord('a') + el[2])}{el[1] + 1}", w)
b = map(lambda el: f"{el[0]}{chr(ord('a') + el[2])}{el[1] + 1}" if el[0] != 'P' else f"{chr(ord('a') + el[2])}{el[1] + 1}", b)
print(f"White: {','.join(w)}")
print(f"Black: {','.join(b)}")