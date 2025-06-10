n = int(input())
votes = {}
parties = {
}
for i in range(n):
    name = input()
    party = input()
    votes[name] = 0
    parties[name] = party
    
n = int(input())
for i in range(n):
    name = input()
    if name in votes.keys():
        votes[name] += 1

max_votes = 0
tie = False
winner = None
for key, val in votes.items():
    if val > max_votes:
        max_votes = val
        winner = key
        tie = False
    elif val == max_votes:
        tie = True
if tie:
    print("tie")
else:
    print(parties[winner])