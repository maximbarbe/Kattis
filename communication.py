MAX_BYTE_VALUE = 255
converted_values = dict()
for i in range(0, MAX_BYTE_VALUE + 1):
    converted_values[(i^(i<<1))%256] = i

n = int(input())
vals = [*map(int, input().split(" "))]
for i in range(len(vals)):
    vals[i] = converted_values[vals[i]]
print(*vals)