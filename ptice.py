n = int(input())
string = input()
a_sequence = ["A", "B", "C"]
b_sequence = ["B", "A", "B", "C"]
g_sequence = ["C", "C", "A", "A", "B", "B"]
b_score = 0
a_score = 0
g_score = 0
for i in range(n):
    if string[i] == a_sequence[i % len(a_sequence)]:
        a_score += 1
    if string[i] == b_sequence[i % len(b_sequence)]:
        b_score += 1
    if string[i] == g_sequence[i % len(g_sequence)]:
        g_score += 1
maximum = max(a_score, b_score, g_score)
print(maximum)
if a_score == maximum:
    print("Adrian")
if b_score == maximum:
    print("Bruno")
if g_score == maximum:
    print("Goran")