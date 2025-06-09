from collections import defaultdict
n = int(input())
dictionary = defaultdict(lambda:0)
for i in range(n):
    string = input()
    print(dictionary[string])
    cur = ""
    for i in range(len(string)):
        cur += string[i]
        dictionary[cur] += 1