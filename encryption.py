s = input()
d = input()
common = input()
s_idx = 0
d_idx = 0
c_idx = 0
res = []
while c_idx != len(common):
    if s[s_idx] == d[d_idx] == common[c_idx]:
        res.append(s[s_idx])
        s_idx += 1
        d_idx += 1
        c_idx += 1
    else:
        if s[s_idx] != common[c_idx]:
            res.append(s[s_idx])
            s_idx += 1
        if d[d_idx] != common[c_idx]:
            res.append(d[d_idx])
            d_idx += 1
        
while s_idx != len(s):
    res.append(s[s_idx])
    s_idx += 1
while d_idx != len(d):
    res.append(d[d_idx])
    d_idx += 1
    
print("".join(res))
    
    
