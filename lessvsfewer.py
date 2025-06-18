correct = {
    "number of": "c",
    "amount of": "m",
    "most": "cm",
    "fewest": "c",
    "least": "m",
    "more": "cm",
    "fewer": "c",
    "less": "m",
    "many": "c",
    "much": "m",
    "few": "c",
    "little": "m"
}

pairing = dict()


n, p = map(int, input().split())
for i in range(n):
    word, char = input().split()
    pairing[word] = char
    
for i in range(p):
    words = input().split()
    phrase = " ".join(words[:-1])
    if pairing[words[-1]] in correct[phrase]:
        print("Correct!")
    else:
        print("Not on my watch!")