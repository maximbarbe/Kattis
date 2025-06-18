import heapq

indices = {
    "q": (0, 0),
    "w": (0, 1),
    "e": (0, 2),
    "r": (0, 3),
    "t": (0, 4),
    "y": (0, 5),
    "u": (0, 6),
    "i": (0, 7),
    "o": (0, 8),
    "p": (0, 9),
    "a": (1, 0),
    "s": (1, 1),
    "d": (1, 2),
    "f": (1, 3),
    "g": (1, 4),
    "h": (1,5),
    "j": (1, 6),
    "k": (1, 7),
    "l": (1, 8),
    "z": (2, 0),
    "x": (2,1),
    "c": (2, 2),
    "v": (2, 3),
    "b": (2, 4),
    "n": (2, 5),
    "m": (2, 6)
}

def substract(first, sec):
    return abs(first[0] - sec[0]) + abs(first[1] - sec[1])


n = int(input())
for i in range(n):
    data = input().split(" ")
    word = data[0]
    num_word = int(data[1])
    heap = []
    for i in range(num_word):
        w = input()
        dist = 0
        for j in range(len(w)):
            dist += substract(indices[w[j]], indices[word[j]])
        heapq.heappush(heap, (dist, w))
    while heap != []:
        cur = heapq.heappop(heap)
        print(f"{cur[1]} {cur[0]}")