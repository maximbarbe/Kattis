def lis_len(arr):
    res = []
    for el in arr:
        if not res or el > res[-1]:
            res.append(el)
        else:
            for i in range(len(res)):
                if el <= res[i]:
                    res[i] = el
                    break
    return len(res) 

n = int(input())
if n == 1:
    print("!", 1)
else:
    res = []
    prev = 0
    for i in range(1, n+1):
        print("?", 1, i)
        response = int(input())
        res.insert(response - prev, i)
        prev = response
    print("!", lis_len(res[::-1]))