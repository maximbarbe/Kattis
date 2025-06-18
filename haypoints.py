dictionary = dict()
m, n = map(int, input().split())
for i in range(m):
    desc, salary = input().split()
    dictionary[desc] = int(salary)
for i in range(n):
    res = 0
    while True:
        line = input()
        if line == ".":
            break
        words = line.split()
        for word in words:
            res += dictionary.get(word, 0)
    print(res)