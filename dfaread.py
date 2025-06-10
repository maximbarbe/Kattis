from collections import defaultdict


def res(state, accept, word, transition):
    for char in word:
        state = transition[state][char]
    return "accept" if state in accept else "reject"
    


n,c,s,f = map(int, input().split())
a = input()
alphabet = {a[i]:i for i in range(len(a))}
accept = set([*map(lambda el: int(el)-1, input().split())])
transition = defaultdict(lambda:defaultdict(lambda:None))
for i in range(n):
    transitions = [*map(int, input().split())]
    for j in range(len(transitions)):
        transition[i][a[j]] = transitions[j] - 1

k = int(input())
for i in range(k):
    print(res(0, accept, input(), transition))