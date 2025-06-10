import sys
seen = set()
for line in sys.stdin:
    
    line = line.strip("\n").split(" ")
    data = []
    for word in line:
        if word.lower() in seen:
            data.append(".")
        else:
            data.append(word)
            seen.add(word.lower())
    print(" ".join(data))