from collections import defaultdict

cycle_found = defaultdict(lambda:False)
longest_cycle = 0
letter = ""
indices = defaultdict(lambda:None)
n = int(input())
for i in range(n):
    pos, string = input().split(" ")
    pos = int(pos)
    for j in range(len(string)):
        if indices[string[j]] == None:
            indices[string[j]] = pos
        else:
            if cycle_found[string[j]] == False:
                cycle_found[string[j]] = True
                if pos - indices[string[j]] > longest_cycle:
                    longest_cycle = pos - indices[string[j]]
                    letter = string[j]
print(letter)