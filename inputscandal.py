lines = []
while True:
    try: 
        lines.append(input())
    except EOFError:
        break
print(len(lines))
for line in lines:
    print(line)