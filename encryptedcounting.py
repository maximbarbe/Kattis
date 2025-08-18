s, c = input().split()
iter = 0
while s != c:
    prev = None
    count = 0
    cur = ""
    for char in s:
        if char != prev:
            if prev != None:
                cur += str(count)+prev
                
            prev = char
            count = 1
        else:
            count += 1
    cur += str(count)+prev
    iter += 1
    s = cur
print(iter)
        