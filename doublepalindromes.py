from itertools import product

n = input()

length = len(n)
n = int(n)
if n >= 300000000000:
    print(39)
    exit()
palindromes = []
digits = "0123456789"
for i in range(1, length + 1):
    if i == 1:
        for d in digits:
            palindromes.append(d)
    else:
        if i % 2 == 0:
            allowed = [*product(digits, repeat=i//2)]
            palindromes.extend(["".join(allowed[i]) + "".join(allowed[i])[::-1] for i in range(len(allowed)) if allowed[i][0] != "0"])
            
        else:
            allowed = [*product(digits, repeat=i//2)]
            allowed = ["".join(allowed[i]) for i in range(len(allowed)) if allowed[i][0] != "0"]

            for j in range(len(allowed)):
                for d in digits:
                    palindromes.append(allowed[j] + d + allowed[j][::-1])
palindromes = [0] + [int(v) for v  in palindromes if int(v) % 2 == 1]
kept = []
n = int(n)
for v in palindromes:
    if v < n:
        kept.append(v)
    else:
        break
res = 0
for v in kept:
    bin_rep = bin(v)[2:]
    if bin_rep == bin_rep[::-1]:
        res += 1
print(res)