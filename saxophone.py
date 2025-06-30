needed = {
    "c": set([2, 3, 4, 7, 8, 9, 10]),
    "d": set([2, 3, 4, 7, 8 ,9]),
    "e": set([2, 3, 4, 7, 8]),
    "f": set([2, 3, 4, 7]),
    "g": set([2, 3, 4]),
    "a": set([2, 3]),
    "b": set([2]),
    "C": set([3]),
    "D": set([1, 2, 3, 4, 7, 8, 9]),
    "E": set([1, 2, 3, 4, 7, 8]),
    "F": set([1, 2, 3, 4, 7]),
    "G": set([1, 2, 3, 4]),
    "A": set([1, 2, 3]),
    "B": set([1, 2])
}


n = int(input())
for i in range(n):
    prev = set()
    res = [0]*10
    s = input()
    for c in s:
        now = needed[c]
        for el in now.difference(prev):
            res[el - 1] += 1
        prev = now
    print(*res)