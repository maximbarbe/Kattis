from string import ascii_uppercase


s1 = set([c for c in ascii_uppercase])
s2 = set([c for c in input()])
if len(s1.intersection(s2)) == 26:
    print("Alphabet Soup!")
else:
    print("".join(sorted(s1.difference(s2))))