from collections import Counter


count = Counter()
trees = set()
while True:
    try:
        string = input()
        trees.add(string)
        count[string] += 1
    except EOFError:
        break
    


sumn = count.total()

for tree in sorted(trees):
    print(f"{tree} {100*count[tree]/sumn}")