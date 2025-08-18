from string import ascii_lowercase


l = set([char for char in ascii_lowercase])
s = set([char for char in input()])
diff = l.difference(s)
if len(diff) == 0:
    print("Good job!")
else:
    print("".join(sorted(diff)))