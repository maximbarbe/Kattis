t = int(input())
for i in range(t):
    string = input().split(" ")
    sounds = dict()
    while True:
        line = input()
        if line == "what does the fox say?":
            break
        else:
            line = line.split(" ")
            sounds[" ".join(line[2:])] = True
    res = []
    for word in string:
        if not sounds.get(word, False):
            res.append(word)
    print(" ".join(res))