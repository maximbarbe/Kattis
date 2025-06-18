n = int(input())
seq = input()
idx =0 
indices = {
    "R": None,
    "B": None,
    "G": None
}
res = ""
j = 0
for i in range(n):
    
    while indices["R"] == None or indices["B"] == None or indices["G"] == None:
        indices[seq[j]] = j
        j += 1
    res += seq[j - 1]
    indices = {
        "R": None,
        "B": None,
        "G": None
    }
print(res)