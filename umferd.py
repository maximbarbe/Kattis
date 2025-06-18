cells = int(input())
lanes = int(input())
cases = cells * lanes
blanks = 0
for i in range(lanes):
    str = input()
    for char in str:
        if char == '.':
            blanks += 1
print(round(blanks/cases, 5))