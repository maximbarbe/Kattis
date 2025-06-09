from collections import Counter


n = int(input())
string = input()
max_length = 0
for i in range(len(string)):
    for j in range(i + 1, len(string) + 1):
        counter = Counter(string[i:j])
        diff_values = set(counter.values())
        if len(diff_values) == 1 and sum(counter.values()) > max_length:
            max_length = sum(counter.values())
print(max_length)