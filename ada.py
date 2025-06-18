vals = [*map(int, input().split(" "))]
n = vals[0]
vals = vals[1:]
deg = 0
sequences = [vals]
while len(set(vals)) != 1:
    new_seq = []
    deg += 1
    for i in range(len(vals) - 1):
        new_seq.append(vals[i + 1] - vals[i])
    sequences.append(new_seq)
    vals = new_seq
current_val = sequences[-1][-1]
for i in range(len(sequences) - 2, -1, -1):
    current_val = current_val + sequences[i][-1]
print(f"{deg} {current_val}")