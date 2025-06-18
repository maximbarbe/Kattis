first = True
while True:
    n = int(input())
    if first:
        first = False
    elif first == False and n != 0:
        print()
    if n == 0:
        break
    words = []
    for i in range(n):
        words.append(input())
    words.sort(key=lambda x: (ord(x[0]), ord(x[1])))
    for word in words:
        print(word)