cards = {
    "T": 0,
    "C": 0,
    "G": 0
}
word = input()
for char in word:
    cards[char] += 1
res = cards["T"]**2 + cards["C"]**2 + cards["G"] ** 2 + 7*min(cards.values())
print(res)