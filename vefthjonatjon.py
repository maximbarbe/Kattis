n = int(input())
cpu = 0
memory = 0
component= 0
for i in range(n):
    chars = input().split(" ")
    if chars[0] == "J":
        cpu += 1
    if chars[1] == "J":
        memory += 1
    if chars[2] == "J":
        component += 1
print(min(cpu, memory, component))