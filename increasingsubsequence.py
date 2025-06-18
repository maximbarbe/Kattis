from math import inf
while True:
    data = list(map(int, input().split(" ")))
    if data[0] == 0:
        break
    els = data[1:]
    elements = [0 for i in range(len(els))]
    subsequences = [[els[i]] for i in range(len(els))]
    subsequences[-1] = [els[-1]]
    max_length = -1 * inf
    max_index = 0
    for i in range(len(els) - 2, -1, -1):
        temp = len(subsequences[i])
        temp_el = subsequences[i]
        for j in range(len(els) - 1, i, -1):
            if els[i] < els[j] and len(subsequences[j]) + temp > len(subsequences[i]):
                subsequences[i] = temp_el + subsequences[j]
        if len(subsequences[i]) > max_length:
            max_length = len(subsequences[i])
            max_index = i
    print(f"{len(subsequences[max_index])} {' '.join(map(str, subsequences[max_index]))}")