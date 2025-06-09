from collections import OrderedDict

# number of variables
n = int(input())

# truth values
truth_values = input().split(" ")

stack = []

values = OrderedDict()


circuit = input().split(" ")
idx = 0

for i in range(len(truth_values)):
    values[chr(ord("A") + i)] = True if truth_values[i] == 'T' else False
idx = 0
for i in range(len(circuit)):
    if circuit[i].isalpha():
        stack.append(circuit[i])
    else:
        if circuit[i] == "-":
            x = stack.pop(-1)
            string = f"-{x}"
            val = not values[x]
            values[string] = val
            stack.append(string)
        elif circuit[i] == "+":
            y = stack.pop(-1)
            x = stack.pop(-1)
            string = f"{x}+{y}"
            val = values[x] or values[y]
            values[string] = val
            stack.append(string)
        else:
            y = stack.pop(-1)
            x = stack.pop(-1)
            string = f"{x}*{y}"
            val = values[x] and values[y]
            values[string] = val
            stack.append(string)
            
print('F' if values[stack[-1]] == False else 'T')