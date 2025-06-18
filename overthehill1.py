def mult(matrix, vector):
    res = [None for i in range(len(vector))]
    for i in range(len(matrix)):
        cur = 0
        for j in range(len(matrix)):
            
            cur += matrix[i][j] * vector[j]
        res[i] = cur % 37
    return res

alphabet = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9,
    'K': 10,
    'L': 11,
    'M': 12,
    'N': 13,
    'O': 14,
    'P': 15,
    'Q': 16,
    'R': 17,
    'S': 18,
    'T': 19,
    'U': 20,
    'V': 21,
    'W': 22,
    'X': 23,
    'Y': 24,
    'Z': 25,
    '0': 26,
    '1': 27,
    '2': 28,
    '3': 29,
    '4': 30,
    '5': 31,
    '6': 32,
    '7': 33,
    '8': 34,
    '9': 35,
    ' ': 36
}

inverse = {val:key for key, val in alphabet.items()}

n = int(input())
matrix = []
for i in range(n):
    matrix.append([*map(int, input().split())])
string = input()
chars = []
for char in string:
    chars.append(alphabet[char])
vectors = []
for i in range(0, len(chars), n):
    vectors.append(chars[i:i+n])

if len(vectors[-1]) != n:
    vectors[-1] += [36] * (n - len(vectors[-1]))
for i in range(len(vectors)):
    vectors[i] = mult(matrix, vectors[i])
res = ""
for vect in vectors:
    for val in vect:
        res += inverse[val]
print(res)