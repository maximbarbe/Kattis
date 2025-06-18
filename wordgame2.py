def get_res(words):
    global res
    if len(words) == 1:
        word = words[0]
        if len(word) < len(res):
            res = word
        elif len(word) == len(res):
            if word < res:
                res = word
    else:
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    for k in range(len(words[i]) -1, -1, -1):
                        if words[j].startswith(words[i][k:]):
                            new_word = words[i][:k] + words[j]
                            get_res([words[v] for v in range(len(words)) if v not in [i, j]] + [new_word])
                            

res = "z"*26            
n = int(input())
words = []
for i in range(n):
    words.append(input())

get_res(words)
if res == "z"*26:
    print(-1)
else:
    print(res)